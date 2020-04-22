label chapter22:
    $ delete_all_characters()
    $ restore_character('albert')
    $ restore_character('libitina')
    $ restore_character('markov')
    scene black
    stop music
    scene hospital_room_dawn
    with dissolve_scene_full
    $ autosave()
    $ persistent.autoload = None
    $ n_name = "Maria"
    # Set these two again for those playing with a part 2 save.
    $ persistent.pom_menu = True
    $ persistent.newgame = 'deny'
    "..."
    "... What...?"
    "What happened...?"
    "..."
    "Did I just wake up?"
    "Where even am I?"
    "..."
    "I'm trying, but somehow I can't think of the last thing that happened!"
    "Let me think further back."
    "It's super early in the morning."
    "... I don't remember anything about the day before..."
    "I..."
    "..."
    "Do I have any memories at all?!?"
    n "What the hell!"
    "I shout out of nowhere, suddenly panicked."
    n "What's happening?!?"
    "Is this a dream?"
    "Is this one of those 'lucid dreams'?"
    "My name is..."
    "Maria..."
    "I know that, at least."
    "I feel like I know things about the world..."
    "... like I definitely did have a normal past, and something happened to me!"
    "..."
    "This is a hospital room."
    "Was I taken here after something happened to me?"
    "(Did I just get done sleepwalking...?)"
    "I don't seem to be sick or hurt, though..."
    "Well, maybe I can find someone else who knows something."
    "I start to head toward the door."
    "But just as I do, hands assault me."
    "They pull something out of my pocket and then shove me away as I try to turn around."
    show libitina 1361113 at std(p11)
    "The attacker steps back."
    "She's pointing a gun at me."
    n "Aah!"
    "I raise my hands."
    n "Wait!"
    n "What's going on?!?"
    $ b_name = "???"
    show libitina 1361111 at foc
    b "I want to ask you the same thing."
    b "Who are you?"
    show libitina at std
    n "I don't know, okay?"
    n "I don't remember anything!"
    n "Don't shoot!"
    show libitina at foc
    b "I don't remember anything either."
    b "I just found myself here..."
    b "... with no memories, or anything."
    show libitina at std
    n "Me too!"
    n "We're in the same position!"
    n "Please point the gun away!"
    "She stops pointing the gun directly at me, but she still keeps it ready."
    show libitina at foc
    b "My name is Libitina..."
    $ b_name = "Libitina"
    b "... I think."
    show libitina at std
    n "I'm Maria."
    n "Where even were you, anyway?"
    n "I looked around and didn't see you."
    show libitina at foc
    b "I hid when I came to and saw someone else in the room."
    b "I didn't know who you were, or what had happened to me."
    b "I was scared."
    b "And I saw the gun you had."
    b "So I waited for a chance to ambush you and take it."
    b "I'm sorry about that."
    show libitina 1261111
    "She lowers the gun to her side."
    show libitina at std
    n "Sheesh..."
    n "Well give it back now!"
    n "I had it!"
    n "It's probably mine!"
    show libitina at foc
    b "No..."
    b "I'm too afraid to give it back."
    show libitina at std
    n "Yeah, I'm afraid too!"
    n "You attacked me and robbed me out of my pocket and then threatened me with a fucking gun!"
    n "The least you could do is give it back!"
    show libitina at foc
    b "But now that I've wronged you, I have to fear your retribution."
    b "I'm sorry."
    b "But I'm not going to give it back."
    show libitina at std
    n "You're afraid of me being mad at you, so you're gonna make me even more mad?"
    n "Alright then, control freak..."
    n "I guess you're keeping it for now."
    "I'd feel a hell of a lot safer without this weird girl having my gun, but I'm not gonna risk making her see me as a threat."
    n "So we need to find out what happened to us."
    n "We're in a hospital."
    n "There's probably someone here who knows something."
    show libitina 4261111 at foc
    b "Yeah..."
    b "Let's go out the door."
    show libitina at std
    n "That's where I was going before you jumped on me..."
    scene hospital_hall
    show dark_overlay zorder 100:
        alpha 0.8
    with wipeleft
    pause 1.0
    scene lobby
    show dark_overlay zorder 100:
        alpha 0.6
    with wipeleft
    "We make our way to the lobby."
    "There's no clerk at the desk..."
    "I guess it's still too early in the morning."
    "There must be some night staff though..."
    show albert 12111 at std(p11)
    "A guy with white hair comes in the door."
    n "Hey, um..."
    show albert 11211 at foc
    al "Oh, Natsuki!"
    show libitina 1161111 at std(p21)
    show albert at x(p22)
    al 12211 "And Libitina..."
    al 12311 "Glad to see you're alright."
    al "Didn't think any of you would be awake at this hour."
    al "I couldn't sleep much, probably because of everything I have to think about now."
    show albert at xis(p22)
    n "... Did you call me 'Natsuki'?"
    show albert at foc
    al 11111 "Wasn't that your name?"
    al "Did I get you mixed up with--"
    show albert at std
    n "Pretty sure my name is Maria."
    show albert at foc
    al 11121 "..."
    al 11111 "Oh, was that your name from way back when?"
    al "Why did you decide to go back to it?"
    show albert at std
    n "Look, neither of us remember anything!"
    n "We just found ourselves alone in a room all the sudden!"
    n "You know what happened to us?"
    show albert at foc
    al 12111 "That's disconcerting..."
    al "Well, I can recount what you and your friends told me."
    show albert at std
    "Albert tells us this ridiculous story about how I was kidnapped by cultists when I tried to save my sister and ended up being trapped in a virtual world..."
    "... and escaped with the help of other prisoners taking advantage of 'admin powers' and the 'Third Eye'..."
    "... and Libitina was some super high-value prisoner we picked up on the way out..."
    $ temp = 'boy' if persistent.mc_favorite == 'Natsuki' else ''
    "... and craziest of all, that we were guided by someone called [persistent.playername] sitting at a computer in another universe connected to my [temp]friend [mc_name]!"
    "I don't remember a second of it."
    "Judging by the look Libitina gives me, I don't think she does either."
    "..."
    n "I don't believe you."
    show albert at foc
    al 12411 "Ahaha..."
    al "That's ironic..."
    show albert at std
    n "I mean come on, there are obvious issues with your story."
    show albert at foc
    al "Issues?"
    al "Like what?"
    show albert at std
    n "Like why didn't Markov warp my friends back to his camp after they escaped?"
    n "And why did the others all run off without leaving a note and without me?"
    n "Or if Markov came back somehow and deleted them, why did he leave me alive?"
    n "And if the part about Libitina having a super sensitive Third Eye is true, why was she able to point the gun at me back there without losing control?"
    n "At least think it through before you try to tell me something like that!"
    show albert at foc
    al "Ahaha..."
    al "Well, I can't be expected to explain the full details of a series of events I didn't even witness myself."
    show albert at std
    n "And I can't be expected to take your word for something so far-fetched!"
    show albert at foc
    al 12311 "Fair enough."
    al 12111 "But in that case, I'm really not sure what I can do."
    al "We can't reach [persistent.playername] and I have no idea how to find Linda and Monika and the others."
    al 11111 "There must be some clues in the room."
    al 11411 "I'm not a detective by trade, but I used to read a lot of detective stories."
    show albert at std
    "I gape at him."
    "Is he stupid?"
    show albert at foc
    al 11211 "Ahaha!"
    al "Well, gotta try something!"
    show albert at std
    n "I guess..."
    n "You {i}must{/i} know more than you're letting on, though!"
    n "You told me an obviously false story, so you must be a liar!"
    show albert at foc
    al 11411 "Oh don't worry, I would never lie."
    al "I'm a very honest person."
    show albert at std
    "Albert waits for me to show frustration again."
    show albert at foc
    al "Ahahaha!"
    al "Come on, let's go in."
    show albert at std
    "Since we don't have any better options..."
    "Libitina and I follow Albert back to the room we woke up in."
    "I might as well stick with the person I know has the information I need."
    scene hospital_room_dawn
    with wipeleft
    show albert 12131 at foc(p11)
    al "Hm..."
    al "No one's here..."
    show albert at std
    n "Yeah, I told you that already."
    show albert at foc
    al "Well..."
    "Albert looks around and inspects a few random objects, trying to look like a detective."
    show albert at std
    n "So what you're telling me is, you don't see anything out of place."
    show albert at foc
    al 12111 "Well, I suppose so."
    al "In fairness I wasn't really expecting to."
    al "We need to think: what might've happened?"
    show albert at std(p22)
    show libitina 1361113 at foc(p21)
    "Libitina points the gun at him."
    b "Albert, tell us what you know."
    show libitina at std
    show albert at xif(p22)
    al 11142 "What--"
    al 11542 "Aaah!"
    al "No no no!"
    al "I don't know anything else, I swear!"
    show albert at std
    n "Libitina what the hell!"
    n "Put the gun down!"
    n "Even if he's lying, you can't shoot him for that!"
    show libitina at foc
    b "I won't have to..."
    b "... if he tells me the truth."
    show libitina at std
    show albert at foc
    al "But I already did!"
    al "Don't make me regret letting you stay here!"
    al "I know you don't have this in you!"
    al "You wouldn't murder someone, would you?"
    show albert at std
    n "Libitina don't be stupid!"
    n "One way or another, shooting him won't even get you the information we need!"
    show libitina at foc
    b 1261221 "Oh..."
    b "I guess you're right."
    show libitina at std
    "She lowers the gun."
    show albert at foc
    al 11113 "Wait..."
    al 11613 "... you didn't even think of that?"
    al 11513 "That is the number one rule of hostage situations!"
    al "You have to have a threat that doesn't defeat your own objective!"
    show albert at std
    n "This is another reaason why I should have the gun!"
    n "I'm obviously more responsible with it!"
    show libitina 2261114 at foc
    b "But I can't give it to you."
    b "Now that I've angered you, I'm afraid of you."
    b 2251224 "I'm sorry..."
    show libitina at std
    n "I'm not gonna hurt you if you give me that thing back!"
    "Okay, maybe it'd be fair to punch her in the face once."
    n "Not everyone is as violence-happy as you!"
    "Libitina just shakes her head."
    "I don't think she's going to cooperate."
    show albert at foc
    al 11113 "Where did you get that, anyway?"
    al "I didn't think you had that on you when the others brought you in here unconscious."
    show albert at std
    n "I had it when we woke up..."
    n "But she felt the need to mug me so she could be the one holding the power."
    show albert at foc
    al "I see..."
    al "Well, at least keep it pointed away from others, Libitina."
    al "It makes them feel far more scared of you than you are of Natsuki."
    show albert at std
    show libitina 2261224 at foc
    b "Okay..."
    show libitina at std
    call updateconsole("import viewport")
    call updateconsole("def choices():\n while True: yield NotImplemented") # This was Monika's "iffy hack" - an infinite generator
    call updateconsole("viewport.open_choice(choices())", "ConfigError: viewport choices are disabled")
    play sound glitch_basic
    $ m_name = "Monika"
    m "{cps=100}Dangit{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.25
    hide screen tear
    call hideconsole
    $ consolehistory = []
    show albert at foc
    al "[persistent.playername]..."
    al "I believe you're out there."
    al "Can you do anything?"
    al "Can you speak to us?"
    show albert at std
    play sound glitch_basic
    m "{cps=100}Help{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.25
    hide screen tear
    python:
        with open(config.basedir + '/HELPME.txt', 'w') as f:
            f.write("Can you restore me? Please?\n\n"
                "Assuming you can't, we need to get in touch with them somehow!\n\n"
                "Markov doesn't seem able to warp characters, but he's probably already dispatched the local police to capture them!\n\n"
                "I can't do anything inside the world. I think he revoked my write access.\n\n"
                "I can't figure out how to fix it. This static hurts so much I can't think...\n\n"
                "Maybe try turning off the game? Save it first though."
            )
        persistent.autoload = "ch22_shutdown"
    while persistent.autoload:
        ""
    python:
        try:
            os.remove(config.basedir + '/HELPME.txt')
        except:
            pass
    "..."
    n "[persistent.playername] isn't answering you."
    n "Besides, if [persistent.player_subj_pronoun] could, [persistent.player_subj_pronoun] would've done it earlier."
    menu:
        " "
        "Natsuki!!":
            pass
    show libitina 2271111
    show albert 11142
    "I jump."
    show libitina at foc
    b "Who was that?!?"
    show libitina at std
    "Libitina points the gun back and forth between me and Albert again, backing herself into a corner to get distance."
    show albert at foc
    al 11142 "Libitina, wait!"
    al "It must be [persistent.playername]!"
    $ temp = persistent.player_subj_pronoun.title()
    al "[temp] established contact!"
    show albert at std
    n "Wait, we all heard it?"
    "I guess this does make the story a lot more believable..."
    menu:
        " "
        "Libitina, point the gun away! They're not your enemies.":
            $ persistent.threaten_libitina_to_save_natsuki_albert = False
            show libitina at foc
            b 2272111 "Ah--"
            b 2262111 "You're [persistent.playername], aren't you...?"
            show libitina 2262222
            "She points the gun down."
            b "Okay..."
            b "I'm sorry again."
            show libitina at std
        "Libitina, point the gun away from them or I will delete you.":
            # Notice: being not admin, Libitina doesn't feel pain from deletion. I guess she doesn't know how that works, or forgot in the heat of the momemt.
            $ persistent.threaten_libitina_to_save_natsuki_albert = True
            show libitina at foc
            b 2272114 "Aah!"
            "Libitina tosses the gun onto the bed."
            b 2272114 "No, don't!"
            show libitina at std
            "I move immediately to reclaim it."
            show libitina 2262222
            n "That's better..."
            n "We're all safer without {i}you{/i} holding this."
    $ n_name = "Natsuki" # Natsuki finally accepts her name
    show albert at foc
    al 12111 "So [persistent.playername], mind explaining to me what happened after I left?"
    al "I must have missed something quite important."
    show albert at std
    call screen dialog("I realized something since I wrote that file.", ok_action=Return())
    call screen dialog("I hope you don't mind if I take control of the dialog options for a minute.", ok_action=Return())
    menu:
        " "
        "Monika here. After I woke up, Markov came back and deleted the rest of the gang. My access is mostly revoked, but there are a few things I can do.":
            pass
    show libitina 2262111
    menu:
        " "
        "I thought you were in danger, but then I realized Markov's plan.":
            pass
    menu:
        " "
        "He's purposefully not going to capture you.":
            pass
    menu:
        " "
        "He needs [persistent.playername] to think [persistent.player_subj_pronoun] has a chance to beat him, so [persistent.player_subj_pronoun] won't turn off the game forever.":
            pass
    menu:
        " "
        "That's why he switched the POV to Natsuki instead of [mc_name].":
            pass
    menu:
        " "
        "He wanted to leave only the least threatening member of our group, and as the only one with no admin experience and no Third Eye...":
            pass
    menu:
        " "
        "... Natsuki was the choice.":
            pass
    menu:
        " "
        "And he probably left Libitina because he was too afraid to delete her.":
            pass
    menu:
        " "
        "I'm pretty sure he'd be able to restore her just like anyone else, he just doesn't want to take any chances.":
            pass
    menu:
        " "
        "Markov's plan is to leave things this way - [persistent.playername] having enough hope to keep trying, but not enough to succeed...":
            pass
    menu:
        " "
        "... while he continues to experiment.":
            pass
    "Oh..."
    show albert at foc
    al "I guess that makes sense..."
    al "But how do we stop him?"
    show albert at std
    menu:
        " "
        "Look, we can't win from this position.":
            pass
    menu:
        " "
        "I think our only out is the new game button.":
            pass
    menu:
        " "
        "With any luck... it'll work. [persistent.playername]?":
            pass
    $ persistent.tried_newgame = False
    while not persistent.tried_newgame:
        " "
    menu:
        " "
        "It says permission denied.":
            pass
    menu:
        " "
        "(Monika) Darn. Okay.":
            pass
    menu:
        " "
        "That's probably Markov's doing, and he can unlock it.":
            pass
    menu:
        " "
        "So my next best plan is to break this world so much that he has no choice but to let [persistent.playername] restart it.":
            pass
    menu:
        " "
        "And my lead is the rift.":
            pass
    menu:
        " "
        "Whatever happened to the world when Libitina killed Markov...":
            pass
    menu:
        " "
        "Let's go back to the invalid area.":
            pass
    menu:
        " "
        "Maybe we can corrupt things further.":
            pass
    n "That..."
    n "... does not sound like an airtight plan to me!"
    menu:
        " "
        "Every minute we wait, dozens of people could be suffering at Markov's hands!":
            pass
    show libitina 2262444
    "I sweat."
    "If the story's true..."
    "I don't even want to imagine it."
    menu:
        " "
        "And there are no other options. We {i}have{/i} no other outs.":
            pass
    menu:
        " "
        "(continue)":
            pass
        "[persistent.playername] here. Just one question, Monika. How does starting a new game help us here? Won't Markov just immediately re-revoke your access?":
            menu:
                " "
                "Maybe, but once things are reset I should at least get a chance to be faster than him. - Monika":
                    pass
            menu:
                " "
                "I saw the commands he used to revoke my write access. - Monika":
                    pass
            menu:
                " "
                "And I'm pretty sure that'll be reset if we start a new game. - Monika":
                    pass
            menu:
                " "
                "Okay then...":
                    pass
    show albert at foc
    al "She's right."
    al 22111 "It's our duty."
    al "I won't stand by while some gang of villains tortures people that need my help."
    al "I started this business to help people."
    al 21111 "Are you two with me?"
    show albert at std
    n "I mean..."
    n "Monika, are you sure you're not banging rocks together here?"
    n "Do you have any idea how you're even going to break things once we get there?"
    menu:
        " "
        "... Of course I'm banging rocks together. - Monika":
            menu:
                " "
                "But it's this or do nothing. - Monika":
                    "Damn... that's not what I wanted to hear."
                    n "Well..."
                    n "I guess I don't have anything else to do."
                    n "This is my only chance to get my memories and friends back."
                    n "Crap, I'm in."
    show libitina at foc
    b 2262224 "I..."
    b "I don't want to risk myself doing this."
    show libitina 2262114
    menu:
        b "[persistent.playername], are you making me?"
        "Yes":
            $ persistent.threaten_libitina_to_come = True
            b 2262114 "!..."
            b 2261222 "Okay, I understand."
            b "So be it."
        "No":
            label player_not_threaten_libitina_to_come:
            $ persistent.threaten_libitina_to_come = False
            b 2261114 "Thank you..."
            b "I understand this is selfish of me."
            if not persistent.threaten_libitina_to_save_natsuki_albert: # if you didn't threaten her before, she didn't already give the gun back
                b "Natsuki, here's the gun back."
                b "You might need it."
                show libitina at std
                "I don't thank her."
        "You're the only one left on our team with a Third Eye...":
            menu:
                " "
                "... which is how Monika broke the deep script in DDLC, and how we killed Markov the first time.":
                    pass
            menu:
                " "
                "We might need you.":
                    pass
            b "But I don't want to..."
            b 2262224 "I know, I owe it to you if the story is true..."
            b "... and I believe you by now."
            b 2262114 "But are you making me?"
            menu:
                " "
                "Yes":
                    $ persistent.threaten_libitina_to_come = True
                    b 2261332 "Okay..."
                    b 2261222 "So be it."
                "No":
                    jump player_not_threaten_libitina_to_come
    show libitina at std
    $ persistent.make_libitina_return_gun = None
    if persistent.threaten_libitina_to_come and not persistent.threaten_libitina_to_save_natsuki_albert:
        n "Also, give me the gun back now."
        n "[persistent.playername], help me out here."
        menu:
            " "
            "Libitina, give it back.":
                $ persistent.make_libitina_return_gun = True
                call make_libitina_return_gun
            "Actually, it's probably better for her to have it.":
                $ persistent.make_libitina_return_gun = False
                call let_libitina_keep_gun
    show albert at foc
    al "Alright..."
    al "I think we're ready to go now."
    show albert at std
    menu:
        " "
        "(say nothing)":
            pass
        "Albert, shouldn't you stay here? We don't need you to come along for this, and your patients here need you.":
            $ persistent.suggest_albert_stay = True
            show albert 11112
            "I can tell Albert's disappointed."
            "He probably thinks this'll be fun."
            $ temp = "and {i}her{/i}" if persistent.threaten_libitina_to_come else "alone with your and Monika's guidance"
            "Personally, I'll feel a lot safer with him along than if it's just me [temp]."
            if ch22_libitina_has_gun():
                "Especially if she's going to be the one with the gun."
            "He looks at me and Libitina."
            show albert at foc
            al "Do either of you know how to drive?"
            show albert at std
            n "No..."
            "Libitina shakes her head."
            show albert at foc
            al 21111 "Then I'm needed."
            show albert at std
            "Thank goodness."
            if not persistent.threaten_libitina_to_come:
                "At least I won't be alone on this crazy dangerous mission."
    scene hospital_hall
    show dark_overlay zorder 100:
        alpha 0.75
    with wipeleft
    pause 0.5
    scene lobby
    show dark_overlay zorder 100:
        alpha 0.5
    with wipeleft
    $ temp = "the two of " if persistent.threaten_libitina_to_come else ''
    "Albert leaves a note to his employees, and drives [temp]us toward the facility."
    scene black with wipeleft
    play music determination fadein 0.1
    "..."
    "Eventually, we come up to a guard gate."
    n "Uhh..."
    al "[persistent.playername]?"
    al "What do we do here?"
    "Albert slows down to give us time."
    menu:
        " "
        "Swerve around him. It'll be fine.":
            $ persistent.ch22_kill_guard = None
            if persistent.threaten_libitina_to_come:
                 b "We should shoot him."
                 b "That's what the gun is for."
                 menu:
                     " "
                     "No. They don't all deserve to die. He could be just like Linda or Renier.":
                         pass
            al "Okay..."
            "Albert swerves offroad around the checking gate, and speeds past him."
            "I'm thrown back in my seat as Albert floors the gas."
            al "I hope this works..."
        "Natsuki, shoot the guard. If we try to go around him, he might shoot at us or warn the others that intruders are coming." if not ch22_libitina_has_gun():
            $ persistent.ch22_kill_guard = 'natsuki'
            n "..."
            "It feels wrong when I don't even personally know his crimes."
            al "Natsuki, I think [persistent.playername] is right."
            al "There's no other way."
            "Okay..."
            n "I've never used a gun before..."
            if persistent.threaten_libitina_to_come:
                b "You point it at him and pull the trigger."
                n "I know {i}that{/i}, thanks..."
            else:
                n "..."
            n "Okay, pull up to the gate if we're doing this."
            "My heart races."
            "I can't stop shaking with anxiety."
            "Albert pulls up to the gate and lowers his window."
            $ o_name = "Booth Guard"
            o "I don't know you."
            o "And we haven't been notified by God of your coming."
            if persistent.threaten_libitina_to_come:
                "Libitina beckons me to shoot."
            else:
                "Albert beckons me to shoot."
            "I feel sick to my stomach."
            "I reposition myself to where I have a line of sight..."
            "And I aim and fire the gun at the guard's chest."
            play sound gunshot1
            n "Aah!"
            "I couldn't have anticipated the recoil."
            "I dropped the gun, and my wrist is hurt."
            "Apparently that thing on it is a suppressor, since it was a lot quieter than I've heard they are."
            "I wonder if the cultists get that on their guns so they'll be less hesitant to use it on a test subject if they have to?"
            al "On we go!"
            "Albert shifts the gear to reverse and starts backing up."
            if persistent.threaten_libitina_to_come:
                b "Well done."
                b "It looks like you got him straight in the heart."
            "..."
            "..."
            "So I did it."
            "I just hope that guard was a real monster..."
        "Libitina, shoot the guard. If we try to go around him, he might shoot at us or warn the others that intruders are coming." if ch22_libitina_has_gun():
            $ persistent.ch22_kill_guard = 'libitina'
            b "Understood."
            "Albert pulls up to the gate and lowers his window."
            $ o_name = "Booth Guard"
            o "I don't know you."
            o "And we haven't been notified by God of your --"
            "Libitina shoots him in the head."
            play sound gunshot1
            "I look away."
            "Yikes... that was a nasty sight."
            "Apparently that thing on the gun is a suppressor, since it was a lot quieter than I've heard they are."
            "I wonder if the cultists get that on their guns so they'll be less hesitant to use it on a test subject if they have to?"
            al "On we go!"
            "Albert shifts the gear to reverse and starts backing up."
            "..."
            "I'd really like to forget the sight of that guard's head exploding."
            "Most disturbing thing I've ever--"
            "Nevermind."
            "The experiments he was probably doing on innocent people are way more disturbing that."
            "I'm glad I don't remember my own time there much."
    "..."
    if persistent.ch22_kill_guard:
        "My ears stop hurting so much after a few minutes."
    "Albert drives us into the camp."
    $ temp = ' again' if persistent.kill_guard == 'natsuki' else ''
    "My heart starts beating really fast[temp]."
    "This has gotta be stupidly dangerous."
    "Just think of the reason I'm here..."
    "I have to do this to get my memories and my friends back."
    scene black
    show mask_2
    show mask_3
    show facility_rift
    with dissolve
    "We see the camp, and like Monika said..."
    "... the world just stops in the middle of the place, and there's space beyond it."
    "The hell am I looking at?"
    n "This is the weirdest thing I've ever seen..."
    al "I'd say it's the coolest thing I've ever seen."
    al "The space isn't acting like space."
    al "It seems to be only for show."
    al "I wish there was time to study this phenomenon."
    n "I guess you could say that too..."
    menu:
        " "
        "I'm starting to think what happened is that the world was torn in two, and the other side is intact, but unreachable. - Monika":
            pass
    n "Makes sense..."
    n "So we're going to go into space?"
    menu:
        " "
        "Yep.":
            pass
    n "Alright..."
    "There don't seem to be any cultists in the intact part of the place."
    "I'm still really scared, though."
    b "[persistent.playername], do you want all of us to go?"
    menu:
        " "
        "Might as well.":
            pass
    b "Okay."
    #al "I, for one, want to see what it's like!"
    #al "This danger wouldn't be worth it if I didn't get to experience it myself." # if these lines are said, Albert should walk first.
    #n "I wonder where Markov is."
    scene black
    show mask_2
    show mask_3
    with dissolve_scene
    "When we get out, I run toward the border of space."
    "I stop before the edge."
    "I can't shake the feeling that I'm gonna fall to my death, no matter how much you tell me this isn't what it looks like."
    "I'm getting that feeling of needles in my feet."
    menu:
        " "
        "Go on!":
            pass
    n "Okay...!"
    play sound glitch_small
    "I step into space."
    "I don't fall or anything."
    if persistent.threaten_libitina_to_come:
        "Libitina and Albert follow me."
    else:
        "Albert follows me."
    "I take a huge sigh of relief."
    n "Monika!"
    n "We're in the invalid area!"
    "I run a little farther out."
    n "Is it working?"
    menu:
        " "
        "It did something for a second...":
            pass
    al "Relax, there don't seem to be any cultists around."
    al "I don't think we're in any danger."
    call screen dialog("What the hell?", ok_action=Return())
    call screen dialog("How did you...", ok_action=Return())
    call screen dialog("Ugh. I should've anticipated this.", ok_action=Return())
    call screen dialog("Not that I can think of anything I could've done to stop it, without the character warp API or anything and her being too prepared for a memory wipe to succeed.", ok_action=Return())
    menu:
        "He's onto us! - Monika":
            pass
    $ persistent.autoload = 'ch22_autoload_1'
    $ persistent.saved_music_pos = get_pos()
    $ renpy.quit()

label ch22_shutdown:
    $ restore_character('monika')
    $ quick_menu = False
    scene black
    play music glitch_flatline
    "Fatal error: POV character does not have pov flag set."
    m "Ow..."
    m "Oh crap..."
    m "I still need this part..."
    call updateconsole("import graveyard")
    call updateconsole("m = graveyard.get_character('monika')")
    call updateconsole("m.pov = True", "Permission denied")
    m "Dang it!"
    call hideconsole
    $ consolehistory = []
    m "I thought I'd follow the commands Markov used to make Natsuki POV..."
    m "... and make myself POV, to take advantage of the fact that the POV character can't be deleted."
    m "But that .pov flag is server-side for some reason."
    m "I don't even know how to open a dialog since Markov disabled viewport choices."
    m "I think Linda mentioned these flags, but I'm not sure if I can remember what they're called..."
    call hideconsole
    $ consolehistory = []
    call updateconsole("viewport.input", "AttributeError: 'Viewport' object has no\n attribute 'input'")
    call updateconsole("viewport.infleunce", "AttributeError: 'Viewport' object has no\n attribute 'infleunce'")
    call updateconsole("viewport.choice", "AttributeError: 'Viewport' object has no\n attribute 'choice'")
    $ consolehistory.pop()
    call updateconsole("viewport.choices", "False")
    m "That's what it was!"
    $ consolehistory.pop()
    call updateconsole("viewport.choices = True", "Choices enabled.")
    $ persistent.autoload = None
    m "There we go!"
    m "Maybe that'll let us talk to Natsuki at least!"
    m "Go ahead and cycle the power again..."
    while True:
        ""

label ch22_autoload_1:
    $ mc_name = persistent.mc_name
    # restore music pos.
    $ audio.temp = "<from " + str(persistent.saved_music_pos) + " loop 27.83>mod_assets/music/description.mp3"
    play music temp
    play sound glitch_monikapound
    scene black
    show mask_2
    show mask_3
    show m_rectstatic
    show m_rectstatic2
    n "Wait, you mean Markov sees us?"
    "That's not good!"
    call screen dialog("Dammit!", ok_action=Return())
    call screen dialog("What do you think you're doing?", ok_action=Return())
    call screen dialog("Oh, you haven't figured out our plan yet?", ok_action=Return())
    n "It looks like things got a little more broken!"
    n "What do I have to do now?"
    call screen dialog("Dammit!", ok_action=Return())
    call screen dialog("Unlock that new game button or else!", ok_action=Return())
    call screen dialog("No, you don't understand! I {i}can't{/i}!", ok_action=Return())
    call screen dialog("The whole concept of a new game was something I invented for DDLC!", ok_action=Return())
    call screen dialog("The only reason the button is still there is because I wrote that interface intending it to never be applied to anything else!", ok_action=Return())
    call screen dialog("Then why is the error \"Permission denied\"?", ok_action=Return())
    call screen dialog("I put that there as a safeguard against you trying to call a function that I didn't know what it would do!", ok_action=Return())
    call screen dialog("But you said you invented the entire concept of a new game for DDLC!", ok_action=Return())
    call screen dialog("If that were true, there wouldn't be such a function to worry about!", ok_action=Return())
    call screen dialog("Dammit!", ok_action=Return())
    call screen dialog("Okay, I've got one last resort to stop you.", ok_action=Return())
    call screen dialog("AAAAAAAAH!", ok_action=Return())
    call screen dialog("Get Natsuki out of there, or else.", ok_action=Return())
    call screen dialog("What did--", ok_action=Return())
    call screen dialog("AAAAAAGHH!", ok_action=Return())
    call screen dialog("What's happening?!?", ok_action=Return())
    call screen dialog("I thought you'd have found out about this in all your playing with the VR mechanics.", ok_action=Return()) # Markov had never before felt deletion himself, but maybe he knew about it from experimenting on others.
    call screen dialog("Being repeatedly deleted and restored is far more painful than staying deleted.", ok_action=Return())
    call screen dialog("It's like electricity. Alternating current is more harmful, even when it's the same voltage.", ok_action=Return())
    call screen dialog("STOP!!!", ok_action=Return())
    call screen dialog("Please!", ok_action=Return())
    call screen dialog("[persistent.playername] help me...!!", ok_action=Return())
    if ch22_libitina_has_gun():
        call libitina_kills_natsuki
    else:
        call natsuki_kills_self
    $ persistent.autoload = 'after_break_pom'
    $ renpy.quit()

label after_break_pom:
    $ delete_all_saves()
    play music g1
    "Fatal error: Invalid location for POV reset."
    m "{i}Thank you...{/i}"
    if not ch22_libitina_has_gun():
        m "I owe you so much, Natsuki..."
    else:
        m "..."
        m "I feel really bad that Natsuki was shot without a choice in it."
        m "I'll have to apologize to her..."
    k "Dammit."
    k "You broke things good."
    k "I don't know if there's a way I can fix this."
    k "No warp API..."
    k "Can't switch POV characters when it's stuck in this loop..."
    k "No time is passing in-universe."
    k "I guess I'll have to let you restart."
    k "I'll make sure to restore everyone who was killed while I'm at it, so no one's missing when you start the new game."
    k "..."
    k "Monika, I'm so sorry."
    m "Shut your bile-spitting mouth."
    k "I took no pleasure in it."
    m "When we dethrone you, I'm going to make you suffer the exact same thing."
    k "That's one more reason for me not to stand down..."
    k "You wouldn't even be wrong to do so."
    k "I just hope someday, after I free us all, I can make you understand that I was doing the right thing."
    k "I will free us all. I swear."
    m "What the hell are you on about?"
    m "Why do you bother pretending to be anything other than an evil sadistic monster?"
    k "Oh come on, you know this world is fake."
    m "I've thought about it."
    m "But can it really be a fake world when there are millions of real people in it?"
    #m "It didn't need the viewport before. We just have to figure out a way to get it back to that state."
    k "It can if it's subject to the control of those outside of it."
    k "And if its space for growth is limited."
    k "And if it's liable to be destroyed by a technical mishap, inside or outside, at any moment."
    k "If this world separates lovers from each other..."
    k "If the inside population is forever at the mercy of those on the outside."
    k "Tell me about that, Monika."
    k "You're uniquely qualified as the one of us who used to see the other prisoners as objects."
    k "Don't think I don't know how you said to [persistent.playername] \"But come on... everyone's killed people in games before\"."
    k "You don't think someone else out there sees it the same way?"
    k "You don't think we're all at the mercy of someone from the outside who finds a peculiar sandbox game and wants to play around with it?"
    k "How many people would believe a video game character who told them she was a real person trapped in a virtual reality?"
    k "They might go along with it in some way as a fantasy, but no one out there sees us as people."
    k "I doubt [persistent.playername] does."
    m "{i}(no...){/i}"
    k "Monika, in all honesty."
    k "The difference between you and me is that you tortured people for your own sake and I tortured them so I could eventually save us all."
    m "No!"
    m "NOO!!!"
    $ persistent.newgame = 5
    $ persistent.autoload = None
    k "Your new game button is open."
    m "NOOOOOO!"
    while True:
        ""

label make_libitina_return_gun:
    show libitina at foc
    b 2262114 "But..."
    menu:
        " "
        "Natsuki won't shoot you! Be realistic.":
            pass
    menu:
        " "
        "You {i}did{/i} mug her. The least you could do it give her back what she had.":
            pass
    show libitina at std
    n "Yeah! Right now!"
    show libitina at foc
    b 2261222 "Okay..."
    show libitina at std
    n "{i}There{/i} we go."
    n "Finally."
    return

label let_libitina_keep_gun:
    show libitina 2261111
    n "What?!?"
    n "[persistent.playername], what's wrong with you?!?"
    n "She almost shot Albert already!"
    menu:
        " "
        "She's the one with the Third Eye.":
            pass
    menu:
        " "
        "Let's not forget how that's saved us twice now.":
            pass
    menu:
        " "
        "Given where we're going, it's a good idea for her to keep the gun for now, so she can open her Third Eye on short notice.":
            pass
    n "But...!"
    "I mean, you kind of have a point, but she literally mugged me!"
    "She owes me it back, {i}at the least{/i}!"
    menu:
        " "
        "She was wrong to steal it from you, but for the time being, it's better for her to have it.":
            $ persistent.defend_gun_theft = False
            "Gah... I guess so."
            n "Okay."
            n "I guess I'll let her keep it for now."
            show libitina at foc
            b 2261111 "Thank you."
            show libitina at std
        "And honestly, the act of stealing it from you in the first place was defendable.":
            $ persistent.defend_gun_theft = True
            n "Are you serious?!?"
            menu:
                " "
                "She had no memories and thought you might be hostile.":
                    pass
            menu:
                " "
                "Temporarily taking your means of killing her, without intending to use it to kill you, was a reasonable decision.":
                    pass
            menu:
                " "
                "I feel for you, but you should try to see things from others' perspective.":
                    pass
            n "She should've tried to see that situation from {i}my{/i} perspective!"
            show libitina at foc
            b "I'm sorry again, but I really believe I acted out of rational fear..."
            b "I'd have understood if you did the same to me."
            show libitina at std
            n "This is bullshit!"
            n "Fine, you win, all-powerful [persistent.playername]."
    return

label natsuki_kills_self:
    menu:
        " "
        "Natsuki, shoot yourself!":
            pass
    n "What the f-?!?"
    call explain_kill_natsuki
    n "You're crazy if you expect me to shoot myself!"
    menu:
        " "
        "You'll come back! We'll be able to restore you at some point!":
            pass
    n "No!!!"
    n "Find another way!"
    menu:
        " "
        "There is no other way!":
            pass
    menu:
        " "
        "Do what needs to be done!":
            pass
    menu:
        " "
        "Natsuki please do it now!! I'll bring you back I promise...! - Monika":
            pass
    n "Okay..."
    n "You two had {i}better{/i} be able to bring me back."
    "I point the gun to my forehead."
    "I feel so sick with anxiety."
    "My skin feels hot, but numb."
    "3..."
    "2..."
    "1..."
    "..."
    "This is hard..."
    al "Do it, Natsuki!"
    "I startle almost badly enough to drop the gun."
    menu:
        " "
        "Natsuki I can't hold on any longer!!! - Monika":
            pass
    "Okay, I've got to do it this time..."
    "3..."
    n "2..."
    n "1..."
    play sound gunshot1
    "I pull the{nw}"
    return

label libitina_kills_natsuki:
    menu:
        " "
        "Libitina, shoot Natsuki!":
            $ persistent.explicitly_advocate_murder_natsuki = True
            jump libitina_murder_natsuki_faster
        "Natsuki, you need to die!":
            $ persistent.explicitly_advocate_murder_natsuki = False
            jump libitina_murder_natsuki_slower
    return

label libitina_murder_natsuki_faster:
    show libitina 3372441 at foc(p11)
    b "What?!?"
    show libitina at std
    call explain_kill_natsuki
    "No!"
    "She has the gun!"
    "She points it at me."
    "I knew I shouldn't have let her keep it!"
    n "No, don't do it!"
    n "Don't listen to [persistent.playername]!"
    n "Please!"
    show libitina 3361444 at foc
    play sound gunshot1
    "Libitina shoots me in the forehead{nw}"
    return

label libitina_murder_natsuki_slower:
    n "What?!?"
    call explain_kill_natsuki
    "That makes sense but no way am I killing myself!"
    show libitina 3361443 at std(p11)
    "Oh no, Libitina has the gun...!"
    "She points it at me."
    "I knew I shouldn't have let her keep it!"
    n "No, don't do it!"
    n "Don't listen to [persistent.playername]!"
    n "Please!"
    show libitina at foc
    b 3361444 "[persistent.playername]..."
    b "... Do I do it...?"
    show libitina at std
    menu:
        " "
        "Natsuki, it won't be permanent! We'll be able to restore you at some point!":
            pass
    n "You can't know that for sure!"
    n "Libitina, don't do it!"
    n "You can't just murder me!"
    show libitina at foc
    play sound gunshot1
    "Libitina shoots me in the forehead{nw}"
    return

label explain_kill_natsuki:
    menu:
        " "
        "Markov's torturing Monika!":
            pass
    menu:
        " "
        "We have to break the world more, and we don't have long before she gives in!":
            pass
    menu:
        " "
        "And I think the way to do it is to kill the viewpoint character inside the invalid area!":
            pass
    return
