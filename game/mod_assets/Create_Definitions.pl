#!/usr/bin/perl -l

# Copyright 2018 J. Kyle Roth
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

use strict;
use warnings;
use File::Find;
use Cwd;
use Data::Dumper qw(Dumper);
use DateTime;

my $start_time = DateTime->now();

my $version_number = "1.4";

my $direct_write = 0;
my $write_status = 1;
my $piece_out_files = 1;
my $just_mode = 0;
my $lightweight_mode = 1;
my $help_only = 0;
my %arg_characters = ();
my %filters = ();
my %filters_by_character = ();
my %additional_filter_calls = ();

my $last_to_first_filters = 1;
my $lines_per_file = 10000;
my $image_size = "(960, 960)";
my $outside_image_init_level = 600;
my $no_outside_init = 0;

my @final_warnings = ();

my $auto_generate_comment = "########################################################################\n# This file was created automatically by the Dynamic Pose Tool v". $version_number . ".   #\n# You may edit this file manually, but be aware it will be overwritten #\n# without confirmation the next time the tool is run and your changes  #\n# will be lost.                                                        #\n#                                                                      #\n# It is recommended to only make temporary changes for test purposes   #\n# which are harmless to lose in an overwrite.                          #\n########################################################################\n";
my $get_character_image_function = "    # Used for applying filters to any image, even those not defined by the tool.\n    def getCharacterImage(char, expression=\"1a\"): # MAS Dev Team\n        return renpy.display.image.images.get((char, expression), None)\n";
my %show_statement_stops = (); # Ren'Py's keywords used in show statements so we know where our image tag ends and the other commands begin.
$show_statement_stops{"as"} = 1;
$show_statement_stops{"at"} = 1;
$show_statement_stops{"behind"} = 1;
$show_statement_stops{"onlayer"} = 1;
$show_statement_stops{"zorder"} = 1;

# Handle optional flags the user can input
foreach my $arg (@ARGV) {
    if ($arg eq "-d") { # Direct Write -- Go straight to the game directory above this one and write the file there.
        $direct_write = 1;
    }    
    elsif ($arg eq "-s") { # Silent Write -- Speed things up a little by not printing messages stating where the process is.
        $write_status = 0;
    }
    elsif ($arg eq "-w") { # Whole File -- Keep the output files as singular individual files instead of splitting them up if they're more than 10,000 lines.
        $piece_out_files = 0;
    }
    elsif ($arg eq "-f") { # Full Output -- Write the full output, even if a tag isn't used in a file. Not recommended with Direct Mode.
        $lightweight_mode = 0;
    }
    elsif ($arg eq "just") { # Just Mode -- Write the outputs only for the characters specified.
        $just_mode = 1;
    }
    elsif ($arg eq "-?" or $arg eq "-h") {
        $help_only = 1;
    }
    else { # Something else? Maybe this was a character we're calling in Just Mode.
        $arg_characters{$arg} = 1;
    }
}

if ($help_only) {
    write_help_text();
    exit;
}

if (not $lightweight_mode and $direct_write) {
    push(@final_warnings, "WARNING: You are writing all permutations directly into your project directory. This is allowed, but Ren'Py might have issues compiling and launching if the files are too large.");
    
    print $final_warnings[-1];
}

gather_filters();

# Set up our file writing, setting up the file name, current directory,
# and game directory (even if we aren't writing to that directory).
my $output_file_name = "chardefinitions.txt";
my $original_directory_name = getcwd;
my $game_directory_name = $original_directory_name;

# What we're doing here is taking the current directory, reversing it, and looking for
# the first instance of "/emag/", the game directory backwards. Then we'll reverse that
# result and tack "/game/" back onto it to make sure it's pointing to the right directory,
# even if the user has it inside some other folder called "game".
# There might be a cleaner way to do this, but... Sh-Shut up, dummy, it works!
my $reverse_directory_name = reverse $original_directory_name;
my @directory_slices = split /\/emag\//, $reverse_directory_name, 2;

if (!defined $directory_slices[1]) { # If we didn't find the game directory, we can't really create a correct file. But we'll try.
    push(@final_warnings, "WARNING: Could not find game directory above this level. Output will be written as though this directory is the game directory, which may not be correct for your code."); 
    
    print $final_warnings[-1];
    
    if ($direct_write) {
        print "The output will be written to \"chardefinitions_df.txt\" in this directory since direct write is not available without a game directory.";
        $output_file_name = "chardefinitions_df.txt";
        $direct_write = 0;
    }    
}
else {
    $game_directory_name = reverse $directory_slices[1];
    $game_directory_name = $game_directory_name . "/game/";
}

my $substring_start = length($game_directory_name); # This will snip the directory we're in, starting us with file names or subdirectory names

# We always want our output to start without a forward slash.
# If we failed to find a game directory, this extra one space
# takes care of that.
if ($game_directory_name eq $original_directory_name) {
    $substring_start += 1;
}

my $image_prefix = "image ";
my $open_composite = " = im.Composite(";
my $filter_composite = "im.Composite(";

my @characters;
my $current_character = "nobody";
my $current_character_directory_name;
my $short_directory_name;

my @digit_splitter;
my $found_digit;
my $found_prefix;
my $found_modifier;
my $this_is_first;

my @next_built_prefix;
my @next_sorting_prefix;
my $next_file_name;
my @file_name_helper;
my $currently_special;
my $currently_default;
my $currently_default_only;

my %exclude_directories;
my %offset_directories;
my %known_defaults;

# This is a 3-layer set of hashes.
# Layer 1: Character name
# Layer 2: Directory
# Layer 3: A digit, marking a render order.
# Layer 3 stores a value of how many times that digit appeared in subdirectories.
# If this is 1, then we don't need prefixes. 2 or more means the first thing within
# the subdirectory will need the prefix. But whichever one is the default will also
# need to shortcut to its appropriate prefix. 
my %character_directories;

# This is a set of hashes for writing lines to the final output.
# There are two places labels and file pieces will be printed.
# (Character Name) > Labels > (Sorting Prefix) > (Label) > (Value)
# (Character Name) > Special > (Label) > (Value)
# Keeping special separate allows us to loop through labels without adding special labels to anything.
my $final_outputs = {};

# It feels a bit inefficient to use Find more than once. 
# But it makes it easier to know what's coming for writing file names and their code tags.
# The first sweep takes inventory of all the directories we'll be working with.
# The second actually gets all of our relevant image file names and locations.
find( \&find_characters, $original_directory_name);

my $definitions_file_name;
my %abbreviation_index;
my %scraped_tags;

if ($lightweight_mode) {
    look_up_defined_characters();
    
    if ($write_status) {
        print "\nSearching through files for tags in use...";
    }
    
    find( \&find_tags_in_use, $game_directory_name);
}

assign_prefixes();
set_up_exclusions();

if ($write_status) {    
    print "\nCharacter directories established. Compiling image files now...";
}

find( \&organize_files, $original_directory_name);

my @line_prefix_stack;
my @line_image_stack;
my $line_filter;

my $final_flattened_list_ref;
my %final_flattened_list;

# TODO: Check for repeats

# By this point, we have our results and are ready to write them to the file!
if ($write_status) {
    print "\nFiles processed. Ready to write output to files.";    
}

my $lines_written = 0;
my $out;
my $output_file_suffix = 0;
my $lines_for_character = 0;

# We might need to switch files after every X lines written so the compiler can handle the large amounts of text!
# Handled below, defaults to 10,000 lines but can be changed from settings.txt.

foreach my $next_final_character(sort keys (%{$final_outputs})) {
    $current_character = $next_final_character;
    $lines_for_character = 0;
    $output_file_suffix = 0;
    
    if ($write_status) {
        if ($lightweight_mode) {
            print "\nComputing permutations for " . $current_character . " (including unused ones)...";
        }
        else {
            print "\nComputing permutations for " . $current_character . "...";        
        }

    }
    
#    print Dumper %{$final_outputs};
    
    $final_flattened_list_ref = get_tags_from_hash($$final_outputs{$next_final_character}, []);
    %final_flattened_list = %{$final_flattened_list_ref};    
    
    if ($write_status) {
        print "Permutations calculated. Writing to file...";
    }
    
    if ($direct_write) {
        if (!defined $directory_slices[1]) {
            $output_file_name = "chardefinitions_df_" . $current_character . ".txt";
        }
        else {
            $output_file_name = "chardefinitions_" . $current_character . ".rpy";
            
            chdir $original_directory_name;
        }
    }
    else {
        $output_file_name = "chardefinitions_" . $current_character . ".txt";
    }
    
    if ($write_status) {
        print "\nWriting output for " . $current_character . " to " . $output_file_name . "...";
    }
    
    # Opening the output file this way blanks it.
    # If we did this earlier before we knew for sure we would be writing lines, we might blank it for nothing.
    open($out, '>', $output_file_name) or die "Could not open file '$output_file_name' $!";
    
    if ($direct_write) {
        # Now that our file is set up, we can handle our operations in the base directory like normal.
        # This might not be necessary, but it keeps us consistent and future proof!
        chdir $original_directory_name;
    }
    
    print $out $auto_generate_comment;
    print $out "# " . uc $next_final_character;
    $lines_written++;
    
    my @filter_names;
    my @next_filter_tag_set;
    
    if (exists($filters_by_character{$current_character})) {
        @filter_names = sort keys(%{$filters_by_character{$current_character}});
    }
    else
    {
        @filter_names = ();
    }
        
    foreach my $next_tag_key(sort keys (%final_flattened_list)) {
        @line_prefix_stack = ( $next_tag_key );
        @line_image_stack = @{$final_flattened_list{$next_tag_key}};
        $line_filter = "";
        
        if (not $lightweight_mode or exists($scraped_tags{$current_character}{$next_tag_key})) {
            write_next_line();
            $lines_written++;
            $lines_for_character++;
            
            #foreach my $next_filter(sort keys (%filters)) {
            foreach my $next_filter(@filter_names) {
                if (not $lightweight_mode or exists($scraped_tags{$current_character}{$next_filter}{$next_tag_key}))
                {
                    $line_filter = $next_filter;
                    write_next_line();
                    $lines_written++;
                    $lines_for_character++;
                    
                    $additional_filter_calls{$current_character}{$next_filter}{$next_tag_key} = 0;
                }
            }
        }        
        
        if ($piece_out_files and ($lines_for_character >= $lines_per_file)) { # We just wrote 10,000 (or other value) lines. Time to switch!
            print $out "\n";
            close $out;
            
            $output_file_suffix++;
            $lines_for_character = 0;
            
            if ($direct_write) {
                if (!defined $directory_slices[1]) {
                    $output_file_name = "chardefinitions_df_" . $current_character . $output_file_suffix . ".txt";
                }
                else {
                    $output_file_name = "chardefinitions_" . $current_character . $output_file_suffix . ".rpy";
                    
                    chdir $original_directory_name;
                }
            }
            else {
                $output_file_name = "chardefinitions_" . $current_character . $output_file_suffix . ".txt";
            }
            
            open($out, '>', $output_file_name) or die "Could not open file '$output_file_name' $!";
    
            if ($direct_write) {
                # Now that our file is set up, we can handle our operations in the base directory like normal.
                # This might not be necessary, but it keeps us consistent and future proof!
                chdir $original_directory_name;
            }
        
            if ($write_status) {
                print $lines_per_file . " lines written. Switching files to " . $output_file_name . " and continuing...";
            }
            
            print $out $auto_generate_comment;
            print $out "# " . uc $next_final_character;
            $lines_written++;
        }
    }
    
    print $out "";
    
    my $print_outside_header = 1;
    
    foreach my $next_filter(@filter_names) {
        if (exists($additional_filter_calls{$current_character}{$next_filter})){
            @next_filter_tag_set = sort keys(%{$additional_filter_calls{$current_character}{$next_filter}});
            $line_filter = $next_filter;
            
            foreach my $next_tag(@next_filter_tag_set) {
                # This skips any tag we've already written once.
                next unless exists($additional_filter_calls{$current_character}{$next_filter}{$next_tag}) and $additional_filter_calls{$current_character}{$next_filter}{$next_tag};
                
                if ($print_outside_header) {
                    $print_outside_header = 0;
                    print $out "# OUTSIDE TAGS";
                    
                    if (not $no_outside_init) {
                        print $out "init " . $outside_image_init_level . ":";
                    }
                }
                
                @line_prefix_stack = ( $next_tag );
                
                if ($no_outside_init) {
                    write_next_line();
                }
                else {
                    write_next_line(1);
                }
            }
        }
    }

    
    print $out "\n";
    
    close $out;
}

my $end_time = DateTime->now();

if ($write_status and 0 < scalar(@final_warnings)) {
    print "\nFINAL REMINDERS:";
    
    foreach my $next_warning(@final_warnings) {
        print $next_warning;
    }
}

print "\nFile generation completed! Wrote " . $lines_written . " lines in " . ($end_time - $start_time)->in_units("seconds") . " seconds.";

# First step is to gather our directories and see what's inside what.
# We can get our list of characters we're creating images for and see
# which directories need prefixes.
# A directory needs a prefix if it has multiple directories of the same
# leading number inside--the third character will be the prefix for that
# sub-directory.
sub find_characters {
    if ($_ =~ /^\./
        or $File::Find::name =~ /.*\/i_.*/) {
        return;
    }
    
    if ($_ =~ /^\w+$/) { # This is a directory
        if ($File::Find::dir eq $original_directory_name) { # We're on the top directory, which means this is a new character folder.
            $current_character = $_;
            my $use_character = 1;
            
            if ($just_mode and not exists($arg_characters{$current_character})) { # Skip this character
                if ($write_status) {
                    print "Skipping " . $current_character;
                }
                return;
            }
            
            push(@characters, $current_character);
            $current_character_directory_name = $File::Find::name;
            
            if ($write_status) {
                if ($just_mode and 1 == scalar (keys (%arg_characters))) {
                    print "Just " . $current_character;
                }
                else {
                    print "Found Character: " . $current_character;                    
                }
            }
        
            $character_directories{$current_character}{substr $current_character_directory_name, $substring_start}{"First"} = 0;
            $character_directories{$current_character}{substr $current_character_directory_name, $substring_start}{"Prefix"} = "";
            $character_directories{$current_character}{substr $current_character_directory_name, $substring_start}{"Assigns Prefix"} = 0;
            $character_directories{$current_character}{substr $current_character_directory_name, $substring_start}{"Digit"} = "";
            $character_directories{$current_character}{substr $current_character_directory_name, $substring_start}{"Sorting Prefix"} = "";
            $character_directories{$current_character}{substr $current_character_directory_name, $substring_start}{"Also Default"} = 0;
        }
        else {
            if ($just_mode and not exists($arg_characters{$current_character})) {
                return;
            }
    
            $short_directory_name = substr $File::Find::name, $substring_start;
            $this_is_first = 0;
    
            # Do some grouping so we know which directories will need prefixes and which won't.
            foreach my $nextDirectory(sort keys %{ $character_directories{$current_character} }) {
                if ($short_directory_name =~ /${nextDirectory}\/\d+_\w+$/) {
                    
                    # First, reverse the directory and get everything "before" the first forward slash
                    $found_digit = reverse $short_directory_name;
                    @digit_splitter = split /\//, $found_digit, 2;
                    
                    # Now unreverse it and get everything before the underscore
                    $found_digit = reverse $digit_splitter[0];
                    @digit_splitter = split(/_/, $found_digit);
                    
                    # That's our leading digit.
                    $found_digit = $digit_splitter[0];
                    
                    # Grab our prefix in case we need it -- Always a single character.
                    $found_prefix = substr $digit_splitter[1], 0, 1;
            
                    #$directoryPrefixes{$short_directory_name} = $found_prefix;
                    
                    # We'll check for a modifier in a moment.
                    $found_modifier = $digit_splitter[-1];
                    
                    if (not exists($character_directories{$current_character}{$nextDirectory}{$found_digit})) {
                        $character_directories{$current_character}{$nextDirectory}{$found_digit} = 0;
                    }
                    
                    $character_directories{$current_character}{$nextDirectory}{$found_digit} += 1;
                    
                    if ($found_digit == 1) {
                        $this_is_first = 1;
                    }
                    else {
                        $this_is_first = 0;
                    }
            
                    $character_directories{$current_character}{$short_directory_name}{"Prefix"} = $found_prefix;
                    $character_directories{$current_character}{$short_directory_name}{"Digit"} = $found_digit;
                    $character_directories{$current_character}{$short_directory_name}{"Assigns Prefix"} = 0;
                    $character_directories{$current_character}{$short_directory_name}{"Did Report Prefix"} = 0;
                    $character_directories{$current_character}{substr $current_character_directory_name, $substring_start}{"Sorting Prefix"} = "";
                    $character_directories{$current_character}{$short_directory_name}{"Also Default"} = 0;
                    
                }
            }
            
            # This works as a quick way to define a new hash we can use later.            
            $character_directories{$current_character}{$short_directory_name}{"First"} = $this_is_first;
        }
    }
    elsif ($_ =~ /^settings.txt$/ or ($_ =~ /.*\.txt$/ and ($current_character ne "nobody") # A text file to read
            and not ($just_mode and not exists($arg_characters{$current_character})))) {
        # Open that file
        my $in_file;
        
        open($in_file, '<', $_) or warn "Could not open file '$_' $!";
        
        if ($write_status) {
            print "Reading instructions from " . $_;
        }
        
        my @split_line;
        my $exclude_subject;
        my $exclude_receiver;
        
        my $offset_subject;
        my $offset_value;
        my $offset_requester;
        my $message_piece;
        my $any_message_written = 0;
    
        # Read in each line
        while (my $next_read_line = <$in_file>) {
            chomp $next_read_line; # Remove the trailing newline we know will be there
        
            if ($next_read_line =~ /^exclude [\d\w]+ from [\d\w]+$/) { # Exclude that directory from this directory
                @split_line = split(" ", $next_read_line);
                
                $exclude_subject = $split_line[1];
                $exclude_receiver = $split_line[3];
                
                # Handle the exclusion here
                $exclude_directories{$current_character}{substr($File::Find::dir, $substring_start)}{$exclude_receiver}{$exclude_subject} = 1;
                
                if ($write_status) {
                    $any_message_written = 1;
                    print $exclude_subject . " will be excluded from " . $exclude_receiver . " for " . $current_character;
                }
            }
            elsif ($next_read_line =~ /^offset [\d\w]+ by \(-?\d+, -?\d+\) for [\d\w]+$/) { # Offset that directory by this much for this directory
                @split_line = split(" ", $next_read_line);
                
                $offset_subject = $split_line[1];
                $offset_value = $split_line[3] . " " . $split_line[4];                
                $offset_requester = $split_line[6];
                
                $offset_directories{$current_character}{substr($File::Find::dir, $substring_start)}{$offset_requester}{$offset_subject} = $offset_value;
        
                if ($write_status) {
                    $any_message_written = 1;
                    print $offset_subject . " will be offset by " . $offset_value . " with " . $offset_requester . " for " . $current_character;
                }
            }
            elsif ($next_read_line =~ /^Lines Per File : \d+$/) { # Setting how many lines are allowed in each output file
                @split_line = split(" ", $next_read_line);
                
                $lines_per_file = $split_line[-1];
        
                if ($write_status) {
                    $any_message_written = 1;
                    print "Setting Lines Per File value to " . $lines_per_file;
                }
            }
            elsif ($next_read_line =~ /^Image Size : \(\d+, \d+\)$/) { # Setting the size of each image
                @split_line = split(" ", $next_read_line);
                
                $image_size = $split_line[-2] . " " . $split_line[-1];
                
                if ($write_status) {
                    $any_message_written = 1;
                    print "Setting Image Size to " . $image_size;
                }
            }
            elsif ($next_read_line =~ /^Last To First Filters: \d+$/) { # Should filter effects on the same pose be applied in first-to-last or last-to-first order?
                @split_line = split(" ", $next_read_line);
                
                $last_to_first_filters = $split_line[-1];
                
                if ($write_status) {
                    $any_message_written = 1;
                    
                    if ($last_to_first_filters) {
                        $message_piece = "True";
                    }
                    else {
                        $message_piece = "False";
                    }
                    
                    print "Setting Last To First Filters to " . $message_piece;
                }
            }
            elsif ($next_read_line =~ /^Outside Image Init Level: \d+$/) { # What init level do we use if we're adding filters to outside images?
                @split_line = split(" ", $next_read_line);
                
                $outside_image_init_level = $split_line[-1];
                
                if ($write_status) {
                    $any_message_written = 1;                    
                    print "Setting Outside Image Init Level to " . $outside_image_init_level;
                }
                
                if (500 == $outside_image_init_level)
                {
                    $no_outside_init = 1;
                }
            }
        }
        
        if ($any_message_written) {
            print "";
        }
        
        close $in_file;
    }
}

sub assign_prefixes {
    my $reported_prefix;
    my $reported_parent_directory;
    my @parent_directory_splitter;
    
    my $reported_directory;
    my @current_directory_splitter;
    my @default_tag_list;
    
    my @exclude_directory_splitter;
    my $exclude_directory_key;
    my $parent_directory_key;
    
    my $next_default_tag;
    my @next_default_splitter;
    
    # Now that we've gathered all the directories, we can set up a final prefix for each one.
    # We just... need to... loop them all over each other is all...
    # O(n^2) makes me a sad kitsune, but that's why Perl's swiftness matters all the more.
    # It's also pretty acceptable since this script is for single uses, not "every frame update" running.
    foreach my $next_character_key(sort keys %character_directories) {
        if ($write_status) {
            print "\nAssigning prefixes for " . $next_character_key . "...";
        
            #print Dumper %{$character_directories{$next_character_key}};
        }
    
        foreach my $next_directory_key(sort keys %{ $character_directories{$next_character_key} }) {
            
            $character_directories{$next_character_key}{$next_directory_key}{"Printed Prefix"} = "";
            
            @next_built_prefix = (); # Clear the old one
            @next_sorting_prefix = ();
            
            $found_digit = $character_directories{$next_character_key}{$next_directory_key}{"Digit"};
            
            if (defined $found_digit
                and $found_digit
                and -1 < $found_digit) { # This isn't a folder with a digit, we skip it
            
                foreach my $next_parent_key(sort keys %{ $character_directories{$next_character_key} }) {
                    if (length($next_parent_key) < length($next_directory_key)) { # We only care about potential parent directories
                        
                        if ($next_directory_key =~ /${next_parent_key}\/[\d\w]+/) { # The parent we're looking at is indeed this folder's immediate parent
                            
                            push (@next_sorting_prefix, "" . $character_directories{$next_character_key}{$next_parent_key}{"Sorting Prefix"});
                            
                            if (exists($character_directories{$next_character_key}{$next_parent_key}{$found_digit})
                                and 1 < $character_directories{$next_character_key}{$next_parent_key}{$found_digit}) { # We need to pass down our prefix
                                $character_directories{$next_character_key}{$next_directory_key}{"Assigns Prefix"} = 1;        
                            }
                            
                            if ($character_directories{$next_character_key}{$next_directory_key}{"First"} # This section only cares about "First" directories, which need prefixes
                                and $character_directories{$next_character_key}{$next_parent_key}{"Assigns Prefix"}) { # Prefix adding time!
                                    push (@next_built_prefix, $character_directories{$next_character_key}{$next_parent_key}{"Prefix"});
                    
                                    if (not $character_directories{$next_character_key}{$next_parent_key}{"Did Report Prefix"}) {
                                        $character_directories{$next_character_key}{$next_parent_key}{"Did Report Prefix"} = 1;
                                        
                                        if ($next_parent_key =~ /_def$/
                                            and 0 < length($character_directories{$next_character_key}{$next_parent_key}{"Prefix"})) {
                                            $character_directories{$next_character_key}{$next_directory_key}{"Also Default"} = 1;
                                            
                                            $next_default_tag = $character_directories{$next_character_key}{$next_parent_key}{"Sorting Prefix"};
                                            @next_default_splitter = split(",", $next_default_tag);
                                            pop @next_default_splitter;
                                            $next_default_tag = join(",", @next_default_splitter);
                                            
                                            $known_defaults{$next_character_key}{$next_default_tag} = $character_directories{$next_character_key}{$next_parent_key}{"Prefix"};
                                        }
                                        
                                        if ($write_status) {
                                            $reported_prefix = $character_directories{$next_character_key}{$next_parent_key}{"Prefix"};
                        
                                            # This trick again--reverse the directory, split on "/", get the first piece,
                                            # and reverse it again to get just the name of our direct parent.
                                            $reported_parent_directory = reverse $next_parent_key;                                            
                                            @parent_directory_splitter = split("/", $reported_parent_directory, 2);
                                            $reported_parent_directory = $parent_directory_splitter[0];
                                            $reported_parent_directory = reverse $reported_parent_directory;
                                            
                                            print "Adding prefix " . $reported_prefix . " for " . $reported_parent_directory;
                                            
                                            if ($character_directories{$next_character_key}{$next_directory_key}{"Also Default"}) {
                                                print "Also recognizing " . $reported_parent_directory . " as the default option.";
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
        
                $character_directories{$next_character_key}{$next_directory_key}{"Printed Prefix"} = join ("", @next_built_prefix);
            }
            
            if (0 < length(join ("", @next_sorting_prefix))
                and (exists($character_directories{$next_character_key}{$next_directory_key}{"Digit"})
                or exists($character_directories{$next_character_key}{$next_directory_key}{"Prefix"}))) {
                push(@next_sorting_prefix, ",");
            }
            
            if (exists($character_directories{$next_character_key}{$next_directory_key}{"Digit"})) {
                push(@next_sorting_prefix, "" . $character_directories{$next_character_key}{$next_directory_key}{"Digit"});
            }
        
            if (exists($character_directories{$next_character_key}{$next_directory_key}{"Digit"})
                and exists($character_directories{$next_character_key}{$next_directory_key}{"Prefix"})
                and 1 < length($character_directories{$next_character_key}{$next_directory_key}{"Digit"} . $character_directories{$next_character_key}{$next_directory_key}{"Prefix"})) {
                push(@next_sorting_prefix, ",");
            }
            
            if (exists($character_directories{$next_character_key}{$next_directory_key}{"Prefix"})) {
                push(@next_sorting_prefix, "" . $character_directories{$next_character_key}{$next_directory_key}{"Prefix"});
            }
        
            $character_directories{$next_character_key}{$next_directory_key}{"Sorting Prefix"} = join ("", @next_sorting_prefix);
            
            if ($next_directory_key =~ /_opt$/) {
                if ($write_status) {
                    $reported_directory = reverse $next_directory_key;                                            
                    @current_directory_splitter = split("/", $reported_directory, 2);
                    $reported_directory = $current_directory_splitter[0];
                    $reported_directory = reverse $reported_directory;
                    
                    print "Recognized " . $reported_directory . " as an optional directory.";
                }
                
                @default_tag_list = split(",", $character_directories{$next_character_key}{$next_directory_key}{"Sorting Prefix"});
                unshift(@default_tag_list, $next_character_key);
                push(@default_tag_list, $character_directories{$next_character_key}{$next_directory_key}{"Printed Prefix"});
                push(@default_tag_list, "");
                
                push_to_final_outputs(@default_tag_list);
            }
        }
    }
    
    #print Dumper %character_directories;
#    print Dumper %exclude_directories;
}

sub set_up_exclusions {
    my $next_sorting_prefix;
    my $next_prefix_begin;
    my $next_prefix_end;
    my @prefix_splitter;
    
    foreach my $next_character_key(sort keys(%exclude_directories)) {
        if ($write_status) {
            print "\nFinalizing excludes for " . $next_character_key . "...";
        }
        
        foreach my $next_directory_key(sort keys(%{$exclude_directories{$next_character_key}})) {
            foreach my $next_sub_directory_key(sort keys(%{$exclude_directories{$next_character_key}{$next_directory_key}})) {
                $next_sorting_prefix = $character_directories{$next_character_key}{$next_directory_key . "/" . $next_sub_directory_key}{"Sorting Prefix"};
                
                next if not defined $next_sorting_prefix;
                
                @prefix_splitter = split(",", $next_sorting_prefix);
                $next_prefix_end = pop(@prefix_splitter);
                $next_prefix_begin = join(",", @prefix_splitter);
                
                foreach my $next_exclude_key(sort keys(%{$exclude_directories{$next_character_key}{$next_directory_key}{$next_sub_directory_key}})) {                    
                    
                    $exclude_directories{$next_character_key}{$next_prefix_begin}{$next_prefix_end}{$next_exclude_key} = $exclude_directories{$next_character_key}{$next_directory_key}{$next_sub_directory_key}{$next_exclude_key};
                }
            }
        }
    }
    
    foreach my $next_character_key(sort keys(%offset_directories)) {
        if ($write_status) {
            print "\nFinalizing offsets for " . $next_character_key . "...";
        }
    
        foreach my $next_offset_directory_key(sort keys (%{$offset_directories{$next_character_key}})) {
            foreach my $next_offset_sub_directory_key(sort keys(%{$offset_directories{$next_character_key}{$next_offset_directory_key}})) {
                $next_sorting_prefix = $character_directories{$next_character_key}{$next_offset_directory_key . "/" . $next_offset_sub_directory_key}{"Sorting Prefix"};
                
                next if not defined $next_sorting_prefix;
                
                foreach my $next_offset_key(sort keys(%{$offset_directories{$next_character_key}{$next_offset_directory_key}{$next_offset_sub_directory_key}})) {                    
                    
                    $offset_directories{$next_character_key}{$next_sorting_prefix}{$next_offset_key} = $offset_directories{$next_character_key}{$next_offset_directory_key}{$next_offset_sub_directory_key}{$next_offset_key};
                }
            }
        }
    }
    
#    print Dumper %offset_directories;
}

sub look_up_defined_characters {
    $definitions_file_name = $game_directory_name . "definitions.rpy";
    my $definitions_file;
    my $file_opened = 0;
    
    if (-f $definitions_file_name) {
        open($definitions_file, '<', $definitions_file_name) or die "Could not open the definitions file in your game directory even though it exists. $!";
        $file_opened = 1;
    
        if ($write_status) {
            print "\nChecking definitions.rpy for defined Dynamic Characters using images for characters this tool has detected...";
        }
            
    }
    else {
        if ($write_status) {
            print "\nCould not find definitions.rpy in the game directory. Checking sub directories...";
        
            find (\&check_for_definitions_file_name, $game_directory_name);
        
            if (-f $definitions_file_name) {
                open($definitions_file, '<', $definitions_file_name) or die "Could not open the definitions file in your game directory even though it exists. $!";
                $file_opened = 1;
                
                if ($write_status) {
                    print "Definitions file found. Checking for defined Dynamic Characters using images for characters this tool has detected...";
                }
            }
            elsif ($write_status) {
                print "Could not find a definitions file. Only lines of code using the \"show\" statement will be considered.";
            }
        }
    }
    
    if ($file_opened) {
        my $found_character;
        my $found_abbreviation;
        my @character_split;
        my @abbreviation_split;
        
        while (my $next_read_line = <$definitions_file>) {
            chomp $next_read_line; # Remove the trailing newline we know will be there
            
            $next_read_line = trim($next_read_line);
            
            next if ($next_read_line =~ /^#/); # Always skip comment lines
            
            if ($next_read_line =~ /^define\s+\w+\s+=\s+DynamicCharacter\(.*image=['"]\w+['"]/) { # A Dynamic Character! Is it using one of our characters?
                @character_split = split("image=", $next_read_line, 2);
                $found_character = $character_split[1]; # The whole tail end of the line
                
                @character_split = split(",", $found_character, 2);
                $found_character = $character_split[0]; # The name with quotes
                
                $found_character = strip_quotes($found_character); # Just the character name.
                
                if (exists($character_directories{$found_character})) { # It's one of ours! Get the abbreviation.
                    @abbreviation_split = split(" ", $next_read_line, 3);
                    $found_abbreviation = $abbreviation_split[1];
                    
                    if (not exists ($abbreviation_index{$found_character})) {
                        $abbreviation_index{$found_character} = ();
                    }
                    
                    push(@{$abbreviation_index{$found_character}}, $found_abbreviation);
                    
                    if ($write_status) {
                        print "Recognized " . $found_abbreviation . " as an abbreviation for " . $found_character . ".";
                    }
                }
            }
        }
        
        close($definitions_file);
    }
}

sub check_for_definitions_file_name {
    if ($_ eq "definitions.rpy") {
        $definitions_file_name = $File::Find::name;
    }
}

sub find_tags_in_use {
    if (not $_ =~ /\.rpy$/) {
        return;
    }
    
    if ($_ =~ /^chardefinitions/) { # We aren't reading our own files.
        return;
    }
    
    my $next_found_tag;
    my $next_found_filter;
    my @found_filter_list;
    my $next_script_file;
    my @next_line_split;
    my $line_scraped = 0;
    my $legit_filter = 0;
    
    open($next_script_file, '<', $_) or die "Could not open file $_ ; $!";     
    
    while (my $next_read_line = <$next_script_file>) {
        chomp $next_read_line; # Remove the trailing newline we know will be there
        
        $next_read_line = trim($next_read_line);
        
        next if ($next_read_line =~ /^#/); # Always skip comment lines
        
        $next_found_tag = "";
        $next_found_filter = "";
        @found_filter_list = ();
        $line_scraped = 0;
        
        foreach my $next_character(sort keys(%character_directories)) {
            next if $line_scraped;
            
            if (exists ($abbreviation_index{$next_character})) {
                foreach my $next_abbreviation($abbreviation_index{$next_character}[0]) { # Pose as part of a say statement
                    if ($next_read_line =~ /^$next_abbreviation\s+\w+/) {
                        @next_line_split = split("\"", $next_read_line, 2);
                        @next_line_split = split(" ", $next_line_split[0]);
                        $next_found_tag = $next_line_split[1];
                        
                        for (my $i = 1; $i < scalar(@next_line_split); $i++) {
                            $next_found_filter = $next_line_split[$i];
                            
                            while ($next_found_filter =~ /\w+:/) {
                                $next_found_filter = substr($next_found_filter, 0, -1); # Removes the last character, which is ':'
                            }
                            
                            if (0 < length($next_found_filter) and exists($filters{$next_found_filter})) { # Make sure the filter exists before we note it
                                push(@found_filter_list, $next_found_filter);
                            }
                        }

                        $next_found_filter = join(" ", @found_filter_list);
                    }
                }
            }
            
            if ($next_read_line =~ /^show\s+$next_character\s+\w+/) { # Show Statement
                @next_line_split = split(" ", $next_read_line);
                $next_found_tag = $next_line_split[2]; # 0 is "show", 1 is character name, 2 is tag
                
                for (my $i = 3; $i < scalar(@next_line_split); $i++) {
                    $next_found_filter = $next_line_split[$i];
                    
                    if (exists($show_statement_stops{$next_found_filter})) {
                        $i = scalar(@next_line_split);
                        next; # Escape the loop since there will be no more filters here.
                    }

                    while ($next_found_filter =~ /\w+:/) {
                        $next_found_filter = substr($next_found_filter, 0, -1); # Removes the last character, which is ':'
                    }

                    if (0 < length($next_found_filter) and exists($filters{$next_found_filter})) { # Make sure the filter exists before we note it
                        push(@found_filter_list, $next_found_filter);
                    }
                }
                
                $next_found_filter = join(" ", @found_filter_list);
            }
            
            if ($next_read_line =~ /^"$next_character(\s+\w+)+".*/) { # Quoted pose as part of an animation
                @next_line_split = split("\"", $next_read_line);
                @next_line_split = split(" ", $next_line_split[1]); # First is empty string, second is everything else.
                $next_found_tag = $next_line_split[1]; # 0 is character name, 1 is tag
                
                for (my $i = 2; $i < scalar(@next_line_split); $i++) {
                    $next_found_filter = $next_line_split[$i];
                    
                    if (exists($show_statement_stops{$next_found_filter})) {
                        $i = scalar(@next_line_split);
                        next; # Escape the loop since there will be no more filters here.
                    }

                    while ($next_found_filter =~ /\w+:/) {
                        $next_found_filter = substr($next_found_filter, 0, -1); # Removes the last character, which is ':'
                    }

                    if (0 < length($next_found_filter) and exists($filters{$next_found_filter})) { # Make sure the filter exists before we note it
                        push(@found_filter_list, $next_found_filter);
                    }
                }
                
                $next_found_filter = join(" ", @found_filter_list);
            }
            
            while ($next_found_tag =~ /\w+:/) {
                
                $next_found_tag = substr($next_found_tag, 0, -1); # Removes the last character, which is ':'
            }
            
            if (0 < length($next_found_tag)) {
                $line_scraped = 1;
                
                if (exists($filters{$next_found_tag}) or (exists($scraped_tags{$next_character}{$next_found_tag}) and $scraped_tags{$next_character}{$next_found_tag} != 1)) {
                    push(@final_warnings, "WARNING: Found a tag in your code files for " . $next_character . " with the same name as the filter \"" . $next_found_tag . "\". Skipping this tag due to technical issues.");
                    print "WARNING: Found a tag in your code files for " . $next_character . " with the same name as the filter \"" . $next_found_tag . "\". Skipping this tag due to technical issues.";
                }
                else {
                    $scraped_tags{$next_character}{$next_found_tag} = 1;
                }
                
                if (0 < length($next_found_filter)) { # If there's a filter on this tag, we also need to mark that for later.
                    
                    if (not exists($scraped_tags{$next_character}{$next_found_filter}) or $scraped_tags{$next_character}{$next_found_filter} == 1) {
                        if (exists($scraped_tags{$next_character}{$next_found_filter}) and $scraped_tags{$next_character}{$next_found_filter} == 1) {
                            push(@final_warnings, "WARNING: Found a tag in your code files for " . $next_character . " with the same name as the filter \"" . $next_found_tag . "\". Skipping this tag due to technical issues.");
                            print "WARNING: Found a tag in your code files for " . $next_character . " with the same name as the filter " . $next_found_tag . ". Skipping this tag due to technical issues.";
                        }
                        $scraped_tags{$next_character}{$next_found_filter} = ();
                    }
                    
                    $scraped_tags{$next_character}{$next_found_filter}{$next_found_tag} = 1;
                    $filters_by_character{$next_character}{$next_found_filter} = 1;
                    
                    $additional_filter_calls{$next_character}{$next_found_filter}{$next_found_tag} = 1;
                }
            }
        }
    }    
}

sub organize_files {
    # Filter out files which start with a '.' (usually hidden system files),
    # files tagged to be ignored with "i_" at the start,
    # and .rpy files or Perl scripts (this file)
    if ($_ =~ /^\.|.*\.pl$|.*\.rpy/
        or $File::Find::name =~ /.*\/i_.*/) {
        return;
    }
    
    $short_directory_name = substr $File::Find::dir, $substring_start;
    
    if ($_ =~ /^\w+$/) { # We're looking at a directory.
        if ($File::Find::dir eq $original_directory_name) { # We're on the top directory, which means this is a new character folder.
            
            my $new_character = 0;
            
            if ($current_character ne $_) {
                $new_character = 1;
            }
        
            $current_character = $_;
            
            if ($write_status and $new_character) {
                if (not ($just_mode and not exists($arg_characters{$current_character}))) {
                    print "\nCompiling images for " . $current_character . "...";
                }
            }
        }
    }
    
    if ($just_mode and not exists($arg_characters{$current_character})) {
        return;
    }
    
    # Used for special poses, like Natsuki vomit (poor Natsuki) which
    # will be named exactly as the files are listed instead of constructed
    if ($File::Find::dir =~ /.*\/special/) {
        $currently_special = 1;
    }
    else {
        $currently_special = 0;
    }
    
    # HANDLE IMAGE FILES HERE
    # New image file types can be added similarly to \.png and \.jpg below -- use '|' as a separator within the parentheses.
    if ($_ =~ /.*(\.png|\.jpg)$/) {
        
        if ($write_status and $currently_special) {
            print "Special pose found: " . $_;
        }
        
        # We have the prefix we need stored in Final Prefix in our hash.
        # Now we can append that to this file's extensionless name and
        # store it in a new key using the directory's digit as the key,
        # along with the file name we have here.
        # We'll put all the permutations together later!
    
        # Once more, we reverse, grab the end, and reverse again
        $next_file_name = reverse $_;
        @file_name_helper = split /\//, $next_file_name, 2;
        
        $next_file_name = $file_name_helper[0]; # We have a backwards name with extention now.
        $next_file_name = reverse $next_file_name;
        
        @file_name_helper = split /\./, $next_file_name, 2;
    
        $next_file_name = $file_name_helper[0]; # And that gives us our name without an extention.
    
        if ($write_status and ($next_file_name eq "base")) {
            my $printed_directory = reverse $short_directory_name;
            my @directory_name_splitter = split("/", $printed_directory, 2);
            $printed_directory = $directory_name_splitter[0];
            $printed_directory = reverse $printed_directory;
            
            print "Base image recognized in " . $printed_directory;
        }
        
        $currently_default = 0;
        $currently_default_only = 0;
    
        if (not $currently_special and $next_file_name =~ /.*_def$/) {
            $currently_default = 1;
        
            if ($next_file_name =~ /.*_only_def$/) {
                $currently_default_only = 1;
                
                if ($write_status) {
                    my $printed_directory = reverse $short_directory_name;
                    my @directory_name_splitter = split("/", $printed_directory, 2);
                    $printed_directory = $directory_name_splitter[0];
                    $printed_directory = reverse $printed_directory;
                    
                    print "Recognized " . $next_file_name . " as a default-only image for " . $printed_directory; 
                }
                
                $next_file_name = "";
            }
            else {
                if ($write_status) {
                    my $printed_directory = reverse $short_directory_name;
                    my @directory_name_splitter = split("/", $printed_directory, 2);
                    $printed_directory = $directory_name_splitter[0];
                    $printed_directory = reverse $printed_directory;
                    
                    print "Recognized " . $next_file_name . " as a default (but selectable) image for " . $printed_directory;
                    
                    @file_name_helper = split /_/, $next_file_name, 2;
                    $next_file_name = $file_name_helper[0];
                }
            }
        }
        
        my @prefix_key_set;
        
        if ($currently_special) {
            push @prefix_key_set, $current_character;
            push @prefix_key_set, "special";
            push @prefix_key_set, $next_file_name;
            push @prefix_key_set, substr($File::Find::name, $substring_start);
        }
        else {
            @prefix_key_set = split /,/, $character_directories{$current_character}{$short_directory_name}{"Sorting Prefix"};
            unshift @prefix_key_set, $current_character;
            
            if ($next_file_name eq "base") {
                push @prefix_key_set, $character_directories{$current_character}{$short_directory_name}{"Printed Prefix"};
            }
            else {
                push @prefix_key_set, $character_directories{$current_character}{$short_directory_name}{"Printed Prefix"} . $next_file_name;
            }

            push @prefix_key_set, substr($File::Find::name, $substring_start);            
        }
    
        push_to_final_outputs(@prefix_key_set);
        
        if ($currently_default and not $currently_default_only and $next_file_name ne "base") {
            @prefix_key_set = split /,/, $character_directories{$current_character}{$short_directory_name}{"Sorting Prefix"};
            unshift @prefix_key_set, $current_character;            
            
            push @prefix_key_set, $character_directories{$current_character}{$short_directory_name}{"Printed Prefix"};            

            push @prefix_key_set, substr($File::Find::name, $substring_start);
            
            push_to_final_outputs(@prefix_key_set);
        }
        
        if ($character_directories{$current_character}{$short_directory_name}{"Also Default"}) {
#            print "Using default option in " . $short_directory_name . " for " . $_;
            
            @prefix_key_set = split /,/, $character_directories{$current_character}{$short_directory_name}{"Sorting Prefix"};
            unshift @prefix_key_set, $current_character;
            
            if ($next_file_name eq "base") {
                push @prefix_key_set, "";
            }
            else {
                push @prefix_key_set, $next_file_name;
            }

            push @prefix_key_set, substr($File::Find::name, $substring_start);
            
#            print "Defaulted version of a default key:\n" . Dumper @prefix_key_set;
               
            push_to_final_outputs(@prefix_key_set);
        }
    }
}

sub push_to_final_outputs {
    # This solution was an adaptation of this handy answer offered on Stack Overflow:
    # https://stackoverflow.com/questions/11505100/perl-how-to-turn-array-into-nested-hash-keys
    my $ref   = \$final_outputs;
    my $value = pop;
    $ref      = \$$ref->{ $_ } foreach @_;
    $$ref     = $value;
    
    $ref        = \$final_outputs;
    my $lastKey = pop;
    $ref        = \$$ref->{ $_ } foreach @_;
    
    my %final_hash = %{$$ref};
    
    if (not exists($$ref->{"Printable Tags"})) {
        $$ref->{"Printable Tags"} = [];
    }
    
    push (@{$$ref->{"Printable Tags"}}, $lastKey);
    push (@_, $lastKey);
}

sub get_tags_from_hash {
    my ($hash, $in_tag_array) = @_;
    
    my %working_result_hash;
    my %ignored_tags;
    
    my @tag_array = @{$in_tag_array};
    
    if (exists $$hash{"Printable Tags"}) {
        my @printableTags = @{$$hash{"Printable Tags"}};
    
        $ignored_tags{"Printable Tags"} = 1;        
    
        foreach my $nextTag(@printableTags) {    
            $ignored_tags{$nextTag} = 1;
            
#            if (length($$hash{$nextTag}) < 1) {
#                print "Blank Tag: " . $$hash{$nextTag};
#                $working_result_hash{0}{$nextTag} = [""];
#            }
#            else {
                $working_result_hash{0}{$nextTag} = [ "(0, 0), \"" . $$hash{$nextTag} . "\"" ]; # We can trust that these values are string values.
#            }
        }
    }
    else {
        $working_result_hash{0}{"base"} = []; # Keeping a blank value here allows us to use our same logic later without needing special cases.
        push(@{$working_result_hash{0}{"base"}}, "");
    }
    
    my @numeric_tags; # We'll always be using 0 in this set.
    push(@numeric_tags, "0");
    my @alpha_tags;
    my @exclusive_numeric_tags;
    
    my @all_tags; # Zero may not need to be here, but doesn't waste much time and future-proofs the function.
    push(@all_tags, "0");
    
    my $tag_as_text;
    
    my $subhash_ref;
    my %next_subhash;
    
    my $next_exclude_key;
    my $next_combined_exclusive_key;
    
    # Get the non-printable tags, which lead to more hashes we can operate on to get results.
    foreach my $next_key(sort keys %{$hash}) {
        next if exists($ignored_tags{$next_key});
        
        $tag_as_text = "" . $next_key;
    
        $next_exclude_key = join(",", @tag_array, $next_key);
    
        if ($tag_as_text =~ /\d+/) { # The tag is one or more numbers
            if (exists($exclude_directories{$current_character}{$next_exclude_key})) {
                
                foreach my $next_sub_key(sort keys(%{$exclude_directories{$current_character}{$next_exclude_key}})) {
                    $next_combined_exclusive_key = join(",", $next_key, $next_sub_key);
                    
                    push(@exclusive_numeric_tags, $next_combined_exclusive_key);
                }
            }
            else {
                push(@numeric_tags, $next_key); # TODO: This doesn't actually work with our current logic. This should be an exclude key too.
            }
            
            push(@all_tags, $next_key);
        }
        elsif ($tag_as_text =~ /\w+/) { # The tag is one or more letters
            push(@alpha_tags, $next_key);
            push(@all_tags, $next_key);
        }
    }
    
    foreach my $next_key(@all_tags) {
        next if (("" . $next_key) eq "0"); # That was our special key, we're not retrieving it.
    
        push(@tag_array, $next_key);
        
        $subhash_ref = get_tags_from_hash($$hash{$next_key}, \@tag_array);
    
        pop(@tag_array);
    
        if (ref($subhash_ref) eq "HASH") { # I can't say I completely understand what happened here, but this does work.
            %next_subhash = %{$subhash_ref};
        }
        else {
            %next_subhash = %{$$subhash_ref};
        }
        
        foreach my $next_sub_key(sort keys %next_subhash) {
            $working_result_hash{$next_key}{$next_sub_key} = $next_subhash{$next_sub_key};
        }
    }
    
    my $exclude_key_begin;
    my $exclude_key_end;
    my @exclude_key_splitter;
    my @next_transfer_array;
    my %untransferred_keys;
    
    foreach my $next_exclusive_key(@exclusive_numeric_tags) {
        @exclude_key_splitter = split(",", $next_exclusive_key);
        $exclude_key_begin = $exclude_key_splitter[0];
        $exclude_key_end = $exclude_key_splitter[1];
        
        if (not exists($untransferred_keys{$exclude_key_begin})) {
            foreach my $next_untransferred_key(sort keys %{$working_result_hash{$exclude_key_begin}}) {
                $untransferred_keys{$exclude_key_begin}{$next_untransferred_key} = 1;
            }
        }
        
        foreach my $next_transfer_key(sort keys %{$working_result_hash{$exclude_key_begin}}) {
            if ($next_transfer_key =~ /^$exclude_key_end.*/) {
                
                if (exists($untransferred_keys{$exclude_key_begin}{$next_transfer_key})) {
                    delete $untransferred_keys{$exclude_key_begin}{$next_transfer_key};
                }
                
                @next_transfer_array = @{$working_result_hash{$exclude_key_begin}{$next_transfer_key}};
        
                foreach my $next_transfer_value(@next_transfer_array) {
                    push (@{$working_result_hash{$next_exclusive_key}{$next_transfer_key}}, $next_transfer_value);
                }
            }
        }
    }
    
    if (0 < scalar(@exclusive_numeric_tags)) {
        my $next_lookup_prefix;
        
        foreach my $next_leading_key(sort keys(%untransferred_keys)) {
            if (exists($known_defaults{$current_character}{$next_leading_key})) {
                $next_lookup_prefix = join(",", $next_leading_key, $known_defaults{$current_character}{$next_leading_key});
                
                foreach my $next_untransferred_key(sort keys(%{$untransferred_keys{$next_leading_key}})) {
                    @next_transfer_array = @{$working_result_hash{$next_leading_key}{$next_untransferred_key}};
                    
                    foreach my $next_transfer_value(@next_transfer_array) {
                        push (@{$working_result_hash{$next_lookup_prefix}{$next_untransferred_key}}, $next_transfer_value);
                    }
                }
            }
        }
    }
    
    # Next step is a recursive function which takes two lists of tags.
    # It shifts from the "in" list and pushes to the "out" list, then gets the result for the rest of the out list.
    # If nothing is in the "in" list, it returns an empty array.
    # Each recurse will get all of its results, then get all permutations with the next result it just got. (If it's empty, the current one is enough.)
    # When it's done, it will pop the "out" list and unshift to the "in" list, then return the result hash.
    
    my $compiled_result_ref;
    my %compiled_result;
    my $next_sub_compiled_hash_ref;
    my %next_sub_compiled_hash;
    my @next_key_set;
    
    my $next_exclude_specs_ref;
    my %next_exclude_specs;
    my $next_full_exclude_key;
    my @next_exclude_key_pieces;
    
    my $next_sorting_tag = join (",", @tag_array);
    
    # If there are no exclusions, numeric tags can all be thrown it at once since they will all be combined with each other.
    if (scalar(@exclusive_numeric_tags) < 1) {
        $compiled_result_ref = compile_results_for_tags(\%working_result_hash, $next_sorting_tag, \@numeric_tags, []);    
        
        if (ref($compiled_result_ref) eq "HASH") { # Again, i-it at least works.
            %compiled_result = %{$compiled_result_ref};
        }
        else {
            %compiled_result = %{$$compiled_result_ref};
        }
    }
    else { # We're dealing with exclusive tags
        # TODO: This is flawed logic which only works with one exclusion. Needs to be more rigorous later for multi-level excludes.
                
        foreach my $next_exclusive_key(@exclusive_numeric_tags) {
            
            $next_full_exclude_key = join(",", @tag_array, $next_exclusive_key);
            
            @next_exclude_key_pieces = split(",", $next_full_exclude_key);
            
            $next_exclude_specs_ref = \%{$exclude_directories{$current_character}};
            
            foreach my $next_main_exclude_key(@next_exclude_key_pieces) {        
                $next_exclude_specs_ref = \%{$next_exclude_specs_ref->{$next_main_exclude_key}};
            }
        
            %next_exclude_specs = %{$next_exclude_specs_ref};            
            
            push (@next_key_set, 0);
            push (@next_key_set, $next_exclusive_key);
        
            foreach my $next_numeric_key(@numeric_tags) {
                next if exists($next_exclude_specs{$next_numeric_key});
                
                push (@next_key_set, $next_numeric_key);
            }
            
            $next_sub_compiled_hash_ref = compile_results_for_tags(\%working_result_hash, $next_sorting_tag, \@next_key_set, []);
        
            if (ref($next_sub_compiled_hash_ref) eq "HASH") {
                %next_sub_compiled_hash = %{$next_sub_compiled_hash_ref};
            }
            else {
                %next_sub_compiled_hash = %{$$next_sub_compiled_hash_ref};
            }
    
            foreach my $next_found_sub_key(sort keys (%next_sub_compiled_hash)) {
                $compiled_result{$next_found_sub_key} = $next_sub_compiled_hash{$next_found_sub_key};
            }
            
            @next_key_set = ();
        }
    }
    
    @next_key_set = ();
    
    push (@next_key_set, 0);
    
    # Alpha tags (letters) are only combined with the 0 layer (usually a "base" image) and are kept separate from each other.
    # This loops through them all and sends them into the recursive function alone with 0, one by one.
    foreach my $next_alpha_key(@alpha_tags) {
        
        push(@next_key_set, $next_alpha_key);
        
        $next_sub_compiled_hash_ref = compile_results_for_tags(\%working_result_hash, $next_sorting_tag, \@next_key_set, []);
        
        if (ref($next_sub_compiled_hash_ref) eq "HASH") {
            %next_sub_compiled_hash = %{$next_sub_compiled_hash_ref};
        }
        else {
            %next_sub_compiled_hash = %{$$next_sub_compiled_hash_ref};
        }
    
        foreach my $next_found_sub_key(sort keys (%next_sub_compiled_hash)) {
            $compiled_result{$next_found_sub_key} = $next_sub_compiled_hash{$next_found_sub_key};
        }
    
        pop(@next_key_set);
    }
    
    return \%compiled_result;
}

sub compile_results_for_tags {
    my ($in_working_hash, $base_sorting_tag, $in_remaining_tags, $in_tags_in_progress) = @_;
    my %working_hash = %{$in_working_hash};
    my @remaining_tags = @{$in_remaining_tags};
    my @tags_in_progress = @{$in_tags_in_progress};
    
    if (scalar(@remaining_tags) < 1) {
        my %empty_hash = (); # This returns a reference to an empty hash instead of the raw empty hash--keeps our return result consistent.
        
        return \%empty_hash;
    }
    
    my $working_tag = shift(@remaining_tags);
    push(@tags_in_progress, $working_tag);
    
    # Anything that can be done with recursion can be done more efficiently
    # using less stack frames with a loop if you're smart enough to set it up.
    # I was not smart enough today, but this works.
    
    my $next_combined_tag;
    
    if ($working_tag eq "0") {
        $next_combined_tag = $base_sorting_tag;
    }
    elsif ($base_sorting_tag eq "") {
        $next_combined_tag = $working_tag;
    }
    else {
        $next_combined_tag = join(",", $base_sorting_tag, $working_tag);
    }
    
    my $raw_hash_result = compile_results_for_tags($in_working_hash, $next_combined_tag, \@remaining_tags, \@tags_in_progress); # Here's our recursive call
    
    my %next_subhash;
    
    if (ref($raw_hash_result) eq "HASH") {
        %next_subhash = %{$raw_hash_result};
    }
    else {
        %next_subhash = %{$$raw_hash_result};
    }
    
    my %result_hash = ();
    
    my @sub_tag_list = sort keys %{$working_hash{$working_tag}};
    my @next_image_string_result;
    my @next_sub_image_string_result; # Be careful not to get these two mixed up when reading from here!
    my @child_tag_list = sort keys %next_subhash;
    my $next_created_key;
    my $effective_left_key;
    my $effective_right_key;
    my $results_added; # The number of results added
    my $next_right_hand_value;
    
    if (scalar(@child_tag_list) < 1) { # No sub level, so we just bubble back our results
        foreach my $next_key(@sub_tag_list) {
            
            $results_added = 0;
            @next_image_string_result = @{$working_hash{$working_tag}{$next_key}};
            $result_hash{$next_key} = [];
            
            foreach my $next_string_result(@next_image_string_result) {
                next if (not defined $next_string_result
                        or $next_string_result eq "");
                
                push(@{$result_hash{$next_key}}, $next_string_result);
                $results_added++;
            }
        
            if (!$results_added) {
                delete $result_hash{$next_key}; # This prevents us from keeping "base" => "" which we add if we need a 0 layer.
            }
        }
    }
    else { # We need to combine each of my results with each result so far.
        my $next_sub_sorting_tag;

        foreach my $next_key(@sub_tag_list) {
            if ($next_key =~ /^\w.*/) {
                if (1 < length($next_key)) {
                    $next_sub_sorting_tag = $working_tag . "," . substr($next_key, 0, 1);
                }
                else {
                    $next_sub_sorting_tag = $working_tag . "," . $next_key;
                }
            }
            else {
                $next_sub_sorting_tag = "";
            }
            
            @next_image_string_result = @{$working_hash{$working_tag}{$next_key}};
    
            foreach my $next_sub_key(@child_tag_list) {
                
        
                @next_sub_image_string_result = @{$next_subhash{$next_sub_key}};
                
                $effective_left_key = $next_key;
                $effective_right_key = $next_sub_key;
            
                # If the key is "base", we know we aren't actually supposed to print that key.
                # Just grab the image location and add it in automatically.
                if ($effective_left_key eq "base") {
                    $effective_left_key = "";
                }
                
                if ($effective_right_key eq "base") {
                    $effective_right_key = "";
                }
                
                $next_created_key = $effective_left_key . $effective_right_key;
        
                if ($next_created_key eq "") { # We just merged two base tags--they'll be a new base tag (which will be blanked in another loop).
                    $next_created_key = "base";
                }
                
                $result_hash{$next_created_key} = [];
                
                # Put this level's results in front...
                foreach my $next_image_string(@next_image_string_result) {
                    next if (not defined($next_image_string)
                            or $next_image_string eq "");
                    
                    push(@{$result_hash{$next_created_key}}, $next_image_string);
                }
                
                # ... and the sub-level's results after it.
                foreach my $next_image_string(@next_sub_image_string_result) {
                    next if (not defined($next_image_string)
                            or $next_image_string eq "");
                    
                    $next_right_hand_value = $next_image_string;
            
                    if (0 < scalar (@remaining_tags)
                        and exists($offset_directories{$current_character}{$next_sub_sorting_tag}{$remaining_tags[0]})) {
                        $next_right_hand_value =~ s/\(\d+, \d+\)/$offset_directories{$current_character}{$next_sub_sorting_tag}{$remaining_tags[0]}/g
                    }
                    
                    push(@{$result_hash{$next_created_key}}, $next_right_hand_value);
                }
            }
        }
    }
    
    # Put the tags back how they were now that we're done with our part
    pop(@tags_in_progress);
    unshift(@remaining_tags, $working_tag);
    
    return \%result_hash;
}

sub write_next_line {
    my $indent_level = 0;
    
    if (0 < scalar(@_)) {
        $indent_level = $_[0];
    }
    
    my $output_line = "";
    
    for (my $i = 0; $i < $indent_level; $i++) {
        $output_line = $output_line . "    ";
    }
    
    if (0 < length($line_filter)) {
        my $filter_prefix = "";
        my $filter_suffix = "";
        my @list_of_filters = split(" ", $line_filter);
        
        foreach my $next_filter_name(@list_of_filters) {
            if ($last_to_first_filters) {
                $filter_prefix = $next_filter_name . "(" . $filter_prefix;                
            }
            else {
                $filter_prefix = $filter_prefix . $next_filter_name . "(";
            }
            
            $filter_suffix = $filter_suffix . ")"
        }
        
        $output_line = $output_line . $image_prefix . $current_character . " " . join("", @line_prefix_stack) . " " . $line_filter . " = " . $filter_prefix . "getCharacterImage(\"" . $current_character . "\", \"" . join("", @line_prefix_stack) . "\")" . $filter_suffix;
        #$output_line = $image_prefix . $current_character . " " . join("", @line_prefix_stack) . " " . $line_filter . " = " . $filter_prefix . $filter_composite . $image_size . ", " . join(", ", @line_image_stack) . $filter_suffix . ")";
    }
    else {
        $output_line = $output_line . $image_prefix . $current_character . " " . join("", @line_prefix_stack) . $open_composite . $image_size . ", " . join(", ", @line_image_stack) . ")";    
    }
    
    $output_line =~ s/(, )?\(\d+, \d+\), \"\"//g; # Simple fix for '(0, 0,), ""' which sometimes gets tacked on due to defaults.
    
#    print $out $image_prefix . $current_character . " " . join("", @line_prefix_stack) . $open_composite . $image_size . ", " . join(", ", @line_image_stack) . ")";
    print $out $output_line;
}

sub trim {
    my $s = shift;
    $s =~ s/^\s+|\s+$//g; # Remove leading and trailing whitespace
    return $s;
}

sub strip_quotes {
    my $s = shift;
    $s =~ s/['"]//g;
    return $s;
}

sub write_help_text {
    print "Dynamic Pose Tool v" . $version_number;
    print "Copyright 2018 J. Kyle Roth";
    print "Released under GNU General Public License\n";
    
    print "Usage:\n       perl Create_Definitions.pl [flags] [character names]\n";
    print "Flags and character names may be entered in any order.";
    print "Ex: perl Create_Definitions.pl -d just monika sayori";
    print "Ex: perl Create_Definitions.pl -f -s\n";
    
    print "Recognized Flags:";
    print "-h or -?    Show this help text and close.";
    print "-d          Direct Write. Write the output as .rpy files (in the game\n            directory if possible) instead of .txt files.";
    print "-s          Silent Write. Suppress console output except error messages.";
    print "-w          Whole File. Instead of splitting up large output files,\n            keep each character's output in a single file.";
    print "-f          Full Output. Write all permutations found for a character,\n            even if they are not used. Not recommended with Direct Write.";
    print "just        Just Mode. Unrecognized arguments will be treated as\n            character names. Output will only be written for characters\n            found this way.\n";
    
    return;
}

sub gather_filters {
    my $filter_file_name = "filters.txt";
    
    if ($write_status) {
        print "Checking for " . $filter_file_name . "...";
    }
    
    if (open(my $filter_file, '<', $filter_file_name)) {
        if ($write_status) {
            print "Compiling filters...";
        }
        
        my $next_filter_code;
        my $in_filter = 0;
        my $next_filter_name = "dummy";
        my @line_pieces;
        my @def_piece_helper;
        my $indent_level = 0;
        
        while (my $next_line = <$filter_file>) {
            chomp $next_line;
            $next_line = trim($next_line);
            
            if ($in_filter) {
                if ($next_line =~ /^\s*$/) { # Nothing but white space--signifies the end of the last block
                    $indent_level-- unless $indent_level <= 0;
                }
                
                for (my $i = 0; $i < ($indent_level + 2); $i++) {
                    $next_filter_code = $next_filter_code . "    ";
                }
                
                $next_filter_code = $next_filter_code . $next_line;
                
                if ($next_line =~ /return.*/) {
                    $filters{$next_filter_name} = $next_filter_code . "\n";
                    $in_filter = 0;
                    if ($write_status) {
                        print "Recognized filter: " . $next_filter_name;
                    }
                }
                elsif ($next_line =~ /.*:$/) { # Ends with a colon
                    $indent_level++;
                    $next_filter_code = $next_filter_code . "\n";
                }
                else {
                    $next_filter_code = $next_filter_code . "\n";
                }
                
            }
            else {
                if ($next_line =~ /(def )?\w+\(image.*\):/ ) { # We just found a new filter beginning
                    
                    @line_pieces = split(/\(/, $next_line, 2);
                    
                    if ($next_line =~/def .*/) {
                        @def_piece_helper = split(/ /, $line_pieces[0], 2);
                        
                        $next_filter_name = $def_piece_helper[1];
                        $next_filter_code = "    " . $next_line . "\n";
                    }
                    else {
                        
                    
                        $next_filter_name = $line_pieces[0];
                        $next_filter_code = "    def " . $next_line . "\n";
                    }
                    
                    $in_filter = 1;
                    $indent_level = 0;
                }
            }
            
            #print $next_line;
        }
        
        close $filter_file;
        
        my @filter_names = sort keys(%filters);
        my @filter_subset;
        my $last_index;
        my $printed_filter_list = "";
        
        if (0 < scalar(@filter_names)) {
            my $filter_effects_file_name = "filter_effects.rpy";
            
            if (open my $filter_effects_file, '>', $filter_effects_file_name) {
                if ($write_status) {
                    print "\nWriting filter effects file...";
                }
                
                print $filter_effects_file $auto_generate_comment;
                
                for (my $i = 0; $i < scalar(@filter_names); $i = $i + 5)
                {
                    if ($i + 5 < scalar(@filter_names)) {
                        $last_index = $i + 4;
                    }
                    else {
                        $last_index = scalar(@filter_names) - 1;
                    }
                    
                    $printed_filter_list = $printed_filter_list . "# " . join(", ", @filter_names[$i..$last_index]);
                    
                    if ($i + 5 < scalar(@filter_names)) {
                        $printed_filter_list = $printed_filter_list . ",";
                    }
                    
                    $printed_filter_list = $printed_filter_list . "\n";
                }
        
                print $filter_effects_file "# Filter Quick Reference List:\n" . $printed_filter_list . "\n";
                
                print $filter_effects_file "init python:";
                
                foreach my $next_name(@filter_names) {
                    print $filter_effects_file $filters{$next_name};
                }
        
                print $filter_effects_file $get_character_image_function;
                
                close $filter_effects_file;
                
                if ($write_status) {
                    print "Filter effects successfully written to " . $filter_effects_file_name . "!\n";
                }
            }
            else {                
                print "\nCould not open " . $filter_effects_file_name . ". Proceeding without writing, but using filters in tags as normal.\n";
            }
        }
        else {
            if ($write_status) {
                print "No filters recognized. Continuing without writing to filter_effects.rpy.\n";
            }
        }
        
    }
    else {
        if ($write_status) {
            print "No filter file found. Proceeding without filters.\n";
        }
    }
}
