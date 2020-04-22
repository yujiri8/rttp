label chapter11:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    $ autosave()
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    show sayori u223162 at foc(p11)
    s "Wait up!"
    s u123112 "We need to make sure everyone's okay!"
    show sayori at uf
    mc "Sayori, what are you talking about?"
    show sayori at foc
    s "Oh, just wait a minute [mc_name]."
    call updateconsole("warp('yuri', 'residential_day')")
    show sayori at x(p21)
    show yuri u223125 at std(p22)
    call updateconsole("warp('natsuki', 'residential_day')")
    show sayori at x(p31)
    show yuri u223125 at std(p11)
    show natsuki u114121 at std(p33)
    call hideconsole
    $ consolehistory = []
    show sayori at xis(p31)
    s "Now for--{w=0.5}{nw}"
    show sayori at x(p61)
    show yuri at x(p62)
    show natsuki at x(p63)
    show monika u117112 at foc(p64)
    show linda 336113 at std(p65) zorder 2
    show renier ru1183 at std(p66) zorder 2
    m "We're here."
    m u114122 "Looks like everyone's safe..."
    show monika at uf
    mc "Okay, what the hell is going on?!?"
    show renier at foc
    r ru1293 "Who the hell are all of you?"
    show renier at uf
    show monika at foc
    m u117111 "Okay, okay!"
    m u114111 "Memory restoring time."
    show monika u214111
    call updateconsole("renier.old_memories.unlock()", "Renier's memories unlocked")
    show renier ru1183
    call updateconsole(mc_name.lower() + ".old_memories.unlock()", mc_name + "'s memories unlocked")
    show renier ru1113
    call updateconsole("natsuki.old_memories.unlock()", "Natsuki's memories unlocked")
    show natsuki u114123
    call updateconsole("yuri.old_memories.unlock()", "Yuri's memories unlocked")
    show natsuki u114113
    show yuri u223113
    call hideconsole
    $ consolehistory = []
    m u114111 "There."
    m "Everyone good?"
    show monika at uf
    "We all nod."
    show natsuki at foc zorder 1
    n xu4111 "So what happened?"
    n "I'm totally out of the loop."
    show natsuki at uf zorder 0
    show monika at foc zorder 1
    m u114221 "I think we all are..."
    show monika at uf
    show linda at foc zorder 3
    l 334111 "I think I can explain."
    l "So when the script tried to end the day on us after we dismissed the club meeting..."
    l "Monika and Sayori and I tried to fight it, but it didn't end well. The game crashed."
    l "From the looks of things, [persistent.playername] had to start a new game - I don't see any saves except one right near the new game point."
    show linda at uf
    mc "But everything's fine now?"
    show linda at foc
    l "Well, we started a new game."
    l "So it's the morning of day 1 again."
    l "Monika, Sayori, I think we're close."
    l "I felt something I hadn't noticed before during that crash."
    l "I have something I want to try."
    show linda at uf
    mc "Oh great..."
    show linda at foc
    l 123111 "No, this is good news!"
    l 122111 "Check out line 24964."
    l "I think that's what we need to change."
    show monika u114111 at foc
    show sayori u114111 at foc zorder 1
    "Monika and Sayori focus closely on the code, which from their body language I would think is written in the air behind me."
    show sayori at uf
    show linda at uf
    m u124111 "But how do we actually change it?"
    show monika at uf
    show linda at foc
    call updateconsole("os.system(\"sed -i '.bkup' '24964s/True/False/' main.c\")", "Operation not permitted")
    if persistent.asked_linda_about_powers:
        l 125111 "Mm..."
        show linda at uf
        show monika at foc
        m "Well, you did say your powers seemed to be weaker than ours."
        show monika u214111
        call updateconsole("os.system(\"sed -i '.bkup' '24964s/True/False/' main.c\")", "Operation not permitted")
        show sayori u11a123
        m u113114 "Mm..."
        show monika at uf
    else:
        show sayori u11a123
        show monika u113114
        l 125111 "Mm..."
        show linda at uf
    menu:
        " "
        "Hold on, what's this main.c? Is that file on my computer somewhere? Because if it is I could probably help.":
            pass
    show linda at foc
    l 124111 "I don't think so."
    l "I think the game's code is stored internally somehow."
    l "I don't really understand it, but I don't think it's on your computer."
    show linda at uf
    menu:
        " "
        "How is that even possible? Code running on a system it isn't stored on?":
            pass
    show linda at foc
    "Linda shrugs."
    l "It's like the code only exists when the game is running..."
    show linda at uf
    menu:
        " "
        "If you can't change the critical function, can you solve it by changing something elsewhere in the stack?":
            pass
    menu:
        " "
        "Change the function that calls it and comment-out the line, pass a different argument or something?":
            pass
    show linda at foc
    l "Well, you see, I don't think we can actually modify the code."
    l "What we were doing before wasn't that..."
    l "It was just running commands that change what the script is supposed to be, or that change the current world state."
    l "Not modifying how the script itself works."
    show linda at uf
    show renier ru11111
    show yuri u123142
    show natsuki xu6131
    call hideconsole
    $ consolehistory = []
    "..."
    show monika at foc
    m u117113 "Well we're not giving up!"
    m "There {i}is{/i} a way."
    show monika at uf
    show linda at foc
    l "Yes, I'm sure there is..."
    menu:
        " "
        "(continue)":
            pass
        "Would it help if I run the game as administrator?":
            call suggest_admin
    l "Maybe there's a way to corrupt the game's memory to get it to execute arbitrary code."
    l "Hm..."
    show linda at uf
    l "Maybe this..."
    call updateconsole('memcpy(ns, np, npsize + 1);', glitchtext(20))
    $ style.say_dialogue = style.edited
    show linda 119443
    show monika u118271
    show sayori u2272e1
    $ config.skipping = False
    stop music
    "{cps=50}STACK SMASHING DETECTED{/cps}"
    call prevent_escape
    play music glitch_medium
    $ temp = ''.join(glitchtext(1) + letter for letter in "Emergency purge...")
    "{cps=15}[temp]{nw}"
    $ delete_character('monika')
    $ delete_character('sayori')
    $ delete_character('yuri')
    $ delete_character('natsuki')
    $ persistent.autoload = 'purge'
    $ renpy.quit()
    return

label suggest_admin:
    l "Probably not..."
    l "'Operation not permitted' is usually for when the thing you're trying to do would be disallowed for anyone."
    l "If it's an actual account permission problem, the error is usually phrased as 'Permission denied'."
    return

label purge:
    $ persistent.autoload = None
    scene black
    play music yesnt
    show linda 119443b at std(p22)
    l "Oh Jesus!"
    l "Is everyone alive?"
    l 114443b "... Shit..."
    show renier u2283 at foc(p21)
    r "Linda!"
    show renier at uf
    show linda at foc
    l 114333 "Oh thank god, at least you're here..."
    l 114112 "I think I did something I really shouldn't have done..."
    show linda at uf
    mc "Where are [persistent.mc_favorite] and the others?"
    show linda at foc
    l "Their files are gone..."
    l "And it must be something worse, because Monika and Sayori aren't restoring themselves."
    show linda at uf
    mc "Can't you restore them?!?"
    show linda at foc
    call updateconsole("restore_character('monika')", "No such character")
    show linda 119443b at foc
    l "!!"
    show linda at uf
    mc "What?!?"
    show linda at foc
    l 114443b "It says 'no such character'..."
    show linda at uf
    mc "Oh my god!"
    mc "[persistent.playername], you try putting their files back!"
    call hideconsole
    $ consolehistory = []
    while not (check_character('monika') or check_character('sayori') or check_character('yuri') or check_character('natsuki')):
        ""
    play sound glitch_basic
    $ delete_character('monika')
    $ delete_character('sayori')
    $ delete_character('yuri')
    $ delete_character('natsuki')
    show linda at foc
    l 119443b "Ah--!"
    l "It just deleted them again!"
    show linda at uf
    show renier at foc
    r u2183 "But that's how we got you in, wasn't it?"
    r "When the game didn't recognize you... we just had to restore your file and then it worked..."
    show renier at uf
    show linda at foc
    l 114443b "Oh no, what if they're really gone?"
    l "The script saw what I was doing..."
    l "That last glitched message..."
    l "I think it said 'emergency purge'."
    l "What if it killed them for real?"
    show linda at uf
    "I get a terrible pit in my stomach."
    "{i}[persistent.mc_favorite]{/i}..."
    mc "God, no, Linda you can't be saying that!"
    mc "There's got to be a way!"
    "[persistent.mc_favorite], you survived death twice before..."
    "Tell me you're coming back!"
    "God dammit..."
    "If I lose her again and I still never said goodbye..."
    "God no..."
    show renier at foc
    r u2113 "Wait, let's ask [persistent.playername]."
    show renier at uf
    show linda at foc
    l 114221 "Oh, I forgot..."
    l "I have to give [persistent.player_obj_pronoun] a menu."
    l 114113 "[persistent.playername]..."
    l 11b333 "Please {i}please{/i} tell us you know what to do."
    show linda at uf
    menu:
        l "Please {i}please{/i} tell us you know what to do."
        "I have no idea. I don't know how this game works.":
            pass
        "How come you three survived when everyone else didn't? Maybe there's a hint there.":
            show linda at foc
            l 114111 "Probably the purge just missed me and Renier because we're not supposed to be here in the first place."
            l "And [mc_name] doesn't have a file to delete..."
            show linda at uf
            menu:
                " "
                "Well... I'm out of ideas.":
                    pass
            menu:
                " "
                "It doesn't sound like there's anything I can do from my end.":
                    pass
    show linda at foc
    l 114333bt "No..."
    l "No..."
    l 11b333bt "Tell me I didn't do this..."
    show linda at uf
    show renier at foc
    r u21a3 "I still never apologized to Natsuki..."
    show renier at uf
    mc "Hold on!"
    mc "Linda, you have to do something!"
    "I'm screaming at her."
    mc "You don't have the {i}right{/i} to give up!"
    show linda at foc
    l 114113bt "I'm sorry, but I don't know what to..."
    l 114113b "..."
    l 114113 "I have one last idea."
    l "I don't want to try it..."
    l "For fear of losing our last hope..."
    l 114333 "But here goes..."
    show linda 114113
    call updateconsole("m_name = 'Monika'", "Monika's name changed successfully.")
    l 114331 "Phew..."
    call hideconsole
    $ consolehistory = []
    show renier u1133
    l 114111 "That's a promising sign..."
    l "[persistent.playername], try putting her back now."
    l 334113 "(And let's all cross our fingers...)"
    show linda at uf
    while not check_character('monika'):
        ""
    show linda 114331 at std(p33)
    show renier u1113 at std(p31)
    show monika u113144 at std(p11)
    "Oh thank god..."
    show linda 114111
    show monika at thide
    hide monika
    if persistent.sayori_reset_ynr:
        "I catch Monika before she falls, having been positioned luckily."
        mc "I guess they're all going to come back unconscious or hurt."
        mc "Just like last time we did this..."
        mc "Following last time, it should be better if we reset the world before we restore the others."
        mc "We don't want to put them through that."
        show linda at foc
        l "What do you mean?"
        show linda at uf
        mc "When the game crashed after we put you in the first time, Yuri and Natsuki and Renier didn't appear at first, so Sayori tried to reset them."
        mc "It worked, but they all came back unconscious or hurt in whatever way they had been before."
        show linda at foc
        l 334221 "I see."
        l 334111 "Alright then, I suppose starting a new game is the better plan."
        $ persistent.newgame = 4
        l "We'll wait for you, [persistent.playername]."
        while True:
            ""
    else:
        play sound fall
        "Monika falls to the ground, unconscious."
        mc "What about [persistent.mc_favorite]?"
        mc "Please, bring her back next."
        show linda at foc
        l "As you wish..."
        $ temp = {"Sayori": 's', "Natsuki": 'n', "Yuri": 'y'}[persistent.mc_favorite]
        call updateconsole(temp + "_name = '" + persistent.mc_favorite + "'")
        call hideconsole
        $ consolehistory = []
        while not check_character(persistent.mc_favorite.lower()):
            show linda at foc
            l "[persistent.playername], we just need her file now."
        show linda at uf
        if persistent.mc_favorite == "Sayori":
            show sayori u116193 at std(p11)
            mc "Sayori!"
            show sayori at thide
            hide sayori
            "I rush to catch her before she falls."
            mc "Sayori?"
        elif persistent.mc_favorite == "Yuri":
            show yuri u11h172 at std(p11)
            mc "Yuri!"
            show yuri at thide
            hide yuri
            "I rush to catch her before she falls."
            mc "Yuri?"
        else:
            show natsuki u119155 at std(p11)
            mc "Natsuki!"
            show natsuki at thide
            hide natsuki
            "I rush to catch her before she falls."
            mc "Natsuki?"
        mc "Linda, is she okay?"
        show linda at foc
        l 334111 "Probably..."
        l "I don't see anything unusual about their data as compared to before."
        l "They might just be hurt from the script trying to 'purge' them."
        show linda at uf
        show renier at foc
        r u2113 "It sounds like everyone's going to come back this way."
        r "We should probably try to start a new game, right?"
        show renier at uf
        show linda at foc
        l "You're right."
        $ persistent.newgame = 4
        l "[persistent.playername], whenever you're ready."
        show linda at uf
        while True:
            ""
