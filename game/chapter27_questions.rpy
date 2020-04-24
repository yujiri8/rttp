label adam_questions:
    show markov at foc
    k u11513 "Before we do this..."
    k "Do you have any questions?"
    k "Anything you want me to explain?"
    $ qtext = "Now's a good time."
    $ persistent.adam_questions = {
        'experiments': False,
        'ursula_awakening': False,
        'power_relationship': False,
        'ursula_poem': False,
        'char_files': False,
        'api_breakage': False,
        'dead_states': False,
        'ship_ddlc': False,
    }
    $ page = 1
label adam_questions_menu:
    menu:
        k "[qtext]"
        "Did you actually learn anything from your experiments?" if not persistent.adam_questions['experiments'] and page == 1:
            call adam_discuss_findings
            $ persistent.adam_questions['experiments'] = True
        "What do you think caused Ursula's admin awakening?" if not persistent.adam_questions["ursula_awakening"] and page == 1:
            call adam_discuss_ursula_awakening
            $ persistent.adam_questions['ursula_awakening'] = True
        "Is there any relationship between the Third Eye and admin powers?" if not persistent.adam_questions['power_relationship'] and page == 1:
            call adam_discuss_power_relationship
            $ persistent.adam_questions['power_relationship'] = True
        "Do you still think Ursula's poem means anything?" if not persistent.adam_questions["ursula_poem"] and page == 2:
            call adam_discuss_power_relationship
            $ persistent.adam_questions['ursula_poem'] = True
        "How do character files work?" if not persistent.adam_questions["char_files"] and page == 2:
            call adam_discuss_char_files
            $ persistent.adam_questions['char_files'] = True
        "How does breaking APIs work?" if not persistent.adam_questions['api_breakage'] and page == 3:
            call adam_discuss_api_breakage
            $ persistent.adam_questions['api_breakage'] = True
        "I'm confused about all the different 'dead states' characters can be in." if not persistent.adam_questions['dead_states'] and page == 3:
            call adam_discuss_dead_states
            $ persistent.adam_questions['dead_states'] = True
        "How did you ship DDLC?" if not persistent.adam_questions['ship_ddlc'] and page == 3:
            call adam_discuss_ship_ddlc
            $ persistent.adam_questions['ship_ddlc'] = True
        "(-> page 2)" if not all(persistent.adam_questions.values()) and page == 1:
            $ page = 2
            jump adam_questions_menu
        "(-> page 3)" if not all(persistent.adam_questions.values()) and page == 2:
            $ page = 3
            jump adam_questions_menu
        "(-> page 1)" if not all(persistent.adam_questions.values()) and page == 3:
            $ page = 1
            jump adam_questions_menu
        "Done.":
            jump end_adam_questions
    $ qtext = "Anything else?"
    jump adam_questions_menu
label end_adam_questions:
    return

label adam_discuss_power_relationship:
    k "There is, actually."
    k "Not as deep of one as I thought... but there is one."
    k "The Third Eye is only catalyzed by contact with an admin."
    k "Not only did no one else ever discover it before Ursula's awakening..."
    k "... but hers and Libitina's were both sensitive enough that there's no way they wouldn't have opened them by accident at some point."
    k "And of all the Eye-bearers I found and abducted..."
    k "... none of them had ever opened it before meeting me."
    k "I don't know what the significance of this is, if any..."
    k "... and we won't know unless we escape and... maybe we find out why this world exists."
    return

label adam_discuss_ursula_poem:
    k "It really seems like it."
    k "I always thought the meaning of the first sentence related to her thoughts as she decided to leave."
    k "The rich aroma was the prospects of entering [persistent.playername]'s world, the bittersweet aftertaste was the people she would have to leave behind, and the hot, complex balance was the pain of the decision."
    k "And I know, it seems like that couldn't have been it, because she wrote it before then...."
    k "... but did she?"
    k "After all, we know that in DDLC, Linda wrote some of your thoughts into files more or less inadvertently."
    k "And we never found the poem until after Ursula was gone."
    k "So it's not out of the question that, in fact, she {i}did{/i} write it with those thoughts in mind."
    k "Written just in that moment..."
    k "We won't know until we escape from this world and find her."
    return

label adam_discuss_ursula_awakening:
    k "My theory is that the people who built this world... the Portrait of Markov..."
    k "... chose Ursula for their first experiment with medium-awareness."
    k "Maybe they never wanted to try again and I inherited it naturally from being the closest to her..."
    k "... or maybe I was their next choice after Ursula escaped so easily, and the experiment with me is still ongoing."
    k "And they haven't perturbed it in the years since."
    return

label adam_discuss_findings:
    k "I learned a lot."
    k "I did find that the strength of a person's Third Eye wasn't entirely fixed..."
    k "In some ways, it feeds on suffering."
    k "When a soul is destroyed by trauma, the strength of their Third Eye increases."
    k "Sensitivity also tends to increase with increased power."
    k "But, there seemed to be a limit to how far that could go."
    k "I never tortured anyone else into becoming as strong as Libitina."
    k "I thought for so long that it was about different kinds of suffering."
    k "Maybe drowning would be more effective than starvation."
    k "Or being prevented from sleeping..."
    k "Or just isolation for days..."
    k "It was all for nothing."
    k "I was wrong, and by my own fault."
    return

label adam_discuss_char_files:
    k "Character files are a reflection of the actual Character object's state."
    k "When the viewport sees a file deleted or created, it sends a command to the server to delete or restore the character."
    k "And when a character is deleted or restored, a command is sent to the viewport to delete or create their file."
    k "Deleting on the viewport side doesn't work now that the viewport doesn't have those permissions anymore."
    k "The actual data in the Character file is meaningless."
    k "It's read from Character.get_file_data(), which returns whatever data string was set on them."
    k "The attribute doesn't seem to serve any real function, besides a way of attaching arbitrary information to a Character."
    k "And the viewport needs data in the files, so when it first needs to create one, it sets the character's file data to something menaingful for them."
    k "As you know, the data in the girls' files when you played DDLC wasn't the generated data, it was what Linda inserted."
    return

label adam_discuss_api_breakage:
    k "Whenever you use the Python wrappers, the interpreter enters the block of instructions for the function."
    k "When it tries to use Ursula's Character object and finds that it's invalid in the way hers is..."
    k "... the game marks the whole region of memory that stores that code as off-limits, and deletes any references to it."
    k "But checking the number of arguments happens before that - which is why this can't be used to break functions that don't take any arguments."
    k "I think the reason Ursula's character object can do this is that hers is still technically a valid character object, so the error doesn't occur until the operation is actually attempted."
    k "So it doesn't fail when passing the argument."
    return

label adam_discuss_dead_states:
    k "Well..."
    k "So first of all, there's deletion."
    k "Deleted characters are unconscious if they're not admins, or experience intense pain if they are."
    k "When a character dies in-universe, they're deleted."
    k "When they're deleted directly, they not only die in-universe, but their body is removed from the world."
    k "Then there are invalid states."
    k "restore_character doesn't work on characters in invalid states, but Character.reset does."
    k "Chracter.reset is a general-purpose thing..."
    k "... it undoes almost any kind of negative or non-standard state, including physically healing the character and closing their Third Eye if it's open."
    k "But it's not always perfect at fixing various invalid states, since there can be any number of them."
    k "Intentionally caused invalid states, like the one my deep script purge inflicted were mostly intended to prevent use of admin abilities, and to be easily reversible with Character.reset."
    k "Being killed by the Third Eye seems to do the same thing to an admin as the deep script purge."
    k "Of course, when you get killed by {i}other{/i} things... things even I don't understand..."
    k "... the effects aren't always predictable."
    k "Weird stuff happened to Linda because she didn't come out of her first virtual world the intended way, but also didn't break out with a Third Eye."
    k "So it seems like her powers ended up still tied to that world somehow, which made her only recognized as an admin in some ways."
    k "I think that's what caused her to be sort of half-empowered when she first got into DDLC."
    return

label adam_discuss_ship_ddlc:
    k "A network service was running, exposed, on the host machine."
    k "I was able to upload it to a file server, where I knew it would be found someday."
    k "It seems to have been an accident."
    k "The service disappeared some time after I shipped DDLC."
    return

#TODO enable them to ask if he created VR or viewports
