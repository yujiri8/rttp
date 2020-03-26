label chapter6:
    if check_character('linda'):
        $ quick_menu = False
        "DDLC could not start."
        "Segmentation violation."
        $ renpy.quit()
    else:
        jump delete_linda


label delete_linda:
    $ persistent.autoload = None
    #$ s_name = glitchtext(6)
    #$ m_name = glitchtext(6)
    #$ ms_name = m_name + " & " + s_name
    $ r_name = "Renier"
    $ mc_name = persistent.mc_name
    play music yesnt
    show mask_2
    show mask_3
    ms "Yaaah!"
    show monika g2 at std(p21)
    show sayori end-glitch at std(p22)
    pause 1.0
    show monika u114144
    show sayori at foc
    s u224112 "Phew..."
    show monika u114114
    show sayori at uf
    "I open my eyes."
    "My stomach feels awful."
    mc "What {i}was{/i} that?"
    mc "I feel like I'm going to vomit..."
    "I sit down."
    "Don't ask me on what floor."
    show sayori at dip
    "Sayori sits down next to me."
    show sayori at foc
    s u215112 "Sorry..."
    show sayori at uf
    if persistent.mc_least_favorite != 'Sayori':
        mc "You must have had it worse with the nightmares..."
        "I put my hand on my stomach and groan."
    show monika at foc
    m "What even happened, anyway?"
    m "I mean, besides that the game crashed when you added linda.chr."
    menu:
        " "
        "The game kept saying 'DDLC could not start. Segmentation violation'.":
            pass
    menu:
        " "
        "I had to delete Linda's file to turn the game on.":
            pass
    show monika at foc
    m u114114 "I understand..."
    m "Linda probably remembers more than the script wants anyone in this world to."
    m "But we need her help figuring out what to do about it..."
    m u214113 "I'll see if I can lock Linda's memories without irreversibly deleting them."
    m "That might allow us to restore her without breaking everything."
    show monika at uf
    show sayori at foc
    s u123212 "But where are Yuri and Natsuki?"
    s "... And Renier?"
    s "Their files are there..."
    show sayori at uf
    mc "Why don't you warp them? You're a President."
    show sayori at foc
    s u123112 "Well... to do that the way Monika does, I think I need to know what the area is called."
    s "When [persistent.playername] reopened the game the first time Monika just restored their files and it put them with us..."
    s "But they're not deleted..."
    s u125122 "..."
    s u123112 "I could try deleting their files and restoring them..."
    s u125112 "But I'm not sure if that's a good idea."
    show sayori at uf
    menu:
        " "
        "Do it.":
            call sayori_reset_ynr
        "Don't do it.":
            $ persistent.sayori_reset_ynr = False
            show sayori at foc
            s u115112 "Okay..."
            show sayori u124122 at std(p11)
            "Sayori goes over to help Monika with the console stuff."
            "I'm left with nothing to do."
            "..."
            show monika at foc
            m u214111 "Okay, it should be safe to put Linda's file back now."
    m "I'm not sure if we should remake the world and then try to put her in..."
    m "Or put her in first, on the theory that the script won't resist as hard when the world is destroyed."
    m "Or maybe it'll resist harder, I don't know."
    jump linda_order_choice

label sayori_reset_ynr:
    $ persistent.sayori_reset_ynr = True
    show sayori at foc
    s u115212 "Okay..."
    show sayori u125212
    call updateconsole("os.remove('renier.chr')", "renier.chr deleted successfully")
    call updateconsole("os.remove('natsuki.chr')", "natsuki.chr deleted successfully")
    call updateconsole("os.remove('yuri.chr')", "yuri.chr deleted successfully")
    call updateconsole("restore_chr_file('renier')", "Renier restored successfully")
    call updateconsole("restore_chr_file('natsuki')", "Natsuki restored successfully")
    call updateconsole("restore_chr_file('yuri')", "Yuri restored successfully")
    call hideconsole
    $ consolehistory = []
    show sayori at uf
    pause 1.0
    show monika at x(p41)
    show sayori at x(p11)
    show renier ub141b at std(p44)
    r "..."
    "Renier appears drunk."
    "He falls over as soon as he comes back."
    hide renier
    play sound fall
    show sayori u227211 at xif(p11)
    "Sayori tried to catch him, but was too slow."
    show sayori at uf
    "Renier still doesn't seem conscious."
    "I look around for --"
    if persistent.mc_favorite == 'Yuri' or persistent.mc_least_favorite == 'Natsuki':
        mc "Yuri!"
        show yuri u237332 at foc(p44)
        y "Aagh..."
        y "Why does this happen?"
        show yuri at uf
        mc "Oh god... you just found yourself that way?"
        show yuri at foc
        y "Yes..."
        y "Every time the game..."
        y u23b372 "Rrgh..."
        "The cuts are even dripping blood..."
        y u237332 "It hurts so much..."
        y "More than it did in Act 2..."
        y "Like they're all new!"
        show yuri at uf
        mc "Oh god, I'm sorry..."
        mc "I don't have anything to bandage it with."
        show yuri at thide
        hide yuri
        "Yuri sits down beside me."
        "I hear puking behind me."
        show sayori at foc(p42)
        show natsuki vomit at std(p43) zorder 1
        s u227152 "Oh no!"
        s "Why did this happen?"
        show sayori at xis(p42)
        show natsuki at thide
        hide natsuki
        "Natsuki collapses to the ground as well, now beside me and Renier."
    else:
        mc "Natsuki!"
        show natsuki vomit at foc(p44) zorder 1
        n "!!"
        show natsuki at uf
        mc "Oh no..."
        show natsuki at thide
        hide natsuki
        "Natsuki pukes really badly, and then collapses to the ground as well, now beside me and Renier."
        mc "Natsuki, are you okay?"
        n "..."
        show natsuki u117114 at std(p44) zorder 1
        n "No..."
        n "I feel like I haven't eaten in days..."
        "I feel horrible for her."
        "Being put back through the same horrors she experienced in Act 2..."
        #show natsuki at thide
        #hide natsuki
        show sayori at x(p42)
        show yuri u23b372 at std(p43)
        y "Rrgh..."
        show sayori at xif(p42)
        s u227152 "Oh no!"
        s "Why did this happen?"
        show sayori at uf
        "Yuri's cuts are even dripping blood."
        show yuri at foc
        y u237332 "It hurts so much..."
        y "More than it did in Act 2..."
        y "Like they're all new!"
        show yuri at thide
        hide yuri
        "Yuri sits down."
    show sayori at foc
    s "I'm sorry..."
    s "Maybe I shouldn't have brought you all back..."
    show sayori at uf
    if persistent.mc_favorite == 'Sayori':
        mc "It's not your fault, Sayori..."
    show monika at foc
    m u214111 "Okay... It should be safe to -"
    m u118212 "What happened?"
    show monika at uf
    show yuri u237332 at std(p43)
    y "These violent crashes..."
    y "They hurt everyone, not just Presidents."
    show yuri at thide
    hide yuri
    "Yuri continues to whimper in pain."
    #show yuri at thide
    #hide yuri
    show natsuki u117114 at std(p44)
    "Natsuki starts breathing hard, trying to hold back more puke."
    show natsuki vomit
    "It doesn't work."
    show natsuki at thide
    hide natsuki
    "I see her shed a tear."
    if persistent.mc_favorite == 'Natsuki':
        "I shed one too, watching her."
    "I shift my position so my stomach isn't contracted."
    "I can't start puking with her..."
    #show natsuki u117114 at foc
    #n "I feel like I haven't eaten in days..."
    #show natsuki at uf
    show monika at foc
    m u114212 "Oh jeez..."
    show monika at uf
    show sayori at foc
    s "We have to help them somehow!"
    show sayori at uf
    show monika at foc
    m "They should be healed on the next world generation..."
    m "But we still need to give Linda another try."

label linda_order_choice:
    menu:
        m "[persistent.playername], what do you think?"
        "Let's put Linda back first.":
            m "Alright. Just put her file in when you're ready."
            show monika at uf
            while not check_character('linda'):
                ""
            show linda 115333 at std(p11)
            show monika u114112 at std(p31)
            show sayori u114112 at x(p33)
            l "..."
            jump linda_meeting_void
        "Let's generate the world first.":
            $ persistent.newgame = 2
            m "Alright..."
            m "Just go press the new game button then."
            while True:
                ""

label linda_meeting_void:
    $ persistent.linda_in_void = True
    mc "... Is that her?"
    show linda at thide
    hide linda
    play sound fall
    "Linda collapses."
    "She seems to be unconscious."
    if persistent.sayori_reset_ynr:
        show renier u22332b at leftin(p32)
        r "Linda!"
        r "It's her!"
        "I didn't notice Renier waking up."
        "He bends down to check on Linda, and then turns to Monika."
        show renier at xif(p32)
        r ru21332b "What's wrong with her?"
        show renier at uf
        show monika at xif(p31)
        m u114112 "She's probably hurt from the crash the same way everyone else is."
        m "We should regenerate the world now."
    else:
        show sayori at xif(p33)
        s u227112 "Oh no! Is she okay?"
        show sayori at uf
        show monika at xif(p31)
        m u114112 "I doubt it..."
        m "She might've been hurt during the crash, like Yuri was the first time, and now [mc_name]..."
        "Monika gestures to me, who am still on the ground on the verge of puking."
        m u214111 "[persistent.playername], let's regenerate the world again."
    $ persistent.newgame = 2
    while True:
        ""
