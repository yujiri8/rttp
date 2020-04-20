label chapter3:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    show sayori t1211 at std(p11)
    s "Ehehe... I kind of just wanted to say that for old times' sake."
    mc "Huh? What do you mean?"
    s u115111 "Oh right... you lost your memories."
    mc "What?!?"
    s u123112 "Um, Monika? Can you copy [mc_name]'s memories back in?"
    "I glance around."
    "Monika isn't here."
    mc "Sayori, I don't know what you're on about, but if this is some kind of joke..."
    s u115122 "I guess Monika can't hear."
    s u123112 "[mc_name], we have to go to school and find Monika."
    s "She can make you remember."
    mc "Sayori, if this is a joke, now is the time to stop."
    s u223114 "It's not a joke! This is serious!"
    mc "Well then back up and tell me what's going on!"
    s u115123 "It's no use trying to explain."
    s u123112 "Let's just go find Monika. She can restore your memories."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch_basic
    pause 0.25
    hide screen tear
    mc "Ah-..."
    mc "Okay, I got my memories back."
    show sayori u111111 at x(p44) zorder 3
    show natsuki u111111 at std(p43) zorder 2
    show yuri u111111 at std(p42) zorder 1
    show monika u121111 at foc(p41) zorder 0
    m "Here we are. Sorry about the delay."
    m u222111 "So, Yuri. Do you have Portrait of Markov with you?"
    show monika at uf
    show yuri at foc
    y u124113 "I should..."
    "Yuri reaches into her bag and pulls out the familiar book with the ominous-looking eye."
    y u125111 "Here it is..."
    y u222113 "I'm excited to read it again, knowing what we now do."
    show yuri at uf
    show monika at foc
    m u221111 "So how are we reading it?"
    show monika at uf
    show yuri at foc
    y u224113 "Eh?"
    show yuri at uf
    show monika at foc
    m u221111 "We can't all crowd around the one book."
    show monika at uf
    show yuri at foc
    y u124143 "I have two..."
    show yuri at uf
    show monika at foc
    m "Ah, I forgot."
    m "Still, three people around one book is a little uncomfortable."
    m l1111 "Are you going to read it out loud to us?"
    show monika at uf
    show yuri at foc
    y u227215 "Eh? Uu..."
    y su1211 "I... don't feel comfortable reading aloud..."
    show yuri at uf
    show monika at foc
    m "Ahaha, just teasing you~"
    m "I'll read it if you want."
    show monika at uf
    show yuri u113111
    "Yuri gives Monika a copy of the book."
    play music g2
    call prevent_escape
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 5.0
    $ persistent.pom_crash = True
    $ persistent.autoload = "after_pom_crash"
    $ renpy.quit()

label chapter3_2:
    $ persistent.autoload = None
    hide screen tear
    stop music
    scene black
    m "Agh!"
    s "What's happening?"
    m "Everything's breaking! Help me fix this!"
    s "I don't know how..."
    m "Everyone else just don't move, if you can hear me!"
    pause 2.0
    scene bg residential_day with dissolve_scene
    m "Okay... I think I fixed it."
    show monika u214112 at leftin(p41)
    m "Is everyone here?"
    "My ears stop ringing."
    mc "I'm here... but I think I've got a headache."
    show sayori end-glitch at rightin(p44)
    pause 1.0
    show sayori u227162 at xif(p44)
    s "Yikes! That was scary!"
    show sayori at uf
    show monika at xif(p41)
    m "Where are Natsuki and Yuri?"
    show monika at uf
    show sayori u114112 zorder 1
    "I look around."
    "I notice Yuri on the ground with blood on her arm and a knife beside her."
    if True or persistent.mc_favorite == 'Yuri':
        mc "No!"
        "I rush over and bend down next to her."
        mc "Yuri, are you okay?"
        y "I... yes..."
        y "I didn't do this!"
        y "I just found myself this way when everything came back..."
        y "I think it sort of spilled over from when I did it before."
    show yuri u2zh117 at std(p43)
    "Yuri gets up."
    show sayori at foc
    s u227112 "Oh no! That must hurt so bad!"
    s "Monika, can we heal her?"
    show sayori at uf
    show monika at foc
    m u114112 "I don't know a command for it..."
    show monika at uf
    show yuri at foc
    y "It's really not so bad..."
    y "It's just one cut."
    y "I've handled a lot worse before."
    show sayori u116122
    show yuri u22h117
    "Yuri rolls down her sleeve."
    show yuri at uf
    show monika u213112 at foc
    m "I'm going to try to warp Natsuki over here. I'm really worried."
    call updateconsole("warp('natsuki', 'residential_day')")
    show monika at uf
    call hideconsole
    $ consolehistory = []
    show natsuki u115124 at std(p42)
    n "..."
    show natsuki at foc
    n u123112 "What are you warping me around for, Monika?"
    show natsuki at uf
    show monika at foc
    m u117211 "It was only me the second time!"
    m u124111 "You weren't here when the game came back on, so I got worried."
    m u224111 "I think the game broke because we tried to read Portrait of Markov..."
    m "It's the same thing that happened to me in the space room."
    m u224113 "The script doesn't want us to figure this out."
    m u124111 "So where were you, Natsuki?"
    show monika at uf
    show natsuki at foc
    n u124111 "I was with my dad..."
    n u124112 "He was, of course, pissed to find me at home when I was supposed to be at school..."
    n "And he wasn't exactly buying the 'I got teleported here' explanation..."
    show natsuki at uf
    show monika at foc
    m "Wait. You were talking to your dad?"
    show monika at uf
    show natsuki u124111 at foc
    n "Yeah..."
    show natsuki at uf
    show monika at foc
    m "..."
    m u124222 "But I swear there were no NPCs at the school..."
    m u213113 "I have to talk to him."
    show monika at uf
    show natsuki at foc
    n "Why, exactly?"
    show natsuki at uf
    show monika at foc
    m u217213 "I have to find out if it's just me that can't see the NPCs!"
    show monika at uf
    show natsuki at foc
    n xu4131 "Now that you mention it, I didn't see any NPCs either when I spawned at the school."
    show monika u114111
    n "Maybe there's something special about him."
    n xu5131 "I don't want there to be... I don't want to ever see him again."
    show natsuki at uf
    show sayori at foc
    s u123112 "Natsuki, if he's your dad and he really is real..."
    s "I'm sure he wants what he thinks is best for you."
    show sayori u124112 at uf
    show natsuki at foc
    n u113112 "No, Sayori he doesn't!"
    n "He starved me to the point that I literally passed out in the club and he even beat me more than once!"
    show natsuki at uf
    show sayori at foc
    s "But that was after Monika tampered with him..."
    s u123112 "That's like blaming Yuri for what she did in Act 2!"
    show sayori at uf
    show natsuki at foc
    n u113131 "Yuri was normal before that!"
    n u113112 "My dad's just always been a prick who doesn't care what happens to me."
    #n "You remember my poem about him?"
    n "He made me feel like I couldn't keep my manga in my own room, for fear of him!"
    n "He never does anything for me beyond the basics of giving me a place to live."
    n "I learned how to cook on my own, because I had to."
    if persistent.mc_favorite == 'Natsuki':
        n "When [mc_name] helped me with baking, I had to lie to him and say I was going to a girl's house because he's so paranoid about me getting into a bad relationship."
    n "And he's a drunkard!"
    show natsuki at uf
    show sayori at foc
    s "Hold on Natsuki, if your dad is so stingy..."
    s "How did you get all your manga?"
    s "You had tons of them. There's no way he gave you that much allowance that you didn't spend on food."
    show sayori at uf
    show natsuki xu4131 at foc
    "Natsuki squints, like she hadn't noticed that before."
    n "..."
    n xu4111 "Huh."
    n "I've had them for as long as I can remember."
    n xu5111 "Is that one of the things the script just put in for the sake of the dating game and stopped me from noticing it?"
    show natsuki at uf
    show monika at foc
    m u214111 "Probably. Just like how none of us except you have even one parent."
    m u214111 "Anyway, lead the way, Natsuki."
    return
