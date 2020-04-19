label chapter29:
    scene road1_night
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
    $ quick_menu = True
    play music yesnt
    mc "Oh my God!"
    "She must've bled out just now..."
    "... and counted as killed by Yuri's Third Eye!"
    "Now we've rifted the world again!"
    python:
        for i in range(10):
            write_error_file()
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
    python:
        for i in range(10):
            write_error_file()
    r u2287 "Fuck, why did no one put a bullet in her?!?"
    show renier at std
    show yuri at foc
    y "What've we done?!?"
    show yuri at std
    show markov at foc
    k "I was too slow to put her into DDLC before she died..."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show natsuki at foc
    n c117124 "Was this for nothing?!?"
    n "Does the portal still work?"
    show natsuki at std
    show markov at foc
    k "I don't know, but don't try it yet..."
    k "It won't fix the world, but I should still be able to restore Libitina..."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show markov at foc
    call updateconsole("ddlc = admin.get_world(\n 'doki_doki_literature_club')", "Doki Doki Literature Club: no such jail")
    k "Whaaat?!?"
    show markov at std
    show linda at foc
    l "Oh my God..."
    show linda at std
    show yuri at foc
    y "What?!?"
    y "I can't see the console!"
    show yuri at std
    show monika at foc
    m c118212 "It's saying DDLC doesn't exist!"
    show monika at std
    call hideconsole
    $ consolehistory = []
    python:
        for i in range(10):
            write_error_file()
    show yuri at foc
    y "Oh no..."
    y "It's my doing..."
    show yuri at std
    python:
        for i in range(10):
            write_error_file()
    show markov at foc
    k "Putting a rift on top of the portal..."
    k "We've broken things worse than I ever thought possible."
    k "I don't think there's any coming back from this."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show monika at foc
    m "This can't be for real!"
    m c117112 "Not only we're stuck in the portal room, but DDLC is gone?"
    m "How are we ever going to resurrect Libitina?"
    m c114212 "Or..."
    python:
        for i in range(10):
            write_error_file()
    m "... anyone else who died in all this?"
    show monika at std
    show markov at foc
    k "I don't know."
    k "I don't know if we can."
    python:
        for i in range(10):
            write_error_file()
    k "Let me go ahead and make it so [persistent.playername]'s choices speak to everyone again..."
    call updateconsole("vp.choices_target = Voice(\n anchor = " + mc_name.lower() + ")")
    call hideconsole
    $ consolehistory = []
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    $ style.say_dialogue = style.edited
    #
    "MAXIMUM NUMBER OF ERROR FILES REACHED."
    "INITIATING FINAL PURGE."
    $ style.say_dialogue = style.normal
    show markov at std
    k "What the hell?!?"
    show markov at std
    $ style.say_dialogue = style.edited
    "SHREDDING ALL CHARACTERS."
    $ style.say_dialogue = style.normal
    show markov at foc
    k "No no no!"
    k "'Shredding'..."
    k "It's going to make them irrecoverable."
    k "Everyone."
    k "We have to stop it!"
    k "Try turning off the game!"
    show markov at std
    $ persistent.autoload = 'shutdown_to_save_pom'
    while True:
        " "
label shutdown_to_save_pom:
    $ persistent.autoload = None
    $ autosave()
    show markov at foc
    k "It didn't stop!"
    k "[persistent.playername], the people of this world are dying right now!"
    show markov at std
    mc "What the hell?!?"
    mc "Is it gonna get us?!?"
    mc "Should we go through the portal?"
    show markov at foc
    k "No, we're not giving up!"
    show markov at std
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
        "If internal stuff can use the broken APIs, then there might still be a way to restore the people!":
            pass
    show markov at foc
    k "Not if they're shredded..."
    k "That would delete all trace of their data."
    k "Even restoring from a backup wouldn't reconnect their minds after a destruction like that."
    show markov at std
    menu:
        " "
        "Corrupt its memory.":
            pass
    show linda at foc
    l "Remember what happened when I tried that!"
    l "It stopped me and almost killed us all!"
    show linda at std
    show markov at foc
    k "I can't just corrupt its memory like that..."
    k "I have to make it think we're already shredded."
    show markov at std
    show linda at foc
    l "The character files!"
    l "What if we shred them?"
#    l "Adam, reauthorize the viewport's access {i}now{/i}!"
    show linda at std
    show markov at foc
    k "That will only save us! We need to save everyone else in this world!"
    show markov at std
    show linda at foc
    l "And since they were never onscreen, they don't have files..."
    show linda at std
    show markov at foc
    k "... I think it's all we can do."
    k "We don't have long left."
    call updateconsole("import random")
    call updateconsole("for c in monika, sayori, yuri, natsuki,\n "+mc_name.lower()+", renier, linda, albert,\n graveyard.get_character('libitina'):\n  c.set_file_data(b''.join(bytes((random.randint(0, 255),)) for i in range(65536))", "No such character")
    show markov at std
    show linda at foc
    l "Idiot, set your variables first so you don't have to retype it!"
    show linda at std
    show markov at foc
    call updateconsole("libitina=graveyard.get_character('libitina')", 'No such character')
    k "I can't get Libitina's data from the graveyard!"
    show markov at std
    show linda at foc
    l "Do it for the rest of us at least!"
    show linda at std
    show markov at foc
    call updateconsole("for c in monika, sayori, yuri, natsuki,\n "+mc_name.lower()+", renier, linda, albert, adam:\n  c.set_file_data(b''.join(bytes((random.randint(0, 255),)) for i in range(65536))")
    python:
        for char in 'monika', 'sayori', 'yuri', 'natsuki', 'linda', 'renier', 'albert', 'adam':
            with open(basedir+'/characters/'+char+'.chr', 'wb') as f:
                f.write(b''.join(bytes((random.randint(0, 255),)) for i in range(65536)))
    k "Did... that work?"
    show markov at std
    show linda at foc
    l "Only time will tell..."
    l "There's got to be something else we can--"
    show linda at std
    $ style.say_dialogue = style.edited
    "ALL CHARACTERS SHREDDED."
    "PURGE COMPLETE."
    "SAFE TO UNLOAD WORLD: Portrait of Markov."
    $ style.say_dialogue = style.normal
    m "Does that mean everyone we didn't just save is dead...?"
    show markov at foc
    k "I think so."
    k "Everyone who never had a character file."
    show markov at std
    show yuri at foc
    y "What about Libitina?!?"
    show yuri at std
    show markov at foc
    k "..."
    "Adam's expression is clear."
    show markov at std
    show yuri at foc
    y "There must be a way!!"
    show yuri at std
    show markov at foc
    k "Her data was shredded..."
    k "There's no trace of her."
    k "And even if there was, there would be no way to restore her."
    show markov at std
    show yuri at foc
    y "No! No!"
    y "That can't be true!"
    show yuri at std
    show markov at foc
    k "After all this..."
    k "It's my fault..."
    k "I..."
    k "I couldn't save my daughter..."
    k "I swear to God, I tried!"
    show markov at std
label finale_lament:
    "So the world is really gone?"
    "We killed everyone?"
    "The whole... world?"
    "{i}Everyone{/i} in the Portrait?"
    "I..."
    "..."
    "What..."
    "This wasn't my fault."
    "It wasn't. My fault."
    "I didn't know this would happen."
    "I'm not the one who should've known."
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
    al "Our escape plan killed more people than Adam ever did."
    al "I can't believe..."
    al "We're the worst malefactors of humanity this world ever knew."
    al "All of us."
    show albert at std
    show renier at foc
    r "Stop! It wasn't our fault!"
    r "it wasn't any of our faults!"
    r "We didn't see this coming!"
    show renier at std
    show albert at foc
    al "We should've been more careful before we toyed with forces that we'd seen destroy worlds."
    al "How irresponsible this was..."
    show albert at std
#    show sayori at foc
#    s "I really wanted a cup--"
#    s "Nevermind."
#    show sayori at std
    show monika at foc
    m "Well..."
    m "Our portal's open."
    m "The portal we worked so hard for."
    "She looks at Adam."
    m "The portal you ruined hundreds of lives for."
    m "If we're lucky..."
    m "It might actually get us out of this Portrait."
    m "We might be escaping to [persistent.playername]'s world."
    m c114112 "It's the portal I killed all my friends for..."
    m c114111 "... only infinitely better than staying in the space room."
    m c1113i1 "[persistent.playername], I can't thank you enough."
    m "I ruined everything for you, and you gave me a chance."
    m "I have no idea where we'll come out."
    m "But if we can, maybe... we'll meet you some day."
    m "In Your Reality."
    menu:
        " "
        "If that ever happens, you owe me.":
            if any(persistent.player_guilt_dokis):
                m "Of course..."
            else:
                m c114311 "Ah..."
                m "You're right."
            m "And [pesistent.playername]..."
            m "I still love you."
            m "I always will."
        "I enjoyed the journey more than you realize.":
            m "I'm glad."
            m "And [persistent.playername]..."
            m "I love you."
            m "I always will."
    # TODO maybe the favorite girl should ask if player loves her
    mc "So..."
    mc "Are we going?"
    "Everyone nods."
    "We're ready."
    # TODO Maybe Adam should go first if he's alive.
#    "Albert goes through first, since he has the least risk of doing anything to it."
#    "Then t"
    # or maybe they just go through all at once to avoid complexity.
    "One by one, we step through the portal."
    "It stays open for each of us." # maybe it only closes when an active Eye goes through it.
    return
