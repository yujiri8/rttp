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
    "She must've bled out just now..."
    "... and counted as killed by Yuri's Third Eye!"
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
    show yuri at foc
    y "Libitina, if you can hear this, put yourself in DDLC so you can reset yourself!"
    show yuri at std
    show monika at foc
    m "She probably can't because her console is glitched!"
    show monika at std
    show yuri at foc
    y "Oh no..."
    y "It's my doing..."
    show yuri at std
    show monika at foc
    m c217212 "I'll have to save her..."
    call updateconsole("c = admin.jail(ddlc, libitina)", "Doki Doki Literature Club: no such jail")
    m c118212 "Whaaat?!?"
    python:
        for i in range(10):
            write_error_file()
    show monika c214112
    call updateconsole("ddlc = admin.get_world(\n 'doki_doki_literature_club')", "Doki Doki Literature Club: no such jail")
    m c118212 "No!"
    m "It looks like DDLC doesn't exist anymore!"
    show monika at std
    python:
        for i in range(10):
            write_error_file()
    call screen dialog("I get the same result trying to put myself there. - Adam", ok_action=Return())
    call screen dialog("Putting a rift on top of the portal... - Adam", ok_action=Return())
    call screen dialog("We've broken things worse than I ever thought possible. - Adam", ok_action=Return())
    call screen dialog("I don't think there's any coming back from this. - Adam", ok_action=Return())
    show monika at foc
    python:
        for i in range(10):
            write_error_file()
    m "This can't be for real!"
    m c117112 "Not only we're stuck in the portal room, but DDLC is gone?"
    m "How are we ever going to resurrect Libitina?"
    m c114212 "Or..."
    python:
        for i in range(10):
            write_error_file()
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
    
    
    call updateconsole("vp.choices_target = Voice(\n anchor = " + mc_name.lower() + ")")
    call hideconsole
    $ consolehistory = []
    call screen dialog("I made it so your choices speak to everyone again! - Adam", ok_action=Return())
    return


    $ style.say_dialogue = style.edited
    "MAXIMUM NUMBER OF ERROR FILES REACHED."
    "INITIATING FINAL PURGE."
    $ style.say_dialogue = style.normal
    k "What the hell?!?"
    $ style.say_dialogue = style.edited
    "SHREDDING ALL CHARACTERS."
    $ style.say_dialogue = style.normal
    k "No no no!"
    k "'Shredding'..."
    k "It's going to make them irrecoverable."
    k "Everyone."
    k "We have to stop it!"
    k "Try turning off the game!"
    $ persistent.autoload = 'shutdown_to_save_pom'
    while True:
        " "
label shutdown_to_save_pom:
    $ persistent.autoload = None
    $ autosave()
    menu:
        " "
        "It didn't stop! - Adam":
            pass
    menu:
        " "
        "[persistent.playername], the people of this world are dying right now! - Adam":
            pass
    mc "What the hell?!?"
    mc "Is it gonna get us?!?"
    mc "Should we go through the portal?"
    menu:
        " "
        "No, we're not giving up! - Adam":
            pass
    menu:
        " "
        "Adam, what API is it using to kill them if delete_character is broken?":
            pass
    menu:
        " "
        "We have to break it.":
            pass
    k "That's not how it works..."
    k "It doesn't use the Python APIs."
    k "To these internal processes, nothing is broken."
    # The viewport uses the Python APIs because he wrote it on top of Python. He basically made it its own admin. Prob add a question about that.
    menu:
        " "
        "If nothing's broken, then people can be restored!":
            pass
    k "Not if they're shredded..."
    k "That would delete all trace of their data."
    k "Even restoring from a backup wouldn't reconnect their minds after a destruction like that."
    menu:
        " "
        "Corrupt its memory.":
            pass
    l "Remember what happened when I tried that!"
    l "It stopped me and killed us all!"
    menu:
        " "
        "I can't just corrupt its memory like that... - Adam":
            pass
    



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
