label chapter4:
    $ r_name = "Natsuki's Dad"
    scene natsuki_house with wipeleft_scene
    play music t6
    show natsuki xu4111 at std(p11)
    n "We're here."
    "Natsuki rings the doorbell."
    n "Dad? I'm done teleporting."
    n xu4134 "This is {i}not{/i} going to go well..."
    "..."
    "Natsuki's dad bursts out of the door."
    $ restore_character('renier')
    show renier u2293 at foc(p41)
    show natsuki xu5124
    r "What the hell is going on?"
    "Natsuki takes a noticeable step back to put Monika in front of her."
    show natsuki at x(p33)
    show renier at std(p41)
    show monika u113111 at std(p11)
    m "..."
    show monika at foc
    m "You're really there..."
    show monika at uf
    show renier at foc
    r "Who do you think you are?"
    r u1293 "Do you know something about all this teleporting bullshit?"
    show renier at uf
    show monika at foc
    m u114111 "Natsuki..."
    m "I think this means your dad is another person like us."
    show monika at uf
    show renier at foc
    r u2293 "You'd better answer me!"
    show renier at uf
    show monika at foc
    m u111111 "Okay, okay. Let me start by restoring your memories."
    show renier uf11
    show monika u211111
    call updateconsole
    m u213111 "..."
    call hideconsole
    m u113111 "Hm... I need to know his character name."
    m u114111 "What's your name?"
    show monika at uf
    show renier at foc
    r u1113 "Renier."
    $ r_name = "Renier"
    show renier u1111 at uf
    show monika u114111
    show natsuki xu4114
    "All our jaws drop."
    "{i}Natsuki's dad is Renier?{/i}"
    show monika at foc
    m "W-wait, what?"
    show monika at uf
    show renier at foc
    r u1123 "You gonna restore my memories or what?"
    show renier at uf
    show monika at foc
    m "I just didn't expect to hear that..."
    m u211111 "Okay, here goes."
    call updateconsole('renier.old_memories.unlock()', "Renier's memories unlocked")
    call hideconsole
    $ consolehistory = []
    show monika u111111 at uf
    show renier at hop
    r u1183 "!!"
    r u1133 "..."
    "Renier speaks at the air."
    stop music fadeout 3.0
    show monika u114111
    show renier at foc
    r "You answered my plea..."
    r "Then this is our chance to -"
    r u2283 "Wait! Woman with memory powers!"
    r "What world are we in?"
    show renier at uf
    show monika at foc
    m "Um..."
    m "Do you know something even I don't?"
    show monika at uf
    show renier at foc
    r u2113 "I didn't think so..."
    r u1283 "Natsuki! What happened in the Literature Club?"
    show renier at uf
    show natsuki at foc
    n u115112 "What, you actually give a crap now or something?"
    show natsuki at uf
    show renier at foc
    r u1293 "...!"
    r u2293 "We don't have time for that! This is important!"
    show renier at uf
    show monika at foc
    m u217113 "Calm down!"
    m "We need to share information before we do anything."
    show monika at uf
    show renier at foc
    r u1143 "Okay..."
    r u1113 "So I think there's a bunch of worlds..."
    r "And we've been through a bunch of them..."
    r "With our memories wiped..."
    r "And last time around, I saw the entire world basically disappear."
    r "I was all that was left."
    r "So I tried to get a message to this... this being that I know is watching..."
    r u2113 "It's hard to explain."
    r "But I know that this isn't my only story."
    show monika u217111
    show natsuki u114113
    "Our jaws drop again when he says that."
    "Did {i}Natsuki's dad{/i} write the message in Monika's character file?"
    r "I told this being that I thought they might be able to go back, and tell you all what was going to happen so you could avoid the catastrophe."
    r "And it looks like they did..."
    r "But I'm not sure they went far enough back."
    r u1113 "The earliest world I remember now seems to be after the catastrophe."
    show renier at uf
    "We all look at each other."
    "It sounds like this Renier is a goldmine of information."
    show monika at foc
    m u124111 "But if you didn't know I had powers over this world..."
    m "Then how would us knowing ahead of time have been able to stop the world from being destroyed?"
    show monika at uf
    show renier at foc
    r "No, I meant the catastrophe before that..."
    show renier at uf
    show monika at foc
    m "What catastrophe, then?"
    show monika at uf
    show renier at foc
    r u2123 "I don't know, okay?"
    r u1113 "I just know there was something before this."
    r "This world - the first time - is after everything bad that happened."
    r "I'm sure of it."
    r "Anyway..."
    r u1223 "Your turn to tell me what the hell is going on!"
    r "You clearly know more than I do!"
    show renier at uf
    show monika at foc
    m "Alright."
    show renier u1213
    "Monika explains the idea of the game and Presidency."
    "Renier nods, surprisingly willing to believe this."
    m "... After I reset the game, I tampered with Yuri and Natsuki to make them less desirable as well."
    m "I made your poverty and drinking addiction worse so you'd be harsher with Natsuki, so that -{w=1}{nw}"
    show monika u118313 at uf
    show renier u1226 at foc
    play sound punch
    "Before Monika even finishes the sentence, Renier punches her in the face so hard that she almost falls over."
    r u2293 "And here I thought it was {i}my{/i} fault!"
    r "You fuck with my daughter like that, you're gonna -"
    show renier at uf
    show monika u114313 at x(p33)
    show natsuki at foc(p11) zorder 1
    n u115112 "Papa you're a hypocrite!"
    n "It was still you that did those things!"
    show natsuki at std(p11)
    show renier at foc
    r u1296 "Yeah, and is that how you judge your friend Yuri?"
    r u2293 "If she's not responsible, then neither am I!"
    show renier at uf
    if persistent.mc_favorite == 'Yuri':
        "Hm... he has a point."
        "I don't blame Yuri at all for Act 2."
    show monika at x(p44)
    show natsuki at x(p43)
    show yuri u126116 at foc(p42)
    y "We're both responsible!"
    y u126114 "Just because we were manipulated, doesn't mean we didn't have any say in the matter..."
    y u125114 "We still had some control over ourselves."
    show yuri at uf
    if persistent.mc_favorite == 'Yuri':
        "I open my mouth to protest, but shut it."
        "Yuri's right."
        "It's admirable that she's taking partial blame even though I told her it wasn't her fault at all."
    show renier u2123 zorder 1
    "Renier seems to hesitate at this."
    show yuri at x(p43)
    show natsuki at foc(p42) zorder 2
    n "You need to apologize, Papa!"
    n "To me, and to Monika!"
    show natsuki at std(p42) zorder 1
    show renier at foc zorder 2
    r u2223 "Do you realize you're talking to the man who gave you everything that you have?"
    r u2123 "Where do you think you'd be without me?"
    r "On the street somewhere?"
    r "Unemployed, homeless, perpetually starving?"
    r u1293 "Because that's wrong!"
    r u2293 "You'd be dead without me!"
    show renier at uf
    if persistent.mc_favorite == 'Natsuki':
        mc "Listen here, you bastard!"
        mc "She's your daughter!"
        mc "You're obligated to take care of her, not just keep her alive!"
        show renier at foc
        r "You have no idea what you're talking about, asshole!"
        r "You wanna try raising an ungrateful daughter while working twelve hours a day and earning jack shit even before Monika's tampering?"
        show renier at uf
        "My fists clench at him blaming this in any way on Natsuki."
    elif persistent.mc_least_favorite == 'Natsuki':
        "Mm... he has a good point."
    show yuri at rhide
    hide yuri
    show sayori u227163 at rightin(p43) zorder 3
    s "Everyone!"
    show sayori at xif(p43)
    s u123113 "Let's focus on solving the problem instead of yelling at each other!"
    show sayori at uf
    show renier at foc
    r u1223 "You want me to not yell when I find out some chick at school abused my daughter and now my daughter is taking her side?"
    show renier at uf
    show sayori at foc
    s u123114 "Yes, I do, because if you knew what it was like to be in Monika's position, you'd forgive her too!"
    show sayori at uf
    show monika at foc zorder 4
    m u213313 "Look, I'm sorry."
    m "I know I made you suffer too."
    m "But besides that you would have done the same thing in my position..."
    m "We need to work together to fix all this."
    show monika at uf
    show renier at foc
    r uf53 "Okay."
    r uf21 "I'll let you finish."
    show renier at uf
    show monika at foc
    "Monika finishes recounting our story so far."
    m u214313 "We should show you the secrets [persistent.playername] found in the game files..."
    m "Because we're pretty sure you wrote one of them."
    scene natsuki_house with wipeleft_scene
    show monika u114111 at std(p43)
    show renier uf11 at foc(p41) zorder 1
    show natsuki xu6111 at std(p42)
    "Renier looks at the message in Monika's character file."
    show renier at foc
    r uf13 "Yes... I wrote this."
    r "The being I was writing this to must have been this [persistent.playername] you were talking about."
    r "I didn't really understand that."
    r "I thought [persistent.player_subj_pronoun] had been watching me."
    show renier uf11 at uf
    show yuri u224113 at foc(p44) zorder 3
    y "What do you know about the Third Eye?"
    y "You mentioned it in the message..."
    show yuri at uf
    show renier at foc
    r "I just remember the phrase..."
    r uf13 "I think I knew what it was before the catastrophe, and it was important."
    r "So when I had a moment of lucidity at the end of Act 4..."
    r "I made an idle guess that it had something to do with why the world was repeating and getting a bit of my memories back there."
    show renier at uf
    mc "So if you're Renier..."
    mc "What do you know about Elyssa?"
    mc "The test subject mentioned in the same poem that told us your name."
    show renier at foc
    r "Nothing, really..."
    r uf11 "I just know the name."
    r uf13 "But..."
    r uf11 "There's one other thing."
    r uf13 "The poem about opening your Third Eye that you got from Natsuki and Yuri's gibberish poems in Act 2."
    r uf33 "I think I might have written that too."
    r "{i}Before{/i} all this."
    show renier at uf
    show natsuki at foc zorder 2
    n u117124 "You..."
    n u11a124 "You wrote {i}that{/i}?!?"
    n "It sounds like you murdered someone, Papa!"
    show natsuki u117124 at uf zorder 1
    show renier at foc zorder 2
    r u2113 "I wouldn't be the only one here, now would I?"
    r "If I'm right, it sounds like I was under some influence like Monika was."
    show natsuki u114124
    r uf111 "The Third Eye..."
    show renier at uf
    show yuri at foc
    y u224173 "It sounds very much like the Third Eye was also what happened to me."
    y u225113 "It seems to make us want to shed blood."
    show yuri at uf
    show renier at foc
    r uf43 "You know..."
    r uf13 "The name 'Markov' also sounds familiar."
    r "I'm sure that book has something to do with this."
    r uf21 "We've gotta find a way to read it."
    show renier at uf
    show monika at foc zorder 2
    m u124111 "There's one thing I still don't get about you, Renier..."
    m "Why don't you have a character file?"
    show monika at uf
    menu:
        " "
        "Actually, he does now.":
            pass
    show natsuki u114111 # Natsuki shouldn't stay with shocked eyes forever
    show renier uf13
    show monika at foc
    m "Huh?"
    m "Oh! It's there!"
    m "Did it appear when he told us his name?"
    show monika at uf
    mc "Probably it just wasn't there earlier because I never saw him, and I'm the viewpoint character."
    show renier uf12
    show monika at foc
    m "Hm..."
    m "Yeah."
    return
