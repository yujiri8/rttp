label chapter21:
    scene hospital_hall
    show dark_overlay:
        alpha 0.95
    with wipeleft
    pause 0.4
    scene hospital_room_night
    show dark_overlay:
        alpha 0.95
    with wipeleft
    "We head over to Libitina's room."
    hide dark_overlay
    "I flip the lights."
    show monika u114112 at foc(p21)
    m "She looks fine, externally..."
    show monika at std
    show linda 334113 at foc(p22)
    l "She vomitied quite a lot of blood."
    l "She's definitely not fine on the inside..."
    show linda at std
    show monika at foc
    m u114112 "Yeah..."
    m u124111 "Hold on, we might have an easy fix for this."
    m "[persistent.playername], have you tried deleting and restoring Libitina?"
    show monika at std
    # The top option ideally should not appear if you haven't deleted her. But I'm not sure
    # how to achieve that, because I don't think I can reliably detect whether she was deleted in the past.
    menu:
        " "
        "Yeah. It didn't seem to do anything.":
            $ persistent.player_deleted_libitina = True
            show monika at foc
            m u114121 "Huh..."
            m u114111 "But you were able to restore everyone else?"
            m "So it's not that you can't affect the world."
            m "Something about what Libitina did must have broken Markov's access control."
            m "I wonder if, since Libitina was so valuable to him..."
            m "... he gave her some kind of special-case delete protection."
            m u114112 "She must be in terrible condition though..."
            m "I wish I could heal her."
        "No, I was too worried it'd mess her up.":
            $ persistent.player_deleted_libitina = False
            show monika at foc
            m u124121 "Ah..."
            m u114112 "Well, she must be in terrible condition."
            m "We really should heal her if we can."
            m u114111 "But I see your concern."
            m "I'll trust your judgement."
    show monika at std
    menu:
        " "
        "Try character.reset().":
            pass
    show monika at foc
    m u114111 "character.reset...?"
    show monika at std
    menu:
        " "
        "Markov used it to prevent Libitina from dying, and it also helped us get Linda back after you broke everything in your frenzy.":
            pass
    show monika at foc
    m "Alright..."
    show monika u214111
    call updateconsole("libitina.reset()", "0")
    call hideconsole
    $ consolehistory = []
    m u114111 "Success return code..."
    m "I don't know how to know if it did anything though."
    show monika at std
    show linda at foc
    l 334111 "I guess we'll find out when she wakes up."
    show linda at std
    show monika at foc
    m "Yeah..."
    m u124111 "Also, what about the content of Libitina's file?"
    m "... Huh."
    m "It's..."
    m "... a picture of a... portal, of some kind."
    m "I don't know what to make of it yet."
    show monika at std
    menu:
        " "
        "Yeah, you should see Markov's file.":
            pass
    menu:
        " "
        "I took the liberty of base64-decoding it and... you gotta read it.":
            pass
    show monika at foc
    m "Okay, just put the decoded text in a file."
    m "I can't easily do that step myself."
    show monika at std
    # changes pose
    if persistent.player_deleted_libitina:
        show linda 124111 at foc
    else:
        show linda 334111 at foc
    l "There's a Python standard library function for base64 decoding, you know."
    show linda at std
    show monika at foc
    m u114111 "There is?"
    show monika at std
    show linda at foc
    "Linda" "import base64\nbase64.b64decode()"
    show linda at std
    show monika at foc
    m u112111 "Oh, neat!"
    m "Okay..."
    show monika u114111
    "Monika gets a pen and paper and writes it down."
    show monika at std
    call showpoem(poem_markov_chr, music=False)
    mc "What... the..."
    "The beginning is the quote from the \"Have a nice weekend!\" file..."
    mc "Linda, did we ever ask you what was with that 'Have a nice weekend' file?"
    show linda at foc
    l 124111 "No..."
    l "I don't remember anything about that one."
    l "I'm not sure how it got there."
    show linda at std
    show renier ru2113 at foc(p55)
    r "So did Markov write this?"
    r "It sounds believable."
    show renier at std
    mc "Does he believe in gods?"
    show yuri u125111 at foc(p51)
    y "He may just be using it metaphorically..."
    show yuri at std
    show natsuki u223111 at foc(p53)
    n "Okay, now I really want to know what the bittersweet aftertaste of the past is!"
    show natsuki at std
    show monika at foc
    m u224111 "I bet it's the time before he started this."
    show monika at std
    show natsuki u124111
    "I read over the message again."
    mc "I guess it could be..."
label libitina_wakes_up:
    "Libitina stirs, as if beginning to wake up."
    "The rest of us fall silent."
    "She does open her eyes."
    show yuri at foc
    y u225118 "Libitina!"
    y "Are you okay?"
    show yuri at std
    b "..."
    "..."
    "Libitina sits up."
    show libitina 1161224 at foc(p11) zorder 10 # No one should ever go on top of her for this scene.
    show monika at thide
    hide monika
    show renier ru1131
    show natsuki u114114 at x(p52)
    b "... What... happened?"
    show libitina at std
    "Her speech is barely audible."
    mc "You saved us all."
    mc "After you passed out, we got you to a hospital."
    show libitina at foc
    b 2261332t "Thank you all so, so much..."
    b 2251332t "I've lived in that hellhole for as long as I can remember."
    show linda 114113
    b 2261332t "I don't know if I ever knew anything else."
    b "I thought I'd never feel whole."
    b 2261224 "..."
    b "I must have had a different life before, though..."
    b "... cause I remember feeling this way."
    b "Feeling... not broken."
    b "I remember knowing what it was like to love someone..."
    b "... and to have any comfort in life other than the pleasures of the Eye."
    b 2261114 "They distort you..."
    b "When violence is your only friend..."
    b "... for so long..."
    b "... you learn to like it aesthetically."
    b 2271223 "Fuck, the worst part was how they gave me dreams about escaping so many damn times!"
    show libitina 2261111 at std
    show yuri u2241y7 at foc
    "Yuri sheds a few tears."
    y "I know this pain..."
    y "They did that to me too..."
    show yuri at x(p52)
    show natsuki at x(p51)
    "Yuri gives Libitina a brief hug."
    show yuri u224112 at xis(p52)
    show libitina at foc
    b 2161111 "Elyssa..."
    "I guess she recognizes Yuri...?"
    b "Do you remember..."
    b "When you tried to kill me?"
    show libitina at std
    show yuri at foc zorder 1
    y u226231 "Yes!"
    y u225231 "Do you understand now?"
    show yuri at std
    show libitina at foc
    b 2251222 "I understood then."
    b "I wanted so badly to let you kill me."
    b "But I knew Markov would reset me."
    b "It wouldn't have been the first time I'd tried to kill myself."
    b "..."
    b 2251112 "I wanted to talk to you about it..."
    b "But they wouldn't let me."
    b "And then I had to listen to you die..."
    show renier ru1133
    b "I heard your screams through the wall."
    b "God, that was a nightmare."
    b "I tried to convince myself it was for a few days."
    b "You were the only person who ever tried to help me, for any reason other than to keep exploiting me."
    b 2261222 "I... missed you, Elyssa..."
    show libitina at std
    show yuri at foc
    y "..."
    y u224117 "If only I'd known..."
    y "I thought you didn't want my help..."
    y "It made me feel even worse..."
    y "And I started vomiting blood when they dragged me back to my cell."
    show yuri at std
    show libitina at foc
    b 2272114t "Oh no, I didn't mean to infect you with that!"
    b "I'm so sorry Elyssa--"
    show libitina at std
    show linda at foc
    l 119111 "Wait, do you know something about that?!?"
    show linda at std
    show libitina at foc
    b 2262114t "Not- not really..."
    b "It just happens sometimes when I distort things."
    show libitina at std
    show linda 114112
    show yuri at foc
    y u125112 "It wasn't your fault..."
    y u125114 "Markov is the one responsible."
    show yuri at std
    show libitina at foc
    b "Thanks..."
    b 2262111 "But..."
    show yuri u125118
    b "Why are Renier and the other examiner here?"
    "Libitina points to Linda."
    "Apparently she never found out her name."
    b "Aren't they... the enemy?"
    show libitina at std
    "Yikes."
    "I'm surprised at how calm she is if she recognizes them as the cultists who experimented on her."
    show linda at foc zorder 1
    l 114113 "I was being kept in the dark!"
    l "I didn't know what was going on there!"
    show linda at std zorder 0
    show renier at foc zorder 1
    r ru2133 "And I'm different now."
    r "They convinced me it was for the greater good..."
    r "... but when I had my first experience with the Third Eye, I stopped believing it."
    r "Linda and I tried to sabotage them."
    show renier ru1113 at std zorder 0
    show libitina at foc
    b 2161441 "Wait--"
    b "Linda as in..."
    b 2171444 "Linda Watson?!"
    b "The... the woman I killed?"
    b 2172444 "I- Ah-"
    show libitina at std
    show linda at foc zorder 1
    l 114111 "Don't worry, that's all in the past."
    l 113111 "I think most of us have pretty much lost the ability to be surprised by finding out we've murdered each other."
    show linda 111111 at std zorder 0
    show libitina at foc
    b 2162114 "Really...?"
    show libitina at std
    show renier at x(p54)
    show linda at thide
    hide linda
    show natsuki u114111
    show yuri u124111
    show renier ru1112
    show sayori t1111 at rightinfoc(p55)
    s "Yeah..."
    s "It's happened to all of us plenty of times now."
    s "But hey, at least none of our deaths have ever been permanent!"
    show sayori at xis(p55)
    mc "Don't worry about it, Libitina."
    mc "I think you more than made up for it saving us all back there."
    show libitina at foc
    b 4261111 "Well, you're welcome."
    b "You saved me."
    show libitina at std
    show natsuki at foc zorder 2
    n u124111 "I still feel like we should talk about your justification for murdering Linda."
    n "Do you actually think that, or were you just being affected by the script or whatever?"
    show natsuki at std
    show yuri u113111
    show sayori u114112
    show renier ru1111
    show libitina at foc
    b 1262111 "I mean..."
    b "It kind of makes sense..."
    show renier ru1123
    show yuri u114118
    b "I know it seems wrong, but..."
    show libitina at std
    show natsuki at foc
    n u223112 "What the shit!"
    n "That's literal murder!"
    n "What makes you any different from any other monstrous killer?!?"
    show natsuki at std
    show libitina at foc
    b 1262111 "I..."
    b "I didn't think I would cause any suffering..."
    b "That's the difference..."
    show libitina at std
    show natsuki at foc
    n "You're lying to yourself!"
    n "You think you'd still believe that if I tried to kill {i}you{/i}?"
    show natsuki at std
    show libitina at foc
    b 2252222 "It might be a favor to me..."
    b 2262222 "... but if that weren't the case..."
    b "... then yeah, I might not want to die before you killed me, but once I'm dead, how can I be a victim?"
    show libitina at std
    show natsuki at foc
    n "You just admitted that it could be a favor!"
    n "If that's true, then it could just as well be the opposite!"
    n "You just proved you already know on the inside that what you did was evil!"
    show natsuki at std
    show libitina at foc
    b 1262114 "No..."
    b "I just meant I might see it as one beforehand..."
    show libitina at std
    show natsuki at foc
    n "And you think that suddenly stops mattering after you're dead?"
    show natsuki at std
    show libitina at foc
    b 2261224 "I'm sorry, Maria..."
    b "But I won't claim to believe something I don't."
    show libitina at std
    show natsuki at foc
    n "I understand."
    n "You're a horrible person."
    n "We're only working with you out of necessity, okay?"
    show natsuki at std
    "Libitina nods."
    show sayori at foc
    s u213111 "I'm sure you'll change your perspective soon enough, Libitina."
    s "You've never appreciated being alive, have you?"
    show sayori at std
    show libitina at foc
    b "Well, I think I did during that first virtual reality experience..."
    b "I really don't have an excuse in your eyes."
    b "I feel bad that you have to think I'm a horrible person right after you rescued me."
    b "I hope it doesn't stay this way."
    "..."
    b 2261114 "So..."
    b "... how did you all get here?"
    show libitina at std
    scene black with close_eyes
    scene hospital_room_night
    show yuri u121111 at std(p52)
    show natsuki u111111 at std(p51)
    show renier ru1112 at std(p54)
    show sayori u111111 at std(p55)
    show libitina 2261111 at std(p53) zorder 10
    with open_eyes
    "We recount the rest of our story."
    "The mood improves as we discuss our recent triumph."
    show libitina at foc
    b "..."
    b "Wow..."
    b 2261111 "I'm sorry for what you've all been through."
    b "You were very brave to come back to the facility."
    b "And thanks again for saving me."
    show libitina at std
    show natsuki at foc
    show renier ru1114
    n u222111 "I see how that went as an absolute win!"
    show natsuki at std
    show sayori at foc
    s u21x111 "Sure did go better than we could've hoped!"
    s u213111 "Also..."
    s "Libitina, did Markov ever tell you..."
    s "... that he's your {i}father{/i}?!?"
    show sayori at std
    show libitina at foc
    b 2161111 "... What do you mean...?"
    show libitina at std
    show sayori at thide
    hide sayori
    show linda at rightinfoc(p55)
    l 124111 "Well, technically we don't know that for certain."
    l "Just that you share his last name."
    show linda at xis(p55)
    show libitina at foc
    b "Whoa..."
    b "No, he didn't."
    b "But now that you mention it..."
    b "I think that affected him."
    b "I think I did have it better than the other subjects, at least for how much more interested he was in studying me."
    b "He was my examiner more often than not..."
    b "But never when it was time to do something horrible to me."
    b "Like it bothered him to see it, even if he still knew he was making it happen."
    b 4261113 "Not like that makes him one bit better, though."
    show libitina at std
    show renier at thide
    hide renier
    show linda at std(p54)
    show monika at rightinfoc(p55)
    m u124111 "So, Libitina..."
    m "Maybe you can help us understand Markov's character file."
    show monika at xis(p55)
    show libitina 4261111 at foc
    "Libitina reads over the message."
    b "He thinks I'm going to \"free us all\"...?"
    b "\"...Full potent\"-"
    b 3371113 "To hell with him!"
    b "I'll free everyone from {i}him{/i}!"
    show libitina 3361113 at std
    "Libitina throws the paper on the ground."
    "Although, being paper, it flutters rather gracefully instead of making a thud."
    mc "I think we all share your feelings on that..."
    show libitina 2161111 zorder 0
    show yuri at foc zorder 1
    y u114111 "What about Albert's file?"
    y "Did he get one?"
    show yuri at std
    show monika at foc
    m u221111 "Sure thing..."
    "Monika takes a moment to read in and transcribe the file."
    show monika u124111 at std
    call showpoem(poem_albert_chr, music=False)
    show natsuki u214111
    show yuri at foc
    y u124111 "Wow..."
    y "It's curious..."
    y "This is exactly what I talked about with Markov when he drew the conclusion that I had a Third Eye."
    y "Does this kind of thought have some relationship to it?"
    show yuri at std
    show natsuki at foc zorder 1
    n "I always thought it was weird that the Third Eye and presidency didn't seem to have anything to do with each other..."
    n "And this kind of thought is basically touching on game awareness."
    n "It'd make a lot of sense if they turned out to be related somehow after all."
    show natsuki at std
    show yuri at foc zorder 2
    y "I agree..."
    y "We should find out if Albert has one."
    show yuri at std
label markov_returns:
    show linda at foc zorder 1
    l 123111 "Oh, hey, I just got an idea."
    l "Monika, now that you have admin powers within this world..."
    l "You could probably read Markov's memories the way I did."
    l 121111 "That's gotta be our best lead."
    show linda at std
    show monika at foc zorder 2
    m u122111 "Sounds good..."
    m "How do I do that?"
    show monika at std zorder 0
    show linda at foc
    l "You need to retrieve a reference to his character object - without restoring him - and then iterate over .memories, using a generator to stop after each block and return control..."
    show linda at std
    show monika at foc zorder 2
    m u222131 "Okay... I got it."
    m u222111 "Here we go..."
    show monika at std
    call updateconsole("import graveyard")
    call updateconsole("markov = graveyard.get_character('markov')")
    "..."
    "..."
    "Seconds pass."
    "Monika is still as a statue."
    "More seconds pass."
    show natsuki u224114
    show yuri u123118
    "A lot more seconds pass."
    "Monika doesn't move at all."
    show linda at foc zorder 3
    l 334113 "Crap, she's frozen, isn't she."
    show linda at std
    show natsuki u223112
    show yuri u125118
    mc "Are you serious?!?"
    mc "That could happen and you didn't tell us?!?"
    show linda at foc
    l 119111 "No!"
    l "I had no way to see this coming!"
    l "There's no reason this should've frozen her!"
    show linda at std
    mc "Well what are we gonna do about it when no one else has admin powers?"
    show linda at foc
    l 114113b "I don't know, okay?"
    l "Just give us time."
    l 114223b "Eventually, Monika will either find a way to unfreeze herself, or I'll think of something."
    show linda at std
    show natsuki at foc zorder 3
    n "But it doesn't even matter what you think of if only Monika can do it!"
    show natsuki at std
    $ restore_character('markov')
    call screen dialog("{i}There{/i} we go.", ok_action=Return())
    call screen dialog("Thanks for the help, Clare.", ok_action=Return())
    call screen dialog("Christ, that hurt.", ok_action=Return())
    call screen dialog("I get how it feels now.", ok_action=Return())
    call screen dialog("My apologies for doing that to you and Abbey and Linda for so long.", ok_action=Return())
    call screen dialog("Actually, my condolences, because it wasn't actually my doing on any of you.", ok_action=Return())
    call screen dialog("But I still have a mission.", ok_action=Return())
    call screen dialog("And you, [persistent.playername], are not able to stop me.", ok_action=Return())
    $ persistent.autoload = "after_markov_returns"
    $ renpy.quit()
