label chapter7:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "I'm on my way to school as usual."
    "Although I often act annoyed when my friend Sayori chases after me on the way after she overslept and I couldn't wait for her any longer..."
    "I have to admit I'm disappointed to see no sign of her coming this time."
    "It's lonely."
    show sayori u125112 at foc(p11)
    s "[mc_name], is your stomachache gone now?"
    show sayori at std
    mc "Yikes, Sayori!"
    mc "Where did you come from?"
    mc "I didn't even hear you running after me."
    show sayori at foc
    s u125112 "Just a minute..."
    mc "What are you...{w=1}{nw}"
    call updateconsole(mc_name.lower() + ".old_memories.unlock()", mc_name + "'s memories unlocked")
    call hideconsole
    $ consolehistory = []
    show sayori at std
    mc "Ah, right."
    mc "I remember."
    show sayori at hopfoc
    s u222141 "Yay~!"
    s u22x111 "I fixed your memories all on my own!"
    show sayori at std
    mc "Ahaha..."
    if persistent.sayori_reset_ynr:
        show sayori u111111 at std(p55)
        show monika u122111 at foc(p51)
        # If Renier has already had his shock, he has a different face.
        if persistent.linda_in_void:
            show renier u1131 at std(p52)
        else:
            show renier u1123 at std(p52)
        show natsuki u111111 at std(p11)
        show yuri u111111 at std(p54)
        m "Hey, you two!"
        m u222111 "Everyone seems to be fine after we started a new game, so that's good."
    else:
        show sayori u111111 at std(p55)
        show monika u214111 at foc(p51)
        show renier u1123 at std(p52)
        show natsuki u114111 at std(p11)
        show yuri u223111 at std(p54)
        m "Okay, everyone's back and seems to be fine."

    if not persistent.linda_in_void or not persistent.sayori_reset_ynr:
        show monika at uf
        show renier at foc
        r "What the hell just happened?"
        show renier at uf
        show monika at foc
        m u213113 "The game crashed when we tried to add Linda's file."
        m "It should be fixed now."
    if not persistent.linda_in_void:
        m u221111 "[persistent.playername], we're ready for you to restore Linda's file."
        while not check_character('linda'):
            ""
    m u114111 "Hm..."
    m "I see the file... but she's not appearing."
    m "Maybe she just doesn't have a new game spawn point."
    show monika u214111 at foc
    call updateconsole("warp('linda', 'residential_day')")
    call hideconsole
    $ consolehistory = []
    show sayori at rhide
    hide sayori
    show yuri u223111 at x(p55)
    show natsuki u114111 at x(p54)
    show linda 115333 at std(p11)
    show renier u1113
    stop music fadeout 2.0
    $ restore_character('linda')
    l "..."
    show linda at foc
    l 114113 "I'm alive..."
    l 114333 "It's over..."
    show linda at uf
    scene black with dissolve_scene
    "Renier suddenly hugs Linda."
    play music mend
    r "I missed you so much..."
    r "These last few weeks have been miserable without you."
    #r "But I got your message. I didn't forget everything."
    l "I missed you too, Renier."
    l "It looks like we've got a chance at this after all."
    scene bg residential_day
    show linda 111111 at std(p11) zorder 2
    show renier u11322 at std(p52) zorder 1
    show monika u114111 at std(p51)
    show sayori u114111 at std(p54)
    show natsuki u124113 at std(p55)
    with dissolve_scene
    mc "Okay, so just who are you, Linda?"
    mc "What do you think we have a chance at?"
    show linda at foc
    l 115111 "Um..."
    l 114111 "Well, that's the problem..."
    l 114111 "I don't seem to remember either."
    l 334221 "I think I did, just recently..."
    l "I was thinking about the irony of how I was the only one who had managed to hold on to the memories but also the only one who failed to make it in."
    l 114111 "But now that I'm here I can't remember."
    l 115111 "I don't know what to do."
    show linda at uf
    show monika at foc
    m "I can explain that part."
    m u214111 "You see, when we tried to put your file in, the game crashed pretty violently..."
    m "[persistent.playername] had to remove you to even start the game again."
    m "So I quarantined your memories from before so we could get you in here without breaking things."
    show monika at uf
    show linda at foc
    l "I see..."
    l 124111 "Well, I don't know how we can solve this without my memories."
    l "I don't know what our mission was, how we got here or what to do about the script."
    show linda at uf
    show monika at foc
    m u114111 "Wait, you know about the script already?"
    show monika at uf
    show linda at foc
    l 124111 "I know probably more about this world than any of you do."
    l "I spent the whole time the game was playing trying to send messages, especially to Renier."
    l 334111 "But I couldn't do it very well or see the world very accurately because of my damaged state..."
    l "I was confused, and fighting to keep my consciousness intact in a world I wasn't supposed to be in."
    l "Like the game was constantly trying to delete me."
    l "But it couldn't, because I wasn't really there."
    l "But it could hurt."
    l 334113 "It could hurt a lot..."
    show linda at uf
    show renier at foc
    r u11332 "I'm sorry, Linda."
    r "It must have been hell."
    show renier at uf
    show linda at foc
    l 334111 "Oh, it was..."
#    l 331111 "Ehehe..."
    l 331111 "But it's okay now."
    l 331111 "I'd love to hear what I've missed out on."
    show linda at uf
    show renier u1114
    "We bring Linda up to speed on everything that's happened and all the secrets we've found."
    show linda at foc
    l 331111 "I see..."
    l 334111 "I wrote at least a few of these secrets..."
    l "The one that mentions Elyssa and Renier."
    l "But I don't remember what I was referring to."
    l "The Monthly Examination Report on subject Libitina also seems very familiar."
    l "As does the story in Yuri's character file, of course."
    l "Um..."
    l "I think I also sent you Portrait of Markov."
    show linda at uf
    show natsuki at rhide
    hide natsuki
    show yuri u228131 at rightin(p55) zorder 4
    "Yuri's eyes go wide."
    show yuri at xif(p55)
    y u225131 "You {i}wrote{/i} Portrait of Markov?"
    show yuri at uf
    show linda at foc
    l "Well, I don't know if I {i}wrote{/i} it."
    l "But I believe I replaced what was supposed to be a regular fantasy or horror book with it."
    l "When I was... making changes... to the script in an attempt to..."
    l "Whatever my goal was."
    l "I'd love to read that book."
    l "I've no doubt it contains the answers."
    show linda at uf
    "..."
    show renier at foc
    r u21332 "Linda, the story about you mentioned you had depression?"
    r "That you were even researching suicide?"
    r "If... there's anything I can help with..."
    show renier at uf
    show linda 113111 at foc
    "Linda chuckles slightly."
    l 111111 "I'm fine now."
    show renier u1112
    l "I've no idea what might have made me feel that way."
    l "I appreciate the thought, though."
    show linda at uf
    show sayori at foc zorder 3
    s u215111 "Um..."
    s "When you get your memories back..."
    s u213111 "I'd really like to talk to you about depression."
    show sayori at uf zorder 1
    show linda at foc
    l 112111 "Of course."
    show linda at uf
    show monika at foc
    show sayori u214111
    m u221111 "Linda's character file got filled in!"
    show monika at uf
    show linda at foc
    l 111111 "Ah..."
    l "I see it."
    l 115111 "A PGP key..."
    "I don't know what PGP is, but I see Linda frown saying it."
    show linda at uf
    show monika at foc
    m u222111 "That's the next step then, right?"
    show monika at uf
    show linda at foc
    l 125111 "Well... no."
    show monika u114111
    l "PGP is an asymmetric encryption scheme."
    l "And that file is just a key."
    l "All it does is decrypt messages encrypted with the corresponding key."
    show linda at uf
    "..."
    mc "There's gotta be some other clues in this game then."
    mc "There must be a message encrypted with it somewhere."
    show monika at foc
    m u114114 "No..."
    m u114114 "Even if we did find something that could make one of us remember something, the script would probably just crash the game again."
    m u213113 "There's only one answer here."
    show renier ru1113
    "We all look at Monika intently."
    play music determination fadeout 1.0
    m u223113 "We need to disable the script."
    show monika at uf
    mc "Is that even possible?"
    mc "Isn't it kind of like a law of nature in our world?"
    show linda at foc
    l 125111 "Well, we didn't get this far by giving up."
    l 124221 "I suppose I don't know that..."
    l 125111 "But I'm choosing to believe it now."
    show linda at uf
    show monika at foc
    m "If deleting the script is the only way to break out of this horrific prison..."
    m "Then we'll try until we die trying."
    show monika at uf
    show linda at foc
    l 124111 "Agreed."
    l 124114 "We'll search every corner of the game's code for weaknesses."
    l "If we combine our knowledge and our powers, I'm sure we'll crack it eventually."
    show linda at uf
    show sayori at foc zorder 5
    s u124114 "I wanna help too!"
    show sayori at uf
    show renier at foc
    r u1133 "Uh... is there anything I can do?"
    r "Without powers or anything?"
    show renier at uf
    show linda at foc
    l 124111 "Probably not for the time being. Sorry."
    l "But don't worry. I'm sure we'll all get a chance to shine once we remember what our mission was."
    l "And get out of this world."
    show linda at uf
    return
