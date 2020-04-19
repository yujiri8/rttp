label chapter29:
    scene road1_night
    y "Oh no..."
    call prevent_skip
    $ delete_character('libitina')
    show screen invert(4, 0)
    play sound glitch_horror
    $ gtext = glitchtext(50) + '\n' + glitchtext(50) + '\n' + glitchtext(50)
    "{cps=300}[gtext]{nw}"
    play sound2 glitch_medium
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.5
    play sound glitch_horror
    pause 0.3
    hide screen tear
    scene black
    show mask_2
    show mask_3
    show portal_half
    $ delete_all_saves()
    $ autosave()
    mc "Oh my God!"
    "She counted as killed by Yuri's Third Eye!"
    "Now we've rifted the world again!"
    show linda at foc
    l 119443 "Nooo!"
    show linda at std
    show sayori at foc
    s c227232 "Oh crap!"
    show sayori at std
    show monika at foc
    m c118212 "Dammit!"
    show monika at std
    show reiner at foc
    r u2287 "Fuck, why did no one put a bullet in her?!?"
    show renier at std
    show yuri at foc
    y "What've we done?!?"
    show yuri at std
    show natsuki at foc
    n c117124 "Was this for nothing?!?"
    n "Does the portal still work?"
    show natsuki at std
    show linda at foc
    l 119443 "I dunno, but don't touch anything!"
    show linda at std
    python:
        for i in range(10):
            write_error_file()
    show monika at foc
    m "Libitina probably can't put herself in DDLC because her console is glitched!"
    m c217212 "I'll have to save her..."
    call updateconsole("c = admin.jail(ddlc, libitina)", "Doki Doki Literature Club: no such jail")
    m c118212 "Whaaat?!?"
    show monika c214112
    call updateconsole("ddlc = admin.get_world(\n 'doki_doki_literature_club')", "Doki Doki Literature Club: no such jail")
    m c118212 "No!"
    m "It looks like DDLC doesn't exist anymore!"
    show monika at std
    call screen dialog("I get the same result trying to put myself there. - Adam", ok_action=Return())
    call screen dialog("Putting a rift on top of the portal... - Adam", ok_action=Return())
    call screen dialog("We've broken things worse than I ever thought possible. - Adam", ok_action=Return())
    call screen dialog("I don't think there's any coming back from this. - Adam", ok_action=Return())
    show monika at foc
    m "This can't be for real!"
    m c117112 "Not only we're stuck in the portal room, but DDLC is gone?"
    m "How are we ever going to resurrect Libitina?"
    m c114212 "Or..."
    m "... anyone else who died in all this?"
    show monika at std
    call screen dialog("I don't know. And I can barely think amid the cacophony... - Adam", ok_action=Return())
    python:
        for i in range(10):
            write_error_file()
    
    
    python:
        with open(basedir + '/WTF.txt', 'w') as f;
            f.write("""
            What the fuck is this static?!?!?!?

            """+persistent.playername+""", what the fuck???

            It hurts like hell!
            """)
    call screen dialog("[persistent.playername], what the fuck is this static?!? - Libitina", ok_action=Return())
    $ temp = glitchtext(200)
    call screen dialog("[temp]!! - Libitina", ok_action=Return())
    call screen dialog("Help me! - Libitina", ok_action=Return())
    
    y "Libitina, if you can hear this, put yourself in DDLC so you can reset yourself!"
    
    
    call updateconsole("vp.choices_target = Voice(\n anchor = " + mc_name.lower() + ")")
    call hideconsole
    $ consolehistory = []
    call screen dialog("I made it so your choices speak to everyone again! - Adam", ok_action=Return())
    return


label next:
    show yuri at foc
    y "What about Mom and Dad?"
    y "Will we never see them again?"
    y "We never told them anything."
    y "To think we missed that chance and now they're dead without any knowledge of what happened, any last words..."
    y "Mom's last moment was possessed by her Third Eye, trying to kill me..."
    show yuri at std
    show natsuki at foc
    n "I left Dad a note because I thought he'd try to stop me..."
    n "... but what a horrible replacement for a conversation."
    show natsuki at std
    show monika at foc
    m "I never even talked to my parents!"
    m "I wanted to when the game reset, but I thought I didn't have time..."
    show monika at std
    show sayori at foc
    s "I'm so glad we did that step...!"
    show sayori at std
    show albert at foc
    al "We've killed more people than Adam ever did."

    s "I really wanted a cup--"
    s "Nevermind."

    m "Well, it's time to go."
    return
