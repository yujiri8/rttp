label poem1_mc_yuri_pref:
    "I give Yuri my poem."
    if persistent.player_allow_free_will_test:
        mc "Um..."
        mc "You should hold it so [persistent.playername] can see it."
        show yuri c124111 at foc
        y "Of course..."
    else:
        show yuri at foc
        y c124111 "I'll hold it so [persistent.playername] can see."
    call showpoem(poem_mc1y, img="yuri c227355", where=foci(p11))
    y c227355 "..." # Have to use the tag again because Create_Definitons.pl doesn't read the function arg, only plain script.
    show yuri at uf
    "Oh no..."
    "It's as bad as I feared, isn't it..."
    mc "... Is it terrible?"
    "I ask in a low voice."
    show yuri at foc
    y "Well..."
    y c124212 "It's not all bad."
    "I look up."
    y c125112 "The last line... has some good ideas going into it."
    show yuri at uf
    mc "You really think so?"
    show yuri at foc
    y c125112 "I think the contrast between the options is interesting."
    y "That is, it's interesting to present the past and the future beside each other like that."
    y c124142 "I think it provides an intriguing sense of... perspective."
    show yuri at uf
    mc "Well, thanks."
    "I'm not sure how sincere the complement is, but it helps nonetheless."
    show yuri at foc
    y c124113 "Um, I also wanted to mention..."
    y c125113 "Are the first and third lines supposed to rhyme?"
    show yuri at uf
    mc "Eh?"
    "I read my poem again."
    "Crap, they don't rhyme!"
    mc "Uh..."
    mc "Yeah..."
    mc "I really thought that rhymed somehow..."
    show yuri at foc
    y c124112 "That's okay..."
    y c124252 "It's not like that was the biggest problem anyway..."
    show yuri at uf
    "Ouch."
    mc "What is the biggest problem, you think?"
    show yuri at foc
    y c125111 "I would say the lack of imagery."
    y c124114 "Human feelings are most easily stimulated by perception..."
    y c125114 "And so it's easier to appreciate a poem when you have an image to envision."
    y c224111 "It's kind of like 'Show, don't tell' in storytelling."
    show yuri at uf
    mc "Ah, that makes sense."
    mc "I'll keep that in mind."
    show yuri at foc
    y c124114 "Also..."
    y c125114 "The phrase 'average Joe' gives such an informal impression that it clashes with the depth of the last line."
    show yuri at uf
    mc "Ooh..."
    mc "I didn't even think about that."
    show yuri at foc
    y c125113 "Don't be discouraged by all this."
    y c125111 "You'll get better."
    show yuri at uf
    mc "Thanks."
    mc "Can I read your poem now?"
    show yuri at foc
    y c221111 "Of course..."
    jump poem1_mc_yuri_shared

label poem1_mc_yuri_notpref:
    "I give Yuri my poem."
    call showpoem(poem_mc1n, img="yuri c227355", where=foci(p11))
    y c227355 "..."
    "Looks like Yuri doesn't think any better of it than Natsuki did..."
    y c224325 "Um..."
    y c227355 "(Where do I start...)"
    show yuri at uf
    mc "Natsuki already told me how bad the forced rhymes are..."
    show yuri at foc
    y c224253 "Uu..."
    y "I see..."
    y c225113 "Well, I'll just add that it seems lacking in depth."
    y c224114 "It's too explicit."
    show yuri at uf
    mc "Funny..."
    mc "Natsuki basically said that was the one good thing about it."
    show yuri at foc
    y c227213 "Eh... well..."
    y c224113 "Perhaps I'm biased."
    y "But I think there is value in letting the feelings of a poem be implied, and Natsuki may underappreciate that."
    y c224111 "It's kind of like 'Show, don't tell' in storytelling."
    show yuri at uf
    mc "That makes sense."
    mc "I'll keep it in mind."
    mc "Want to show me your poem now?"
    show yuri c111111
    "Yuri nods."
    jump poem1_mc_yuri_shared

label poem1_mc_yuri_shared:
    # We can't jump into the middle of this track, it sounds terrible, so handle the music here
    play music third_eye fadeout 2.0
    call showpoem(poem_y1, img="yuri c113111", music=False)
    play music t5 fadeout 2.0
    show yuri c113111 at uf
    mc "Yuri...?"
    mc "Did you figure something out about the Third Eye?"
    show yuri at foc
    y c124112 "No..."
    y c125112 "I just thought it would be fun to theorize."
    if not persistent.asked_yuri_about_cutting:
        y "I am fairly sure it has something to do with my..."
        y c124142 "My cutting..."
    show yuri at uf
    mc "Hm..."
    mc "Well, I liked the poem."
    mc "I'm not sure I understand the last line though."
    show yuri at foc
    y c125111 "I thought it would be interesting to show the subject's change in perspective as she starts to identify with the darkness and doesn't even want to be free of it anymore."
    y c125112 "It's kind of like what happened to me in Act 2..."
    y "I mean, I knew there was something wrong with me..."
    y c125131 "But it felt so good."
    y c125111 "And so I gave up on trying to fight it."
    show yuri at uf
    mc "That's..."
    mc "Really dark."
    mc "Someone should write a horror novel about that."
    show yuri at foc
    y "I think that's what Portrait of Markov is..."
    show yuri at uf
    mc "Oh right..."
    mc "Well, thanks for sharing."
    return

label poem1_mc_natsuki_pref:
    "I give Natsuki my poem."
    if persistent.player_allow_free_will_test:
        mc "You should hold it so [persistent.playername] can see it."
        show natsuki at foc
        n c123111 "I'm not a dummy, you know."
        show natsuki at uf
        mc "Sorry..."
    else:
        show natsuki at foc
        n c124111 "I'll hold it so [persistent.playername] can see."
    call showpoem(poem_mc1n, img="natsuki c113111", where=foci(p11))
    n "..."
    show natsuki at uf
    "Oh crap..."
    mc "... How bad is it?"
    show natsuki at foc
    n xc4111 "I guess I shouldn't have expected one of the good ones you showed me in Act 1..."
    n xc4131 "One of the fake ones..."
    n c114111 "Honestly, it's not the worst thing ever though."
    show natsuki at uf
    mc "Well that's good..."
    show natsuki at foc
    n "At least it has a meaningful message."
    n c113112 "But really, it doesn't count as a rhyme if you just use the same word!"
    n c115112 "Or if you add a line that does absolutely {i}nothing{/i} except complete one of those fake rhymes!"
    n c113112 "That line is pure cringe!"
    show natsuki at uf
    "Ouch..."
    mc "I'm sorry for my failures..."
    mc "I'll do better next time."
    show natsuki at foc
    n c124111 "It's okay."
    n "Mistakes are how you learn."
    n c221113 "Check out my poem."
    show natsuki at uf
    if persistent.mc_favorite == "Natsuki":
        call showpoem(poem_n1_fav)
    else:
        call showpoem(poem_n1_notfav)
    mc "This is..."
    mc "Really good..."
    mc "I'm impressed."
    show natsuki at foc
    if persistent.mc_favorite == "Natsuki":
        n c222111 "Glad to know I'm still the best!"
    else:
        n c222111 "So you're saying my poem is the best?"
    show natsuki c222146 with dissolve
    "The two of us share a laugh."
    show natsuki at uf
    mc "I really appreciate the sentiment."
    call poem1_mc_natsuki_shared
    return

label poem1_mc_natsuki_notpref:
    "I give Natsuki my poem."
    call showpoem(poem_mc1y, img="natsuki c113111")
    show natsuki c113111
    "I brace."
    "Please don't kill me..."
    show natsuki at foc
    n xc5131 "I guess I shouldn't have expected something better than the first one in Act 1..."
    n c223111 "But seriously, this is the definition of uninspired."
    n c313111 "It sounds like in the first paragraph, you just threw whatever rhymes you could think of that didn't take any imagination, because it's literally what you've already expressed..."
    n c314111 "And in the second paragraph you just tried to copy Yuri and make it sound all deep and you didn't succeed."
    n c113111 "Also, are the first and third line supposed to rhyme? Because they don't!"
    show natsuki at uf
    mc "Yeah... I realize that now..."
    show natsuki at foc
    n c223155 "Is it so hard to proofread your poem?"
    show natsuki at uf
    mc "Man, I proofread it dozens of times..."
    show natsuki at foc
    n xc4111 "Whatever. It's your first real try."
    n xc3111 "Just take this away: a poem isn't worth writing unless you have something meaningful to say."
    n "Something worth taking the time to find a really powerful way of saying."
    show natsuki at uf
    mc "Okay, thank you..."
    mc "I'll do better next time..."
    show natsuki at foc
    n c124111 "It's okay."
    n "Mistakes are how you learn."
    n c114111 "Wanna read my poem now?"
    show natsuki at uf
    mc "Yeah, I guess..."
    "Natsuki gives me her poem."
    call showpoem(poem_n1_notfav)
    mc "Ahaha..."
    mc "Fitting..."
    show natsuki at foc
    n c124112 "Well?"
    show natsuki at uf
    "I reread the poem."
    "?!?!"
    "I didn't even think about what this meant at first..."
    "I never thought I'd hear this from her."
    "I'm impressed."
    mc "It's a really good poem."
    mc "And I really appreciate the sentiment..."
    show natsuki at foc
    n xc4231 "I mean, you'd be a jerk if you didn't..."
    call poem1_mc_natsuki_shared
    n "I'm going to share with Yuri now."
    return

label poem1_mc_natsuki_shared:
    show natsuki at foc
    n c124113 "It's something I've been thinking about for a while."
    n "I guess hearing Monika and Sayori's confessions helped me overcome it."
    n c114113 "Finding out two of my friends could do such terrible things, and I'd still see them as friends..."
    n "And there was something admirable about how Monika handled her confession."
    n "If she could bring back the people she murdered, give us our memories back when she could have made an excuse not to, and just tell us everything so bravely..."
    n "... Then I shouldn't be afraid of my friends not liking my poems."
    show natsuki at uf
    mc "Ah..."
    mc "That's..."
    mc "A really good way of looking at it."
    mc "I'm proud of you, Natsuki."
    show natsuki at foc
    n c122113 "Me too, I guess~"
    n c122113 "Hehe."
    n c121113 "I'm really glad I wrote this."
    return

label poem1_natsuki_yuri:
    scene bg club_day with wipeleft_scene
    show yuri c113113 at std(p21)
    show natsuki c114111 at std(p22)
    "Yuri and Natsuki exchange poems."
    play sound page_turn
    "..."
    show natsuki at foc
    n c114114 "Yuri? Is this...?"
    show natsuki at uf
    show yuri at foc
    y c124112 "No, it's just idle theory..."
    y c225114 "And I haven't cut myself since."
    show yuri at uf
    show natsuki at foc
    n c114111 "Okay..."
    n c114131 "Well..."
    "Natsuki thinks for a moment, trying to say this without starting an argument."
    n c114111 "I still just don't really get the point of this kind of poem."
    n "There doesn't seem to be anything to learn from it."
    show natsuki at uf
    show yuri at foc
    y c124113 "It's just... a story."
    y "I don't think the point of poetry has to be to send messages."
    show yuri at uf
    show natsuki at foc
    n "Well, when you put it that way..."
    n c114113 "I guess it makes sense."
    n c114111 "It's not my thing because I don't really know anything like what this poem is describing."
    n "But I do think it's good."
    show natsuki at uf
    show yuri at foc
    y c124211 "Ah..."
    y c124111 "Thank you..."
    y "Um..."
    y c125111 "I really appreciate your poem as well."
    y "You've shown me that your style has merits."
    y c125112 "And I'm sorry that I was inconsiderate the first time."
    show yuri at uf
    show natsuki at foc
    n c121113 "No problem."
    show natsuki at uf
    show yuri c111111
    "I smile."
    "It's really nice to see them get along this well in the context of poetry."
    return
