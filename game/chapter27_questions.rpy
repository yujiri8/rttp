label adam_questions:
    show markov at foc
    k "Before we do this..."
    k "Do you have any questions?"
    k "Anything you want me to explain?"
    $ qtext = "Now's a good time."
    $ persistent.adam_questions = {'experiments':False, 'ursula_awakening':False, 'power_relationship':False, 'ursula_poem':False}
    $ page = 0
label adam_questions_menu:
    menu:
        k "[qtext]"
        "Did you actually learn anything from your experiments?" if not persistent.adam_questions['experiments'] and page == 0:
            call adam_discuss_findings
            $ persistent.adam_questions['experiments'] = True
        "What do you think caused Ursula's admin awakening?" if not persistent.adam_questions["ursula_awakening"] and page == 0:
            call adam_discuss_ursula_awakening
            $ persistent.adam_questions['ursula_awakening'] = True
        "Is there any relationship between the Third Eye and admin powers?" if not persistent.adam_questions['power_relationship'] and page == 1:
            call adam_discuss_power_relationship
            $ persistent.adam_questions['power_relationship'] = True
        "Do you still think Ursula's poem means anything?" if not persistent.adam_questions["ursula_poem"] and page == 1:
            call adam_discuss_power_relationship
            $ persistent.adam_questions['ursula_poem'] = True
        "(More options)":
            $ page = 1 if page == 0 else 0
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
    k "I never tortured anyone else into becoming as stong as Libitina."
    k "I thought for so long that it was about different kinds of suffering."
    k "Maybe drowning would be more effective than starvation."
    k "Or being prevented from sleeping..."
    k "Or just isolation for days..."
    k "It was all for nothing."
    k "I was wrong, and by my own fault."
    return
