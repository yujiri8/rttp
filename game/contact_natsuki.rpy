label contact_natsuki:
    scene bg kitchen with dissolve_scene_full
    if not persistent.contacted:
        play music stroll fadein 2.0
    "I pour the carrrots into the soup."
    "At least this will be really good."
    "I'm due for it after how today and the last few days have been."
    "With Mom and Dad finally breaking up..."
    "... and Elyssa deciding to stay with Mom..."
    "Suddenly, my memories come back."
    ma "..."
    "I let go of the stirring spoon."
    n "Oh my god!"
    $ dad_name = "Maria's Dad"
    dad "What?!?"
    "Dad looks over from the table where he's doing paperwork on an important phone call."
    "Ugh..."
    "How am I gonna...?"
    n "I have to go!"
    "I burst out the door."
    scene black with wipeleft
    "I need to think!"
    scene street1 with wipeleft
    "I run a ways away from the house."
    "I just had no idea how to talk to him."
    "But I think I remember everything I'm supposed to."
    n "Okay..."
    n "... So did it work?"
    if ch22_libitina_has_gun():
        menu:
            " "
            "Yes. And I'm really sorry about that back there. - Monika":
                pass
        n "Not your fault, Monika."
        if persistent.explicitly_advocate_murder_natsuki:
            n "But [persistent.playername], you are {i}lucky{/i} I'm okay!"
            n "Cause if I wasn't, I'd break a few of your ribs!"
            menu:
               " "
               "I'm sorry. But I had to.":
                    pass
            n "Save it."
            n "I don't want to hear your excuses or whatnot."
            n "If we ever meet in your world, you owe me."
            n "But for now, let's move on."
        else:
            n "But she's lucky I'm okay!"
            n "I still plan to bloody her nose."
            menu:
                " "
                "Natsuki, she had to...":
                    pass
            menu:
                " "
                "I'm sure you would've done it eventually, but the situation was too urgent.":
                    pass
            n "Save it!"
            n "You wouldn't be saying that if you were the one who got shot!"
            call screen dialog("[persistent.playername], I think she needs some time to think about it first. - Monika", ok_action=Return())
            "I feel like what I just said probably isn't true, which leaves a bad taste in my mouth."
            "[persistent.playername]'s argument kind of makes sense."
            "But it just wasn't okay for her to do that to me!"
            n "Anyway..."
            n "Where are we at?"
    else:
        "I'm alive after shooting myself. That's nice."
        n "Did we restart alright?"
        menu:
            " "
            "Yes, we got it. Thank you. - Monika":
                pass
        "I laugh a little."
        n "Well..."
        n "Ha!"
        n "I shot myself and survived!"
        n "Pretty badass, I'd say!"
        n "You're welcome, Monika."
    menu:
        " "
        "(explain rest of situation)":
            pass
    scene black with dissolve_scene
    scene street1 with dissolve_scene
    n "Oh, well crap..."
    n "What's the plan then?"
    n "What can I do?"
    $ temp = "Albert's on his way to pick you up."
    if not 'linda' in persistent.contacted:
        $ temp = "I'll send Linda or Albert to pick you up."
    menu:
        " "
        "Honestly, probably just wait where you are. [temp]":
            pass
    n "I'm staying here?"
    n "I was kind of hoping you'd give me a reason not to go back home..."
    n "Dad's gonna be mad I ran out on him like that after I told him I'd take care of the soup..."
    n "... and he's gonna want to what happened."
    n "I don't know what I'm gonna tell him."
    n "I have no proof and he'll get even more mad if I tell him the truth."
    n "But okay, I'll sort it out for now."
    n "You can switch to someone else."
    return

label albert_pickup_natsuki:
    scene computer_room with dissolve_scene_full
    menu:
        " "
        "We're back. Anything new?":
            pass
    n "[persistent.playername]?"
    n "No..."
    n "I'm just doing homework while I wait for Albert, to put Dad in a good mood."
    n "How soon will Albert get here?"
    menu:
        " "
        "Just a few minutes.":
            pass
    n "Good."
    n "I'm itching to get back with everyone."
    n "I already wrote a note for Dad."
    n "He deserves to know what's going on, even if he won't believe it for now."
    "..."
    "Not long after, I hear the sound of Albert arriving."
    "Perfect!"
    "I leave my note on Dad's desk and head out."
    scene street3 with wipeleft
    show albert 11211 at foc(p11)
    al "Natsuki!"
    al "Great to see you in one piece after that!"
    show albert at std
    if ch22_libitina_has_gun():
        n "Great to be in one..."
    else:
        n "Great to be in one!"
    n "Ready to go?"
    show albert at foc
    al 11111 "Did you tell your father...?"
    al "I'd feel very bad for him if you just left."
    show albert at std
    n "I left him a note..."
    show albert at foc
    al "Shouldn't you at least speak to him in person?"
    al "If my daughter disappeared on me like this with only a note, I'd be worried sick..."
    al "... and a bit angry, too."
    show albert at std
    n "Well..."
    n "... I don't think he'll take too well to this."
    n "I don't have an easy way to prove my story, and he's not just gonna let me leave if there's anything he can do about it."
    show albert at foc
    al "Alright."
    al "Let's go then, I guess."
    show albert at std
    "I climb into Albert's car and he pulls out."
    if persistent.mc_least_favorite != 'Natsuki':
        "I can't wait to see [mc_name]."
    scene driving with dissolve_scene
    al "Actually, [persistent.playername] and Monika..."
    al "Why don't Natsuki and I head to where you are first?"
    al "If Linda's already on the way to pick up [mc_name] and Sayori, it's best if we come pick up you and Libitina."
    al "That way we could sooner get everyone on wheels."
    n "I guess that does make more sense..."
    if persistent.mc_least_favorite != 'Natsuki':
        "I'll still see [mc_name] soon."
    menu:
        " "
        "Sounds good. - Monika":
            pass
    # She gives him the address, but I'm not going to make one up.
    al "Alright!"
    al "We're on our way."
    if ch22_libitina_has_gun():
        "..."
        al "I wanted to ask you something."
        "How do you feel about what happened back there?"
        "I sigh."
        al "I'm sure I'd be angry too."
        n "I hate to say it, but I'm over it."
        if persistent.explicitly_advocate_murder_natsuki:
            n "[persistent.playername] was right. There was no other choice."
            n "And I would've done the same thing."
        else:
            n "She had to..."
            n "... and I would've done the same thing."
        al "Ah..."
        al "Well, I'm glad to hear it."
    return
