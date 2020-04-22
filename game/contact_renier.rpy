label contact_renier:
    scene city3 with dissolve_scene_full
    if not persistent.contacted:
        play music stroll fadein 2.0
    "I stand outside for a few seconds before going back in."
    "Going back to work after lunch has got to be worse than coming here in the morning, cause half the day is gone and I'm still at it."
    "Then suddenly, I start to have visions about all kinds of horrible stuff, and I feel like--"
    r "What the shit!"
    "I remember...!"
    "My god..."
    "..."
    "... but what happened?!?"
    "We were all in Albert's hospital and then..."
    menu:
        " "
        "(explain situation)":
            pass
    scene black with dissolve_scene
    scene city3 with dissolve_scene
    r "I see..."
    r "Damn."
    r "So we've got no clue where he is."
    r "I'm gonna head to where the facility eventually is."
    r "It probably isn't there yet."
    r "But maybe the place had some significance before that."
    r "Or maybe the rift is still there, and we can use it to break the world again."
    menu:
        " "
        "Alright. Just be careful. - Monika":
            pass
    r "I'm not sure 'careful' really applies when Adam could screw us all over permanently at any minute if he figures out how to disconnect the viewport, but okay."
    if 'linda' in persistent.contacted:
        r "So I guess that weird text I got earlier was from Linda."
        r "From now on, we'll be able to stay in touch."
    else:
        r "This was before I met Linda, so I don't have her as a contact..."
        r "But I know her number from after I did."
        r "Once you restore her memories, we'll be able to talk without you switching between us."
    r "You better switch to someone else now."
    return
