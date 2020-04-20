label contact_sayori:
    scene road2 with dissolve_scene_full
    "I hope I don't end up regretting this decision..."
    "Maybe I should've stayed put and waited for Monika to come."
    "She restored my memories, so she must've got un-stuck."
    "But there's no taking it back now."
    "I just hope we're all meeting at the warehouse, but it seems less and less likely the more I think about it."
    menu:
        " "
        "Sayori, we can talk now!":
            pass
    "I startle so bad I swerve and..."
    show white:
        alpha 0.8
        linear 1 alpha 0.0
    s "Kya--!"
    "I fell off the bike!"
    hide white
    s "Owwww!!!"
    "I have a few scrapes, and I think my knee is bleeding."
    "Dang it!"
    s "Ow...!"
    menu:
        " "
        "Sorry! I had to talk.":
            pass
    "I drag myself off the road incase any cars come."
    menu:
        " "
        "Hold on, I've got a remedy! - Monika":
            pass
    call updateconsole("sayori.reset()", "0")
    call hideconsole
    $ consolehistory = []
    "My knee feels all better."
    s "Phew!"
    s "That Character.reset thing works like a charm!"
    menu:
        " "
        "I thought about breaking it earlier to stop Adam from using it to turn off people's Third Eyes. Glad I waited. - Monika":
            pass
    s "So what in the heck's going on?"
    menu:
        " "
        "(explain situation)":
            pass
    scene black with dissolve_scene
    scene road2 with dissolve_scene
    s "I see..."
    if not 'mc' in persistent.contacted:
        s "Well, with no directions, I kinda just figured I'd go to the warehouse."
        s "I figured it was the only place we could all separately agree to meet at without talking about it."
        s "I'm in the middle of nowhere now!"
        s "I guess it was a bad idea to start going after all..."
        call player_send_to_warehouse
        s "Okay then..."
        s "Guess I'm going to the spooky house of evil anyway."
    else:
        s "I was heading to the warehouse too..."
        s "I guess I'll keep going then."
    s "It sure is a lonely journey..."
    s "But I guess you better go switch to someone else."
    return
