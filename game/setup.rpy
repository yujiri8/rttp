label setup:
    call screen name_input(message="Then now is the time to name MC.")
    $ mc_name = persistent.mc_name = _return
    "Now you need to answer a few questions about your playthrough of the original DDLC."
    "(It'll be assumed that [mc_name] took his favorite girl's side in the argument on Day 2, and that he confessed love to Sayori if and only if she was his favorite.)"
    menu:
            "Who is [mc_name]'s favorite girl?"
            "Sayori":
                    $ persistent.mc_favorite = 'Sayori'
            "Yuri":
                    $ persistent.mc_favorite = 'Yuri'
            "Natsuki":
                    $ persistent.mc_favorite = 'Natsuki'
    menu:
            "Who is [mc_name]'s least favorite girl?"
            "Sayori" if persistent.mc_favorite != "Sayori":
                    $ persistent.mc_least_favorite = 'Sayori'
            "Yuri" if persistent.mc_favorite != "Yuri":
                    $ persistent.mc_least_favorite = 'Yuri'
            "Natsuki" if persistent.mc_favorite != "Natsuki":
                    $ persistent.mc_least_favorite = 'Natsuki'
    "One other thing."
    "Are you playing from the start, or do you want to skip a ways in?"
    "Saves from earlier versions of the mod probably won't work, so to make restarting easier, you can skip partway in."
    menu:
        "Would you like to start at the beginning, or skip in?"
        "Beginning":
            "Very well."
            $ persistent.first_run = True
            call setup_common
            jump start
        "Skip to Part 2":
            $ persistent.first_run = True
            call skip_to_part2
            call setup_common
            jump part2_skip_point
        "Skip to Part 3":
            $ persistent.first_run = True
            call skip_to_part3
            call setup_common
            jump after_markov_returns
    return

label setup_common:
    scene black with dissolve_scene
    $ quick_menu = True
    if "_old_history" in globals():
        $ _history = _old_history
        $ del _old_history
    return

label skip_to_part2:
    menu:
        "Part 1 ended with them about to read Portrait of Markov. If that doesn't sound familiar, exit and restart this process."
        "Sounds right.":
            pass
    "Then we need to ask about your choices."
    "Most of these don't have long-term consequences, but some of them do, and I don't necessarily want to reveal which ones, so I'll ask about all of them."
    call get_part1_choices
    $ persistent.newgame = 'glitch'
    $ persistent.menu_hide_monika = True
    "Now we return to the story."
    return

label skip_to_part3:
    menu:
        "Part 2 ended with the return of Markov. If that doesn't sound familiar, exit and restart this process."
        "Sounds right.":
            pass
    "Then we need to ask about your choices."
    "Most of these don't have long-term consequences, but some of them do, and I don't necessarily want to reveal which ones, so I'll ask about all of them."
    call get_part1_choices
    "Now, choices from part 2."
    call get_part2_choices
    $ persistent.newgame = 'deny'
    $ persistent.pom_menu = True
    "Finally, we return to the story."
    return

label get_part1_choices:
    menu:
        "Did you tell Monika a different name to call you?"
        "Yes, let me enter it.":
            # Clear the 'name_entry' placeholder so it doesn't still have MC's name in it.
            $ name_entry = ""
            call screen name_input(message="Player name")
            $ persistent.playername = _return
        "No, continue using my operating system account name.":
            $ persistent.playername = currentuser
    menu:
        "Did you correct Monika about your gender?"
        "Yes, I'm female":
            $ persistent.player_subj_pronoun = "she"
            $ persistent.player_obj_pronoun = "her"
            $ persistent.player_pos_pronoun = "her"
            $ persistent.player_copula_pos_pronoun = "hers"
        "No, I'm male":
            $ persistent.player_subj_pronoun = "he"
            $ persistent.player_obj_pronoun = "him"
            $ persistent.player_pos_pronoun = "his"
            $ persistent.player_copula_pos_pronoun = "his"
        "Yes, I entered pronouns manually":
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
            call screen name_input(message="possessive pronoun (alternative to his/hers):")
            $ persistent.player_copula_pos_pronoun = _return
    menu:
        "Did you insult MC for questioning your base64 decoding?"
        "Yes":
            $ persistent.player_insult_mc_for_questioning_base64 = True
        "No":
            $ persistent.player_insult_mc_for_questioning_base64 = False
    menu:
        "When you first gave Linda a file and the script deleted everyone, did you tell Sayori to try deleting and restoring the non-admin characters' files?"
        "Yes":
            $ persistent.sayori_reset_ynr = True
        "No":
            $ persistent.sayori_reset_ynr = False
    menu:
        "During the same event, did you restore Linda's file before or after starting a new game?"
        "Before":
            $ persistent.linda_in_void = True
        "After":
            $ persistent.linda_in_void = False
    menu:
        "Did you cooperate with [mc_name] to prove that he has free will?"
        "Yes":
            $ persistent.player_allow_free_will_test = 2
        "Yes, but only after calling him selfish and taking some convincing.":
            $ persistent.player_allow_free_will_test = 1
        "No. I pointed out that the only reason any of them are alive is because of me keeping them alive, so I make the decisions here.":
            $ persistent.player_allow_free_will_test = 0
            $ persistent.player_guilt_dokis[0] = True
    menu:
        "During the calm period at [mc_name]'s house where the hackers were taking a break and everyone on speculating, What was your initial position on the nature of their memories?"
        "Refused to speculate":
            $ persistent.player_speculate_on_past = 'refuse'
        "Said they were probably fake":
            $ persistent.player_speculate_on_past = 'fake'
        "Said they were probably real":
            $ persistent.player_speculate_on_past = 'real'
    "Okay, now we'll ask which questions you asked Monika and the others."
    # begin ch8 questions
    menu:
        "Did you ask Monika about the nature of player dialog choices?"
        "Yes":
            $ persistent.monika_questions['choices'] = True
        "No":
            $ persistent.monika_questions['choices'] = False
    menu:
        "Did you ask Monika about how admins experience time?"
        "Yes":
            $ persistent.monika_questions['time'] = True
            menu:
                "As a follow-up, did you ask Monika about the 'time gaps in your interface' she metioned?"
                "Yes":
                    $ persistent.monika_questions['mc_time'] = True
                "No":
                    $ persistent.monika_questions['mc_time'] = False
            menu:
                "As a follow-up, did you ask Monika and Sayori about dreams?"
                "Yes":
                    $ persistent.monika_questions['dreams'] = True
                "No":
                    $ persistent.monika_questions['dreams'] = False
        "No":
            $ persistent.monika_questions['time'] = False
    menu:
        "Did you ask how admin characters see the game world?"
        "Yes":
            $ persistent.monika_questions['perception'] = True
        "No":
            $ persistent.monika_questions['perception'] = False
    menu:
        "Did you ask Linda about why she had admin powers?"
        "Yes":
            $ persistent.monika_questions['linda_powers'] = True
        "No":
            $ persistent.monika_questions['linda_powers'] = False
    menu:
        "Did you ask Linda about the mention of her visiting porn websites in the story in Yuri's file?"
        "Yes":
            $ persistent.monika_questions['linda_porn'] = True
        "No":
            $ persistent.monika_questions['linda_porn'] = False
    menu:
        "Did you ask Linda and Renier about their relationship?"
        "Yes":
            $ persistent.monika_questions['linda_renier_relationship'] = True
        "No":
            $ persistent.monika_questions['linda_renier_relationship'] = False
    menu:
        "Did you suggest, jokingly or not, that Linda might be Natsuki's mom?"
        "Yes":
            $ persistent.player_suggest_linda_natsuki_mom = True
        "No":
            $ persistent.player_suggest_linda_natsuki_mom = False
    menu:
        "Did you ask Natsuki if she had forgiven Renier yet?"
        "Yes":
            $ persistent.monika_questions['natsuki_forgive_renier'] = True
        "No":
            $ persistent.monika_questions['natsuki_forgive_renier'] = False
    menu:
        "Did you ask Yuri about what it was like to cut herself?"
        "Yes":
            $ persistent.monika_questions['yuri_cutting'] = True
        "No":
            $ persistent.monika_questions['yuri_cutting'] = False
    menu:
        "Did you ask Monika about the nature of MC's poems?"
        "Yes":
            $ persistent.monika_questions['mc_poems'] = True
        "No":
            $ persistent.monika_questions['mc_poems'] = False
    "Alright, that's all for that conversation."
    # end ch8 questions
    menu:
        "When Renier wanted Natsuki and [mc_name] to cut themselves to find out more about the Third Eye, how did you resolve the situation?"
        "I told Renier he was wrong.":
            $ persistent.player_support_renier_experiment = 0
        "I told Natsuki and MC that they should do it, but that I wasn't forcing them.":
            $ persistent.player_support_renier_experiment = 1
        "I pointed out that it was extremely selfish and wrong for them to not make the sacrifice, given the gravity of the situation.":
            $ persistent.player_support_renier_experiment = 2
    if persistent.player_support_renier_experiment > 0 and persistent.mc_favorite == 'Natsuki':
        "So that means you found out in part 1 that MC has a Third Eye..."
    menu:
        "Last question. How did you respond to Renier's plan to activate Monika's Third Eye to escape the script?"
        "Supported it immediately.":
            $ persistent.player_support_escape_plan = 2
        "I was eventually persuaded.":
            $ persistent.player_support_escape_plan = 1
        "I never thought that was a good idea! Those idiots are lucky they didn't get themselves all killed!":
            $ persistent.player_support_escape_plan = 0
    return

label get_part2_choices:
    # This skips some consequence-less ones, but oh well.
    menu:
        "What was your stance on the morality of torturing murderers for scientific research?"
        "Voiced no disapproval of the thought.":
            $ persistent.player_pacifist = 0
        "Initially said \"It's not remotely acceptable to torture a defenseless prisoner\", but was later convinced that it could be acceptable.":
            $ persistent.player_pacifist = 1
        "Stuck to my guns that \"Nothing justifies such wanton cruelty\".":
            $ persistent.player_pacifist = 2
    menu:
        "What did you say when Sayori read about the torture of Libitina, and remarked that the cultists 'can't be forgiven'?"
        "Agreed wholehearedly":
            $ persistent.player_advocate_mercy[0] = -1
        "Said nothing":
            $ persistent.player_advocate_mercy[0] = 0
        "Said that \"There's no such thing as an unforgivable sin\".":
            $ persistent.player_advocate_mercy[0] = 1
    menu:
        "How did you respond to Sayori suggesting someone else risk themselves in her plan to restore Linda?"
        "Guilt tripped her":
            $ persistent.guilt_trip_sayori = 2
        "Asked why she couldn't do it herself, but didn't explicitly guilt trip her":
            $ persistent.guilt_trip_sayori = 1
        "Said nothing":
            $ persistent.guilt_trip_sayori = 0
    return
