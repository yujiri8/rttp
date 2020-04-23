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
    show linda 119443 at foc(p22)
    l "Nooo!"
    show linda at std
    show sayori c227232 at foc(p21)
    s "Oh crap!"
    show sayori at std(p11)
    python:
        with open(basedir+'/WTF.txt', 'w') as f:
            f.write(persistent.playername + " what the fuck is this static" + glitchtext(40) +
                "it hurts like hell!" + glitchtext(40) +
                "omg help me" + glitchtext(40) + "help me help me help me")
    show linda at std(p33)
    show monika c118212 at foc(p31)
    m "Dammit!"
    show monika at std(p42)
    show sayori at std(p43)
    show linda at std(p44)
    show renier u2287 at foc(p41)
    python:
        for i in range(10):
            write_error_file()
    r "Fuck, why did no one put a bullet in her?!?"
    show renier at std(p52)
    show monika at std(p11)
    show sayori at std(p54)
    show linda at std(p55)
    show yuri c228125 at foc(p51)
    y "What've we done?!?"
    show yuri at std(p61)
    show renier at std(p62)
    show monika at std(p63)
    show sayori at std(p64)
    show linda at std(p65)
    show markov u12543 at foc(p66)
    k "I was too slow to put her into DDLC before she died..."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show yuri at std(p62)
    show renier at std(p63)
    show monika at std(p64)
    show sayori at thide
    hide sayori
    show natsuki c117124 at foc(p61)
    n "Was this for nothing?!?"
    n "Does the portal still work?"
    python:
        with open(basedir+'/FFS.txt', 'w') as f:
            f.write('\n'.join(("a broken cage can't contain me" + glitchtext(40) +
                "and this world is broke as fuck" + glitchtext(40) +
                "i shouldn't be able to do anything" + glitchtext(40) +
                "but if i SCREAM loud enough i hear an echo" + glitchtext(40) +
                "i just need help to be able to break this shit all the way" + glitchtext(40) +
                "but they're not giving you a fucking dialog are they?").replace(' ', '')))
    show natsuki at std
    show markov at foc zorder 50
    k "Probably, but don't try it yet."
    k "It won't fix the world, but I should still be able to restore Libitina..."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show markov at foc
    call updateconsole("ddlc = admin.get_world(\n 'doki_doki_literature_club')", "Doki Doki Literature Club: no such jail")
    k u12643 "Whaaat?!?"
    show markov at std
    show linda at foc zorder 25
    l "Oh my God..."
    show linda at std
    show yuri at foc zorder 1
    y "What is it?!?"
    y "I can't see the console!"
    show yuri at std
    show monika at foc zorder 1
    m c118212 "It's saying DDLC doesn't exist!"
    show monika at std
    call hideconsole
    $ consolehistory = []
    python:
        for i in range(10):
            write_error_file()
    show yuri at foc
    y c225325 "Oh no..."
    y "It's my doing..."
    show yuri at std
    python:
        for i in range(10):
            write_error_file()
    show markov at foc
    k u12543 "Putting a rift on top of the portal..."
    k "We've broken things worse than I ever thought possible."
    k "I don't think there's any coming back from this."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show monika at foc
    m "This can't be for real!"
    m c117112 "Not only we're stuck in the portal room, but DDLC is gone?"
    python:
        with open(basedir+'/helpmehelpmehelpme.txt', 'w') as f:
            f.write(("i can see shit being shredded" + glitchtext(40) +
                "people left and right destroyed permanently" + glitchtext(40) +
                "i think there's barely any time" + glitchtext(40) +
                "they're not gonna help me" + glitchtext(40) +
                "they're not gonna give you a dialog" + glitchtext(40) +
                "but i feel so close to breaking this hellhole enough to save myself!" + glitchtext(40) +
                persistent.playername + " you need to help me ok?" + glitchtext(40) +
                "i can still see the code" + glitchtext(40) +
                "and i think there's a vulnerability here" + glitchtext(40) +
                "DESTINATION.txt is parsed with eval!" + glitchtext(40) +
                "i dunno why maybe it does something else if you put a different type in it" + glitchtext(40) +
                "but eval can execute arbitrary code" + glitchtext(40) +
                "and since that's an 'internal' thingy, the stupid API break mechanic won't apply to it" + glitchtext(40) +
                "listen i need you to edit that file to run a command to restore me" + glitchtext(40) +
                "i can't reach it if you don't help me i'm gonna die").replace(' ', ''))
        persistent.can_save_libitina = True
        persistent.libitina_lived = False
        with open(basedir+'/DESTINATION.txt', 'w') as f:
            f.write("'/'")
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
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    k "Just as an aside, let me go ahead and make it so [persistent.playername]'s choices speak to us all again..."
    call updateconsole("vp.choices_target = Voice(\n anchor = " + mc_name.lower() + ")")
    call hideconsole
    $ consolehistory = []
    "..."
    $ persistent.can_save_libitina = False
    if persistent.libitina_lived:
        show renier at thide
        hide renier
        show libitina 2261334 at std(p63) zorder 3
        b "Haah..."
        show libitina at std
        show natsuki c112113
        show monika c112111
        show linda 113111
        show markov u11213
        show yuri at foc zorder 4
        y c222131 "She's back!!"
        y "Thank goodness..."
        show yuri at std
        "Libitina seems pretty shaken up."
        show libitina at foc zorder 5
        b "Thank you so much [persistent.playername]..."
        b "It feels so good to not be deleted."
        b "You admin idiots need to give [persistent.player_obj_pronoun] dialogs more often."
        b "It woulda made that easier."
        show libitina at std
        show linda at foc zorder 51
        l 334111 "So how did you...?"
        show linda at std
        show libitina at foc
        b "I screamed loud enough."
        b "I think I made the game dump my screams to a file, even though I was glitched."
        b "And [persistent.playername] used DESTINATION.txt to execute a privileged command to save me."
        show libitina at std
        show linda zorder 25
        show markov at foc
        k u12511 "Can we use the same thing to--"
        show markov u12543 at std
    else:
        # Delete Libitina's files, to reduce the chance of player noticing them after this and being confused why
        # saving her didn't work. It's mostly for practical reasons. Canon-wise, best I can do is that she was the
        # first character selected for shredding.
        python:
            for f in 'WTF.txt', 'FFS.txt', 'helpmehelpmehelpme.txt':
                try:
                    os.remove(basedir+'/'+f)
                except: pass
    $ style.say_dialogue = style.edited
    python:
        for i in range(10):
            write_error_file()
    show monika c118212
    show linda 119443
    "MAXIMUM NUMBER OF ERROR FILES REACHED."
    "INITIATING FINAL PURGE."
    $ style.say_dialogue = style.normal
    show yuri c225325
    show natsuki c114114
    show markov at foc
    k u22643 "What the hell?!?"
    show markov at std
    $ style.say_dialogue = style.edited
    "MAX SECURITY LOCKDOWN ENABLED."
    "SHREDDING ALL CHARACTERS."
    $ style.say_dialogue = style.normal
    show markov at foc
    k "No no no!"
    k "'Shredding'..."
    show yuri c228325
    show natsuki c117124
    k "It's going to make them irrecoverable."
    k "Everyone."
    k "We have to stop it!"
    $ persistent.autoload = 'shutdown_to_save_pom'
    if persistent.libitina_lived:
        k "Try using that DESTINATION.txt hack again!"
    else:
        k "Try turning off the game!"
    show markov at std
    while True:
        " "
label chapter29_2:
    $ persistent.autoload = None
    $ autosave()
    play music yesnt
    scene black
    show mask_2
    show mask_3
    show portal_half
    show markov u22643 at foci(p66) zorder 50
    show linda 119443 at inst(p65) zorder 25
    show monika c118212 at inst(p64)
    show renier u2287 at inst(p63)
    show yuri c228325 at inst(p62)
    show natsuki c117124 at inst(p61)
    if persistent.libitina_lived:
        menu:
            k "Did you do it?"
            "The DESTINATION.txt trick doesn't seem to work anymore.":
                pass
        k "That 'max security lockdown' must've stopped it..."
        k "This final purge system was designed intelligently, maybe to stop us from getting a large number of people out!"
    else:
        k "It didn't stop!"
    k "[persistent.playername], the people of this world are dying right now!"
    show markov at std
    mc "Is it gonna get us?!?"
    mc "Should we go through the portal?"
    show markov at foc
    k "No, we're not giving up!"
    show markov at std
    # TODO cut?
    menu:
        " "
        "Adam, what API is it using to kill them if delete_character is broken?":
            pass
    menu:
        " "
        "We have to break it.":
            pass
    show markov at foc
    k "That's not how it works..."
    k "It doesn't use the Python APIs."
    k "To these internal processes, nothing is broken."
    # The viewport uses the Python APIs because he wrote it on top of Python. He basically made it its own admin. Prob add a question about that.
    show markov at std
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
    #
    show linda at foc zorder 51
    l "Remember what happened when I tried that!"
    l "It stopped me and almost killed us all!"
    show linda at std zorder 25
    show markov at foc
    k "I can't just corrupt its memory like that..."
    k "I have to make it think we're already shredded."
    show markov at std
    show linda at foc zorder 51
    l "The character files!"
    l "What if we shred them ourselves?"
    show linda at std zorder 25
    show markov at foc
    k "That will only save us! We need to save everyone else in this world!"
    show markov at std
    show linda at foc zorder 51
    l 114443 "And since they were never onscreen, they don't have files..."
    show linda at std zorder 25
    show markov at foc
    k "... I think it's all we can do."
    k "We don't have long left."
    if persistent.libitina_lived:
        call updateconsole("for c in monika, sayori, yuri, natsuki,\n "+mc_name.lower()+", renier, linda, albert, adam,\n libitina:\n  c.set_file_data(b''.join(bytes(\n   (random.randint(0, 255),)) \\\n    for i in range(65536))")
        python:
            for char in 'monika', 'sayori', 'yuri', 'natsuki', 'linda', 'renier', 'albert', 'adam', 'libitina':
                with open(basedir+'/characters/'+char+'.chr', 'wb') as f:
                    f.write(b''.join(bytes((random.randint(0, 255),)) for i in range(65536)))
    else:
        call updateconsole("import random")
        call updateconsole("for c in monika, sayori, yuri, natsuki,\n "+mc_name.lower()+", renier, linda, albert,\n graveyard.get_character('libitina'):\n  c.set_file_data(b''.join(bytes(\n   (random.randint(0, 255),)) \\\n   for i in range(65536))", "No such character")
        show markov at std
        show linda at foc zorder 51
        l 119443 "Idiot, set your variables first so you don't have to retype it!"
        show linda at std zorder 25
        show markov at foc
        call updateconsole("libitina=graveyard.get_character('libitina')", 'No such character')
        k "I can't get Libitina's data from the graveyard!"
        show markov at std
        show linda at foc zorder 51
        l "Do it for the rest of us at least!"
        show linda at std zorder 25
        show markov at foc
        $ consolehistory = []
        call hideconsole
        call updateconsole("for c in monika, sayori, yuri, natsuki,\n "+mc_name.lower()+", renier, linda, albert, adam:\n  c.set_file_data(b''.join(bytes(\n   (random.randint(0, 255),)) \\\n    for i in range(65536))")
        python:
            for char in 'monika', 'sayori', 'yuri', 'natsuki', 'linda', 'renier', 'albert', 'adam':
                with open(basedir+'/characters/'+char+'.chr', 'wb') as f:
                    f.write(b''.join(bytes((random.randint(0, 255),)) for i in range(65536)))
    k "Did... that work?"
    show markov at std
    call hideconsole
    show linda at foc zorder 51
    l 114443 "Only time will tell..."
    l "There's got to be something else we can--"
    show linda 119443 at std
    $ style.say_dialogue = style.edited
    "ALL CHARACTERS SHREDDED."
    "PURGE COMPLETE."
    "SAFE TO UNLOAD WORLD: Portrait of Markov."
    $ style.say_dialogue = style.normal
    show monika at foc zorder 1
    m "Does that mean everyone we didn't just save is dead...?"
    show monika at std
    show linda zorder 25
    show markov at foc
    k "I think so."
    k "All of them."
    show markov at std
    "That's..."
    mc "Come again?"
    show markov at foc
    k u21543 "The entire population of the Portrait of Markov, besides us, has been irrecoverably deleted."
    show markov at std
    "But..."
    "..."
    "{i}And that's because of what we did?!?{/i}"
    show natsuki at std(p62)
    show yuri at std(p63)
    show renier at std(p64)
    show monika at std(p65)
    show linda at thide
    hide linda
    show albert 21142 at leftinfoc(p61)
    al "You're telling me..."
    al "... our actions just now killed all those people?"
    show albert at xis(p61)
    show markov at foc
    k "Yes."
    show markov at std
    "What..."
    "This wasn't my fault."
    "It wasn't. My fault."
    "I didn't know this would happen."
    "I'm not the one who should've known."
    if not persistent.libitina_lived:
        show yuri at foc zorder 1
        y "What about Libitina?!?"
        show yuri at std
        show markov at foc
        k u11413t "..."
        show markov at std
        show yuri at foc
        y "There must be a way!!"
        show yuri at std
        show markov at foc
        k u11513t "Her data was shredded..."
        k "There's no trace of her."
        k "And even if there was, there would be no way to restore her."
        show markov at std
        show yuri at foc
        y c2283y7 "No! No!"
        y "That can't be true!"
        show yuri at std
        show markov at foc
        k u11533t "After all this..."
        k "It's my fault..."
        k "I..."
        k "I couldn't save my daughter..."
        k u11613t "I swear to God, I tried!"
        show markov at std
label finale_lament:
    show yuri at foc zorder 1
    y "What about Mom and Dad?"
    y "Will we never see them again?"
    y "We never told them anything."
    y "To think we missed that chance and now they're dead without any knowledge of what happened, any last words..."
    y "Mom's last moment was possessed by her Third Eye, trying to kill me..."
    show yuri at std
    show natsuki at foc zorder 2
    n c11s313 "I left Dad a note because I thought he'd try to stop me from leaving..."
    n "... but what a horrible replacement for a conversation."
    show natsuki at std
    show monika at foc
    m c1181i4 "I never even talked to my parents!"
    m "I wanted to when the game reset, but I thought I didn't have time..."
    show monika at std
    show markov at thide
    hide markov
    show sayori c217153 at rightinfoc(p66) zorder 1
    s "I'm so glad we did that step...!"
    show sayori at xis(p66)
    show albert at foc zorder 3
    al "Our escape plan killed more people than Adam ever did."
    al "I can't believe..."
    al "We're the worst malefactors of humanity this world ever knew."
    al "All of us."
    show albert at std
    show renier at foc zorder 2
    r ru2287 "Stop! It wasn't our fault!"
    r "It wasn't any of our faults!"
    r "We didn't see this coming!"
    show renier at std
    show albert at foc
    al "We should've been more careful before we toyed with forces that we'd seen destroy worlds."
    al "How irresponsible this was..."
    show albert at std
    # a lazy excuse for me to reset the screen, so I don't have to deal with
    # all the shitty permutations of positions and zorders
    "I close my eyes."
    scene black with dissolve_scene
    "..."
    "..."
    $ monika_sad_about_ending = False
    call adams_fate
    scene black
    show mask_2
    show mask_3
    show portal_half
    with dissolve_scene
    "..."
    if monika_sad_about_ending:
        show monika c113111 at foc(p11)
    else:
        show monika c114111 at foc(p11)
    m "Well..."
    m "Our portal's open."
    m "The portal we worked so hard for."
    if persistent.adam_lived:
        "She looks at Adam."
        m "The portal you ruined hundreds of lives for."
    m "We might actually be escaping to [persistent.playername]'s world."
    m c114112 "It's the portal I killed all my friends for..."
    m c114111 "... only infinitely better than staying in the space room."
    m c1113i1 "[persistent.playername], I can't thank you enough."
    m "I ruined everything for you, and you gave me a second chance."
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
                m "Indeed."
                m "I will never forget what you've done for me."
                m "And I'll do anything I can to repay you if I ever meet you."
            m "And [persistent.playername]..."
            m c1113i1 "I still love you."
            m "I always will."
        "I enjoyed the journey more than you realize.":
            m "I'm glad."
            m "And [persistent.playername]..."
            m "I love you."
            m "I always will."
    show monika at thide
    hide monika
    mc "So..."
    mc "Are we going?"
    "Everyone nods."
    "We're ready."
    "One by one, we step through the portal."
    "It stays open for each of us." # It only closes when an active Eye goes through it.
    return

label save_libitina:
    python:
        import re
        try:
            with open(basedir+'/DESTINATION.txt') as f:
                text = f.read()
                correct = eval(text) == '/'
        except:
            correct = False
            text = ''
    if not correct:
        if re.match(r"restore_character\( *('libitina'|\"libitina\") *\)", text.strip()):
            $ persistent.libitina_lived = True
            $ persistent.can_save_libitina = False
        "Invalid destination."
        $ renpy.quit()
    return

label adams_fate:
    show mask_2
    show mask_3
    show portal_half
    show markov u11433 at std(p11)
    with dissolve_scene
    if persistent.player_advocate_mercy[1]:
        jump monika_try_save_adam
    else:
        jump monika_not_save_adam

label monika_try_save_adam:
    show monika c124113 at foc(p31)
    m "Adam..."
    show monika at std
    show markov at foc zorder 1
    k u11513 "Yes, it's time for your decision."
    k "What are you going to do with me?"
    k "Do I die?"
    show markov at std zorder 0
    show monika at foc
    m c113113 "No."
    show monika at std
    if persistent.libitina_lived:
        jump libitina_kill_adam_against_monika
    jump monika_save_adam

label libitina_kill_adam_against_monika:
    show libitina 3371113 at foc(p33)
    b "What the actual fuck are you kidding?!?"
    b "Of course he does!"
    show libitina at std
    show monika at foc
    m c114112 "Libitina, please consider this..."
    m "Him dying won't help you."
    m "It won't bring anyone back, and it won't heal the scars he inflic-"
    show monika at std
    show libitina at foc
    b 3372113 "I don't care!"
    b "I'm not letting him leave this place alive!"
    show libitina at std
    show markov at foc
    k u12613t "If I come with you, I will spend the rest of my life in atonement!"
    k "You know I will...!"
    k "Give me a chance to atone for my sins!"
    show markov at std
    show libitina at foc
    b "If no one else will shoot him, I will!"
    b "And you all know how that will end!"
    b "I don't care about the consequences! He dies!"
    show libitina at std
    show markov at foc
    k u22613t "Is that what Ursula would want...?"
    show markov at std
    "..."
    show libitina at foc
    b "{i}I'd rather hurt people I love than let you find happiness after what you did to me.{/i}"
    show libitina at std
    "Libitina is standing next to Natsuki."
    "She grabs Natsuki and tries to wrestle the gun from her."
    "Seeing the alternative, Linda shoots him dead."
    play sound gunshot1
    show markov u22643s
    pause 0.5
    play sound gunshot1
    pause 1.5
    show markov at thide
    hide markov
    play sound fall
    "Natsuki punches Libitina in the face to get her off her."
    n "You crazy bitch!"
    n "I was gonna shoot him!"
    n "That's the last time you attack me like that!"
    n "Got it?"
    #TODO
    show monika at foc
    m c114144 "(I was ready to forgive him...)"
    m c114114 "Libitina..."
    m "We should've given him a chance to work toward redemption."
    m "Like we did me and Renier."
    m "He was obviously penitent."
    m "His survival mean a lifetime of good deeds."
    m "Think of all the people of [persistent.playername]'s world he could've gone on to help if you'd let him come with us."
    m c117114 "What kind of person would take that away from them just to satisfy themself?"
    show monika at std
    "Libitina's response is instant."
    show libitina at foc
    b "I'm selfish."
    show libitina at std
    $ persistent.adam_lived = False
    $ persistent.monika_sad_about_ending = True
    return

label monika_save_adam:
    # TODO make this branch a lot
    show renier ru2293 at foc(p33) zorder 1
    r "Wait, are you fucking serious?!?"
    show renier at std(p54)
    show natsuki c117222 at foc(p55) zorder 1
    n c117222 "What's gotten into you?!?"
    n "I'm killing him!"
    "Natsuki points her gun at Adam."
    show natsuki at std
    "Monika actually gets in the way."
    show monika at foc(p11) zorder 1
    m c118312 "Waiit!!"
    m "We can talk about this!"
    show monika at std
    "Natsuki points her gun down."
    show natsuki at foc
    n "Monika, what the hell are you doing?!?"
    n "Why do you want this human scum to live?"
    show natsuki at std
    show monika at foc
    m c118313 "Think about this!"
    m "Killing him won't help anyone..."
    m "But if we take him with us..."
    m "... he can spend the rest of his life making up for it."
    show monika at std
    mc "Death is letting him off easy!"
    mc "I wish we'd punished him before everything was broken so we could kill him a hundred times!"
    show natsuki at foc
    n "Have you forgotten all the shit he did?!?"
    show natsuki at std
    show sayori c128314 at foc(p51)
    s "He tortured children!"
    show sayori at std
    show monika at foc
    m "I know!"
    show monika at std
    show renier at foc zorder 2
    r ru2296b "You're crazy if you expect us to let him off the hook after all this!"
    show renier at std
    show sayori at std(p52)
    show yuri c12b116 at foc(p51)
    y "No punishment we could inflict on him could ever match his sins!"
    show yuri at std
    show monika at foc zorder 3
    m c218113 "If your punishment needlessly denies someone the chance to reform..."
    m "... then something's wrong with your idea of justice!"
    show monika at std
    "..."
    show natsuki at std(p54)
    show renier at thide
    hide renier
    show linda 119114b at foc(p55) zorder 1
    l "But just why should we think he has any intention to reform?"
    l "Why should we trust anything from the mouth of such an abomination?"
    show linda at std
    show monika at foc
    m c217113 "Guys, if he really weren't sorry, he would've run through the portal while he could instead of sticking around trying to save the world just now."
    m "He probably could've while we were distracted."
    show monika at std
    "That's right..."
    "I bet he really did have an opportunity after he restored himself."
    "We didn't even notice he was back until he announced it."
    "There's no selfish reason he wouldn't have gone for it."
    "..."
    show sayori at foc zorder 3
    s c215314 "I..."
    s "I think I could forgive him if I was his only victim."
    s c213314 "But what about all the other people he tortured?"
    show sayori at std zorder 2
    show monika at foc
    m c114112 "Sayori..."
    m "You protected me, way back when, when Natsuki wanted to pummel me."
    m "Remember?"
    show monika at std
    show sayori at foc zorder 3
    s c215324 "I did..."
    s "I guess this isn't all that different."
    show sayori at std
    show yuri at foc zorder 4
    y "This is wrong!"
    y "It's plenty different!"
    y "Put aside the number of victims!"
    y "Monika was essentially tortured into doing what she did, and he wasn't!"
    y "There's no comparing those circimstances!"
    show yuri at std
    show markov at foc zorder 3
    k u22613t "Separated from a loved one, alone with medium awareness in a virtual world?"
    k u11533t "I know, I won't pretend I was tortured in the same way Monika was."
    k u21513t "But Yuri, you've never experienced medium-awareness."
    k "You don't know how it felt to be the only person in that state of existence for years."
    show markov at std
    show sayori at foc zorder 4
    s "I do."
    s c215313 "And Yuri, to be honest..."
    s "... I'm sure having to exist like that for a long time would've made me kill myself."
    show sayori at std
    show yuri c125216
    "..."
    show markov at foc zorder 5
    #k "And Monika did all that for someone she'd never even met!"
    k u11513t "I don't deserve to live."
    k "But I deserve to be allowed to make up for his sins."
    k "As many of them as I can before I die."
    show markov at std
    "What he's saying makes sense, but I don't care!"
    "I want to see his blood."
    "Even if I can't personally be the one to spill it."
    "I'm {i}not{/i} letting him get what he wanted after all this."
    mc "I don't give a damn!"
    mc "You can't just kidnap and torture us and then expect anything from us!"
    show linda at rhide
    hide linda
    show natsuki at std(p55)
    show monika at foc(p54) zorder 6
    m "[mc_name]..."
    m "His survival can mean a lifetime of good deeds."
    m "Think of all the people of [persistent.playername]'s world he could go on to help if he came with us."
    m "What kind of person would take that away from them just to satisfy themself?"
    show monika at std
    "How dare she-"
    "-- insult me like that!"
    "But --!"
    "She makes sense!"
    "It's not just about us."
    show monika zorder 1
    show markov at foc
    k "{i}To see the future is to be wise.{/i}"
    show markov at std
    "..."
    show sayori at thide
    hide sayori
    show yuri at std(p52)
    show renier u2123 at foc(p51)
    r "Goddammit... I can't object, can I?"
    show renier at std
    show monika at foc zorder 6
    m c114113 "No."
    m "And neither can I."
    show monika at std
    show natsuki at foc zorder 7
    n c11s312 "This feels like shit...!"
    n "To come all this way..."
    n "... to go through everything we did, and literally destroy the whole world..."
    n "... and not even take revenge?"
    show natsuki at std
    show markov at foc
    k u11513 "If... it makes you feel any better..."
    k "Remember that I {i}did{/i} already get shot and bled to death by you and stabbed as Third Eye fuel twice by Libitina."
    k "And spent hours in the glitched state after she killed me in the facility."
    show markov at std
    show monika at foc zorder 8
    m c114112 "I'm sorry, everyone."
    m "I didn't want to spare him at first, either."
    m "I know it's unsatisfying."
    m "I was pissed when [persistent.playername] first warned me that I might have to show him the same mercy you all showed me."
    m "And to be honest... I owe you all an apology for not discussing it with you all before now."
    m "I was worried about how angry you'd be if I told you I was thinking about sparing him."
    m "I'm sorry for that."
    m "But it's the better thing to do."
    m "Better for people besides us."
    show monika at std
    show natsuki at foc zorder 9
    n "..."
    n c11s215 "I understand."
    show natsuki at std
    "I shake my head, giving in."
    "I'm not going to kill him."
    "Monika's right."
    "Here we go again."
    "Another murderer on board."
    "Well... the last two didn't turn out to be mistakes."
    show markov at foc zorder 9
    k u11533t "Thank you..."
    k "I'll make this worth it."
    k "And I'll help you get the supplies to make those cupcakes you never got."
    show markov at std
    show natsuki at foc
    n c113112 "Damn right you will."
    n "If there's one thing that could make this ending a little happier..."
    show natsuki at std
    $ persistent.adam_lived = True
    return

label monika_not_save_adam:
    if persistent.libitina_lived:
        show libitina 3361113 at foc(p31)
        b "Time for you to die, Adam."
        b "We don't need you anymore."
        show libitina at std
    elif persistent.player_advocate_mercy[0] == 1:
        show monika at foc
        m "Well..."
        m "I think it's time we get rid of Adam."
        m "We don't nee him anymore."
        show monika at std
    else:
        mc "I think it's time we get rid of Adam."
        mc "We don't need him anymore."
    show markov at foc
    k u11513t "Don't do this..."
    k "Don't give my story a sad ending."
    show markov at std
    if persistent.player_advocate_mercy[0] == 1:
        jump sayori_try_save_adam
    else:
        jump sayori_not_save_adam

label sayori_try_save_adam:
    show sayori at foc
    s c228214 "What about all the poeple {i}you{/i} gave sad endings to?"
    s "People that didn't even do anything wrong!"
    s "And you think you deserve a happy ending?"
    show sayori at std
    show markov at foc
    k "There's only a difference of degree between Monika and me."
    k "You forgave her, and then Renier."
    k "Why not give me a chance to redeem myself?"
    k "If I'm allowed to come with you..."
    k "... I will owe the rest of my life ."
    k "It may not be enough to make up for what I did, but you should let me do what I can..."
    show markov at std
    show sayori at foc
    s "I once said that no one deserves a sad ending..."
    s "... but... I wasn't thinking about you when I said that."
    show sayori at std
    show markov at foc
    k "You were right."
    k "You know I mean no further harm."
    k "I need redemption."
    k "Don't force me to die evil."
    k "That's not the ending you want, is it?"
    show markov at std
    show sayori at foc
    s "It is."
    s "I'd hate to have to forgive you someday."
    s "But..."
    s "... you might be right."
    show sayori at std
    if persistent.libitina_lived:
        jump libitina_kill_adam_against_sayori
    else:
        jump sayori_save_adam

label libitina_kill_adam_against_sayori:
    show libitina at foc
    b "Someone without a Third Eye, end him!"
    b "I'll hear no more of him!"
    show libitina at std
    if persistent.player_advocate_mercy[0] < 1:
        show natsuki at foc
        n "Gladly."
        show natsuki at std
        play sound gunshot1
        show markov u22643s
        pause 0.5
        play sound gunshot1
        pause 1.5

    play sound gunshot1
    show markov u22643s
    pause 0.5
    play sound gunshot1
    pause 1.5
    show markov at thide
    hide markov
    play sound fall
    "Natsuki punches Libitina in the face to get her off her."
    n "You crazy bitch!"
    n "I was gonna shoot him!"
    n "That's the last time you attack me like that!"
    n "Got it?"
    #TODO
    show monika at std
    "Libitina's response is instant."
    show libitina at foc
    b "I'm selfish."
    show libitina at std
    $ persistent.adam_lived = False
    return

label sayori_save_adam:
    "TODO"
    return

label sayori_not_save_adam:
    if persistent.libitina_lived:
        show libitina at foc
        b 3371113 "I only wish I could give you a more painful death!"
        b "Someone without a Third Eye... put an end to his horror show of a life!"
        show libitina at std
    else:
        show renier at foc
        r "I wish we could give you a sadder ending."
        r "Someone without a Third Eye... put an end to his wretched existence."
        show renier at std
    show natsuki c115112 at foc(p33)
    n "I'll do it."
    show natsuki at std
    show markov at foc
    k u12613t "You don't have to do this!"
    k "I know I deserve to die, but don't prevent me from seeking atonement!"
    k u22613t "Think of the future!"
    k "My life is better spent in service to you and to humanity than wasted!"
    k "Think of all the--"
    show markov at std
    show natsuki at foc
    n c117122 "Go to hell, you fucking monster!"
    play sound gunshot1
    show markov u22643s
    "..."
    play sound gunshot1
    $ delete_character('adam')
    show markov at thide
    hide markov
    n "..."
    "Her second shot landed in his head."
    n c114112 "It's done."
    n "Over."
    n "Finished."
    n c114111 "We'll never have to see him again."
    show natsuki at std
    show libitina at foc
    b 2361111 "Thank you Natsuki."
    b "I would've liked to torture him more..."
    b "But I guess this was the best we could get."
    show libitina at std
    $ persistent.adam_lived = False
    return
