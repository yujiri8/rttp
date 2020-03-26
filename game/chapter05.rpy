label chapter5:
    m u223113 "We need to crack Renier's file."
    m "That has to be our next step."
    m u224113 "It looks like base64."
    m "There should be free base64 decoders online..."
    m "We'll wait for you."
    show monika at uf
    menu:
        " "
        "I'm done.":
            pass
    m u222111 "Great. What does it say?"
    menu:
        " "
        "Unfortunately, there seems to be another layer of encryption.":
            pass
    show renier uf11
    m u123121 "Mm..."
    m u123111 "Try putting the decoded version in the game files, as renier_decrypt.txt."
    m "We might be able to help figure it out."
label decrypt_base64:
    $ proceed = ""
    while not proceed:
        ""
        python:
            # Check both filenames, to get around Windows filename BS
            try:
                text = ''
                try:
                    with open(config.basedir + "/renier_decrypt.txt", "r") as f:
                        text = f.read()
                except:
                    with open(config.basedir + "/renier_decrypt.txt.txt", "r") as f:
                        text = f.read()
                if not text:
                    pass
                elif text.strip().replace('\n','').replace('\r','') == renier_unbase64.strip().replace('\n','').replace('\r',''):
                    proceed = "renier_unbase64"
                else:
                    proceed = "renier_unbase64_incorrectly"
            except:
                pass
    jump expression proceed


label renier_unbase64_incorrectly:
    m "That doesn't look like the right base64-decrypted text..."
    python:
        try:
            with open(config.basedir + "/renier_decrypt.txt", "w") as f:
                f.write("")
        except:
            pass
    m "Try decoding it again."
    jump decrypt_base64


label renier_unbase64:
    show monika at foc
    m u121111 "I see it."
    m "I'll write it down in-world so everyone else can read."
    "Monika pulls out a notebook and pen and transcribes the characters."
    show monika at uf
    mc "Looks like garbage to me..."
    mc "[persistent.playername], are you sure you did the base64 thing right?"
    menu:
        " "
        "Yes, I'm quite sure.":
            $ persistent.player_insult_mc_for_questioning_base64 = False
        "Dude, I'm not an idiot. Didn't realize the same couldn't be said for you.":
            $ persistent.player_insult_mc_for_questioning_base64 = True
            mc "Wha- hey!"
            mc "I didn't do anything stupid!"
            show monika at foc
            m l5111 "Ahaha~"
    show monika l5111 at foc
    m "[mc_name], what did you expect it to look like when [persistent.player_subj_pronoun] said there was more encryption?"
    show monika at uf
    mc "I don't know..."
    show yuri at foc
    y u124152 "This looks like a shift cipher..."
    y u124113 "Have you tried frequency analysis?"
    show yuri at uf
    $ showing_chars = ['r', 'n', 'm', 'y']
    menu:
        " "
        "No. I'll go try it.":
            show monika at foc
            m u111111 "Thanks."
            m "Let us know if you find anything or give up."
            m "We'll be trying it too."
            show monika at uf
            show natsuki at thide
            hide natsuki
            show monika at x(p42)
            show yuri at x(p43)
            show sayori t1211 at rightin(p44)
            s "Wait, what's frequent analysis?"
            "Yuri explains the concept, and the six of us start working."
            pause 5.0
            scene black with dissolve_scene_full
            scene natsuki_house
            show renier u1151 at std(p41)
            show monika u114124 at std(p42)
            show yuri u123157 at std(p43)
            show sayori u116113 at std(p44)
            menu:
                " "
                "I've given up... have you guys found anything?":
                    mc "No... it doesn't seem like there's any possible substitution that makes this message decode to anything."
        "Yeah... I tried for a while, but I couldn't get anything coherent.":
            show monika at foc
            m u124111 "Hm... maybe it's a vigenere cipher?"
            m u224111 "The have a nice weekend file was, if I remember correctly."
            jump vigenere
        "I don't know what that is...":
            show monika at foc
            m u121111 "No need, we can do it ourselves."
            show monika at uf
            show natsuki at thide
            hide natsuki
            show monika at x(p42)
            show yuri at x(p43)
            show sayori t1211 at rightin(p44)
            s "Wait, what's frequent analysis?"
            "Yuri explains the concept, and the six of us start working."
            scene black with dissolve_scene_full
            scene natsuki_house
            show renier u1151 at std(p41)
            show monika u114124 at std(p42)
            show yuri u123157 at std(p43)
            show sayori u116113 at std(p44)
            mc "We can't figure it out, [persistent.playername]..."
            mc "It doesn't seem like there's any possible substitution that makes this message decode to anything."
    show monika at foc
    m u124114 "Maybe it's a vigenere cipher."
    m u224114 "The have a nice weekend file was, if I remember correctly."
    $ showing_chars = ['r', 'm', 'y', 's']
    jump vigenere

label vigenere:
    show monika at uf
    show renier at foc zorder 2
    r u1113 "Then we'll need to know the key."
    r uf111 "Let me think..."
    show renier at uf
    "While Renier is thinking, the rest of us try the obvious - libitina, thirdeye, openyourthirdeye, markov, elyssa..."
    "..."
    if 's' in showing_chars:
        show sayori u114111
    show yuri u123111
    show renier at foc
    r u1113 "I've got it."
    r u1213 "Try 'ihavegrantedkidstohell'."
    r u1113 "The splash screen message..."
    r u1111 "I have this nagging feeling about it."
    show renier at uf
    "We try it."
    "..."
    if 's' in showing_chars:
        show sayori u114131
    show yuri u124131
    show monika at foc
    m u224111 "Well... that looks like it."
    m "I'll write the result to a file so you can look at it with us."
    python:
        with open(config.basedir + "/renier_decrypted.txt", "w") as f:
             f.write(renier_decrypted)
    show monika at uf
    "Monika gives the solution to Renier."
    show renier at foc
    r u1183 "..."
    r u1133 "No... L..."
    "We're all watching him anxiously."
    show yuri u224131
    r u22a3 "Linda!"
    r "She's in this game somewhere!"
    r "We have to save her!"
    show renier at uf
    show monika at foc
    m u214113 "Whoa, hold on!"
    m "What did you remember?"
    show monika at uf
    show renier at foc
    r u12a3 "Linda Watson, from the story!"
    r "I just know she wrote this!"
    r "Can't you restore her with your president jumbo or something?"
    show renier at uf
    show monika at foc
    m u114114 "I don't have a backup to restore from."
    show monika at uf
    show renier at foc
    r u22a3 "[persistent.playername]! Make an empty linda.chr in the characters folder!"
    while not check_character('linda'):
        ""
    call prevent_escape
    play sound glitch_basic
    pause 0.4
    show screen invert(1.5, 0.3)
    play sound2 glitch_mscare
    play sound3 glitch_horror
    $ gtext = glitchtext(50) + '\n' + glitchtext(50) + '\n' + glitchtext(50)
    "{cps=300}[gtext]{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch_basic
    pause 0.6
    $ persistent.autoload = "after_linda_crash"
    $ renpy.quit()
