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
    show sayori at std(p32)
    show linda at std(p33)
    show monika c118212 at foc(p31)
    m "Dammit!"
    show monika at std(p42)
    show sayori at std(p43)
    show linda at std(p44)
    show reiner u2287 at foc(p41)
    python:
        for i in range(10):
            write_error_file()
    r "Fuck, why did no one put a bullet in her?!?"
    show renier at std(p52)
    show monika at std(p53)
    show sayori at std(p54)
    show linda at std(p55)
    show yuri c228125 at foc(p51)
    y "What've we done?!?"
    show yuri at std
    show markov u12543 at foc
    k "I was too slow to put her into DDLC before she died..."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show natsuki c117124 at foc
    n "Was this for nothing?!?"
    n "Does the portal still work?"
    show natsuki at std
    show markov at foc
    k "I don't know, but don't try it yet."
    k "It won't fix the world, but I should still be able to restore Libitina..."
    show markov at std
    python:
        for i in range(10):
            write_error_file()
    show markov at foc
    call updateconsole("ddlc = admin.get_world(\n 'doki_doki_literature_club')", "Doki Doki Literature Club: no such jail")
    k u12643 "Whaaat?!?"
    show markov at std
    show linda at foc
    l "Oh my God..."
    show linda at std
    show yuri at foc
    y "What is it?!?"
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
label chapter29_2:
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
    r "It wasn't any of our faults!"
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
    call adams_fate
    show monika at foc
    m "Well..."
    m "Our portal's open."
    m "The portal we worked so hard for."
    if persistent.adam_lived:
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
    "One by one, we step through the portal."
    "It stays open for each of us." # It only closes when an active Eye goes through it.
    return

label adams_fate:
    if persistent.player_advocate_mercy[1]:
        show monika at foc
        m "Adam..."
        show monika at std
        show markov at foc
        k "Yes, it's time for your decision."
        k "What are you going to do with me?"
        k "Do I die?"
        show markov at std
        show monika at foc
        m "No."
        show monika at std
        if persistent.player_advocate_mercy[0] == -1:
            show renier at foc
            r u2293 "Wait, are you fucking serious?!?"
            show renier at std
            show natsuki at foc
            n c117222 "What's gotten into you?!?"
            n "I'm killing him!"
            "Natsuki points her gun at Adam."
            show natsuki at std
            "Monika actually gets in the way."
            show monika at foc
            m c118312 "Waiit!!"
            m "We can talk about this!"
            show monika at std
            "Natsuki points her gun down."
            show natsuki at foc
            n "Monika, what the hell are you doing?!?"
            n "Why do you want this human scum to live?"
            show natsuki at std
            show monika at foc
            m "Think about this!"
            m "Killing him won't help anyone..."
            m "But if we take him with us..."
            m "... he can spend the rest of his life making up for it."
#            m ""
            show monika at std
            mc "Death is letting him off easy!"
            mc "I wish we'd punished him before everything was broken so we could kill him a hundred times!"
            show natsuki at foc
            n "Have you forgotten all the shit he did?!?"
            show natsuki at std
            show sayori at foc
            s c128314 "He tortured children!"
            show sayori at std
            show monika at foc
            m "I know!"
            show monika at std
            show renier at foc
            r u2296b "You're crazy if you expect us to let him off the hook after all this!"
            show renier at std
            show yuri at foc
            y "No punishment we could inflict on him could ever match his sins!"
            show yuri at std
            show monika at foc
            m "If your punishment needlessly denies someone the chance to reform..."
            m "... then something's wrong with your idea of justice!"
            show monika at std
            "..."
            show linda at foc
            l "But just why should we think he has any intention to reform?"
            l "Why should we trust anything from the mouth of such an abomination?"
            show linda at std
            show monika at foc
            m "Guys, if he really weren't sorry, he would've run through the portal while he could instead of sticking around trying to save the world just now."
            m "He probably could've while we were distracted."
            show monika at std
            "That's right..."
            "I bet he really did have an opportunity after he restored himself."
            "We didn't even notice he was back until he announced his presence."
            "There's no selfish reason he wouldn't have gone for it."
            show sayori at foc
            s "I think I could forgive him if I was his only victim."
            s "But what about all the other people he tortured?"
            show sayori at std
            show monika at foc
            m "Sayori..."
            m "You protected me, way back when, when Natsuki wanted to pummel me."
            m "Remember?"
            show monika at std
            show sayori at foc
            s "I did..."
            s "I guess this isn't all that different."
            show sayori at std
            show yuri at foc
            y "This is wrong!"
            y "It's plenty different!"
            y "Put aside the number of victims!"
            y "Monika was essentially tortured into doing what she did, and he wasn't!"
            y "There's no comparing those circimstances!"
            show yuri at std
            show markov at foc
            k "Separated from a loved one, alone with medium awareness in a virtual world?"
            k "I know, I won't pretend I was tortured in the same way Monika was."
            k "But Yuri, you've never experienced medium-awareness."
            k "You don't know how it felt to be the only person in that state of existence for years."
            show markov at std
            show sayori at foc
            s "I do."
            s "Yuri, to be honest..."
            s "... I'm sure having to exit like that for a long time would've made me kill myself."
            show sayori at std
#            k "And Monika did all that for someone she'd never even met!"
            "..."
            k "I don't deserve to live."
            k "But I deserve to be allowed to make up for his sins."
            k "At least as many of them as I can before I die."
            show markov at std
            #
            "What he's saying makes sense, but I don't care!"
            "I want to see his blood."
            "Even if I can't personally be the one to spill it."
            "I'm {i}not{/i} letting him get what he wanted after all this."
            mc "I don't give a damn!"
            mc "You can't just kidnap and torture us and then expect anything from us!"
            show monika at foc
            m "[mc_name]..."
            m "His survival can bring about a lifetime of good deeds."
            m "Think of all the people of [persistent.playername]'s world he could go on to help if he came with us."
            m "What kind of person would take that away from them just to satisfy themself?"
            show monika at std
            "How dare she-"
            "-- insult me like that!"
            "But --!"
            "She makes sense!"
            "It's not just about us."
            show markov at foc
            k "{i}To see the future is to be wise.{/i}"
            show markov at std
            "..."
            show renier at foc
            r "Damn it... I can't object, can I?"
            show renier at std
            show monika at foc
            m "No."
            m "And neither can I."
            show monika at std
            #
            #k "And... if it makes you feel any better..."
            #k "Remember that I {i}did{/i} already get shot and bled to death by you and stabbed twice by Libitina."
            #k "And spent hours in the glitched state after she killed me in the facility."
            #
            show natsuki at foc
            n "This feels like shit...!"
            n "To come all this way..."
            n "... to go through everything we did, and literally destroy the whole world..."
            n "... and not even take revenge?"
            show natsuki at std
            show monika at foc
            m "I'm sorry."
            m "I didn't want to spare him at first, either."
            m "I know it's unsatisfying."
            m "I was pissed when [persistent.playername] first warned me that I might have to show him the same mercy you all showed me."
            m "But it's the better thing to do."
            m "Better for people besides us."
            show monika at std
            show natsuki at foc
            n "..."
            n "I understand."
            show natsuki at std
            #
            "I shake my head, giving in."
            "I'm not going to kill him."
            "Monika's right."
            "Here we go again."
            "Another murderer on board."
            show markov at foc
            k "Thank you..."
            k "I'll make this worth it."
            k "And I'll help you get the supplies to make those cupcakes you never got."
            show markov at std
#            show natsuki at foc
#            n "Damn right you will."
#            n "If there's one thing that could make this ending a little happier..."
#            show natsuki at std
        elif persistent.player_advocate_mercy[0] == 0:
            "TODO"
        else:
            "TODO"
        $ persistent.adam_lived = True
    else:
        # TODO maybe another version if the others were told to have mercy and Monika wasn't. Linda could do the shooting.
        mc "I think it's time we get rid of Adam."
        mc "We don't need him anymore."
        show markov at foc
        k "Don't do this..."
        k "Don't give my story a sad ending."
        show markov at std
        mc "We've all had enough of you!"
        mc "Natsuki! Send him to hell!"
        show natsuki at foc
        play sound gunshot1
        show markov
        "..."
        play sound gunshot1
        $ delete_character('adam')
        show markov at thide
        hide markov
        n "Go to hell, you fucking monster!!"
        show natsuki at std
        $ persistent.adam_lived = False
    return
