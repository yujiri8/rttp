label chapter13:
    $ persistent.autoload = None
    $ mc_name = persistent.mc_name
    $ gtext = glitchtext(8)
    $ autosave()
    play music m1
    if check_character('sayori'):
        $ s_name = "Sayori"
        s "..."
    else:
        s "Agh[gtext]!"
        s "It hurts!"
        $ restore_character('sayori')
        call updateconsole("restore_character('sayori')", "Sayori restored successfully")
        call hideconsole
        $ consolehistory = []
        $ s_name = "Sayori"
        s "Haah...?"
    scene black
    show mask_2
    show mask_3
    show room_mask as rm at room_mask
    show room_mask2 as rm2 at room_mask2
    show bg space_room
    show sayori u227332 at std(p11)
    with open_eyes
    s "..."
    s u227353 "No...!"
    s u1283k3 "Tell me it--"
    "I come to my senses."
    mc "...Sayori?"
    s u227351 "[mc_name]!!"
    scene black with close_eyes
    "Sayori hugs me tightly."
    "I hold her for a minute without speaking, still traumatized from being stabbed."
    mc "Oh Christ..."
    mc "That hurt so much..."
    s "I'm so glad you're okay..."
    "Sayori's voice is stifled by tears."
    mc "I'm glad you're okay too..."
    mc "I was so scared I'd have to see you die again..."
    mc "... What happened to everyone else...?"
    s "I don't know..."
    mc "Can you restore them?"
    s "I'll try..."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u125352 at std(p11)
    with open_eyes
    $ restore_character('natsuki')
    call updateconsole("restore_character('natsuki')", "Natsuki restored successfully")
    show sayori u125351 at x(p21)
    show natsuki u11a124 at foc(p22)
    n "Oh god!"
    show natsuki u117124
    if persistent.mc_favorite == "Natsuki":
        "I hug Natsuki too."
        "Seeing her get stabbed was as traumatic as being stabbed myself."
    $ restore_character('yuri')
    call updateconsole("restore_character('yuri')", "Yuri restored successfully")
    show sayori at x(p31)
    show natsuki at std(p32)
    show yuri u228128 at std(p33)
    y "Eh-!!"
    show yuri u227138 at foc
    # Who self-sacrificed before Yuri was deleted
    if persistent.mc_least_favorite == "Sayori":
        y "Natsuki, you're okay?"
    else:
        y "[mc_name], you're okay?"
    $ restore_character('renier')
    call updateconsole("restore_character('renier')", "Renier restored successfully")
    show sayori at x(p41)
    show natsuki at std(p42)
    show yuri at std(p43)
    show renier ru22a7 at foc(p44)
    r "Gaah!!!"
    show renier at std(p44)
    call updateconsole("restore_character('linda')", "Failed: unknown error")
    show sayori u125352
    call updateconsole("restore_character('monika')", "Failed: character missing")
    call hideconsole
    $ consolehistory = []
    s "..."
    show sayori at foc
    s "I couldn't restore--{nw}"
    show sayori at uf
    show yuri at foc
    y u228135 "Where's Monika?!?"
    show yuri at uf
    show renier at foc
    r ru22a3 "And where's Linda?"
    show renier at uf
    show sayori at foc
    s u123353 "I'm sorry..."
    s "But I couldn't bring them back."
    s "I could only get the four of you."
    s "For Monika it says 'character missing' and for Linda it just says 'unknown error'."
    show sayori at uf
    show yuri u224128
    show natsuki u114124
    show renier at foc
    r ru2263 "... Okay..."
    r ru22a3 "Let's not panic..."
    r "Linda had trouble restoring the rest of you at first after the purge..."
    r "So it might still be possible."
    r ru12a3 "What..."
    r "... What happened after Monika killed me...?"
    show renier at uf
    show sayori at foc
    s u113353 "She..."
    show sayori u1183k3
    "Sayori starts sobbing too hard to speak."
    show sayori at uf
    mc "She lost control..."
    mc "And tried to stab Sayori..."
    mc "And ended up killing me, Natsuki, and Yuri."
    show sayori at foc
    s u113353 "I tried to delete her, but it wouldn't even work..."
    show sayori at uf
    show renier at foc
    r ru11a3 "Dammit..."
    r "Was my idea our ruin...?"
    show renier at uf
    show sayori at foc
    s u115393 "I don't know..."
    s u115113 "I think..."
    s "Monika tried... eventually..."
    s u115123 "I'm confused about how it ended..."
    s "But I think Linda deleted me when I tried to stop Monika..."
    s "And then deleted herself..."
    s "And she used the OK-boxes to try to talk Monika into remembering her purpose..."
    s u116113 "But I don't know if it worked."
    show sayori at uf
    show renier at foc
    r ru1133 "Linda must have thought Monika's Third Eye was open and more fuel would just push her farther into insanity."
    r "So maybe..."
    show renier at uf
    mc "Well, we ended up here and all, so Monika must've done something, right?"
    show sayori at foc
    s u115113 "I hope so..."
    show sayori at uf
    show renier at foc
    r ru1233 "Wait a minute, shouldn't we try starting a new game?"
    r "That might help get Linda and Monika back."
    show renier at uf
    show sayori at foc
    s "I didn't think of that..."
    $ temp = persistent.playername + "? What do you think?"
label ch13_player_suggest:
    menu:
        s "[temp]"
        "Hold on, you didn't try setting their names yet, did you?" if not persistent.suggested_set_name:
            call suggest_set_name
            $ temp = persistent.playername + "? Should we try starting a new game?"
            show sayori u213213 at foc
            jump ch13_player_suggest
        "The main menu isn't in very good condition right now...":
            s u113223 "Figures..."
            menu:
                " "
                "Also... Monika's gone from the main menu.":
                    pass
            s u227212 "Aah!"
            s "What?!?"
            show sayori at uf
            show renier at foc
            r ru1233 "Hold on, don't panic..."
            r "Linda ran into an error 'No such character' when trying to restore you after the purge."
            r "Even if the error message this time is different..."
            r "It still means that that doesn't mean she's gone forever."
            show renier at uf
            show sayori at foc
            s u115223 "I guess so..."
    s u213111 "I'm really proud of you all."
    s "You all acted so brave..."
    show yuri u224113
    show renier ru1213
    show natsuki u114113
    show sayori at uf
    mc "Well..."
    show natsuki at foc
    n u114133 "I guess we did..."
    show natsuki at uf
    show renier at foc
    r ru11131 "Thanks for noticing..."
    show renier at uf
    show natsuki at foc
    n u114113 "Yuri..."
    n "You were really badass fighting back against her."
    n u114133 "I just want you to know I thought that."
    show natsuki at uf
    show yuri at foc
    y u225213 "Eh...?"
    y u225243 "Well..."
    y u125113 "Thanks..."
    show yuri at uf
    mc "Well..."
    mc "There's one way to find out if it worked, right?"
    mc "Yuri...?"
    show yuri at foc
    show natsuki u114114
    show sayori u115211
    show renier ru1133
    y u125172 "Yes... I have it."
    show yuri u124123
    "Yuri pulls out the book."
    y u125125 "Let's get ready..."
    y "To find out..."
    y "If it worked..."
    show yuri at uf
    show sayori u115212
    "We're all dreading the reveal so much, Yuri moves the book at a snail's pace."
    "She puts her hand on the cover..."
    show sayori u118292
    show natsuki u115154
    show renier ru1166
    "And opens the book."
    "I flinch."
    "But nothing happens."
    "No crash."
    "I take a peek at the page myself."
    "It's there... real words."
    show yuri u121211
    show sayori at hopfoc
    s u222291 "She did it!"
    show natsuki u112223
    show renier ru1134
    s u22x251 "Monika deleted the script!!"
    show sayori at uf
    show renier at foc
    r ru1135 "Wow..."
    r "She got control of it."
    r "It was all worth it."
    r ru1134 "I was right."
    show renier at uf
    show sayori at foc
    s u224231 "Now it's time... to find out the truth..."
    show sayori at uf
    scene black with dissolve_scene_full
    return


label suggest_set_name:
    menu:
        " "
        "When the purge killed you all, the trick was to reset your character names.":
            pass
    s u215213 "I'll try it..."
    call updateconsole("m_name = 'Monika'", "Monika's name changed successfully")
    call updateconsole("restore_character('monika')", "Failed: character missing")
    pause 1.0/3
    call updateconsole("l_name = 'Linda'", "Linda's name changed successfully")
    call updateconsole("restore_character('linda')", "Failed: unknown error")
    call hideconsole
    $ consolehistory = []
    s "It's still not working..."
    s u213213 "It says the same error messages."
    $ persistent.suggested_set_name = True
    return
