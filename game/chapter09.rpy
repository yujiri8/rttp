label chapter9:
    scene living_room with wipeleft_scene
    play music yawa fadeout 3.0
    "..."
    show renier uf43 at foc(p31)
    r "I feel so useless."
    show renier uf11 at uf
    mc "Now you know how I felt staring at Yuri's corpse for three days."
    show natsuki xc4131 at foc(p11)
    n "And how I felt trying to stop her from dying in the first place..."
    show natsuki at uf
    "The four of us sit in silence for a moment."
    show renier at foc
    r u21131 "This sure would be a good time for a beer..."
    show renier at uf
    "..."
    show yuri c125113 at foc(p33)
    show renier u1111
    show natsuki xc4111
    y "There's something I've been thinking about..."
    y "What would have happened if Monika had never killed us?"
    y "If the festival had just gone well the first time?"
    show yuri at uf
    mc "You know..."
    mc "It's not obvious."
    mc "Knowing our world is a visual novel, what would happen to us if it ended?"
    show yuri at foc
    y c226114 "It would be worse."
    y c225114 "Wouldn't it?"
    y "There are two possibilities: either we would have all stopped existing when the game ended..."
    y "Or we'd live on, our world no longer bound to the software on [persistent.playername]'s computer, but trapped forever in a universe with only the six of us."
    y "We wouldn't even have Linda."
    y c225134 "And [persistent.playername] would never even know."
    y c225114 "It's ironic, but..."
    y c225111 "Monika's actions are the only reason any of us have any hope."
    show yuri at uf
    show natsuki xc6131 at std(p11)
    show renier uf111
    "..."
    mc "Wow. Hadn't thought of it that way."
    show yuri c114111 at foc(p33)
    y c112111 "I feel inspired to write poetry."
    y c112141 "I can't imagine what my mind will be able to come up with now..."
    show yuri at uf
    show natsuki xc1111
    mc "That sounds fun."
    if persistent.monika_questions['mc_poems']:
        mc "Maybe I can be a poet after all."
    "Yuri and Natsuki and I all get notebooks and pencils."
    if not persistent.monika_questions['mc_poems']:
        call chapter9_realize_poems
    "We sit down to write."
    play music t4 fadeout 1.0
    scene black with dissolve_scene
    "..."
    "..."
    "....."
    "......."
    "........."
    "Man. Writing is hard."
    "It's been like ten minutes and I haven't come up with anything."
    "Honestly, I'm afraid to write anything down, because I'm used to [persistent.mc_favorite] liking my poems and so I'm terrified of showing her the first one that's actually mine."
    "There's no way it's not going to be garbage..."
    "..."
    "..."
label school_warp:
    play sound glitch_basic
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.25
    scene bg club_day
    hide screen tear
    play music t3
    "..."
    show monika c117112 at leftin(p41)
    m "Yikes! Is everyone okay?"
    show monika at x(p41)
    show sayori c224132 at std(p42)
    show natsuki c113113 at std(p43)
    show yuri c227135 at std(p44)
    mc "I don't see Linda and Renier..."
    show monika at xif(p41)
    m c114111 "I guess the script got fed up with us not being in the club during club hours."
    m "Linda and Renier probably got left behind because they're not club members."
    show monika at uf
    show sayori c115111
    show natsuki c114111
    show yuri c113111
    "..."
    show natsuki at rhide
    show yuri at rhide
    hide natsuki
    hide yuri
    show renier ruf12 at std(p44)
    show linda 124111 at foc(p43)
    l "Ah... here everyone is."
    l 123111 "At least nothing broke..."
    l 124111 "We'd better stay here then."
    l "We don't want to upset the script if we don't have to."
    show monika at lhide
    show sayori at lhide
    show linda at lhide
    hide monika
    hide sayori
    hide linda
    show renier ruf11
    "The three hackers move to sit around the teacher's desk."
    show natsuki c112111 at foc(p31)
    n "Well, we kept our notebooks and pencils."
    show natsuki at uf
    "Natsuki sits down and continues writing."
    show yuri sc1121 at foc(p11)
    y "It feels out of place being at school out of uniform..."
    show yuri at uf
    show natsuki c222111 at foc
    n "No one around to see us!"
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    "Natsuki and Yuri and I go back to working on our poems."
    show renier ruf111
    "Renier is left by himself."
    #u1113 "I'm going to go for a walk."
    show renier at thide
    hide renier
    "..."
    "Eventually, I manage to get some solid ideas and come up with the beginnings of a poem."
    "I stand up to stretch my legs."
    mc "I think I need to take a break."
    mc "Writing is really tiring."
    if persistent.mc_favorite == "Sayori":
        call walk_just_mc
    elif persistent.mc_favorite == "Natsuki":
        call walk_mc_natsuki
    else:
        call walk_mc_yuri
label return_from_walk:
    scene bg corridor with wipeleft
    pause 0.25
    scene bg club_day with wipeleft
    mc "Monika and everyone!"
    mc "We need to talk to [persistent.playername]!"
    show monika c114112 at foc(p31)
    show sayori c114112 at std(p11)
    show linda 116111 at std(p33)
    m "What's up?"
    show monika at std(p41)
    show sayori at x(p42)
    show linda at x(p43)
    show renier ru2283 at foc(p44)
    r "[persistent.playername] needs to put files for the other characters!"
    show renier at uf
    show monika at foc
    m c117111 "What other characters? Back up!"
    show monika at uf
    show renier at foc
    r "Just let [persistent.playername] speak!"
    show renier at uf
    menu:
        " "
        "I'm not sure if putting those files in is a good idea.":
            show sayori at foc
            s c223112 "What files?!?"
            s c227162 "I'm out of the loop!"
            show sayori at uf
            show monika at foc
            m "Okay, you seriously have to explain what's going on now."
            show monika at uf
            show renier at foc
            show sayori c224112
            r ru2283 "The other characters mentioned in the game files!"
            r "If Linda was lurking in the aether, they might be too!"
            r "We have to try restoring them!"
            show renier at uf
            show linda at foc
            l 114113 "Oh no..."
            l 119113 "Renier's right!"
            l "[persistent.playername], give them character files!"
            show linda at uf
            menu:
                " "
                "Last time I did that, it crashed the game and it wasn't comfortable for anyone.":
                    show monika at foc
                    m c114113 "No, last time, we fixed it."
                    m c217113 "If there might be more people suffering with that, we've got to help them!"
                    show monika at uf
                    show linda at foc
                    l "Do it, [persistent.playername]!"
                    show linda at uf
                    show sayori at foc
                    s c125112 "We'll be okay if it crashes..."
                    s c123112 "Don't worry about us!"
                    show sayori at uf
                    menu:
                        " "
                        "Okay, it's done.":
                            pass
                "Okay, it's done.":
                    pass
        "Renier, I already put the files in.":
            pass
    "..."
    show monika c114222 at foc
    show sayori c115222 at foc
    show linda 114221 at foc
    'Hackers' "\"Nothing's happening...\""
    'Hackers' "\"I don't even feel anything different.\""
    show monika at uf
    show sayori at uf
    show renier ru1111
    l 124111 "I suppose they aren't here."
    l "They're probably in whatever place we were in before this game."
    show linda at uf
    mc "Where do you think that might have been?"
    show monika at foc
    m c114111 "Do you think it's possible we used to exist in [persistent.playername]'s world, and the catastrophe Renier mentioned was when someone trapped us in this game?"
    show monika at uf
    show linda at foc
    l "No..."
    l "I can't imagine how it would be possible to move a person into a piece of software."
    l "More likely we were always in a virtual world, and DDLC is another world like it..."
    l "... or a pocket dimension of that world somehow."
    show linda at uf
    show monika c114144 at foc
    "Monika sighs."
    play music t9 fadeout 3.0
    m c1141h4 "Just wishful thinking."
    m c1171h4 "I want so much to get out of this world somehow..."
    m c117114 "Even if we solve the President nightmares, it'll still be a terrible ending if we're stuck in this world forever."
    m c114144 "(Tell me that's not the life I'm doomed to live...)"
    show linda 114113
    show monika at uf
    "Monika sits down."
    "She seems to be on the verge of tears."
    mc "... Monika?"
    mc "I mean, I'm not trying to say that wouldn't be a horrible ending, but..."
    mc "Weren't you the one talking after we all got brought back about how we had to solve this so [persistent.playername] could move on?"
    show monika at foc
    m c114114 "I had accepted death when I tried to end it all in Act 4."
    m "I thought it was the only possibility to escape the horrors of Presidency."
    m "And I was still taking that for granted when you brought us all back."
    m "But all this Portrait of Markov and secret stuff is so promising..."
    m "... that I took the excuse to get my hopes up for a better ending."
    m c114114 "But it'll feel so much worse if we solve it all and are still trapped in here, our lives as meaningless as ever."
    m "I cling to this hope that the truth will set us free, even though it'll probably just hurt me more in the end."
    "Monika does break into tears."
    m c1181g4 "Dammit!"
    m c1171i4 "I don't want to live a life that means nothing!"
    m c1141g4 "And the worst part is, I know I deserve that fate..."
    m "I'm lucky to be alive at all after what I've done."
    show monika at uf
    "Sayori hugs Monika."
    show sayori at foc zorder 1
    s c213153 "No! No one deserves that fate!"
    s c213152 "No one deserves a sad ending..."
    s c115152 "I would know..."
    s c227152 "Because I'm the only one who chose to give myself a sad ending!"
    s c213151 "So even if we all end up sad, we won't deserve it."
    s "Thinking that will just make it worse."
    s c113153 "I know that from experience too..."
    show sayori at uf
    show monika c1141i1
    "..."
    m "..."
    show monika at foc
    show sayori c115111
    m "Thank you, Sayori..."
    m "That means a lot."
    "Monika wipes the tears off her face."
    m c114111 "I... I'm ready to get back to work now."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show linda at thide
    hide linda
    show renier at thide
    hide renier
    stop music fadeout 2.0
    "The hackers return to their investigation."
    "I guess it's time to finish my poem."
    play music t4
    "..."
    "...."
    "....."
    "......"
    "......."
    "........"
    "........."
    ".........."
    "..........."
    "............"
    "Okay!"
    "This is looking basically finished."
    "I just need to rewrite it on a new sheet of paper."
    "And... done."
    "I'm still really nervous about it though."
    play music t5 fadeout 3.0
    show natsuki c214111 at std(p11)
    n "My poem is ready, I guess."
    show natsuki at std(p21)
    show yuri c124113 at foc(p22)
    y "Mine too..."
    show yuri at uf
    mc "Alright, so is mine."
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        mc "Yuri, want to share first?"
        show natsuki at thide
        hide natsuki
        show yuri at foc(p11)
        y c121111 "Gladly."
        show yuri at xis(p11)
        "I think about asking her to show me hers first this time, given how anxious I am about this, but I decide it's better to get it over with and end on the good note."
        call poem1_mc_yuri_pref
        scene bg club_day with wipeleft_scene
        show natsuki c214111 at foc(p11)
        n "Ready to share?"
        show natsuki at uf
        mc "Yeah..."
        call poem1_mc_natsuki_notpref
    else:
        mc "Natsuki, want to share first?"
        show yuri at thide
        hide yuri
        show natsuki at foc(p11)
        n c222111 "Sure!"
        show natsuki at xis(p11)
        "I think about asking her to show me hers first this time, given how nervous I am about this, but I decide it's better to get it over with and end on the good note."
        call poem1_mc_natsuki_pref
        scene bg club_day with wipeleft_scene
        if persistent.least_favorite == "Yuri":
            show yuri c223113 at std(p11)
            mc "Yuri, ready to share?"
            show yuri at foc
            y c224113 "Yes..."
        else:
            show yuri c223111 at std(p11)
            mc "Yuri, ready to share?"
            show yuri at foc
            y c224111 "Yes..."
            show yuri at uf
            "Yuri doesn't seem very enthusiastic, after how she stopped sharing with me in Act 1 because she was convinced I didn't like her writing..."
            "Hopefully it'll go better this time."
        call poem1_mc_yuri_notpref
    call poem1_natsuki_yuri
    mc "Hey, you two should show your poems to everyone else."
    mc "I'm sure Monika and Sayori would love to see them."
    show yuri at foc
    y c112111 "I'd like to as well..."
    y c114111 "But..."
    y c114142 "If they're too busy working on the code, I don't want to interrupt them..."
    show yuri at uf
    show natsuki c114111
    mc "Ah..."
    if not persistent.player_allow_free_will_test:
        "[persistent.playername], you'd better not disallow this too."
    mc "Well, it's not urgent."
    mc "And I'm sure they'd appreciate a short break."
    show natsuki c111111
    show yuri at foc
    y c115111 "Well, alright."
    y c125111 "Let's show them."
    show yuri at uf
    show natsuki at foc
    n c113111 "Hey!"
    n c122131 "I mean..."
    n c222155 "Okay, everyone!"
    n c222111 "We wrote some poems for you!"
    show natsuki at uf
    show yuri c112161
    "Yuri and I giggle at the use of Monika's catchphrase."
    show natsuki at rhide
    show yuri at rhide
    hide natsuki
    hide yuri
    show sayori c114131 at leftin(p11) zorder 2
    s "Poems?!?"
    s c22x111 "That sounds really fun!"
    show sayori at x(p44)
    show monika c111111 at leftin(p43) zorder 1
    show linda 116111 at leftin(p42) zorder 0
    show renier uf12 at leftin(p41) zorder 1
    "Natsuki and Yuri lay their poems on a desk."
    "I hold mine back."
    "I don't really want to share it..."
    show sayori at xif(p44)
    s c21x111 "[mc_name], did you write a poem too?"
    show sayori at uf
    mc "Um..."
    mc "Not re-{nw}"
    show renier at x(p51)
    show linda at x(p52)
    show monika at x(p11)
    show sayori at std(p54)
    show natsuki c222111 at rightin(p55) zorder 3
    n "Yeah, he did!"
    show natsuki at xif(p55)
    n c222155 "But it was really bad!"
    show natsuki at uf
    mc "Natsuki!"
    show natsuki at rhide
    hide natsuki
    show renier at x(p41)
    show linda at x(p42)
    show monika at x(p43)
    show sayori at x(p44)
    mc "I don't really want to show it..."
    show renier at xif(p41)
    r u1223 "You don't learn by not being criticized, [mc_name]."
    show renier at uf
    "Impulsively, I raise my voice."
    show sayori c114112
    mc "I already got criticism, okay?"
    mc "I {i}know{/i} it's bad."
    #show monika c114111
    show sayori at xif(p44)
    s c113112 "It's okay, [mc_name]."
    s c111112 "You don't have to show your poem."
    show sayori c111111 at uf
    show renier uf11
    "The four of them read over Natsuki and Yuri's poems."
    show sayori at foc
    s c21x111 "These are really good, both of you!"
    show sayori at uf
    show linda at foc zorder 1
    l 113111 "Ehehe..."
    l "The mistakes one is cute..."
    show renier at x(p51)
    show linda at std(p52)
    show monika at x(p11)
    show sayori at std(p54)
    show natsuki xc3111 at rightin(p55) zorder 3
    n "You {i}can't{/i} be serious."
    show linda at xif(p52)
    l 114111 "Eh?"
    l "I don't understand..."
    show linda at uf
    show natsuki at xif(p55)
    n xc3131 "I can see that..."
    show natsuki at uf
    show linda zorder 0
    show renier at xif(p51)
    r u1223 "What is your problem, Natsuki?"
    r "It was a compliment."
    show renier at uf
    show sayori c114112
    show monika c114111
    show natsuki at xif(p55)
    n c113112 "My problem is that every time I write about something serious people just tell me it's cute!"
    show natsuki c115112 at uf
    "Her sudden spike in volume surprises even me."
    show monika at xif(p11)
    m c117112 "Everyone, cool it!"
    m c114112 "No one meant any insult."
    m c214112 "Natsuki is just used to being dismissed for being cute."
    show monika at uf
    show renier at foc
    r "And how was Linda supposed to know that?"
    show renier at uf
    show monika at foc
    m c117111 "She wasn't!"
    m c114111 "I'm just saying we should try to understand where each other are coming from."
    show monika at uf
    show natsuki xc6111
    show renier u1111
    show linda at foc
    l "I didn't mean to offend..."
    l "For the record, I think it's a good poem."
    show linda at uf
    show monika c111111
    show sayori c111111
    show natsuki at thide
    hide natsuki
    show yuri c113111 at std(p55) zorder 3
    "Renier picks up Yuri's poem."
    show renier at foc
    r u1113 "The Third Eye..."
    stop music fadeout 4.0
    "He whispers to himself."
    show yuri c113113
    r u11131 "The Third Eye, the Third Eye, the Third Eye..."
    "He whispers it to himself faster and faster."
    show yuri c114213
    show sayori c114111
    show monika c114111
    r u1283 "I know it's in there!"
    show renier at uf
    show yuri at foc
    y c125233 "In where?"
    show yuri at uf
    show renier at foc
    r "In me!"
    r u1183 "I have to try something."
    show sayori c117131
    show monika c117111
    show linda 119441
    r "Yuri, give me a knife."
    show renier at uf
    show yuri at hop
    y c228125 "--!!!"
    show yuri at foc
    y "What are you thinking?!?"
    show yuri at uf
    show renier at foc
    r "I have to cut myself."
    r "I have to see if anything happens."
    show renier at uf
    show yuri at foc
    y "Ah--!"
    y "That's a terrible idea!"
    show yuri at uf
    show renier at foc
    r u1213 "Any information we gain about the Third Eye might help us."
    r "We have to do this."
    show yuri c227125
    show renier at uf
    show linda at foc zorder 2
    l "Renier, wait!"
    l "Remember that secret poem you said you might have written?"
    l "Where you were possessed by the Third Eye and killed someone?"
    l "We aren't going to risk that!"
    show linda at uf zorder 0
    show renier at foc
    r "There's no risk."
    r "None of us can die."
    r "Besides, we can just have [persistent.playername] make a save first and then go back to it, right?"
    show renier at uf
    show linda at foc zorder 2
    l 114221 "Well... I suppose so..."
    l 114111 "But what's the benefit?"
    l "We need to disable the script one way or another to get out of this, and once we do that, we'll be able to read Portrait of Markov and have my memories."
    l "You don't need to do this!"
    show linda at uf zorder 0
    show renier at foc
    r "It might reveal something that could help you."
    r "The Third Eye might be related to Presidency."
    r "Monika cut herself too at one point, remember?"
    r "Special poem number 4."
    r "She even wrote that it was 'exhilarating'."
    show renier at uf
    show monika at foc
    m c114221 "I do remember that..."
    show monika at uf
    show renier at foc
    r "One way or another, I'm going to try it."
    show renier u1113 at uf
    show yuri at foc
    y c225174 "Well..."
    y c225114 "Alright."
    y "I might as well cooperate."
    show yuri at uf
    "Yuri hands Renier a knife."
    show renier u1111
    show linda 334111 at foc
    if persistent.experiment_over: # Put it in both places just incase
        jump save_scum_experiment
    menu:
        l "[persistent.playername], you should make a save now. Make sure it's at this exact moment, otherwise something might go wrong."
        "I've made a save.":
            pass
    if persistent.experiment_over:
        jump save_scum_experiment
    l "Due to the way dialog choices work, you'll probably have to say it again when you load the save."
    l "Also, don't load the save before we're ready."
    l "Alright..."
    l "Renier, the save is ready."
    show linda at uf
    show renier u1211 at foc
    "Renier puts the knife to his wrist, and gives himself a cut."
    stop music
    show renier u1383
    show yuri c224138
    show monika c114111
    "We all watch his face."
    r "..."
    "He doesn't say anything."
    show renier at uf
    show linda at foc zorder 2
    l 114443 "Renier?!?"
    l "It did something didn't it?"
    l "Please say something!"
    show linda at uf zorder 0
    show renier at foc
    r u2383 "Holy fuck..."
    r "Yuri's poem was exactly right."
    r "It feels good..."
    r "Way too good."
    show renier at uf
    show sayori c114112
    show linda at foc zorder 2
    l 114113 "It didn't do anything, though?"
    l "It's not messing you up?"
    show linda at uf zorder 0
    show renier at foc
    r u1313 "No..."
    r u1113 "Come to think of it..."
    r "Yuri, you experienced it this way too, didn't you?"
    r "Cutting yourself suppressed the Third Eye rather than activating it?"
    show renier at uf
    show yuri at foc
    y c124141 "Yes..."
    show yuri at uf
    show renier at foc
    r "I wonder if it's like an addictive drug."
    r "Cutting relieves the symptoms in the moment, but makes the problem worse."
    r "..."
    show renier at uf
    show renier at foc
    r u2113 "We need to find out who all has this."
    r "We should all try it."
    show renier at uf
    show monika c117111
    show yuri c228125
    show linda 339443
    show sayori at foc zorder 4
    s c227131 "Aah?!?"
    s c227162 "No!"
    s c123112 "Let's not all cut ourselves!"
    s c223114 "Duh!"
    show sayori at uf
    show renier at foc
    r "We need to figure out what the pattern is."
    r "It's obvious from the Subject Libitina report that the Third Eye has some kind of power."
    r "It's a longshot, but maybe if we could harness that power and figure out how to control it it could help us get out of here."
    r "If the four of us non-hackers can't do anything else to help, we've got to do this."
    show renier at uf
    "His eyes land on me and Natsuki."
    show sayori at thide
    hide sayori
    show natsuki c117121 at foc(p54) zorder 3
    show monika c117111
    show natsuki at foc
    n c117122 "Fuck no!"
    n "You're not doing that to me!"
    show natsuki at uf
    mc "Me neither!"
    mc "This is stupid!"
    show natsuki at foc
    n c117121 "[persistent.playername], tell him he's way out of control!"
    show natsuki at uf
    $ questioned_specifics = False
label player_judge_experiment:
    menu:
        " "
        "Renier, what's your logic behind choosing [mc_name] and Natsuki?" if not questioned_specifics:
            menu:
                " "
                "Everyone who has any signs of the Third Eye right now is either Club President or has some preexisting connection.":
                    pass
            menu:
                " "
                "You have the secret poem you apparently wrote, and Yuri read Portrait of Markov a bunch, which might have fostered it in her.":
                    pass
            menu:
                " "
                "So it seems by far the most likely that [mc_name] and Natsuki don't have it.":
                    pass
            show renier at foc
            #r "[mc_name] also read Portrait of Markov at least once."
            r "I would suggest doing it on one of the people with code powers, but that sounds dangerous."
            r "Natsuki and [mc_name] are the only two who don't have code powers and haven't already done it."
            r "And remember we don't know anything about any of the club members' real pasts."
            r "And given how we're all in here together, it's not unlikely they were at the facility too at some point."
            #r "Maybe they were test subjects."
            show renier at uf
            $ questioned_specifics = True
            jump player_judge_experiment
        "Renier, you sound exactly like the cultists in Portrait of Markov right now!":
            $ persistent.player_support_renier_experiment = 0
            menu:
                " "
                "Don't you think this is what they told themselves to justify their actions?":
                    pass
            jump no_experiment_emotional
        "Renier, your experiment costs more than it gives.":
            $ persistent.player_supported_renier_experiment = 0
            menu:
                " "
                "{i}Maybe{/i} we learn something that {i}might{/i} help us, but it's such a stretch that the amount of the hackers' time this has costed already outweighs the expected gain.":
                    pass
            jump no_experiment_logical
        "Renier has a point. You should do it.":
            $ persistent.player_support_renier_experiment = 1
            show natsuki at foc
            n c117122 "...!!"
            show natsuki at uf
            show yuri at thide
            hide yuri
            show sayori c223113 at foc(p55) zorder 3
            s "Hold on!"
            s "Natsuki and [mc_name] don't have to do this!"
            show sayori at uf zorder 0
            menu:
                " "
                "They should.":
                    menu:
                        " "
                        "The cultists from Portrait of Markov might still be out there and still be experimenting.":
                            pass
                    menu:
                        " "
                        "If we can do something that might get us to taking them down and saving their victims sooner, even if it's a slim chance, we should do it.":
                            pass
                    menu:
                        " "
                        "I'm not forcing them, but they should.":
                            pass
                    show natsuki c114112
                    mc "Thanks, I'm not."
                    "Natsuki's expression gets a lot less defensive."
                    "To my surprise, she seems to be considering it now."
                    mc "Natsuki...?"
                    mc "Are you...?"
                    show natsuki at foc
                    n c114111 "You know what, yeah."
                    n c114112 "I'll do it."
                    show natsuki at uf
                    show renier u1111
                    show sayori c115112
                    show monika c114111
                    jump natsuki_cut
                "They have to.":
                    $ persistent.player_support_renier_experiment = 2
                    menu:
                        " "
                        "Look, the cultists from Portrait of Markov might still be out there and still be experimenting.":
                            pass
                    menu:
                        " "
                        "If we can do something that might get us to taking them down and saving their victims sooner, even if it's a slim chance, we have to do it.":
                            pass
                    show natsuki c115122 at foc
                    n "..."
                    show natsuki at uf
                    if not persistent.player_allow_free_will_test and persistent.player_insult_mc_for_questioning_base64:
                        mc "[persistent.playername], we don't care what you think!"
                        mc "You can't force us!"
                    else:
                        mc "But [persistent.playername]!"
                    show natsuki at foc
                    n c113112 "You know what?"
                    n c115112 "I'll do it."
                    show natsuki at uf
                    show renier u1111
                    show sayori c115112
                    show monika c114111
                    jump natsuki_cut


label walk_just_mc:
    scene bg corridor with wipeleft
    "I step outside."
    "I realize I don't think I've ever been in any part of this school other than the clubroom, the one other classroom, and this hallway."
    "I want to explore the world I'm trapped in."
    scene courtyard with wipeleft
    "..."
    "The world looks so real."
    "So convincing."
    "Though I guess I shouldn't be surprised by that, given that it's specifically designed to convince me."
    "You don't notice how beautiful your world is until you find out it's fake."
    "How does your world look to you, [persistent.playername]?"
    "Would it change your perspective if you found out it was a simulation?"
    "Just a weird thought I had, I dunno."
    "I wonder how far this world extends for."
    "What would happen if I left the school grounds?"
    "I'd imagine that if the game is designed as a dating game, it wouldn't be prepared to render an infinite range of environments."
    "Probably just the backgrounds it needed for the school and my house and stuff."
    "But I guess I shouldn't try it, since that might crash it."
    show renier u1111 at std(p11)
    "I notice Renier is out here."
    mc "Oh, hi."
    jump walk_renier

label walk_mc_natsuki:
    show natsuki c114113 at foc(p11)
    n "I'll come too."
    show natsuki at uf
    scene bg corridor
    show natsuki c221113 at std(p11)
    with wipeleft
    play music beautiful_interior fadeout 2.0
    scene courtyard
    show natsuki c221113 at std(p11)
    with wipeleft
    "We step outside."
    show natsuki c222113 at std(p11)
    "Natsuki exhales with satisfaction, enjoying the fresh air."
    show natsuki c112113 at foc
    n "You know, I've never felt this free before."
    n c114113 "Able to explore the world without worrying about school or my dad being mad at me for getting home late."
    n c114113 "In a way, I have to say I'm pretty happy about how things have changed since I met you."
    n c222113 "If things stay this good, it was worth dying for."
    show natsuki at uf
    mc "That's pretty extreme..."
    show natsuki at foc
    n c124113 "Well, it was only a few days of hell."
    n c122133 "And it's not like I miss any of the NPCs..."
    n c124113 "So it's really a strict improvement in the long-term."
    n c121113 "And I even got to be better friends with Yuri!"
    show natsuki at uf
    mc "Well, I guess you're right."
    mc "It was worth it for me too, having gotten to meet you."
    show natsuki at foc
    n c122146 "Ehehe."
    show natsuki c114134
    "Natsuki's expression darkens."
    n c114111 "It's not going to stay this good though, is it?"
    n "As soon as Monika and Sayori and Linda crack the code or whatever, things are gonna change."
    n "I don't know how..."
    n "But I doubt it's gonna be all leisure and time with friends for much longer."
    show natsuki at uf
    mc "Would you rather they didn't crack the code?"
    show natsuki at foc
    n "No, obviously."
    n "I mean, in the long term staying in this game with just the seven of us would be worse than anything."
    n c111111 "But it's been enjoyable so far."
    n "And no matter what happens, it'll be better for having met you."
    show natsuki at uf
    "It's time."
    "I'm going to formally tell her I love her."
    "I'm just deciding between 'I love you' and 'I love you too'."
    "What she just said was pretty close to saying it..."
    "But it wasn't quite, so I'm worried that it's presumptuous if I say the latter."
    show natsuki at foc
    n c124111 "Are you just gonna stand there with that dumb look on your face?"
    show natsuki at uf
    "Okay, I'll go with the safer option that might make me look dense."
    mc "I love you, Natsuki."
    show natsuki at foc
    n c114213 "--!!"
    show natsuki at uf
    mc "Come on, don't act surprised!"
    show natsuki at foc
    n c112246 "Ahaha!"
    n c111211 "I love you too, [mc_name]."
    show natsuki c114213 at face with dissolve
    "Natsuki steps closer to me."
    "I guess we're going to complete the kiss that got interrupted last time."
    "But just as we're about to do it, I catch sight of Renier out of the corner of my eye."
    show natsuki c115224 at unface
    "I pull back immediately."
    "Thankfully, Renier doesn't seem to have seen us."
    "He does now."
    show natsuki xc5132 at std(p22)
    show renier u1113 at foc(p21)
    r "Hi..."
    play music t3 fadeout 4.0
    jump walk_renier

label walk_mc_yuri:
    show yuri sc3111 at foc(p11)
    y "I'd like to go with you, if you don't mind."
    show yuri at uf
    mc "Mind?!? Yuri, of course not!"
    show yuri sc3211
    mc "Come on."
    scene bg corridor
    show yuri c111111 at std(p11)
    with wipeleft
    play music serenity fadeout 2.0
    scene courtyard
    show yuri c111111 at std(p11)
    with wipeleft
    "We step outside."
    show yuri c112111 at foc(p11)
    y "The open air is wonderful."
    y c112141 "The open virtual air."
    show yuri at uf
    mc "Maybe you should write a poem about it."
    mc "I'm sure it would be great."
    show yuri at foc
    y c112111 "Huhu."
    y c114111 "[mc_name]..."
    y c125112 "What do you think we are?"
    show yuri at uf
    mc "Eh?"
    mc "What do you mean?"
    show yuri at foc
    y "We think ourselves people, but we exist inside of a piece of software."
    y "What are we then, metaphysically?"
    y c125132 "Monika said we aren't just code, but how can we be anything else?"
    y "What can we be such that our actions and experiences are confined to a program, if we're not just pieces of the code?"
    show yuri at uf
    mc "I..."
    mc "I don't know."
    show yuri at foc
    y c125112 "Are we disembodied souls who have control over some region of the computer's memory?"
    show yuri at uf
    mc "Hm..."
    mc "Well, one thing's for certain."
    show yuri c123112
    mc "We're not pieces of code."
    mc "Whatever happens, I will believe that."
    mc "Because I won't believe that every word you and I have ever said to each other and everything we've done are just products of an algorithm."
    mc "Believing that would take away the value in it."
    show yuri at foc
    y "..."
    y c225111 "You're right..."
    y c221111 "You always know how to put my thoughts in perspective."
    show yuri at uf
    "I smile back."
    show yuri at foc
    y c224213 "[mc_name]... I..."
    y c225214 "I want to say this officially."
    y c225233 "I love you."
    show yuri at uf
    "I respond without hesitation."
    "I've been longing for this moment."
    mc "I love you too."
    show yuri c221111
    "As I say it, I'm reminded of the kiss we never had."
    mc "Hey..."
    mc "Want to kiss?"
    show yuri c224211
    "Yuri immediately blushes."
    show yuri c221211
    "But then, she smiles."
    show yuri at foc
    y c224111 "Yes..."
    y "Now is as good a time as any."
    show yuri at face(y=600) with dissolve
    "But just as we're about to do it, I catch sight of Renier out of the corner of my eye."
    show yuri c227335 at unface
    "I pull back immediately."
    "Thankfully, Renier doesn't seem to have seen us."
    "He does now."
    show yuri at std(p22)
    show renier u1113 at foc(p21)
    r "Hi..."
    show yuri c227253
    play music t3 fadeout 4.0
    jump walk_renier

label walk_renier:
    show renier at foc
    r u1113 "I've been scouting the school grounds."
    r "There's definitely no one else here."
    if persistent.mc_favorite == "Natsuki":
        show renier at uf
        show natsuki xc4112 at foc
        n "We already knew there were no NPCs, Renier."
        show natsuki at uf
        show renier at foc
        r u1113 "I know..."
    elif persistent.mc_favorite == "Yuri":
        show renier at uf
        mc "Monika already told us that..."
        show renier at foc
        r u1113 "I know..."
    else:
        r u11131 "I know Monika already said there wasn't..."
    r u1111 "But I felt the need to confirm it."
    if persistent.mc_favorite == "Yuri":
        show yuri c223113
    # If MC's with his girl, he doesn't want to stay with Renier, so Renier will get the lines.
    if persistent.mc_favorite != "Sayori":
        r u21131 "Also..."
        r u2113 "It doesn't really make sense."
        r "Me and Linda are here, even though we're not part of the intended story."
        show renier at uf
        mc "Well, you two said you came to this world with a mission of some sort, right?"
    else:
        show renier at uf
        mc "But you and Linda are here."
        mc "Even though you aren't part of the intended story."
        "Renier shrugs."
        mc "You two said you came to this world with a mission of some sort, right?"
    mc "Did you mean all of us?"
    mc "Or just you two?"
    show renier at foc
    r u2113 "I have no idea, and it's probably useless to speculate."
    show renier at uf
    mc "I was just thinking, if there are at least two people here that aren't part of the dating game..."
    if persistent.mc_favorite == "Natsuki":
        show natsuki xc4111
    mc "I wonder about the others mentioned in the secrets."
    mc "Libitina, Elyssa, and Markov, at least."
    mc "Are they in here somewhere?"
    mc "Maybe somewhere else in the game world?"
    show renier at foc
    r u11111 "..."
    r u1113 "You know..."
    r "I'm not entirely without a place in the dating game."
    r "I was related to Natsuki."
    r "Maybe the script would have used me on her route if Monika hadn't cut it short."
    r u2113 "But Linda's the only one who doesn't belong at all..."
    r "And we had to do special stuff to get her in."
    r u1113 "So if the others are around somewhere, they're probably like Linda was."
    show renier at uf
    if persistent.mc_favorite == "Sayori": # It's just MC and Renier
        "I slowly realize the implication."
        mc "So that means..."
    elif persistent.mc_favorite == "Natsuki":
        "Natsuki and I slowly realize the implication."
        show natsuki at foc
        n xc4134 "So that means..."
        show natsuki xc4114 at uf
    else:
        "Yuri and I slowly realize the implication."
        show yuri at foc
        y c225118 "So that means..."
        show yuri c225138 at uf
    show renier at foc
    r u1233 "What if they're suffering right now as she was?"
    r u1283 "[persistent.playername]! Add character files for them!"
    show renier at uf
    "..."
    if persistent.monika_questions['choices']:
        mc "[persistent.playername] can't speak to us without a hacker to give [persistent.player_obj_pronoun] a dialog choice."
    else:
        mc "I don't think [persistent.playername] can talk to us."
        mc "We have to have a meta-aware character with us."
    show renier at foc
    r u2283 "Let's go back!"
    return

label chapter9_realize_poems:
    mc "..."
    mc "I just realized something."
    show natsuki xc4111
    show yuri c113111
    mc "I can't remember any of my poems."
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        show yuri at foc
        y c114111 "Um..."
        y c115111 "Now that you mention it..."
        y c113141 "I can't remember them either."
        show yuri at uf
    else:
        show natsuki at foc
        n c114111 "Now that you mention it..."
        n "Neither can I."
        n "Any of yours, I mean."
        show natsuki at uf
    mc "I can remember yours..."
    "What did I write?"
    if persistent.mc_favorite == "Yuri":
        "The first poem I wrote, and I was so proud to see Yuri like it..."
    elif persistent.mc_favorite == "Natsuki":
        "The first poem I wrote, and Natsuki was so cute trying to pretend she didn't like it..."
    else:
        "The first poem I wrote, and Sayori was the only one who liked it..."
    "How can I not remember?"
    "Not a single line of it?"
    show renier at foc
    r u1213 "It's probably because you never wrote any."
    show renier at uf
    mc "Eh?"
    show renier at foc
    r uf13 "You're the player character, remember?"
    r "And this is a dating game..."
    r "So maybe you didn't actually write your poems."
    r uf11 "Maybe [persistent.playername] was just picking who to write for from a menu, or playing a minigame or something."
    show renier at uf
    mc "I..."
    # Reverse this time, give the less-liked girl some lines.
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        show natsuki at foc
        n c114111 "The game probably just gave us nondescript memories when we read your poems, like it did you and Yuri with Portrait of Markov."
        show natsuki at uf
    else:
        show yuri at foc
        y c125112 "The script may have just given us nondescript memories when we read your poems, like it did with Portrait of Markov."
        show yuri at uf
    mc "It makes sense..."
    "I look down and sigh."
    mc "So it was all a lie."
    mc "I thought I was getting better at poetry..."
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        show yuri at foc
        y c124118 "[mc_name]..."
        y c125112 "It's okay."
        y "You don't have to be a great poet."
        y c125213 "You're a good enough friend without that."
        show yuri at uf
        mc "Ah..."
        mc "Thanks..."
    else:
        show natsuki at foc
        n c114114 "Well..."
        n "You don't have to be a writer, you know."
        n c222156 "I mean, I wouldn't mind having that advantage over you for the rest of our lives."
        show natsuki at uf
        mc "But you already have the advantage of being an impeccable baker..."
    return

label no_experiment_emotional:
    show renier at foc
    r u2323 "Do you really not see the difference between volunteering for these experiments and imprisoning people to force it on them?"
    r u2326 "That's like not seeing the difference between charity and stealing!"
    show renier at uf
    show natsuki at foc
    n c117112 "I don't consent!"
    n "And neither does [mc_name]!"
    show natsuki at uf
    show renier at foc
    r u2323 "I'm not even doing anything!"
    r u1323 "I'm just pointing out that if you really want to have the best chance of getting us all out of here, you'll volunteer."
    r u2326 "And somehow someone is comparing me to murderous cultists?"
    show renier at uf
    show linda at foc zorder 2
    l "Renier...!"
    l "This probably won't help!"
    l "At best we gain a piece of data that {i}might{/i} help us, but it's a totally unreasonable stretch!"
    show linda at uf zorder 0
    show renier at foc
    r u1326 "..."
    r u1143 "Okay."
    show yuri c223113
    show monika c114111
    show linda 334113
    r u2123 "Fine. You don't have to do the right thing."
    r "I can't blame you for being selfish."
    show renier uf21 at uf
    show natsuki at foc
    n xc5112 "'Selfish'..."
    n xc3112 "Sure, cause it's {i}selfish{/i} to not want to cut myself as an experiment."
    show natsuki at uf
    show linda at foc zorder 2
    l 119114 "Natsuki!"
    l 114114 "Renier made a personal sacrifice in the interests of solving our problem!"
    l "You have no right to be acting so hostile when he's done nothing wrong!"
    show linda at uf zorder 0
    show monika at foc
    m c114112 "Um..."
    $ persistent.experiment_over = True
    m c214112 "Before this gets more heated, maybe we should just load the save."
    while True:
        ""

label no_experiment_logical:
    show linda 334443
    show natsuki c113111
    show yuri c227125
    show renier at foc
    r u21131 "..."
    show renier at uf
    show linda at foc zorder 2
    l 119113 "... Yes, that's right!"
    l "We'll solve this faster anyway if we don't argue about this!"
    show linda at uf zorder 0
    show renier at foc
    r u2326 "But that's just because you've all been arguing!"
    r u2323 "It'll still be best if you just work with me!"
    show renier at uf
    show monika at foc
    m c217113 "Hold on, that shouldn't affect {i}your{/i} decision!"
    m "If we're not going to cooperate, then the optimal decision for you is to not argue!"
    m "And it's clear that convincing us to cooperate will take more time than it's worth!"
    show monika at uf
    show renier at foc
    r u23261 "Grrh..."
    r u11231 "Fine."
    r u2123 "If no one else is willing, I'll let it go."
    show renier at uf
    $ persistent.experiment_over = True
    show linda at foc zorder 2
    l 334111 "[persistent.playername], we're ready for you to load the save now."
    while True:
        ""

label natsuki_explain_cut:
    show natsuki at foc
    n c113112 "I'm not an asshole like [persistent.playername] and Renier."
    n "I'll do the selfless thing."
    show natsuki at uf
    return

label natsuki_cut:
    show linda 334113
    if persistent.mc_favorite == "Natsuki":
        mc "Ah--!"
        if persistent.player_support_renier_experiment == 2:
            call natsuki_explain_cut
        jump mc_cut
    "I open my mouth in shock."
    if persistent.player_support_renier_experiment == 2:
        call natsuki_explain_cut
    show natsuki c116134 at foc
    "Natsuki puts the knife to her wrist."
    "She sighs uncomfortably."
    "Then, she makes a cut."
    show natsuki c113113 at hopfoc
    n "Aagh!"
    n c115134 "Grr..."
    show natsuki c115155
    "Natsuki inhales deeply."
    n c117112 "Okay, there, I did your stupid test!"
    n "It doesn't feel good!"
    show natsuki at uf
    show renier at foc
    r uf13 "I guess Natsuki doesn't have a Third Eye."
    r "It's me, Yuri, and Monika, but not all of us."
    r uf131 "What could the pattern be?"
    show renier at uf
    show natsuki at foc
    n c113112 "Are you not even going to thank me for my bravery?"
    show natsuki at uf
    show renier at foc
    r u1323 "I don't hear anyone thanking me for doing it to myself when I had to convince others that I should even be allowed to instead of having to be pressured into doing it."
    show renier at uf
    show natsuki c115112 at foc
    "Natsuki clenches her fists."
    show natsuki at uf
    show monika at foc
    m c114112 "Um...!"
    $ persistent.experiment_over = True
    m c214112 "Before this gets more heated, maybe we should just load the save."
    while True:
        ""

label mc_cut:
    "I'm shocked."
    "On the bright side, she's taking the pressure off me."
    "But on the other hand, I feel bad not being as brave as her."
    "Is it really right for me to let Natsuki get hurt, after how I neglected her in Act 2?"
    "As Natsuki takes the knife from Renier, I decide the answer is no."
    "I'm going to protect my girlfriend."
    mc "Wait!"
    mc "I'll do it!"
    show natsuki c114213 at foc
    "Natsuki's face is conflicted."
    "On one hand, she's glad to not have to do this, but on the other hand, she probably doesn't want to have me take the hit for her in front of everyone else."
    show natsuki at uf
    "I make up a justification for her so silly that I almost laugh at myself."
    mc "I'm bigger than you, so I have more blood, so losing the same amount will hurt me less."
    show natsuki at foc
    n "Okay..."
    n "Thanks."
    show natsuki at uf
    "Natsuki hands me the knife, embarrassed but grateful."
    "Crap..."
    "Now I have to cut myself."
    "I don't feel nearly as good about the decision now that I'm holding the knife."
    "I sigh uncomfortably."
    show sayori at thide
    hide sayori
    show yuri c224138 at std(p55)
    "I look at Yuri for encouragement."
    "{i}'How much does it hurt?'{/i} I want to ask her."
    "Well, here goes..."
    "I'll just make a small cut."
    "..."
    show natsuki c114214
    mc "Aagh!"
    "It hurts!"
    "But at the same time, somehow, it's really satisfying."
    "Wait..."
    "Oh no..."
    "Does this mean I have a Third Eye?"
    "I shiver."
    "I start to hyperventilate and sweat."
    mc "Oh no..."
    show linda 334443
    "This can't be real..."
    show natsuki at foc
    n "[mc_name]...?"
    show natsuki at uf
    mc "{i}(No...){/i}"
    scene black with close_eyes
    "I close my eyes."
    r "Looks like he has it..."
    "I feel so suddenly powerless."
    "Like there's this dark psychic force in me now that I'm at the mercy of."
    scene bg club_day
    show natsuki c113114 at foc(p11)
    with open_eyes
    n "Calm down, [mc_name]!"
    n "I'm not gonna let you go off the deep end!"
    show natsuki at uf
    mc "..."
    show yuri c125118 at foc(p33)
    y "Take a deep breath, [mc_name]."
    y "You're going to be fine."
    $ persistent.experiment_over = True
    y c125113 "We can just load the save now, right?"
    show yuri at uf
    show linda 334111 at foc(p31)
    l "Yes... [persistent.playername], we're ready for you to load the save."
    show linda at uf
    while True:
        ""
