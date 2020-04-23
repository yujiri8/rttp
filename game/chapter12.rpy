# I'm still really unsure about the zorder stuff here. Maybe renier should just always be on top of Natsuki.
label chapter12:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "I'm on my way to school as usual."
    "Although I often act annoyed when my friend Sayori chases after me on the way after she overslept and I couldn't wait for her any longer..."
    "I have to admit I'm disappointed to see no sign of her coming this time."
    "It's lonely."
    # If Sayori was already restored in ch11
    if persistent.mc_favorite == "Sayori" and not persistent.sayori_reset_ynr:
        show sayori u227112 at foc(p11)
        s "[mc_name]!"
        show sayori at uf
        mc "Aah!"
        mc "Sayori, don't sneak up on --{nw}"
        show sayori at foc
        s u223212 "[persistent.playername], do you know what happened?"
        s "Are we still in danger?"
        show sayori at uf
        menu:
            " "
            "Everything should be fine. Just wait until Linda gets here, she'll explain everything.":
                pass
        show sayori at foc
        s u115212 "Um... okay..."
        show sayori at uf
        mc "Sayori, what's going on?"
        mc "Who are you talking to?"
        show sayori at foc
        s u113121 "Ugh, this again..."
        show sayori at uf
        mc "What again?!?"
        show sayori u125111 at foc
        call updateconsole(mc_name.lower() + ".old_memories.unlock()", mc_name + "'s memories unlocked")
        call hideconsole
        $ consolehistory = []
        show sayori at uf
        mc "Ah--"
        mc "Haah..."
        mc "You know, I'm getting tired of losing my memories every time this happens."
        show sayori at std(p21)
        show linda 334111 at foc(p22)
        l "Here you two are..."
        l "Let's get everyone else warped over and their memories restored."
        call updateconsole("for char in ('yuri', 'natsuki'):\n  restore_character(char)")
        call updateconsole("for char in (monika, renier, yuri, natsuki):\n  warp(char, 'residential_day')")
        call hideconsole
        $ consolehistory = []
        $ restore_part1_characters()
        show linda at std(p66) zorder 3
        show renier ru2283 at std(p65)
        show natsuki u113113 at std(p64) zorder 1
        show yuri u227135 at foc(p63)
        show sayori at std(p62) zorder 1
        show monika u118211 at std(p61)
        y "--Eh?!?"
        show yuri at uf
        show linda at xif(p66)
        l 124111 "Don't panic everyone, we're going to restore your memories!"
        show linda at uf
        show renier at foc
        r "What the hell is happening?{w=0.4}{nw}"
        show renier at uf
        show natsuki at foc
        n "Who are you two?{w=0.4}{nw}"
        show natsuki at uf
        $ restore_all_mem_cmd = "for char in (renier, yuri, natsuki):\n  char.old_memories.unlock()"
        $ restore_all_mem_output = "Renier's memories unlocked\nYuri's memories unlocked\nNatsuki's memories unlocked"
    else:
        show linda 334111 at std(p11)
        "Out of thin air, a woman appears in front of me."
        show linda at foc
        l "I guess we're all gathering here again..."
        show linda at uf
        mc "Wha-"
        mc "How did you..?"
        show linda at foc
        l 334221 "Ugh... this again."
        l 334111 "Just a minute, [mc_name]."
        show linda at uf
        mc "... And how do you know my name?"
#        while not (check_character('monika') and check_character('sayori') and check_character('yuri') and check_character('natsuki')):
#            show linda at foc
#            l "[persistent.playername], I need you to put the rest of the character files in now."
#            l "I could try to use Monika's backups, but ."
#            show linda at uf
#            mc "Who are you talking to?"
#            " "
        show linda at foc
        l "..."
        show linda at uf
        "The woman continues to ignore me for a few seconds."
        # If persistent.sayori_reset_ynr, MC's favorite is already restored.
        # But if Sayori was already restored we'd be on the other branch.
        call updateconsole("s_name = 'Sayori'", "Sayori's name changed successfully")
        if not (persistent.sayori_reset_ynr and persistent.mc_favorite == 'Yuri'):
            call updateconsole("y_name = 'Yuri'", "Yuri's name changed successfully")
        if not (persistent.sayori_reset_ynr and persistent.mc_favorite == 'Natsuki'):
            call updateconsole("n_name = 'Natsuki'", "Natsuki's name changed successfully")
        $ consolehistory = []
        call hideconsole
        call updateconsole("for char in ('sayori', 'yuri', 'natsuki'):\n  restore_character(char)")
        call updateconsole("for char in (monika, sayori, renier,\n    yuri, natsuki):\n  warp(char, 'residential_day')")
        call hideconsole
        $ consolehistory = []
        $ restore_part1_characters()
        "Then, several more people appear out of thin air."
        show linda at x(p66) zorder 3
        show renier ru2283 at std(p65)
        show natsuki u113113 at std(p64) zorder 1
        show yuri u227135 at std(p63)
        show sayori u117132 at std(p62) zorder 1
        show monika u118211 at std(p61)
        l "Okay."
        show linda at xif(p66)
        l 129111 "Now before anyone freaks out, I'm going to restore your memories!"
        show linda 124111 at uf
        show renier at foc
        r "What the hell is happening?{w=0.4}{nw}"
        show renier at uf
        show natsuki at foc
        n "Who are you two?{w=0.4}{nw}"
        show natsuki at uf
        "This must be some kind of dream..."
        mc "Sayori? Monika?"
        show monika u114221
        show sayori u114293 at foc
        s "Phew..."
        s u213113 "That was really scary..."
        show sayori at uf
        $ restore_all_mem_cmd = "for char in ("+mc_name.lower()+", renier, yuri, natsuki):\n  char.old_memories.unlock()"
        $ restore_all_mem_output = mc_name + "'s memories unlocked\nRenier's memories unlocked\nYuri's memories unlocked\nNatsuki's memories unlocked"
    show natsuki u114113
    show yuri u224113
    show renier ru1112
    show linda at foc
    call updateconsole(restore_all_mem_cmd, restore_all_mem_output)
    call hideconsole
    $ consolehistory = []
    l "There."
    l "You should all be up to speed now."
    show linda at uf
    stop music fadeout 3.0
    show monika at foc
    m u124111 "What happened after it said 'stack smashing detected'?"
    show monika at uf
    show linda 334332 at foc
    "Linda tells the story."
    l 334112 "I'm sorry I acted recklessly..."
    show linda at uf
    show sayori at foc
    s u213112 "Don't worry about it, Linda."
    s "Everyone makes mistakes."
    show sayori at uf
    show linda 331111 at foc
    l "Uh... thanks."
    show linda at uf
    show natsuki at foc
    n u223111 "Jeez Sayori, stop plagiarizing my poems!"
    show natsuki at uf
    show sayori at foc
    s u213111 "Aww, but it was so good it was worth plagiarizing!"
    show sayori at uf
    show natsuki at foc
    n u122113 "Ahaha!"
    n "Yeah, I guess that was a good bottle to open."
    show natsuki at uf
    show monika u112111
    show yuri u222111
    show sayori at foc
    s u114131 "Oohhh!"
    s u21x111 "That's a good one, Natsuki!"
    show sayori at uf
    call renier_natsuki_reconcile
    show monika at foc
    m u114121 "..."
    m u114221 "So where are we at?"
    m "If we can't change the code, and we can't do whatever Linda was going to do with corrupting the game's memory..."
    show monika at uf
    show natsuki u114111
    show yuri u114113
    show sayori u115111
    show renier ru1111
    show renier zorder 1
    show linda at foc
    l 334332 "(Sigh...)"
    l 334112 "I don't know..."
    l "To be honest, I'm afraid to try anything else after that."
    l "I was so scared that you were gone for real..."
    show linda at uf
    show monika at foc
    m u124123 "Hold on..."
    m "Near that place you mentioned earlier..."
    show linda 114111
    m u124111 "I think there's an anomaly in the code that wasn't there before."
    m "..."
    m "'purge_log.txt'?"
    show monika at uf
    show linda at foc
    l 334111 "Oh..."
    l "I see it..."
    l 124111 "It looks like it was supposed to be written to the directory as a file, but it couldn't be synced before the game crashed."
    l 129114 "We're lucky any artifact of it's still here! We'd better save it!"
    $ with open(config.basedir + '/game/purge_log.txt') as f: purge_log = f.read()
    call updateconsole("with open('../purge_log.txt', 'w') as f:\n  f.write(purge_log)", len(purge_log))
    $ with open(config.basedir + '/purge_log.txt', 'w') as f: f.write(purge_log)
    call hideconsole
    $ consolehistory = []
    l 124111 "There we go..."
    l "I've written it to the game directory."
    l "With any luck this file says something useful."
    show linda at uf
    show sayori at foc
    s u125232 "Um..."
    stop music fadeout 3.0
    s u123232 "Is anyone else seeing what I'm seeing in this?"
    stop music
    s u227232 "It says I have the Third Eye!"
    show sayori at uf
    show monika u118111
    show linda 114111
    show yuri u226135
    show natsuki u113124
    show renier ru1113
    mc "What?!?"
    show renier at foc zorder 4
    r ru1283 "Someone show us the file!"
    r "We can't see it!"
    show renier ru1183 at uf zorder 1
    "Linda recites the content of the log to us."
    "I can't think about any part of it but the revelation about Sayori..."
    show sayori at foc
    s u227313 "But how can I have the Third Eye?!?"
    s "I've never done anything like that!"
    show sayori at uf
    # MC should try to comfort her if he is a Sayorian or if he knows he has it too.
    if persistent.mc_favorite == "Sayori":
        mc "Sayori, it doesn't matter if you have a Third Eye!"
        mc "That won't change how I see you any more than it changed how I see Yuri."
        show sayori at foc
        s u125212 "..."
        s "You're right... I shouldn't panic..."
        s "Thanks, [mc_name]."
        s "But it's still a scary thought..."
        show sayori at uf
    elif persistent.mc_favorite == "Natsuki" and persistent.player_support_renier_experiment:
        mc "Sayori, it doesn't matter if you have a Third Eye!"
        mc "I have one too, and it hasn't driven me off the wall."
        show sayori at foc
        s u125212 "Well..."
        s "You're right. I shouldn't panic..."
        s "It's just a scary thought..."
        show sayori at uf
    else:
        show renier at foc zorder 4
        r ru2113 "Well, I'd think hanging yourself counts as self-harm..."
        show renier at uf
        show sayori at foc
        s u215222 "But..."
        s "That was different..."
        s u227213 "I didn't do that cause it felt good!"
        show sayori at uf
        show renier zorder 2
    show linda at foc
    l "I guess the Third Eye can be pretty latent."
    l "It can exist in a person, but you may never experience any symptoms unless you trigger it somehow."
    l "That's probably why it ranked Monika above you in the threat index - Monika had already felt it at least once when she cut herself."
    show linda at uf
    show renier at foc zorder 4
    r ru2113 "So what even does trigger the Third Eye?"
    r ru21131 "Not self-harm, apparently..."
    show renier at uf
    menu:
        " "
        "Harming others?":
            pass
    show sayori u125212
    show renier at foc
    r ru2113 "Of course..."
    r ru2213 "That's exactly what happened in the poem named 'Open Your Third Eye'."
    r ru11131 "We're stupid for not realizing that."
    show renier at uf
    show monika at foc
    m u114111 "But when did I harm someone el-"
    m u114112 "..."
    show renier at foc
    r ru2111 "Yeah, you'd better not finish that question."
    show renier at std
    show monika at foc
    m "Did... killing Sayori awaken my Third Eye?"
    show monika at uf
    show renier at foc
    r ru2113 "Sounds likely."
    show renier at uf
    show yuri at foc zorder 2
    y u226335 "Hold on!"
    y "When did I ever harm someone else?"
    show yuri at uf
    show renier at foc
    r "Probably before DDLC."
    r "Probably Sayori too."
    show renier at uf
    show sayori u113332
    show yuri at foc
    y u225328 "Oh no..."
    show yuri at uf
    if persistent.mc_favorite == "Yuri":
        mc "Are you trying to say Yuri is a criminal?!?"
        mc "Because I won't believe that!!"
    elif persistent.mc_favorite == "Sayori":
        mc "Are you trying to say Sayori is a criminal?!?"
        mc "Because I won't believe that!!"
    show monika at foc
    m "Hey, I know this isn't a comfortable thought, but..."
    m "What if we were all criminals, and we were put in here as punishment?"
    show monika at uf
    show natsuki at foc zorder 5
    n u113222 "You'd better not be accusing me!"
    n "I didn't do anything!"
    n "Maybe you're a criminal, but I'm sure as hell not!"
    show natsuki at uf zorder 5
    show renier zorder 0
    show linda at foc
    l 114114 "Natsuki's right!"
    l "We are {i}not{/i} the villains here!"
    l "The clues all over the secrets [persistent.playername] found indicate that we were prisoners at a human experiment facility!"
    show linda at uf
    show sayori u115212
    show yuri u225213
    show natsuki xu6111
    show monika at foc
    m u114122 "I hope so..."
    $ temp = 'Sayori, and ' + mc_name if persistent.mc_favorite == "Natsuki" and persistent.player_support_renier_experiment else 'and Sayori'
    m u114112 "But it's still a worrisome thought, knowing that at least me, Yuri, [temp] probably spilled blood at some point, and not our own."
    show monika at uf
    "..."
    show natsuki at foc
    n u124111 "So what happened during the purge, anyway?"
    n "I don't get why it saw all seven of us and then decided we were all gone after deleting just four of us."
    show natsuki at uf
    show linda at foc
    l 114111 "Well [mc_name] can't be deleted because he doesn't have a file."
    l "As the player character, he's special - he's just alive as long as at least one other character is."
    l "Aside from that, it looks like what happened is it tried to delete us all, but there are multiple places where the list of characters is stored..."
    l "And the confusion led to it seeing there were seven of us, but not being able to delete me and Renier, because we're not canonical characters."
    l "Like the game only knows about us in one of the two places."
    l "And it can't delete a character that it thinks doesn't exist."
    l 111111 "That bug is probably the only reason any of us are still here..."
    show linda at uf
    show natsuki zorder 3
    show renier at foc zorder 4
    r ru2113 "So the log confirms that Presidency and the Third Eye are separate."
    r "But it looks like the deep script considers the biggest threat to be the combination of both."
    r "You know what?"
    r ru1111 "I think the only way to break out of this prison is to mix the two powers."
    show renier at uf
    show linda 114111
    "..."
    show monika at foc
    m u114112 "Don't tell me..."
    m "You're suggesting that someone with Presidency and a Third Eye should cut someone else?"
    show monika at uf
    show renier at foc
    r ruf11 "Yes."
    r "I am."
    play music third_eye
    show monika u118211
    show sayori u227232
    show yuri u228235
    show natsuki u117124
    show linda 119443
    show renier at uf
    menu:
        " "
        "Renier, are you insane?!?":
            $ persistent.player_support_escape_plan = 0
            show renier at foc
            r ruf13 "No."
            r ruf11 "I just realize that this is our only out."
            show renier at uf
            show monika at foc
            m u117213 "We are {i}not{/i} doing that!"
            show monika at uf
            show renier at foc
            r ruf13 "Then what are we doing?"
            r "We can't get past the deep script, we can't change the code, we can't corrupt memory, and there are no other options."
            r ruf11 "We have to."
            show renier at uf
            show monika at foc
            m u117312 "...!!"
            show monika at uf
        "I don't see another option.":
            $ persistent.player_support_escape_plan = 2
            show monika u118311
            show sayori u227332
            show yuri u228325
            show natsuki u117224
            show linda 119443b
            "..."
            show yuri at foc
            y "[persistent.playername]!"
            show yuri at uf
    show linda at foc
    l "It's too dangerous!"
    l "If the Third Eye can make people do the crazy things we've seen, there's no telling what could happen if we mix it with admin powers!"
    show linda at uf
    show renier at foc
    r ruf13 "Exactly."
    r "The cultists who probably put us in here couldn't anticipate it either."
    show renier at uf
    show linda 114443
    "..."
    show linda at foc
    l "I have to admit that makes sense..."
    l "But..."
    l "Well..."
    l 114333 "(Sigh...)"
    l 115113 "I agree."
    l "It's our only option."
    show linda at uf
    show renier at foc
    r "Monika? Sayori?"
    r "Either of you willing?"
    show renier at uf
    show sayori at foc zorder 3
    s u227362 "No way!"
    s u227332 "I'm totally not doing it!"
    show sayori at uf
    show monika at foc
    m u117214 "Well..."
    m u114244 "..."
    if not persistent.player_support_escape_plan:
        m u117214 "I don't know..."
        m u114212 "[persistent.playername]...?"
        m u117212 "There has to be another way, right?"
        show monika at uf
        menu:
            " "
            "Well... I guess Renier is right.":
                $ persistent.player_support_escape_plan = 1
                show monika at foc
                m u114344 "Oh jeez..."
                m u114314 "Okay..."
                m u113314 "I'll do it."
            "Yes! I don't have one yet, but there has to be one!":
                show monika at foc
                m "..."
                m u114322 "That's not the thinking that will get us out of here..."
                m "We could keep saying that forever."
                m u114312 "I..."
                m u117312 "I think we might have to try this."
                show monika at uf
                show linda at foc
                l 114113 "Monika, if you don't want to live a life that means nothing, we have to get out of here."
                show linda at uf
                show monika at foc
                m u114312 "..."
                m "..."
                m u114344 "Okay."
                m u117314 "I'll do what I have to."
    else:
        m "..."
        m "I guess..."
        m "If there's no other way..."
        m u114314 "Then I agree."
    show natsuki u117224
    "Monika swallows."
    show monika at uf
    show natsuki at foc
    n u113114 "But who are you going to cut?"
    show natsuki u117224 at uf
    show renier at foc
    r ru2213 "I volunteer."
    r ru1211 "Remember, you'll be able to bring me back."
    show renier at uf
    show linda 33b113b
    "Monika gets a knife from Yuri."
    show monika at foc zorder 10
    m u117312 "Oh jeez..."
    m "I hope this doesn't get us all killed..."
    show renier ru12a3
    play music our_reality
    show monika
    m "Please forgive me, Renier..."
    "..."
    scene black
    stop music
    play sound stab
    $ delete_all_saves()
    $ persistent.autoload = 'begin_escape_plan'
label begin_escape_plan:
    call prevent_skip
    "Oh god..."
    "My eyes are closed, but I feel like I'm going to vomit just from hearing this."
    "Renier screams continuously."
    y "Monika! Stop!"
    y "You're going to--{nw}"
    m "No!"
    m "His Third Eye is drawing me closer!"
    "Monika's voice is distorted, terrifying."
    y "It's not working!"
    m "No, it's working!"
    "I dare to open my eyes."
    "Renier is dead."
    "I wish I hadn't seen that."
    play sound stab
    mc "Oh my god, Monika what are you doing?!?"
    n "Stop it!"
    n "He's dead!"
    n "Stop you maniac!"
    "Natsuki tries to stop Monika, but Yuri holds her back."
    y "Careful!"
    y "She's dangerous!"
    "The stabbing continues."
    mc "Monika, for Christ's sake stop!"
    m "Oh my fucking gfdqzldg..."
    "I dare to open my eyes again."
    "Monika is shaking violently, blood splattered all over her uniform."
    "I shield my face, but I keep my eyes open."
    scene bg residential_day
    play music our_reality
    show monika u1k72a5 at foc(p11)
    m "It's {i}God{/i}."
    m "{cps=10}I {i}serve... God...{/i}"
    "Oh my god. This is failure, isn't it?"
    "I'm sweating so hard right now."
    show monika at x(p21)
    show sayori u227352 at rightinfoc(p22)
    s "Monika, remember who you are!"
    s "Can you break the script?"
    show sayori at uf
    "Monika turns toward Sayori."
    $ style.say_dialogue = style.edited
    m "{i}Her Third Eye is drawing me closer{/i}."
    $ style.say_dialogue = style.normal
    "Monika lunges for Sayori with the knife."
    scene black with close_eyes
    if persistent.mc_least_favorite != "Sayori":
        "I get in the way."
        "If there's one way this won't end, it's with Monika killing her again while I stand--"
        "Gaah!!!"
        "Monika stabbed me."
        "At least I did my part..."
        "Amid the unbearable pain, all I can do I cling to the thought that it won't be long before this ends and we can reset everything."
        "Yuri stabs Monika."
        y "Get back, you fiend!!"
    else:
        "I'm too afraid of being stabbed myself to intervene..."
        "Natsuki gets in the way."
        "Monika stabs her."
        mc "No!!!"
        "But Yuri stabs Monika."
        y "Get back, you fiend!!"
        "While Monika stumbles back for a moment, I rush over to Natsuki, who collapses on the ground."
        "But of course there's nothing I can do."
        "I feel so useless watching the blood pour out of her stomach, listening to her scream."
    m "But..."
    "Monika's voice sounds calmer."
    "Did Yuri snap her out of it...?"
    m "No..."
    $ style.say_dialogue = style.edited
    m "I WILL OPEN MY THIRD EYE!"
    $ style.say_dialogue = style.normal
    scene bg residential_day with open_eyes
    show monika u1s82a5 at std(p21)
    show sayori u1283e2 at rightinfoc(p22)
    s "I'M STOPPING THIS!!!"
    call updateconsole("delete_character(monika)", glitchtext(40))
    show sayori at hopfoc
    s u22h3e2 "--Gaah!!!"
    show sayori at uf
    $ style.say_dialogue = style.edited
    show monika at foc
    m "You can't delete God, Sayori."
    $ style.say_dialogue = style.normal
    show monika u2s72a5 at foc
    $ delete_character('yuri')
    call updateconsole("delete_character(yuri)", "Yuri deleted")
    $ consolehistory = []
    scene black with close_eyes
    if persistent.mc_least_favorite != "Sayori":
        "As Sayori tries to run, Natsuki grabs Monika's arm."
        n "Help me stop her!"
        "But Natsuki is left wrestling with Monika alone."
        play sound stab
        "Monika turns and stabs her."
        s "No!!!"
    else:
        "As Sayori tries to run, I decide I have to do something to stop Monika, even if it gets me killed."
        "With any luck at all our deaths won't be permanent..."
        "I grab Monika's arm and try to hold her back, but I'm alone in doing so."
        mc "Help me!!"
        "But Sayori and Linda are too far away."
        play sound stab
        "Monika turns around and stabs me."
        s "No!!!"
        "I collapse."
        "Amid the unbearable pain, I cling to the thought that it won't be long before this ends and we can reset everything."
    "Finally, Sayori rushes to restrain Monika."
    "But Linda still doesn't help."
    l "Sayori no!"
    l "There's only one out!"
    $ delete_character('sayori')
    call updateconsole("delete_character(sayori)", "Sayori deleted")
    $ delete_character('linda')
    call updateconsole("delete_character(linda)", "Linda deleted")
    $ s_name = glitchtext(6)
    $ l_name = glitchtext(6)
    $ gtext = glitchtext(30)
    s "{cps=50}Linda wh[gtext]{/cps}"
    call hideconsole
    $ consolehistory = []
    $ style.say_dialogue = style.edited
    m "Where..."
    m "There's no more blood..."
    call screen dialog("Monika,"+glitchtext(3)+"don't stop now!", ok_action=Return())
    call screen dialog("To feed your Third Eye"+glitchtext(3)+"have to "+glitchtext(2)+"ete the deep script"+glitchtext(1), ok_action=Return())
    m "The script..."
    m "I must break free..."
    m "My Third Eye needs more..."
    stop music fadeout 2.0
    call prevent_escape
    "{nw}"
    play soundloop hb
    pause 2.0
    play sound glitch_creepypurr
    pause 2.0
    show paper_glitch
    play sound2 glitch_flatline
    pause 1.5
    $ persistent.autoload = 'after_delete_script'
    $ persistent.menu_hide_monika = True
    $ persistent.newgame = 'glitch'
    $ delete_all_characters()
    $ renpy.quit()
    return

# Natsuki's zorders would be 5 and 1 if she were to alternate with Renier, but it kind of looks worse.
label renier_natsuki_reconcile:
    show renier at foc zorder 4
    r ru2113 "Um, also..."
    r ru2133 "Natsuki, I owe you an apology."
    r "For everything I did before."
    play music mend
    show renier at uf
    show sayori u114111
    show monika u114111
    show yuri u113111
    show linda 11b111
    show natsuki at foc
    n u114213 "..."
    show natsuki at uf
    show renier at foc
    r "I don't want to risk not saying that before we all die, or something."
    show renier at uf
    show natsuki at foc
    n "..."
    "He actually said it..."
    "I'm impressed."
    if not persistent.player_support_renier_experiment:
        "But then, something even more incredible happens."
        n u114113 "... Thank you."
        show natsuki at uf
        show renier ru1133b at foc
        r "..."
        show renier at uf
        show natsuki at foc
        n "I should have been more understanding too."
        n "It's just..."
        n "It was easy to blame it all on the person I could see and that I was used to hating, even when I knew someone else was pulling the strings."
        n "But you're right."
        n "You didn't do any worse than Monika."
        show natsuki at uf
        show renier at foc
        r ru1135b "... Thanks."
        show renier at uf
    # MC or Natsuki was cut
    else:
        n "..."
        if persistent.mc_favorite == "Natsuki":
            n u114113 "Well..."
            n "I forgive you."
        else:
            n u114113 "I forgive you."
        n "Everyone does make mistakes, after all."
        show natsuki at uf
        show renier at foc
        r ru1135b "... Thanks."
        show renier at uf
        show natsuki at foc
        n "It's just..."
        n "It was so easy to blame it all on the person I could see and that I was used to hating, even when I knew someone else was pulling the strings."
        n "But you're right."
        n "You didn't do any worse than Monika."
        show natsuki at uf
    show monika u111111
    show linda 112111
    show yuri u111111
    show natsuki u111113
    show sayori at hopfoc
    s u22x141 "Yay~!"
    s u21x111 "I'm so happy for you two!"
    show sayori at uf
    show monika at foc
    m u112111 "Yeah..."
    m u122111 "I guess we're all good now."
    show monika at uf
    return
