label contact_linda:
    scene office with dissolve_scene_full
    if not persistent.contacted:
        play music stroll fadein 2.0
    "I read over the patient notes one last time before saving them."
    "Looks correct..."
    "Suddenly, my memories flood back."
    l "Aaah!"
    "I stand up out of the computer chair."
    l "What...!"
    l "What happened?!?"
    l "[persistent.playername]? Monika?"
    menu:
        " "
        "(explain situation)":
            pass
    scene black with dissolve_scene
    scene office with dissolve_scene
    l "I see..."
    l "This is horrible..."
    l "I'm so sorry I told you to--"
    menu:
        " "
        "Linda, there's no time! We need your help. - Monika":
            pass
    l "Okay..."
    if 'renier' in persistent.contacted:
        l "So I guess that strange text I got earlier was from Renier."
        l "From now on, we'll be able to stay in touch."
    else:
        l "This was before I met Renier, so I don't have him as a contact..."
        l "But I remember his number from after I did."
        l "Once you restore his memories, we'll be able to talk without you switching between us."
    l "I'll go find Albert and bring him up to speed too."
    l "He's part of this now."
    menu:
        " "
        "Good idea. I'll restore his memories. - Monika":
            pass
    scene hospital_hall with wipeleft
    scene lobby with wipeleft
    "I go behind the front desk."
    l "Albert!"
    l "Do you remember what happened?"
    al "Linda?"
    show albert 11211 at foc(p11)
    al "We must've started a new game alright!"
    al "Do you know what happened?"
    show albert at std
    l "Yes!"
    l "We need a better place to talk."
    show albert at foc
    al "Agreed."
    show albert at std
    "This must look crazy to the other employees and customers, but there's no time."
    scene hospital_outside with wipeleft
    show albert 11111 at foc(p11)
    a "So [persistent.playername], Monika?"
    al "What's going on?"
    show albert at std
    menu:
        " "
        "(explain situation)":
            pass
    scene black with dissolve_scene
    scene hospital_outside
    show albert 12111 at foc(p11)
    with dissolve_scene
    al "This isn't such a great situation..."
    al "So what's even our plan?"
    al "We've got to find this Adam somehow."
    show albert at std
    menu:
        " "
        "At least one adult should head to the warehouse.":
            pass
    if 'mc' in persistent.contacted and 'sayori' in persistent.contacted:
        $ text = "Sayori and " + mc_name + " are heading there on bikes, and"
    elif 'mc' in persistent.contacted:
        $ text = mc_name + " and probably Sayori are heading there on bikes, and"
    elif 'sayori' in persistent.contacted:
        $ text = "Sayori and probably " + mc_name + " are heading there on bikes, and"
    else:
        $ text = "Sayori and MC are probably heading there, and they're probably not traveling by car, so"
    menu:
        " "
        "[text] they could use a ride next time they need to get somewhere.":
            pass
    show albert at foc
    al "That makes sense."
    al "But it only requires one of us."
    al "What about the others?"
    show albert at std
    if 'yuri' in persistent.contacted and 'natsuki' in persistent.contacted:
        $ text = "Yuri and Natsuki both also need rides." # this doesn't really make sense if you talk to them before Renier, but w/e.
    elif 'yuri' in persistent.contacted:
        $ text = "Yuri also needs a ride, and probably Natsuki too."
    elif 'natsuki' in persistent.contacted:
        $ text = "Natsuki also needs a ride, and probably Yuri too."
    else:
        $ text = "Yuri and Natsuki probably both also need rides."
    menu:
        " "
        "[text]":
            pass
    show albert at foc
    al "If we head straight for the warehouse, we'll probably still arrive before [mc_name] and Sayori."
    al "So why don't Linda and I split up, so we can pick up Natsuki and Yuri as well before going there?"
    al "The two of us can deliver all required rides."
    show albert at std
    l "Sounds good!"
    "Albert and I both head out, me to pick up Yuri and him to pick up Natsuki."
    scene driving with dissolve_scene
    menu:
        " "
        "So Linda, do you think you could help me understand some console commands that I think are part of his plan to disconnect [persistent.playername]? - Monika":
            pass
    menu:
        " "
        "I wrote them down before he broke memory reading. - Monika":
            pass
    l "Sure! Read them out to me."
    scene driving with dissolve_scene_full
    l "Oh..."
    l "That's not good."
    l "It sounds like he's trying to brute-force a hash collision."
    l "How it's going to work, I'm not exactly sure, but I bet he's going to use it to overcome checksumming and get the viewport to accept an invalid packet that wil corrupt it, for good."
    l "I bet his plan works. He seems to know what he's doing."
    menu:
        " "
        "How long do we have?":
            pass
    l "Impossible to say without knowing the host's CPU power."
    l "But that he seems to think this is even a reasonable plan for him is itself an indication that it won't take very long."
    l "This is {i}really{/i} scary."
    l "I highly doubt we have more than a day or two."
    "The three of us tested how admin consoles use cores back in DDLC when we were working in [mc_name]'s room."
    "We found that each admin is allocated an equal share of the available CPU power..."
    "... so worse, we can't run our own CPU-intensive processes to detract from his."
    l "Also, Monika..."
    l "I remembered another API that might be important."
    l "The API for putting characters inside virtual reality subsystems."
    menu:
        " "
        "Wait, could I use that on Adam?!? - Monika":
            pass
    l "No, it only works on unconscious characters."
    l "I was going to say that might be why he hasn't used it on you, rather than it being broken."
    menu:
        " "
        "I see. - Monika":
            pass
    l "I doubt it would do much anyway."
    l "He and you both have access to his key that could get you out from the inside with admin.extract."
    l "But I can't be sure. If he could get you inside DDLC and then mess with it from the outside..."
    l "... I don't know what he could do."
    l "So just incase, whatever you do, don't fall asleep."
    l "I thought I should tell you now incase I don't get a chance later."
    menu:
        " "
        "I'll keep that in mind. - Monika":
            pass
    menu:
        " "
        "I doubt he wants to trap me since he thinks he has to keep [persistent.playername] hoping, but I'll make sure not to risk it. - Monika":
            pass
    menu:
        " "
        "Do you remember what the function's called, by any chance? It's worth a try even if he knows to avoid it. - Monika":
            pass
    l "If I remember correctly, it's admin.jail..."
    l "The first parameter is the world object, which you get by its name from admin.get_world, I think."
    call updateconsole("ddlc = admin.get_world(\n 'doki_doki_literature_club')")
    call updateconsole("ddlc", "<Virtual world 'doki_doki_literature_club'>")
    call updateconsole("challenge = admin.jail(ddlc, adam)", "ValueError: character conscious")
    menu:
        " "
        "Yeah, it didn't work. Thanks for telling me about it though. - Monika":
            pass
    l "Glad my knowledge is still helpful!"
    l "I miss teaching you and Sayori about the admin stuff."
    l "Well, goodbye for now then, I guess."
    return

label ask_linda_etas:
    scene driving with dissolve_scene_full
    "I flip the radio back off."
    "I normally listen to music while I drive, but it just seems inappropriate at a time like this."
    "The viewport music was always tailored to the situation or it played nothing if it didn't have anything appropriate, but the radio is so naive..."
    menu:
        " "
        "Linda, we're back.":
            pass
    l "Oh, hi."
    l "You contacted everyone?"
    menu:
        " "
        "Yep.":
            pass
    l "Alright..."
    menu:
        " "
        "Can you call Renier and Albert and find out their ETAs?":
            pass
    l "Already did."
    l "Albert will pick up Natsuki in a few minutes."
    l "I'll be coming into Yuri's town borders a few minutes after."
    l "Renier's got about an hour left."
    l "I also gave them each others' numbers, so they can talk directly now."
    menu:
        " "
        "Alright. We'll switch to Albert then.":
            pass
    return
