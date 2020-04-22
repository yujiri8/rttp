label contact_mc:
    scene road1 with dissolve_scene_full
    if not persistent.contacted:
        play music stroll fadein 2.0
    "Darn..."
    "Maybe I should've stayed put."
    "Will I even get there before sundown?"
    menu:
        " "
        "[mc_name], we can talk now!":
            pass
    "I startle so bad I swerve and almost fall off my bike..."
    "... but I manage to put my foot down and stop safely."
    mc "[persistent.playername]!"
    mc "Thank goodness!"
    mc "What the hell happened?!?"
    menu:
        " "
        "(explain situation)":
            pass
    scene black with dissolve_scene
    scene road1 with dissolve_scene
    mc "Jeez..."
    if not 'sayori' in persistent.contacted:
        mc "I don't know how to drive, so I was biking over to the town with the warehouse."
        mc "I figured it was the best place for me to go, since it's the only one we all know where to find."
        mc "I'm in the middle of nowhere now."
        call player_send_to_warehouse
        mc "Alright..."
        mc "Guess I gotta finish this journey."
    else:
        mc "Yeah, I was heading over to the warehouse too."
        mc "Figured it was better than waiting around."
    mc "I'm really regretting not working out more right now."
    mc "Well, thanks for contacting me."
    mc "It's a lot nicer having your assurance that I'm going to the right place."
    mc "I guess you better switch to someone else now."
    return


label player_send_to_warehouse:
    menu:
        " "
        "Actually, the warehouse might be a good place for you to head.":
            pass
    menu:
        " "
        "It could contain clues at where to find Adam, especially if he was using it already by this time.":
            pass
