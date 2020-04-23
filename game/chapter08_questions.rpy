label questions(showing_chars):
    show monika at foc
    m c121111 "So [persistent.playername], I've been meaning to give you a chance to ask some questions."
    $ qtext = "Is there anything you'd like to ask?"
    $ persistent.monika_questions = {
        'choices': False,
        'time': False,
        'mc_time': False,
        'dreams': False,
        'linda_powers': False,
        'linda_renier_relationship': False,
        'linda_porn': False,
        'perception': False,
        'natsuki_forgive_renier': False,
        'mc_poems': False,
        'yuri_cutting': False,
    }
    $ page = 0
label questions_menu:
    menu:
        m "[qtext]"
        "(done)":
            return
        "How does this question thing work?" if page == 0 and not persistent.monika_questions['player_choices']:
            m c121111 "I suppose that's a good question..."
            m c222111 "So, normally the script only gives you a choice when it's one that's part of the intended game, like which girl to write for."
            m c214111 "Outside of that, I don't think you can get any choices unless I - or someone else with code powers - gives you one."
            m c221111 "But I've learned how to not restrict you to options I can think of."
            m "It's a bit of an iffy hack, but it works."
            $ persistent.monika_questions['player_choices'] = True
        "How do you experience time?" if page == 0 and not persistent.monika_questions['time']:
            m c122111 "Ah. Well..."
            m c222111 "I experience in-game time, the same as the other characters do."
            m "I'm aware when there's a time gap in your interface, like when a day passes, but I still experience the entire evening and all."
            m "The only reason I can tell when you're skipping is because that information is stored in config.skipping."
            $ persistent.monika_questions['time'] = True
        "How do the 'time gaps in my interface' work?" if page == 0 and persistent.monika_questions['time'] and not persistent.monika_questions['mc_time']:
            m c222111 "Well, in game we all experience time as we would if our world was real."
            m "The game binds a display on your computer to [mc_name]'s experience."
            m "But sometimes, when the script calls for it, some time is skipped."
            m c221111 "We still experience it, but you don't."
            #show monika at std
            #mc "Huh..."
            #mc "I wonder if I can control that somehow?"
            #mc "Maybe it just happens when there's nothing during it that I felt was very important?"
            $ persistent.monika_questions['mc_time'] = True
        "What kind of dreams did you have overnight?" if page == 0 and persistent.monika_questions['time'] and not persistent.monika_questions['dreams']:
            m c122111 "Ah... that's a good question."
            m c222111 "I think it was after day 1 I had the dream I described in the special poem about falling asleep at a friend's house."
            m c214111 "It is an obvious allegory for what that day was like for me."
            m c121111 "Other than that, and not counting the nightmares from the game being off, I don't remember any dreams."
            show monika at std
            menu:
                " "
                "What about you, Sayori?":
                    pass
            if 's' in showing_chars:
                show sayori c21f111 at foc
            else:
                show natsuki at rhide
                hide natsuki
                show sayori c21f111 at foc(p44)
                $ showing_chars[3] = 's'
            s "Um..."
            s c213111 "I don't think I can remember any."
            s "I never had a night as President."
            show sayori at std
            menu:
                " "
                "Neither of you remember any dreams from before day 1 of the acts where you were President?":
                    pass
            menu:
                " "
                "Nothing that kind of foreshadowed it before you realized it?":
                    pass
            show monika at foc
            show sayori at foc
            ms "Nope."
            show sayori at std
            $ persistent.monika_questions['dreams'] = True
        "Linda, how do you have code powers?" if page == 1 and not persistent.monika_questions['linda_powers']:
            show monika at std
            if 'l' not in showing_chars:
                show natsuki at thide
                hide natsuki
                show linda 336111 at std(p43)
                $ showing_chars[2] = 'l'
            menu:
                " "
                "You weren't ever Club President, right?":
                    pass
            show linda at foc
            l 334221 "I don't think so..."
            l "I really don't know the answer to that."
            l 334111 "I suppose we'll need to unlock my memories to understand."
            l "Although..."
            l "It does seem that my powers are weaker than Monika's and Sayori's."
            l "Even now that I'm here, I can't manipulate the game as well as they can."
            l "I have a head start in knowledge of the code, but my abilities aren't as strong as theirs."
            menu:
                " "
                "(continue)":
                    pass
                "Vice Presidency?":
                    l "I don't know..."
                    l "I mean, as far as I remember, I wasn't physically in the world or part of the game until you gave me a character file."
                    l "So I don't see how I could have ever been Vice President of the club."
            show linda at std
            $ persistent.monika_questions['linda_powers'] = True
        "I want to know more about Linda and Renier's relationship." if page == 1 and not persistent.monika_questions['linda_renier_relationship']:
            if 'l' in showing_chars:
                show linda at foc
            else:
                show natsuki at thide
                hide natsuki
                show linda 334111b at foc(p43)
                $ showing_chars[2] = 'l'
            if 'r' in showing_chars:
                show renier u1112b
            else:
                show yuri at thide
                hide yuri
                # Yuri will either be in p41 or p42.
                if showing_chars.index('y') == 0:
                    show renier u1112b at std(p41)
                    $ showing_chars[0] = 'r'
                else:
                    show renier u1112b at std(p42)
                    $ showing_chars[1] = 'r'
            l 334111b "Ah..."
            show linda at std
            show renier at foc
            r u1113 "[persistent.playername], we've told you, we don't remember anything."
            show renier at std
            menu:
                " "
                "You seem to have some inklings.":
                    pass
            menu:
                " "
                "Linda, in Renier's file you wrote \"don't forget everything I taught you\".":
                    pass
            menu:
                " "
                "Don't you have any idea what you meant?":
                    pass
            show linda at foc
            l 334111 "No, I really don't."
            show linda at std
            show renier at foc
            r "Me neither..."
            r "I just know it meant something."
            show renier u1111 at std
            menu:
                " "
                "(continue)":
                    pass
                "You two seem close. Is it possible Linda is Natsuki's mom?":
                    show renier u1123b
                    show linda 114111b
                    if 'n' not in showing_chars:
                        show sayori at rhide
                        hide sayori
                        show natsuki c223112 at foc(p44)
                        $ showing_chars[3] = 'n'
                    else:
                        show natsuki c223112 at foc
                    n "For Christ's sake [persistent.playername], weren't you listening?"
                    n "Renier probably isn't even my real dad!"
                    n "So there's no logic there!"
                    show natsuki at std
                    show renier u1112
                    $ persistent.player_suggested_linda_natsuki_mom = True
            $ persistent.monika_questions['linda_renier_relationship'] = True
        "Linda, the story about you mentioned porn websites. Do you really do that?" if page == 1 and not persistent.monika_questions['linda_porn']:
            show monika at std
            if 'l' not in showing_chars:
                show natsuki at thide
                hide natsuki
                show linda 114113b at foc(p43)
                $ showing_chars[2] = 'l'
            else:
                show linda at foc
            l 114113b "Ah--"
            l 119113b "I don't remember the details of that story, but I swear I'm not a pervert!"
            show linda at std
            if 'r' in showing_chars:
                show renier u2226 at foc zorder 2
            else:
                show yuri at thide
                hide yuri
                # Yuri will either be in p41 or p42.
                if showing_chars.index('y') == 0:
                    show renier u2226 at foc(p41) zorder 2
                    $ showing_chars[0] = 'r'
                else:
                    show renier u2226 at foc(p42) zorder 2
                    $ showing_chars[1] = 'r'
            r "[persistent.playername], how can you judge Linda for that while you forgive Monika and Sayori for murdering us all?"
            show renier at std
            menu:
                " "
                "I wasn't trying to cast shame. I was just asking.":
                    show renier uf11
                    menu:
                        " "
                        "(continue)":
                            pass
                        "But seriously, porn is bad for you.":
                            menu:
                                " "
                                "It's addictive, and not a long-term source of happiness.":
                                    show linda at foc
                                    l "Ah--..."
                                    l "I kn- I-I'm not addicted to porn! I swear!"
                                    l "I don't know what that file was talking about!"
                                    l 119223b "If I was, that was a long time ago... or something."
                                    show linda at std
                                    show renier at foc
                                    r u2113 "Let's talk about something else."
                                    r u1112 "This is obviously making Linda uncomfortable."
                                    show renier at std
                    show linda 334221b
                "That comparison is totally inaccurate. Besides the excuses Monika and Sayori have, they've both already been more than punished.":
                    show linda 11a113b
                    show renier at foc
                    r u2293 "But so has she!"
                    r u1293 "Are you deaf, [persistent.playername]?"
                    r u2293 "She was in hell too the entire time!"
                    show renier at std
                    if 's' not in showing_chars:
                        if showing_chars[3] == 'n':
                            show natsuki at thide
                            hide natsuki
                        else:
                            show linda at thide
                            hide linda
                        show sayori c215212 at rightin(p44)
                        $ showing_chars[3] = 's'
                    else:
                        show sayori c215212 at foc
                    s "Um..."
                    show sayori c213212 at foc
                    if persistent.player_speculate_on_past == "real": # On this route, a similar exchange has already taken place.
                        s "Can we not fight this time?"
                    else:
                        s "Can we not fight?"
                    show sayori at std
                    show linda at foc
                    show renier u1111
                    l 334112b "Yes, let's please talk about something else."
                    l "I'm not going to go browsing porn or anything."
                    show linda 334222b at std
            show renier zorder 0
            $ persistent.monika_questions['linda_porn'] = True
        "Do Presidents see the world as 3-dimensional, or like I do?" if page == 2 and not persistent.monika_questions['perception']:
            m c221111 "We see it as if it's real to us, but we can also see your display."
            m c122111 "It's a bit weird to be able to see myself like this..."
            m c222111 "It's also kind of funny how the sprites work."
            m "Seeing how limited the onscreen representation of us is."
            m "Especially how each one of us has only a few poses that we use repeatedly."
            m "Like how I always do this pointing thing."
            m "But surprisingly, it's mostly accurate."
            m c122111 "That position just feels really natural to me."
            $ persistent.monika_questions['perception'] = True
        "Natsuki, do you forgive Renier yet?" if page == 2 and not persistent.monika_questions['natsuki_forgive_renier']:
            show monika at std
            if 'n' in showing_chars:
                show natsuki xc5112 at foc
            else:
                show sayori at rhide
                hide sayori
                show natsuki xc5112 at foc(p44)
                $ showing_chars[3] = 'n'
            if 'r' not in showing_chars:
                show yuri at thide
                hide yuri
                # Yuri will either be in p41 or p42.
                if showing_chars.index('y') == 0:
                    show renier u1111 at std(p41)
                    $ showing_chars[0] = 'r'
                else:
                    show renier u1111 at std(p42)
                    $ showing_chars[1] = 'r'
            if 'l' in showing_chars:
                show linda 114111
            n "We are {i}not{/i} having this conversation."
            show natsuki at std
            menu:
                " "
                "(continue)":
                    pass
                "But you forgive Monika! This is totally inconsistent!":
                    show natsuki at foc
                    n xc3112 "Monika had a way bigger excuse, and already spent the whole time in the void."
                    n "And like I said before, Yuri was only bad after she got tampered with."
                    n "Renier was just a prick all along."
                    show natsuki at std
                    show renier u1223 at foc zorder 2
                    r "I've had it with your ingratitude, Natsuki!"
                    r u2223 "I provided for you! Everything!"
                    r u1293 "And you repay me by comparing me to the girl who murdered you?"
                    show renier at std
                    show natsuki at foc
                    n c113112 "You only did that because you were responsible for me!"
                    n "Or thought you were!"
                    show natsuki at std
                    if 'l' in showing_chars:
                        show linda at foc
                    else:
                        show sayori at rhide
                        hide sayori
                        show linda 114114 at foc(p44)
                        $ showing_chars[3] = 'l'
                    l 114114 "Natsuki, you're being inconsiderate."
                    l "Renier had things just as bad as you!"
                    l "He was in poverty too, only he was working for it!"
                    l "Just because he was responsible for you doesn't mean you can count only the bad things about him!"
                    show linda at std
                    show renier uf21
                    show natsuki at foc
                    n "He hasn't even apologized!"
                    show natsuki at std
                    show renier u1223 at foc
                    r "Because you haven't shown any gratitude."
                    show renier uf21 at std
                    show natsuki xc5112 at foc
                    n "And I'm not going to."
                    show natsuki at std
                    show renier zorder 0
                    show monika at foc
                    m c114112 "Well, I don't think that went very well..."
                    show renier uf11
                    show natsuki xc6111
            if 'l' in showing_chars:
                show linda 114111
            $ persistent.monika_questions['natsuki_forgive_renier'] = True
        "Yuri, what was it like to cut yourself?" if page == 2 and not persistent.monika_questions['yuri_cutting']:
            if 'y' in showing_chars:
                show yuri sc4132 at foc
            else:
                show renier at thide
                hide renier
                if showing_chars.index('r') == 0:
                    show yuri sc4132 at foc(p41)
                    $ showing_chars[0] = 'y'
                else:
                    show yuri sc4132 at foc(p42)
                    $ showing_chars[1] = 'y'
            y "Eh--?"
            y sc2122 "Well..."
            show yuri c223177
            "Yuri clears her throat."
            y c225117 "At first it was a way of calming down."
            if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
                y "When I got too excited, like when I went to [mc_name]'s house..."
                y "I couldn't stop shaking with anxiety."
                y "I wasn't really that nervous..."
                y "But my body was acting like I was."
                y "And somehow, cutting helped me calm down."
                y "Maybe it was a distraction of some sort."
                y "But it seemed to have a more profound effect than that could explain."
                y c225247 "I did it again when you left the room..."
                show yuri at std
                mc "Oh no..."
                mc "I'm so sorry, Yuri."
                show yuri at foc
                y c225117 "In Act 2, I did it a lot more because I got so much more excited from being around you..."
                y "Even just reading with you would make me feel the need."
            else:
                y "When I got too excited..."
                y "Sometimes I just couldn't stop shaking and my heart would pound uncontrollably."
                y "And for some reason, cutting helped me calm down."
                y "Maybe it was a distraction of some sort."
                y "But it seemed to have a more profound effect than that could explain."
                y "In Act 2, I did it a lot more because I got so much more excited from being around [mc_name]..."
                y "Even just reading with him would make me feel the need."
            y "It wasn't until I wrote the..."
            y c225347 "The poem with blood on it..."
            y c225147 "That I started to actually enjoy cutting."
            y c225117 "Or maybe I just realized that I always had."
            y "It still hurt..."
            y "But, at the same time, it felt good."
            y "It wasn't that it wasn't painful, but it was outweighed by the pleasure."
            show yuri at std
            if 'l' in showing_chars:
                show linda at foc
            else:
                show natsuki at thide
                hide natsuki
                show linda 334111 at foc(p43)
                $ showing_chars[2] = 'l'
            l 334111 "Seems unmistakably the influence of the Third Eye."
            l 334221 "Now I {i}really{/i} want to get that book open."
            show linda at std
            $ persistent.monika_questions['yuri_cutting'] = True
        "What about [mc_name]'s poems?" if page == 2 and not persistent.monika_questions['mc_poems']:
            show monika at std
            mc "What about them?"
            show monika at foc
            m c122211 "Ahaha..."
            m c122212 "I forgot..."
            m c114112 "[mc_name], I hate to tell you this but your poems were a game mechanic."
            m "They were just twenty words [persistent.playername] picked off a list."
            show monika at std
            mc "But..."
            mc "But...."
            "I realize I don't remember any of them."
            mc "But wait! The other girls must have seen real poems when they looked at mine, right?"
            if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
                if 'y' in showing_chars:
                    show yuri c115112 at foc
                else:
                    show renier at thide
                    hide renier
                    if showing_chars.index('r') == 0:
                        show yuri c115112 at foc(p41)
                        $ showing_chars[0] = 'y'
                    else:
                        show yuri c115112 at foc(p42)
                        $ showing_chars[1] = 'y'
                y "Um..."
                y c125112 "I'm sorry to say, but I don't remember your poems either."
                y "I think the game merely gave us nondescript memories, like it did with Portrait of Markov."
                show yuri at std
            else:
                if 'n' in showing_chars:
                    show natsuki c114114 at foc
                else:
                    show sayori at thide
                    hide sayori
                    show natsuki c114114 at foc(p44)
                    $ showing_chars[3] = 'n'
                n "Um..."
                n "I'm sorry to say this, but I don't remember your poems either."
                n c114111 "The game probably just gave us nondescript memories, like it did you and Yuri with Portrait of Markov."
                show natsuki at std
            mc "So it was all a lie."
            mc "I thought I was getting better at poetry..."
            if persistent.mc_favorite == "Sayori":
                if 's' in showing_chars:
                    show sayori c115112 at foc
                else:
                    if showing_chars[3] == 'n':
                        hide natsuki at rhide
                        hide natsuki
                    else:
                        hide linda at rhide
                        hide linda
                    show sayori c115112 at foc(p44)
                    $ showing_chars[3] = 's'
                s "Aw..."
                s c213112 "[mc_name], you don't have to be a good writer."
                s "Maybe writing just isn't your thing."
                s "And that's fine."
                s tc1211 "I mean, I remember it wasn't my thing either until I randomly decided it would be fun to help start a club..."
                show sayori at std
                mc "Ahaha."
                mc "Well, thanks."
                mc "I appreciate that."
                show sayori c111111
            elif persistent.mc_favorite == "Yuri":
                show yuri at foc
                y c124118 "[mc_name]..."
                y c125112 "That's okay."
                y "You don't have to be a great poet."
                y c125213 "You're a good enough friend without that."
                show yuri at std
                mc "Ah..."
                mc "Thanks..."
            else:
                show natsuki at foc
                n c114114 "Well..."
                n "You don't have to be a writer, you know."
                n c222156 "I mean, I wouldn't mind having that advantage over you for the rest of our lives."
                show natsuki at std
                mc "But you already have the advantage of being an impeccable baker..."
                show monika c122131 at foc
                m "Ahaha~"
            $ persistent.monika_questions['mc_poems'] = True
        "(more options)" if not all(persistent.monika_questions.values()):
            $ page = {0:1,1:2,2:0}[page]
            jump questions_menu
    $ qtext = "Any other questions?"
    show monika c121111 at foc
    jump questions_menu
