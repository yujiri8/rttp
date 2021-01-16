label chapter2:
    "Natsuki and Yuri give the information a minute to sink in."
    show yuri at foc
    y u125128 "So what are we going to do?"
    y "Do we have any leads?"
    show yuri at uf
    show monika at foc
    m u113124 "I don't."
    m u114114 "[currentuser]..."
    m "Do you have any ideas?"
    menu:
        " "
        "There are a lot of weird cryptic messages in this game.":
            pass
    menu:
        " "
        "Like the \"Special\" poems I got throughout Act 2.":
            pass
    menu:
        " "
        "And your character files.":
            pass
    mc "I think this [currentuser] is saying there are a lot of weird cryptic messages in this game."
    mc "Like the \"special\" poems throughout \"Act 2\" and our character files."
    show monika at foc
    m u214111 "Oh, hold on..."
    m "The player's dialog choices only speak to [mc_name]."
    m "I'll make it so they speak to all of us."
    call updateconsole("import viewport")
    call updateconsole("vp = viewport.get_viewport()")
    call updateconsole("vp.choices_target = Voice(\n anchor = " + mc_name.lower() + ")")
    call hideconsole
    $ consolehistory = []
    m u124111 "There we go..."
    m "We should all be able to hear [currentuser] directly now."
    m "So let's see those secrets."
    scene black with dissolve_scene
    show monika u114111 at foc(p41) zorder 0
    show yuri u226135 at std(p42) zorder 1
    show natsuki u117123 at std(p43) zorder 2
    show sayori u227131 at std(p44) zorder 0
    m "That's some weird stuff..."
    show monika at uf
    show natsuki at foc
    n u114121 "Some of it was really disturbing..."
    n "Like that part in my gibberish poem..."
    n u113121 "Who the hell wrote that shit?"
    n "Cause I definitely didn't!"
    show natsuki at uf
    show sayori u114111
    show monika at foc
    m u114121 "I remember writing a few of these messages."
    m "I wrote the secret topic in the file for Act 3... but only the plaintext."
    m "I have no idea how that base64 got there."
    show monika at uf
    mc "You must have written a lot of these..."
    mc "Most of the special poems, and the files that appeared in the game directory."
    show monika at foc
    m u114111  "Most of the files I wrote were part of a strategy of hinting at my epiphany without coming out."
    m "I was trying to create a mystery about me so [currentuser] would want to investigate..."
    #m "That was also why I did that thing where I made the screen fade out while I was talking to the player..."
    #m "I thought that would make it completely irresistible for the player to make you come talk to me the next day."
    #m "That was before I realized the game just didn't have a route for me and I thought the player was ignoring me by choice."
    #m u114121 "Actually I don't think I did..."
    m u114121 "But I didn't write the 'Have a nice weekend!' file..."
    m u117111 "And I definitely didn't make that happy thoughts thing!"
    show monika at uf
    mc "Wait a minute."
    if persistent.mc_favorite == 'Yuri' or persistent.mc_least_favorite == 'Natsuki':
        mc "Yuri..."
        mc "What about that poem about going to the emergency room?"
        mc "That seems like it has to be you during Act 2, but you couldn't have written files in the game directory, could you?"
        show yuri at foc
        y u124152 "Ah..."
        y "I don't know."
    else:
        mc "Natsuki..."
        mc "What about that poem about your dad?"
        mc "That seems like it has to be you during Act 2, but you couldn't have written files in the game directory, could you?"
        show natsuki at foc
        n xu4131 "Yeah... I dunno."
        n "I don't remember writing that."
        n "I would have, though."
        show natsuki at uf
    show yuri at foc
    y u125113 "I wonder if, due to the game's broken nature, our thoughts somehow spilled into some of these files unintentionally."
    show yuri at uf
    show monika at foc
    m u124111 "That would explain a lot."
    m "But there are still so many mysteries."
    m "Besides the nice weekend thing and the messed up poems, there's the special poem about drowning, the one mentioning Elyssa and Renier, the weird splash screen messages..."
    m "I wrote some of those obviously, but not all of them."
    m "Definitely not the one that says 'I have granted kids to hell'."
    m "And that's not even to mention our character files."
    m "They don't seem to have anything to do with whose file they're in."
    show monika at uf
    mc "Hold on."
    mc "Monika, in your monologue in the space classroom, didn't you mention something about Portrait of Markov?"
    show monika at foc
    m u221111 "Ah! I do remember that. That's a great clue."
    show monika at uf
    mc "And then you stopped yourself?"
    mc "You {i}must{/i} have known what that meant!"
    show monika at foc
    m u214222 "Ah-..."
    m u114222 "What...?"
    m "I don't..."
    m "I don't understand what happened!"
    show monika at uf
    mc "What do you mean?"
    mc "Just tell us what you were thinking when you said that."
    show monika at foc
    m "I don't remember!"
    m "All I remember is I was about to say something about it, but then I felt compelled to stop myself..."
    m "And I just... didn't have any cognition after that!"
    m "It was like my memory of the topic disappeared..."
    m u114144 "{i}No{/i}..."
    m u114114 "It was the script, wasn't it?"
    m "It forced me not to talk about something that wasn't in the intended scope of the game!"
    m "Urgh! Even I'm not free from its control!"
    show monika at uf
    show sayori at foc
    s u215111 "I don't really understand how this 'script' thing works..."
    show sayori at uf
    show monika at foc
    m u214111 "I think it's basically a force that pushes on our minds to make us predisposed to carry out the intended plot."
    m "As club president, I was able to change it..."
    m u214114 "But apparently the script still has power over me?"
    m "Enough to basically control my mind?"
    m u114111 "It doesn't make any sense!"
    show monika at uf
    mc "Well, regardless it seems like a good clue."
    mc "Portrait of Markov might be related to the answers we seek."
    mc "Yuri, you read the book a bunch of times, right?"
    show yuri at foc
    y u125213 "Uu... yes..."
    y "But I don't seem to remember anything other than what the script made me say about it."
    show yuri at uf
    mc "Alright, I say we need to get that book."
    mc "Now that we're all aware, the game shouldn't be able to get away with cheating our memories like that."
    mc "It should have to show us an actual book."
    show yuri at foc
    y u125111 "That's a good idea."
    y "Let's do it."
    show yuri at uf
    show monika at foc
    m "I'm not sure this will work..."
    m "The game might just show us nothing."
    m "But we've nothing to lose."
    m "I think to get the book, we have to re-generate the world."
    m "With the new game button, that is."
    show monika at uf
    show natsuki at foc
    n u113112 "Good..."
    n "I'm getting really sick of this place."
    show natsuki at uf
    show monika at foc
    m "Hm..."
    m "I'm not sure about you guys's memories."
    m "Sayori and I should be fine, but I'm not sure the rest of you won't have your memories wiped when a new game starts."
    m "I didn't manually wipe them after the first time."
    m "I don't know if just knowing the truth without having been president will enable you to keep your memories."
    m "Well, I guess I'll just restore them again."
    m "Time to see if this works."
    m "[currentuser]..."
    m "Actually, before we do this, I think now would be a good time to ask you something."
    menu:
        m "Do you have another name you want us to call you?"
        "Yes":
            # Clear the 'name_entry' placeholder so it doesn't still have MC's name in it.
            $ name_entry = ""
            call screen name_input(message="What is it?")
            $ persistent.playername = _return
        "No":
            $ persistent.playername = currentuser
    m "Also, I've been assuming you were a guy... am I wrong?"
    menu:
        " "
        "Yes, I'm a gal":
            $ persistent.player_subj_pronoun = "she"
            $ persistent.player_obj_pronoun = "her"
            $ persistent.player_pos_pronoun = "her"
            $ persistent.player_copula_pos_pronoun = "hers"
        "No, I'm a guy":
            $ persistent.player_subj_pronoun = "he"
            $ persistent.player_obj_pronoun = "him"
            $ persistent.player_pos_pronoun = "his"
            $ persistent.player_copula_pos_pronoun = "his"
        "Can I enter my own pronouns?":
            m "Oh, of course!"
            $ name_entry = ""
            call screen name_input(message="Subject pronoun (alternative to he/she):")
            $ persistent.player_subj_pronoun = _return
            $ name_entry = ""
            call screen name_input(message="Object pronoun (alternative to him/her):")
            $ persistent.player_obj_pronoun = _return
            $ name_entry = ""
            call screen name_input(message="Possessive adjective (alternative to his/her):")
            $ persistent.player_pos_pronoun = _return
            $ name_entry = ""
            call screen name_input(message="Possessive pronoun (alternative to his/hers):")
            $ persistent.player_copula_pos_pronoun = _return
    $ persistent.newgame = 1
    m "Alright [persistent.playername], we're waiting on you to start a new game."
    while True:
        " "
