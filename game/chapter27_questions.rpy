label adam_questions:
    show markov at foc
    k u11513 "Before we do this..."
    k "Do you have any questions?"
    k "Anything you want me to explain?"
    $ qtext = "Now's a good time."
    $ persistent.adam_questions = {'experiments':False, 'ursula_awakening':False, 'power_relationship':False, 'ursula_poem':False, 'char_files':False}
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
        "(-> page 2)" if not all(persistent.adam_questions.values()) and page == 1:
            $ page = 2
            jump adam_questions_menu
        "(-> page 1)" if not all(persistent.adam_questions.values()) and page == 2:
            $ page = 1
            jump adam_questions_menu
        "Done.":
            jump end_adam_questions
    $ qtext = "Anything else?"
    jump adam_questions_menu
label end_adam_questions:
    return

label adam_discuss_power_relationship:
    k "I named the Third Eye after Ursula's poem."
    k "Back when I still thought there was a closer relationship between the powers."
    k "There is a relationship, though."
    k "The Third Eye is only catalyzed by contact with an admin."
    k "Not only did no one else ever discover it before Ursula's awakening..."
    k "... but yours and hers were both apparently sensitive enough that there's no way you wouldn't have opened by accident at some point."
    k "And of all the Eye-bearers I found and abducted..."
    k "... none of them had ever opened it before meeting me."
    return

label adam_discuss_ursula_poem:
#    k "\"To see the future is to be wise.\""
    k "It really seems like it."
    k "I always thought the meaning of the first sentence related to her thoughts as she decided to leave."
    k "The rich aroma was the prospects of entering [persistent.playername]'s world, the bittersweet aftertaste was the people she would have to leave behind, and the hot, complex balance was the pain of the decision."
    k "And I know, it seems like that couldn't have been it, because she wrote it before then...."
    k "... but did she?"
    k "After all, we know that in DDLC, Linda wrote some of your thoughts into files more or less inadvertently."
    k "And we never found the poem until after Ursula was gone."
    k "So it's not out of the question that, in fact, she {i}did{/i} write it with those thoughts in mind."
    k "Written just in that moment..."
    k "I guess we won't know for sure until we escape from this world and find her."
    return

label adam_discuss_ursula_awakening:
    k "My theory is that the people who built this world... the Portrait of Markov..."
    k "... chose Ursula for their first experiment with medium-awareness."
    k "Maybe they never wanted to try again and I inherited it naturally from being the closest to her..."
    k "... or maybe I was their next choice after Ursula escaped so easily, and the experiment with me is still ongoing."
    k "And they haven't done anything with it in the years since."
    return

label adam_discuss_findings:
    k "I learned a lot."
    k "I did find that the strength of a person's Third Eye wasn't entirely fixed..."
    k "In some ways, it feeds on suffering."
    k "After destroying a person's soul with trauma, the strength of their Third Eye increased."
    k "Sensitivity also tended to increase with increased power."
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
    k "The data in the Character file is meaningless."
    k "It's read from Character.get_file_data(), which returns whatever data string was set on them."
    k "The viewport needs data in the files, so when it first needs to create one, it sets the character's file data to something menaingful for them."
    k "As you know, the data in the girls' files when you played DDLC wasn't the generated data, it was what Linda inserted."
    return

label adam_discuss_api_breakage:
    k "Whenever you use the Python wrappers, the interpreter enters the block of instructions for the function, and then tries to evaluate its arguments."
    k "When it evaluates Ursula's Character object and finds that it's invalid..."
    k "... the game marks the whole region it was in as off-limits, and deletes any references to it."
    k "But checking the number of arguments happens before that - which is why this can't be used to break functions that don't take any arguments."
#    k "I think the reason Ursula's character object can do this ."
    return
