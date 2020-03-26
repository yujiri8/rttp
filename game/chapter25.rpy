label chapter25:
    "..."
    scene facility with wipeleft_scene
    "..."
    show yuri c115111 at foc(p11)
    y "So what was this place?"
    y "It couldn't have been his facility."
    show yuri at std
    l "Maybe it was built for something unrelated, and he commandeered it later?"
    l "Maybe it was some kind of research facility for something else."
    l "Or maybe some other top-secret, horrifying thing..."
    l "Who knows."
    show yuri at std(p22)
    show renier at foc(p21)
    r u1113 "It must've been easy to take it over when he can basically control people's minds with scripts and memory wiping."
    show renier at std
    scene facility with wipeleft_scene
    "Several minutes pass."
    show mc c124115 at foc(p11)
    mc "I don't know how long we should be expecting this to take..."
    show mc at std
    l "Let's give her some time."
    l "Maybe she had some issues with the world, and is still trying to explain the plan to Libitina..."
    l "Or maybe she's just about to tell Libitina to kill her."
    l "And that decision is taking some time."
    l "Even if she's prepared..."
    l "It must be really difficult to condemn yourself to that, when you have no one to exhort you."
    l "I'm not sure how long it would take me."
    scene facility with wipeleft_scene
    "We wait a while longer."
    show mc c126215 at foc(p11)
    mc "Okay, what time is it?"
    mc "How long has she been in there?"
    show mc at std(p21)
    show albert 11111 at foc(p22)
    al "It's been almost twenty minutes."
    al "For those wondering, it's 5 o'clock."
    show albert at std
    l "Okay, that's really concerning."
    l "I don't know of anything we can do though."
    show mc at std(p31)
    show albert at std(p32)
    show yuri c125111 at foc(p33)
    y "What if we switch the viewport destination back?"
    y "Could [persistent.playername] help her?"
    y c125118 "She probably got stuck somehow...!"
    show yuri at xis(p33)
    l "But what if the viewport gets stuck in that world?"
    l "That's what Monika was afraid of earlier."
    l "Especially if we know it's broken and dangerous..."
    l "The risk is too high."
    l "We can't."
    l "If she really is stuck due to the world being broken, it's probably not something [persistent.playername] could help with, anyway."
    show yuri at foc
    y c124142 "I suppose so..."
    y "I wish there was anything we could do to help."
    show yuri at std
    "..."
    show mc at std(p41)
    show albert at std(p42)
    show yuri at std(p43)
    show sayori c113113 at foc(p44)
    s "I'm hungry."
    s c115123 "I know it's not really appropriate..."
    show sayori at std(p54)
    show mc at std(p51)
    show albert at std(p52)
    show yuri at std(p53)
    show renier ru1113 at foc(p55)
    r "That makes two of us."
    show renier at std
    show sayori at xif(p54)
    s c113111 "How long was he expecting his troops to stand here?"
    s "They must've been hungry too."
    show yuri at xif(p53)
    y c114111 "He would've left them standing guard until nightfall."
    y "He viewed their suffering as a positive good."
    y "He recognized them as evil for following his orders, even though he didn't see himself as evil for giving them."
    y "I still can't believe that he could convince himself his actions were justified..."
    show yuri at std
    if persistent.player_support_experiment:
        show renier at foc
        r ru1113 "Well, like you taught me way back when..."
        r "People can convince themselves of whatever they want."
        show renier at std
    else:
        l "Well, like I learned in my time in the cult..."
        l "There's almost no limit to what we can convince ourselves of if we really want to think it."
    show yuri at foc # TODO pose
    y "Hmm..."
    show yuri at std
    "..."
    show albert at foc
    al 12111 "So, Sayori and [mc_name]."
    al "How did you two and Monika escape?"
    show albert at std
    show sayori c115123
    show mc
    "Sayori and [mc_name]'s expressions darken."
    show albert at foc
    al 21112 "If... you don't mind..."
    show albert at std
    show mc at foc
    mc "Well..."
    mc "It started with me."
    mc "One day, they were doing a test on violence against animals."
    mc "They gave me a knife and made me kill a mouse."
    mc "But the guard doing the test got careless, and I killed him."
    mc "I was lucky, cause Sayori and Monika were nearby."
    mc "I used my Third Eye to open theirs."
    mc "And they helped me."
    show mc at std
    show renier at foc
    r u1113 "Wait..."
    r "You used your Third Eye to open theirs?"
    r "You could do that?"
    show renier at std
    show mc at foc
    mc "Apparently."
    mc "My recollection might not be the clearest, but that was what it looked like."
    show mc at std
    show renier at foc
    r "Everyone's Third Eye distorted reality a little differently."
    r "But I don't remember seeing anyone else with a power like that."
    show renier at std
    show sayori at foc
    s "We combined our Third Eye powers to overcome the guards."
    s "They couldn't shoot us."
    s "Well, eventually one of them did..."
    s "But I think it actually turned out to be what saved us."
#    s "[mc_name] had killed enough guards to start to peter out."
    s "One of them shot me."
    s "It didn't overcome my Third Eye completely..."
    s "... but it made me sort of lucid for a moment, kind of like how we saw it affect Monika when Yuri stabbed her."
    s "I think it was what made me decide to flee instead of staying to kill more of them."
    s "I don't remember everything I was thinking, but I think some part of me knew that I'd peter out soon if I kept killing..."
    s "And for some reason, even though we couldn't communicate, [mc_name] and Monika followed me."
    s "And my wound healed before my Third Eye gave out."
    show sayori at std
    show renier at foc
    r "Wow..."
    r "It sounds like you had positive distortion."
    r "That was a pretty rare trait."
    r "Most subjects had pretty low positivity."
    r "They could shrug off almost anything when they were fully activated, but not actually heal."
    show renier at std
    #TODO
#    "Adam must've not been there."
#    "Wait a minute..."
#    "warp was broken, but there were other ways ."
#    "According to the book she compiled, Linda read his memories a long time after that point."
#    "Is it really possible he didn't know about memory reading?"
    scene facility with wipeleft_scene
    "A few more minutes pass."
    show natsuki c223111 at foc(p11)
    n "This is awful!"
    n "There's obviously something wrong!"
    n "[persistent.playername], point the viewport over there!"
    show natsuki at std
    l "I'm starting to agree..."
    # I kinda hate to use the "last second" trope, but oh well.
    $ restore_character('monika')
    $ restore_character('libitina')
    $ restore_character('adam')
    show natsuki c224113 at std(p33)
    show libitina 2271111 at foc(p11)
    b "Hello...?"
    show libitina at std
    "Libitina's back...!"
    show monika c114282 at foc(p31)
    m "Haah..."
    m c114244 "..."
    show monika at thide
    hide monika
    "Monika collapses."
    show sayori at leftinfoc(p31)
    s c22x151 "You did it, Monika!"
    "Sayori runs over to comfort the traumatized Monika."
    s "We we getting so worried about you!"
    show sayori at std
    show libitina at foc
    b 2262114 "Um..."
    b "I don't understand."
    b 2272114 "Wasn't I supposed to keep my admin status?!?"
    show libitina at std(p43)
    show sayori c224132 at std(p41)
    show natsuki c224114 at std(p44)
    show monika c114382 at foc(p42)
    m "What...?"
    m c117382 "You're telling me you didn't?!?"
    show monika at xis(p42)
    show libitina at xif(p43) zorder 1
    b "No, I didn't!"
    b "Everything feels normal again!"
    b "And there's no console!"
    show libitina at std
    show sayori c117212
    show natsuki c114124
    show monika at foc
    m c118284 "NOOO!"
    "Monika's scream is so loud it hurts my ears."
    m c117244 "It was for nothing...!"
    m c1172g4 "Damn it..."
    show monika at std
    "This can't be real."
    "It can't be real."
    "I feel kind of numb and hot."
    l "I don't understand!"
    l "That should've worked!"
    l "You made her Club President and then had her open her Third Eye, right?"
    show monika at foc
    m "Yes!"
    show monika at std
    l "Did you... wait for her to power off and then extract her?"
    l "You had to have her use her Third Eye to break it while it was active...!"
    show monika at foc
    m "No!"
    m "I'm not stupid!"
    m "I get how this piece of crap work-"
    m "Guh! Nevermind..."
    show monika at std
    "Monika cries some more."
    "..."
    "I'm speechless."
    "I thought we had it, and..."
    "... now we have nothing. Not even have any clue why."
    "This must feel even worse for her."
    "Lord, what the hell do we do now..."
    menu:
        " "
        "Hey, I noticed something weird while you were gone.":
            pass
    menu:
        " "
        "Adam's file disappeared for a minute too.":
            pass
    show sayori c115213
    show monika at foc
    m c114114 "Oh, that?"
    m "Yeah, he got in near the end."
    m "But I just kicked him back out with admin.extract."
    show monika at std
    "..."
    show sayori at std(p51)
    show monika at std(p52)
    show libitina at std(p53)
    show natsuki at std(p55)
    show mc c114235 at foc(p54)
    mc "So... what took so long?"
    show mc at std
    show monika at xif(p52)
    m c124114 "I spent most of it trying to figure out how to make her admin."
    m "Just declaring her Club President didn't work."
    m "Turns out, it doesn't take effect until a new game is started..."
    m "So I had to mess around until I managed to fix the world enough to open the new game functionality."
    m "And new games reset the world state, so I ended up having to delete myself before starting a new game and restore myself after."
    m "DDLC has a priority system where when a new game starts, the character with the highest 'President Priority' is made President of the Literature Club."
    m "The game recognized me, so of course if I started a new game with me alive, it just made me President."
    show monika at std
    show libitina at xif(p53)
    b 2261111 "And then things were all weird and I thought I remembered starting the Literature Club..."
    b "Wait..."
    b "What was that API I noticed while I was active...?"
    show libitina at std
    show sayori c115212
    show mc c114111
    show monika at foc
    m c114112 "Huh...?"
    show monika at std
    show libitina at foc
    b "When I was at my peak, I looked around trying to find how to break out..." # it isn't done with admin.extract
    b "... I was delirious, but I think I saw a method that the normal part of me decided to keep in mind for once we got out."
    b "Was it viewport.set_strict_mode?"
    show libitina at std
    l "I don't know of that one, but is it what it sounds like?"
    show libitina at foc
    b "I have no idea."
    b "I'm just pretty sure I saw a function called that while I was crazy."
    show libitina at std
    l "Because that sounds like it could stop what Adam's trying to do!"
    show sayori c114212
    show natsuki c114114
    show monika at foc
    m c114211 "{i}Salvation...?{/i}"
    m "Maybe that wasn't for nothing."
    show monika c214211 at std
    call updateconsole("import viewport")
    call updateconsole("vp = viewport.get_viewport()")
    call updateconsole("print(vp.set_strict_mode.__doc__)", "Enables or disables strict data\nvalidity checks to prevent corruption\ninstead of relying on checksums.\nStrict mode has performance drawbacks.")
    m c212211 "No way! It's real!"
    call updateconsole("vp.set_strict_mode(True)", "Viewport strict data validity checks enabled.")
    m c122111 "It says viewport strict data validity checks enabled!"
    m "That should stop him from corrupting it!"
    call hideconsole
    $ consolehistory = []
    show sayori c222111 at hopfoc zorder 1
    show natsuki c112113
    show libitina 2211111
    show mc c113111
    s "Woohoo!"
    show sayori c224112 at std
    show natsuki c114114
    show libitina 2261114
    show mc c114235
    show monika c114212
    l "Break it, quick!"
    l "Before he notices and flips it back off and breaks it!"
    show monika c214212 at foc zorder 1
    call updateconsole("vp.set_strict_mode(ursula)", "ERROR: escaped character. Disabling\n viewport.Viewport.set_strict_mode.")
    m c122111 "Done!"
    call hideconsole
    $ consolehistory = []
    show sayori c222111
    show natsuki c112113
    show libitina 2211111
    show mc c113111
    m "Haha!"
    m "It's broken! There's no turning the protection off!"
    show monika at std
    "I let out a long sigh of relief."
    show sayori at foc zorder 2
    s c122111 "You did it!"
    s "You're a hero!"
    show sayori at std
    l "I think we turned the tables..."
    l "His plan to cut [persistent.playername] out of the picture should be impossible now."
    show natsuki at foc zorder 1
    n "I'll be sure to make those cupcakes as soon as we have time..."
    show natsuki at std
    show monika at foc zorder 3
    m "Good~!"
    show monika at std
    show sayori at foc zorder 4
    s c12x111 "Play the triumph music!"
    show sayori at std zorder 2
    show monika at foc
    m c222111 "Sure thing!"
    call updateconsole("play music t8")
    call hideconsole
    $ consolehistory = []
    play music t8
    show monika at std
    show sayori at foc zorder 4
    s c125112 "..."
    s c115113 "Oh wait..."
    s tc3112 "I forgot I can't hear it anymore..."
    s "Aww... I really wanna hear it!"
    show sayori at std zorder 2
    show monika at foc
    m c122212 "Sorry..."
    show monika at std
    show sayori at foc zorder 4
    s c111111 "Oh well..."
    s "I'll just hum it."
    show sayori at std
    "Sayori starts to hum what she remembers the tune to be."
    "I'm pretty sure she has it wrong, but whatever."
    menu:
        " "
        "What?!? - Adam":
            pass
    menu:
        " "
        "No, dammit! I forgot about that method! - Adam":
            pass
    show monika c121111
    show sayori at foc
    s c22x114 "So much for your plan!"
    s "Eat glitch text, you monster!"
    show sayori at std
    show mc c123111 at foc zorder 1
    mc "Guess our timing was pretty lucky."
    mc "We broke it like one minute before he checked."
    show mc at std
    menu:
        " "
        "Well... - Adam":
            pass
    menu:
        " "
        "... - Adam":
            pass
    menu:
        " "
        "I don't know how I can win anymore. - Adam":
            pass
    show sayori at thide
    hide sayori
    show renier u2223 at leftinfoc(p51) zorder 3
    r "Give it up, asshole!"
    r "We got you!"
    show renier at std
    show natsuki c225112 at foc zorder 2
    n "Surrender now and we'll make your death a little less painful!"
    show natsuki at std
    menu:
        " "
        "I never wanted to do any of this. - Adam":
            pass
    menu:
        " "
        "I made a horribly wrong choice and... - Adam":
            pass
    menu:
        " "
        "... there's no going back. - Adam":
            pass
    #TODO should Monika offer redemption here or not?
    menu:
        " "
        "I just wanted to get rid of [persistent.playername] to protect myself. - Adam":
            pass
    menu:
        " "
        "I wasn't going to go back to doing the horrible things I did! I swear! - Adam":
            pass
    # TODO Posing is not done from here on.
    show yuri at foc
    y c126116 "Your actions speak louder than your words!"
    y c12b116 "You claim to be sorry, but you continue to thwart us and force us to do things like Monika just had to do!"
    show yuri at std
    menu:
        " "
        "I didn't mean for that to happen... and I'm sorry. - Adam":
            pass
    menu:
        " "
        "I will meet you at the warehouse. - Adam":
            pass
    "..."
    #TODO more dialog, but it depends on whether the redemption dialog happened earlier.
    show sayori at foc
    s c115111 "At least we'll be able to get food once we're back in town."
    show sayori at std
    show mc at foc
    mc c214111 "Are we actually going there?"
    show mc at std
    l "We still have to find him to win..."
    show mc at foc
    mc "It's gotta be a trap."
    show mc at std
    show monika at foc
    m c223113 "We'll make it {i}our{/i} trap."
    m "He's the one who doesn't have a Third Eye, and almost all the admin powers that could help him in a confrontation are broken."
    m "If he confronts us, he's going down."
    m "Even if he has more cultists with him."
    show monika at std
    show albert at foc
    al 21111 "About that!"
    al 11111 "You should break the ability to restore memories to stop him from restoring the memories of more people who used to be his cultists."
    show albert at std
    show monika at foc
    m c124111 "Good idea..."
    m c224112 "I feel a little nervous breaking this one, but I guess it's safe with memory wiping also broken..."
    show monika at std
    show natsuki at foc # TODO pick who should say this and pose
    n "Wait, maybe you shouldn't?"
    n "If he's planning to get more cultists and ambush us, it was probably his first thought and he already restored their memories."
    n "Maybe you should keep the function around for our own use."
    show natsuki at std
    show monika at foc
    m c124111 "Even though memory wiping is broken...?"
    show monika at std
    show natsuki at foc
    n "Well... it's still possible we could need it in other ways."
    n "Isn't it possible the new game memory wipe doesn't depend on that API?"
    n "Or he might come up with some other weird way of doing it?"
    n "I feel like we should keep that power just incase."
    show natsuki at std
    m c114212 "Hm..."
    m "I think you're right."
    m "Of course, maybe you gave him time to restore their memories by delaying me..."
    show monika at std
    show natsuki at foc
    n "Uu.... well..."
    show natsuki at std
    show monika at foc
    m "No matter."
    m "Regardless, there's no way he hasn't done it by now if he's going to."
    m "I'll leave the API intact."
    show monika at std
    show albert at foc
    al 11131 "So we're probably going to have to through cultists after all..."
    show albert at std
    show natsuki at foc
    n c224111 "Everyone should pick up one of these before we leave."
    show natsuki at std
    "Natsuki picks up a gun from a fallen cultist."
    "I pick one up as well."
    show libitina at foc
    b 2261111 "With one of these, it'll be trivial for me to open my Third Eye in a pinch."
    show libitina at std
    show albert at foc
    al 11111 "Wonderful..."
    al "I feel safer than ever before."
    show albert at std
    show natsuki at foc
    n xc4111 "Me too..."
    n "... but she seems stable with it for now."
    show natsuki at std
    return
