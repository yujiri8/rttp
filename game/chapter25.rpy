label chapter25:
    "..."
    scene facility_ruin with wipeleft_scene
    play music yawa
    "..."
    show yuri c115111 at foc(p11)
    y "So what was this place?" # Maybe Albert could get these lines if Yuri gets the admin.inflict_epiphany dialogue.
    y "It couldn't have been his facility."
    show yuri at std
    l "Maybe it was being built for something unrelated, and he commandeered it later?"
    l "Maybe it was going to be some kind of research facility for something else."
    l "Or maybe some other top-secret, horrifying thing..."
    l "Who knows."
    show yuri at std(p22)
    show renier u1113 at foc(p21)
    r "It must've been easy to take it over when he can basically control people's minds with scripts and memory wiping."
    show renier at std
    scene facility_ruin with wipeleft_scene
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
    show mc at foc
    mc "I guess so..."
    scene facility_ruin with wipeleft_scene
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
    show natsuki c124111 at foc(p55)
    n "That makes two of us."
    n "I'm really looking forward to those cupcakes I promised..."
    show natsuki at std
    show sayori at xif(p54) zorder 1
    s c123111 "Me too!"
    s c111321 "Ehehe..."
    "..."
    s c113111 "How long was he expecting his troops to stand here?"
    s "They must've been hungry too."
    show yuri at xif(p53)
    y c114111 "He would've left them standing guard until nightfall."
    y "He viewed their suffering as a positive good."
    y "He recognized them as evil for following his orders, even though he didn't see himself as evil for giving them."
    y "I still can't believe that he could convince himself his actions were justified..."
    show yuri at std
    if persistent.player_support_experiment:
        show mc at std(p61)
        show albert at std(p62)
        show yuri at std(p63)
        show sayori at std(p64)
        show natsuki at std(p65)
        show renier ru1113 at rightinfoc(p66)
        r "Well, like you taught me way back when..."
        r "People can convince themselves of whatever they want."
        show renier at std
    else:
        l "Well, like I learned in my time in the cult..."
        l "There's almost no limit to what we can convince ourselves of if we really want to think it."
    show yuri at foc
    y c113112 "Hmm..."
    show yuri at std
    "..."
    show albert at foc zorder 1
    al 12111 "So, Sayori and [mc_name]..."
    al "How did you two and Monika escape?"
    show albert at std
    show sayori c115123
    show mc c114115
    "Sayori and [mc_name]'s expressions darken."
    show yuri c114118
    show natsuki c114114
    show renier ru1133
    show albert at foc
    al 21112 "If... you don't mind..."
    show albert at std
    show mc at foc zorder 2
    mc "Well..."
    mc "It started with me."
    mc "One day, they were doing a test on violence against animals."
    mc "They gave me a knife and made me kill a mouse."
    mc "But the guard doing the test got careless, and I killed him too."
    mc "I was lucky, cause Sayori and Monika were nearby."
    mc "I used my Third Eye to open theirs."
    mc "And they helped me."
    show mc at std
    if not persistent.player_support_experiment:
        show mc at std(p61)
        show albert at std(p62)
        show yuri at std(p63)
        show sayori at std(p64)
        show natsuki at std(p65)
        show renier ru1113 at rightinfoc(p66)
    else:
        show renier ru1113 at foc
    r "Wait..."
    r "You used your Third Eye to open theirs?"
    r "You could do that?"
    show renier at xis(p66)
    show mc at foc
    mc "Apparently."
    mc "My recollection might not be the clearest, but that was what it looked like."
    show mc at std
    show renier at foc
    r "Everyone's Third Eye distorted reality a little differently."
    r "But I don't remember seeing anyone else with a power like that."
    show renier at std
    show sayori at foc
    s c115113  "We combined our Third Eye powers to overcome the guards."
    s "They couldn't shoot us."
    s "Well, eventually one of them did..."
    s "But I think it actually turned out to be what saved us."
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
    l "I'm surprised you three were able to see each other as allies at all while under that kind of influence."
    l "I've never seen that before."
    show renier at foc
    r "I don't think he did any of the tests with two subjects at once after... I brought you into things."
    r "I remember a few from before then."
    r "The ones with a control rating of more than 5 or so were usually able to cooperate to some extent, if they had a common objective."
    r "It was more dangerous than one subject at once, though, so he stopped doing it after it didn't yield any useful results."
    r "But it might be [mc_name]'s Third Eye also has a sort of rallying effect on others he opens with it..."
    show renier at std
    l "That would be interesting..."
    l "... and maybe useful at some point."
    show renier at foc
    r "What were Monika's unique powers?"
    r "I don't think anyone ever found out mine... and I don't remember finding anything unusual with Yuri." # TODO it would be good to mention Yuri's unique power here. She could do something memory-related or something.
    show renier at std
    show sayori at foc
    s c213111 "I think Monika's was a sort of time bubble effect."
    s "When she distorted things, time only seemed to pass in the area around her, and anything far away pretty much stopped moving."
    s "I think that's why Adam couldn't do anything about our escape."
    s "To him, it all happened in a second, and we were gone before he even heard about it."
    show sayori at std
    show albert at foc zorder 2
    al "Wow..."
    al "Well, thanks for sharing."
    show albert at std
    scene facility_ruin with wipeleft_scene
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
    l "You had to have her use her Third Eye to break out while it was active...!"
    show monika at foc
    m "No!"
    m "I'm not stupid!"
    m "I get how this piece of crap work-"
    m "Guh! Nevermind..."
    show monika at std
    show libitina 2262332
    "Monika cries some more."
    "..."
    "I'm speechless."
    "I thought we had it, and..."
    "... now we have nothing. Not even any clue why."
    "This must feel even worse for her."
    "Lord, what the hell do we do now..."
    menu:
        " "
        "Hey, I noticed something weird while you were gone.":
            pass
    show libitina 2262222
    menu:
        " "
        "Adam's file disappeared for a minute too.":
            pass
    show sayori c115213
    show monika at foc
    m c114114 "Oh, that?"
    m "Yeah, he got in near the end."
    m "But I just kicked him back out with admin.extract_character."
    show monika at std
    "..."
    show sayori at std(p51)
    show monika at std(p52)
    show libitina at std(p53)
    show natsuki at std(p55)
    show mc c114235 at foc(p54)
    mc "So, if everything seemed to go as planned... what took so long?"
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
    b "And then things were all weird and I thought I remembered starting the Literature Club..."
    b 2261111 "Wait... that reminds me..."
    b "What was that API I noticed while I was active...?"
    show libitina at std
    show sayori c115212
    show mc c114111
    show monika at foc
    m c114112 "Huh...?"
    show monika at std
    show libitina at foc
    b "When I was at my peak, I looked around trying to find how to break out..." # it isn't done with admin.extract_character
    b "... I was delirious, but I think I saw a method that the normal part of me wanted to keep in mind for once we got out."
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
    call updateconsole("vp.set_strict_mode(ursula)", "ERROR: escaped character.\nDisabling viewport.Viewport.set_strict_mode.")
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
    stop music fadeout 5.0
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
    show libitina 2261113
    show mc c124113
    show monika c124113
    show natsuki c115112
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
    if persistent.player_advocate_mercy[1]:
        call monika_offer_redemption
    else:
        menu:
            " "
            "I just wanted to get rid of [persistent.playername] to protect myself. - Adam":
                pass
        menu:
            " "
            "I wasn't going to go back to doing the horrible things I did! I swear! - Adam":
                pass
    show renier at std(p62)
    show monika at std(p63)
    show libitina at std(p64)
    show mc at std(p65)
    show natsuki at std(p66)
    show yuri at leftinfoc(p61) zorder 4
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
    show yuri c114111
    show renier u2113
    show monika c114111
    show libitina 2261111
    show mc c124111
    show natsuki c124111
    "..."
    if persistent.player_advocate_mercy[1]:
        show natsuki at foc
        n "Did you actually fool him?"
        n "Does he really think we plan to forgive him?"
        show natsuki at std
        show monika at foc
        m c114222 "..."
        show monika at std
        l "Not if he checks the history and sees that you said that."
        show natsuki at foc
        n c124231 "Uu..."
        n "Well..."
        n c124211 "He can read your thoughts anyway..."
        show natsuki at std
        l "Yeah..."
        l "Oh well."
        l "Maybe if we talk about something else to flush the history and take our minds off it?"
    else:
        mc "So I guess he thinks we think he thinks he's tricking us?"
    # TODO posing not done after this.
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
    show natsuki at foc
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
    l "Hey um, Monika?"
    l "Could you switch someone else to be POV?"
    l "Since Adam can see the POV character's thoughts, I think it's best if it's not me."
    l "Since I know a lot about admin stuff, I'm more likely to get a useful idea, and be unable to not divulge the plan."
    if mc_dislike_player() < 2:
        show mc at foc
        mc "I guess I wouldn't mind having [persistent.playername] back."
        mc "I kind of miss feeling important, like I'm the eyes and ears of our guardian angel."
        show mc at std
        show monika at foc
        m "Great!"
        $ temp = mc_name.lower()
        call updateconsole("vp.pov_character = [temp]", "POV changed to [mc_name]")
    else:
        show mc at foc
        mc "Okay, how do I say this..."
        mc "[persistent.playername], I don't want you back in my head."
        mc "I don't consider you a friend."
        show mc at std
        l "Well, there's a real downside to [persistent.player_subj_pronoun] being in mine..."
        show sayori at foc
        s "I could be POV."
        show sayori at std
        l "But you also have admin experience."
        l "That kinda defeats the point."
        show albert at foc
        al "What about me?"
        al "I wouldn't mind."
        show albert at std
        show monika at foc
        m "It can't be you..."
        m "Your pov flag isn't set. Adam broke it before I could set it, so it won't let you be POV."
        show monika at std
        show renier at foc
        r "How about me?"
        r "I'll do it."
        show renier at std
        show monika at foc
        m "Sounds good."
        show monika at std
        call updateconsole("vp.pov_character = renier", "POV changed to Renier")
    return


label monika_offer_redemption:
    show monika at foc zorder 4
    m c227113 "Adam, there's such a thing as redemption!"
    m "I found it!"
    m c114111 "And I truly think you can too."
    show monika at std
    "Wait..."
    "... Oh. She's just trying to trick him into cooperating. I see."
    menu:
        " "
        "But Libitina will kill me... - Adam":
            pass
    show monika at foc
    m "If you die to fix your sins, you'll have done the most heroic thing you can do."
    show monika at std
    "..."
    menu:
        " "
        "Redemption is a lot more appealing when I can survive. - Adam":
            pass
    menu:
        " "
        "Throwing away everything for my conscience? - Adam":
            pass
    menu:
        " "
        "That's something only a hero does. - Adam":
            pass
    menu:
        " "
        "I'm a villain. - Adam":
            pass
    m c217115 "Dammit, you bastard!"
    m "I didn't act like that when I had the chance to restore my victims and change my ways!"
    #m "Maybe we don't have so much in common after all!"
    menu:
        " "
        "You weren't facing a certainty of torture and death. - Adam":
            pass
    menu:
        " "
        "And you didn't even really have a choice. - Adam":
            pass
    menu:
        " "
        "If you had had the option to wipe [persistent.playername]'s memories and go back to being with [persistent.player_obj_pronoun] in the space room, would it have been so easy to resist? - Adam":
            pass
    m c114113 "..."
    menu:
        " "
        "I wasn't even going to go back to doing all the horrible things I did. - Adam":
            pass
    menu:
        " "
        "I just wanted to get rid of [persistent.playername] to protect myself. - Adam":
            pass
    return
