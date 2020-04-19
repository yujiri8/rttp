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
    menu:
        " "
        "I get the same result trying to put myself there. - Adam":
            pass
    menu:
        " "
        "Putting a rift on top of the portal... - Adam":
            pass
    menu:
        " "
        "We've broken things worse than I ever thought possible. - Adam":
            pass
    menu:
        " "
        "I don't think there's any coming back from this. - Adam":
            pass
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
    menu:
        " "
        "I don't know. And I can barely think amid the cacophony... - Adam":
            pass
    python:
        for i in range(10):
            write_error_file()
    menu:
        " "
        "Let me go ahead and make it so [persistent.playername]'s choices speak to everyone again... - Adam":
            pass
    call updateconsole("vp.choices_target = Voice(\n anchor = " + mc_name.lower() + ")")
    call hideconsole
    $ consolehistory = []
    python:
        for i in range(10):
            write_error_file()
    $ style.say_dialogue = style.edited
    "MAXIMUM NUMBER OF ERROR FILES REACHED."
    "INITIATING FINAL PURGE."
    $ style.say_dialogue = style.normal
    menu:
        " "
        "What the hell?!? - Adam":
            pass
    $ style.say_dialogue = style.edited
    "SHREDDING ALL CHARACTERS."
    $ style.say_dialogue = style.normal
    menu:
        " "
        "No no no! - Adam":
            pass
    menu:
        " "
        "'Shredding'... - Adam":
            pass
    menu:
        " "
        "It's going to make them irrecoverable. - Adam":
            pass
    menu:
        " "
        "Everyone. - Adam":
            pass
    menu:
        " "
        "We have to stop it! - Adam":
            pass
    menu:
        " "
        "Try turning off the game! - Adam":
            pass
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
    menu:
        " "
        "That's not how it works... - Adam":
            pass
    menu:
        " "
        "It doesn't use the Python APIs. - Adam":
            pass
    menu:
        " "
        "To these internal processes, nothing is broken. - Adam":
            pass
    # The viewport uses the Python APIs because he wrote it on top of Python. He basically made it its own admin. Prob add a question about that.
    menu:
        " "
        "If nothing's broken, then people can be restored!":
            pass
    menu:
        " "
        "Not if they're shredded... - Adam":
            pass
    menu:
        " "
        "That would delete all trace of their data. - Adam":
            pass
    menu:
        " "
        "Even restoring from a backup wouldn't reconnect their minds after a destruction like that. - Adam":
            pass
    menu:
        " "
        "Corrupt its memory.":
            pass
    show linda at foc
    l "Remember what happened when I tried that!"
    l "It stopped me and almost killed us all!"
    show linda at std
    menu:
        " "
        "I can't just corrupt its memory like that... - Adam":
            pass
    menu:
        " "
        "I have to make it think we're already shredded. - Adam":
            pass
    l "The character files!"
    l "What if we shred them?"
#    l "Adam, reauthorize the viewport's access {i}now{/i}!"
    menu:
        " "
        "That will only save us! We need to save everyone else in this world! - Adam":
            pass
    l "And since they were never onscreen, they don't have files..."
    menu:
        " "
        "... I think it's all we can do. - Adam":
            pass
    menu:
        " "
        "We don't have long left. - Adam":
            pass
    call updateconsole("import random")
    call updateconsole("for c in monika, sayori, yuri, natsuki,\n "+mc_name.lower()+", renier, linda,\n graveyard.get_character('adam'),\n graveyard.get_character('albert'),\n graveyard.get_character('libitina'):\n  c.set_file_data(b''.join(bytes((random.randint(0, 255),)) for x in range(65536))", "No such character")
    l "Idiot, set your variables first!"
    call updateconsole("adam=graveyard.get_character('adam')")
    call updateconsole("albert=graveyard.get_character('albert')")
    call updateconsole("libitina=graveyard.get_character('libitina')", 'No such character')
    menu:
        " "
        "It's her! It can't get her data from the graveyard! - Adam":
            pass
    show linda at foc
    l "Do it for the rest of us at least!"
    show linda at std
    call updateconsole("for c in monika, sayori, yuri, natsuki,\n "+mc_name.lower()+", renier, linda, adam, albert:\n  c.set_file_data(b''.join(bytes((random.randint(0, 255),)) for x in range(65536))")
    menu:
        " "
        "Did... that work? - Adam":
            pass
    show linda at foc
    l "Only time will tell..."
    show linda at std


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
