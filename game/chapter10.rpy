label chapter10:
    # This comes in from loading the save to get out of chapter 9.
    $ save_is_before_experiment = False
    # Restore poses
    show renier u1111 at std(p51)
    show linda 334111 at std(p52)
    show monika c114221 at std(p11)
    show sayori c117131 at std(p54)
    show yuri c225114 at std(p55)
    "..."
    show monika c114111
    show sayori c115111
    show linda at foc zorder 2
    l "That was it."
    show linda at std
    show yuri c223113
    show renier at foc
    r u2113 "Wait, we did the experiment?"
    show renier at std
    show linda at foc
    l "I'll restore everyone's memories..."
    call updateconsole("for char in (renier, "+mc_name.lower()+", natsuki, yuri):\n  char.old_memories.unlock()", "Renier's memories unlocked\n"+mc_name+"'s memories unlocked\nNatsuki's memories unlocked\nYuri's memories unlocked")
    call hideconsole
    $ consolehistory = []
    show linda at std
    if persistent.player_support_renier_experiment and persistent.mc_favorite == "Natsuki":
        mc "Ugh..."
        mc "I kind of don't want to remember that..."
        show monika at thide
        hide monika
        show natsuki at foc(p11) zorder 3
        n c214114 "[mc_name], you're gonna be fine."
        n "We loaded the save, remember?"
        n "So it's like it never happened."
        show natsuki at std
        mc "I mean, I know, but..."
        mc "It's still a scary thought that I have a Third Eye in the first place."
        show renier u2113 at foc(p51)
        r "What I don't get was why cutting seemed to make him all hyper."
        r "Didn't we decide cutting suppressed the Third Eye?"
        show renier at std
        show yuri c125111 at foc
        y "I think it does suppress it normally, he was just being affected by the stress."
        show yuri at std
        mc "Sounds plausible..."
        show renier at foc
        r u11111 "Hm..."
        r u1113 "So do we all have it then?"
        show renier at std
        show linda 334111 at foc(p52) zorder 4
        l "I wouldn't be surprised..."
        l "We're all in this mess together."
        l "It's likely we all came from that experimentation facility."
        show linda at std
        show renier at foc
        r "Yeah..."
        r "Hell, maybe we're still in that facility?"
        r "What if \"Doki Doki Literature Club\" is one of the experiments they're doing?"
        show renier at std
        mc "Don't scare me like that..."
        show linda at foc
        l "Well, we should get back to work now."
    else:
        show renier at foc
        r u11111 "Oh... right..."
        show renier at std
        show linda at foc
        l "We should get back to work now."
    show linda at std
    "The hackers return to their work, leaving me, Yuri, Natsuki and Renier alone again."
    scene bg club_day with wipeleft_scene
    play music yawa
    if not persistent.player_support_renier_experiment:
        call chapter10_no_experiment
    elif persistent.mc_favorite == "Natsuki":
        call chapter10_mc_cut
    else:
        call chapter10_natsuki_cut
    jump chapter10_request_explore

label chapter10_no_experiment:
    show renier u1113 at foc(p21)
    r "What do you three say we go exploring?"
    show renier at std
    mc "I mean, we got nothing else to do."
    show renier at foc
    r "I wonder what happens when we try to leave the game area."
    show renier at std
    mc "That doesn't sound like a good idea."
    mc "We don't want to crash things again."
    show renier at foc
    r "It might give us information about how this world works that could help the hackers."
    r "And at worst it'll hurt temporarily."
    show renier at std
    mc "That's basically the same argument you made for your violent experiment."
    show renier u1123
    mc "What about the interruption it would cause them if it crashes?"
    mc "As small as it is, that's got to be worth at least as much as the chance of learning something useful."
    show renier u1163
    "Renier sighs."
    show renier at foc
    r u1133 "I just really want to help."
    r "I feel so useless."
    show renier u11311 at std
    call yuri_wise
    return

label yuri_wise:
    "I'm really surprised."
    "Is Renier admitting that he was wrong?"
    show yuri c125111 at foc(p22)
    show renier u1131
    y "I understand."
    y "You told yourself both were wise because you wanted them to be."
    y "Self-deception is easy, and can be very tempting."
    y "But you have to resist it."
    y c125112 "When I first started getting addicted to cutting..."
    y "I told myself that it wasn't a problem because I could stop if I wanted to."
    y "Essentially, I told myself that I didn't need to stop because I could."
    y "It was a trap I didn't climb out of..."
    y c125131 "It led to my death."
    y c125111 "So you need to examine your thoughts rationally, because self-deception is harmful."
    show yuri at std
    show renier u1113
    r "..."
    show renier at foc
    r u1113 "I think those are wise words."
    r u1133 "I just..."
    r "I thought this was my story."
    r "I even wrote that to [persistent.playername]."
    r u21331 "{i}Time to be a fucking hero{/i}."
    r u1113 "But you're right."
    r "I'll get my chance when we break out of this game."
    r "I just need to be patient."
    show renier at std
    return

label chapter10_natsuki_cut:
    "I sit down next to Natsuki."
    mc "Thanks for your bravery, Natsuki."
    show natsuki xc6131 at std(p11)
    "Natsuki just shrugs."
    mc "Natsuki...?"
    show natsuki at foc
    n xc4131 "I kind of don't want to be thanked anymore..."
    show natsuki at std
    mc "Huh?"
    mc "Why's that?"
    show natsuki at foc
    n c113112 "Cause I hate that I did it!"
    n "The thought that I let Renier and [persistent.playername] guilt trip me like that is worse than the pain was!"
    n c223155 "They took advantage of my need to not feel less noble than Renier!"
    n "And I fell for it!"
    n c223132 "And they were totally wrong about the experiment!"
    n "It didn't teach us shit!"
    show natsuki c225132 at std
    "Natsuki is yelling suddenly."
    show natsuki at x(p22)
    show renier u1213 at foc(p21)
    r "Just because it didn't work doesn't mean it was the wrong thing to do."
    r "I had no way of knowing what would or wouldn't happen."
    show renier at std
    show natsuki at foc
    n c115112 "That doesn't excuse you for--"
    show natsuki at std
    return

label chapter10_mc_cut:
    show natsuki c114114 at std(p11)
    "Natsuki sits next to me."
    show natsuki at foc
    n "I'm sorry, [mc_name]."
    n "I shouldn't have let you take my place."
    show natsuki at std
    mc "What?"
    mc "No, that wasn't {i}your{/i} fault!"
    show natsuki at foc
    n "It was, though."
    n "I was the one who agreed to do it."
    n "I made you feel the need to take my place and then let you."
    n "I should've just told Renier and [persistent.playername] no."
    n "The experiment didn't teach us crap, anyway."
    show natsuki at std
    mc "Come to think of it..."
    mc "What {i}did{/i} we learn, Renier?"
    mc "How does it help us to know we probably all have the Third Eye?"
    show natsuki at x(p22)
    show renier u2113 at foc(p21)
    r "Well..."
    show renier u21131 at std
    "Renier sighs."
    mc "So, you put me through that for nothing."
    show renier at foc
    r u1213 "I didn't 'put you through' anything."
    r u1223 "And stop acting like I didn't go through the exact same thing you did."
    show renier at std
    show natsuki at foc
    n c115112 "Shut up and admit your mistakes, Renier!"
    n "He had to cut himself because of you and [persistent.playername] and for nothing!"
    show renier u2226
    "Just as Renier is about to respond, Linda comes over."
    return

label chapter10_request_explore:
    if persistent.player_support_renier_experiment:
        show renier ru2113 at std(p11)
        show natsuki at std(p33)
    else:
        show renier ru1111 at std(p11)
        show yuri at std(p33)
    show linda 333111 at leftin(p31)
    l "Everyone?"
    l 331111 "It's time to run a test."
    if persistent.player_support_renier_experiment:
        show natsuki c113113
    else:
        show yuri c113111
    show renier at xif(p11)
    r ru1115 "A... test?"
    show renier at std
    show linda at xif(p31)
    l 331111 "We've found a section of code that just might be related to the deep script, and to test our theory, we need to trigger it."
    show linda at std
    mc "That sounds like a really bad idea..."
    show renier ru1115 at foc
    r "That's great!"
    r "Can we just open Portrait of Markov?"
    show renier at std
    # If Natsuki and Yuri have been traumatized by this.
    if persistent.sayori_reset_ynr:
        if persistent.player_support_renier_experiment:
            show natsuki at foc
            n c115212 "Wait!!"
            if persistent.mc_favorite == "Natsuki":
                n c113212 "You're not going to put me and [mc_name] through that again!"
            else:
                n c113212 "You're not going to make me puke my stomach out like that again!"
            show natsuki at std
            show linda at x(p41)
            show renier at x(p42)
            show natsuki at std(p43)
            show yuri c225335 at foc(p44)
            y "I'd also much prefer to not do that again..."
            show yuri at std
        else:
            show yuri at foc
            y c226335 "Wait!!"
            y c225355 "I don't want to get all those cuts again..."
            show yuri at std
            show linda at x(p41)
            show renier at x(p42)
            show yuri at std(p43)
            show natsuki c114214 at foc(p44)
            n "And I really don't wanna puke like that again..."
            show natsuki at std
        show renier ru1113
        show linda at foc
        l 334223 "Oh..."
        l "I forgot about that..."
        l 334113 "But we have to do this..."
        l "And it might be possible to trigger the deep script without crashing the game."
        show linda at std
        if persistent.player_support_renier_experiment:
            show yuri at foc
            y "Okay..."
            show yuri at std
            show natsuki at foc
            n xc5132 "..."
            n xc3155 "..."
            n xc4132 "Okay..."
            show natsuki at std
        else:
            show yuri at foc
            show natsuki at foc
            ny "Okay..."
            show yuri at std
            show natsuki at std
        show linda at foc
        if persistent.player_support_renier_experiment:
            l 334113 "Thank you."
        l 334221 "Portrait of Markov might work..."
    else:
        show linda at foc
        l 334111 "Maybe..."
    l "The deep script's goal is to stop us from finding out the truth or escaping."
    l "So maybe if we have just one person open the book by themselves and it isn't [mc_name] or someone with code powers..."
    l 334111 "It might not consider that an immediate threat?"
    l "After all, it didn't crash the game when Monika was getting ideas about the book in the space room..."
    l "It waited until she was about to spill the beans to stop her."
    l "So I think we should try with someone who can read the book without being able to immediately show what they learn to [persistent.playername]."
    l "If my theory about the code is right, we should still see the internal activity I'll be looking for."
    show linda at std
    # The condition for Natsuki being already on screen
    if persistent.player_support_renier_experiment or persistent.sayori_reset_ynr:
        show natsuki c114111
    # The only way Yuri's not on screen
    if persistent.player_support_renier_experiment and not persistent.sayori_reset_ynr:
        show linda at x(p41)
        show renier at x(p42)
        show natsuki at x(p43)
        show yuri c125111 at foc(p44)
    else:
        show yuri c125111 at foc
    y "That makes sense..."
    y "So I'll go out by myself and open it?"
    y "It should be safe with me, right?"
    show yuri at std
    show linda at foc
    l "I think so."
    show linda at std
    show yuri at thide
    hide yuri
    "Yuri leaves with the book."
    show sayori c114111 at std(p51)
    show monika c124111 at std(p52)
    show linda 334111 at std(p11)
    show renier ru1113 at std(p54)
    show natsuki c114111 at std(p55)
    mc "Alright, let's brace ourselves..."
    "We wait a few seconds."
    show linda 123111 at foc zorder 2
    l "I see the log output!"
    show renier ru1115
    show natsuki c111111
    show sayori c11x111
    show monika c122111
    l 123331 "I was right!"
    show linda at std
    show sayori c114111 at std(p62) zorder 0
    show monika c124111 at std(p63) zorder 0
    show linda 334111 at std(p64) zorder 1
    show renier ru1113 at std(p65) zorder 0
    show natsuki c114111 at std(p66) zorder 1
    show yuri c226131 at leftinfoc(p61) zorder 0
    y "I read part of the book! It said-"
    y c225142 "... It said..."
    y c225142 "... I don't remember..."
    show yuri at xis(p61)
    show natsuki at foc
    n xc4111 "Well that was a disappointment..."
    show natsuki at std
    show yuri at foc
    y sc1111 "Uu..."
    show yuri at std
    show linda at foc
    l 124111 "That probably wouldn't have worked anyway."
    l "The deep script would've just hijacked everything as soon as the information was about to be passed on to someone who could act on it."
    l 123111 "But we confirmed that that's where the deep script checks whether it needs to act!"
    l "This is huge progress!"
    show linda at std
    show sayori at foc zorder 1
    s c224131 "Ohhh!"
    play music t8
    s c22x111 "We forgot something!"
    show sayori at std
    show linda at foc
    l 124111 "What's that?"
    show linda at std
    show sayori at hopfoc
    s c222111 "Natsuki's cupcakes!"
    s "This is day one, so they should be in the clubroom!"
    s "We can celebrate our breakthrough!"
    show sayori at std
    show yuri c111111
    show monika c122111
    show natsuki c222113 at foc
    n "I forgot too!"
    n "Thanks for reminding me!"
    n "It would've been terrible if we never got to eat them!"
    show natsuki at std
    show yuri at foc
    y c112111 "I'll make some tea then too..."
    show yuri at thide
    hide yuri
    "Natsuki gets out the cupcakes, and they're as fluffy and delicious as I remember them."
    show yuri c111111 at std(p61)
    "Yuri soon returns with the tea to match."
    show linda 111111
    show renier ru1114
    # Renier doesn't drink tea.
    "Soon after we finish our cupcakes, I hear the bell ring."
    show monika at foc zorder 2
    m c122211 "Oh..."
    m "Ahaha..."
    m "Club period is over..."
    show monika at std
    mc "We heading back to my house, then?"
    show monika at foc
    m c121111 "I guess so."
    m c222111 "Okay, everyone..."
label dayend:
    scene living_room
    pause 0.1
    play sound glitch_basic
    scene black with Dissolve(0.1)
    play music g2
    m "Ah!"
    pause 2.0
    ms "What's happening?"
    l "The script is trying to end the day on us because the club meeting is over..."
    l "We can stop it."
    l "Help me out here."
    pause 1.0
    play sound glitch_basic
    scene living_room
    show monika glean at leftin(p31)
    m "[mc_name]--{w=0.2}{nw}"
    play sound glitch_monikapound
    scene black
    m "Ow!"
    s "Maybe we shouldn't do this!"
    s "What if we just let the script skip to tommorow?"
    m "That's not how it works!"
    m "It doesn't actually skip time for us."
    if persistent.monika_questions['time']:
        s "Oh right..."
    m "And there's no telling what else it might adjust on realizing Linda and Renier are here!"
    l "Hold on, I think I've got this!"
    play sound glitch_medium
    l "Oh god{w=0.4}{nw}"
    $ persistent.newgame = 3
    $ delete_all_saves()
    $ renpy.quit()
