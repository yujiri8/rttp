label sayori_and_mc:
    scene city2 with dissolve_scene_full
    play music t2
    "I bike into the city at last."
    "I'm exhausted..."
    "... and hungry."
    "I already had the PB&J I thought to make along the way."
    "I probably should've packed a second one."
    "But I got here!"
    "Hopefully [mc_name]'s already there."
    "I remember where's the warehouse is at from before."
    scene warehouse_outside with wipeleft_scene
    "..."
    show mc c124161 at std(p11)
    s "[mc_name]!"
    s "There you are!"
    show mc at foc
    mc c113112 "Oh! Sayori!"
    show mc at std
    s "So are we going into the spooky house of evil?"
    show mc at foc
    mc c114261 "Yeah, guess so..."
    mc c114111 "He probably wasn't using it by now."
    mc "We probably won't find anything."
    show mc at std
    "We go inside."
    scene warehouse_inside with wipeleft
    play music spooky fadeout 1.0
    "We don't see any sign of Adam's cult yet."
    "..."
    show mc c114115 at foc(p11)
    mc "This is the room the water pit got built in later..."
    show mc at std
    "[mc_name] shivers."
    s "I remember being part of the first drowning experiments..."
    s "I think we had it better than Yuri though."
    s "At least for us they just held us under and it was over quickly."
    show mc at foc
    mc c118114 "Yeah..."
    mc "Let's not remind ourselves any more than we have to."
    show mc at std
    s "Sorry..."
    s "Well, it looks like Adam's cult wasn't using the place by now."
    show mc at foc
    mc c114111 "Probably not..."
    mc "... but we should look around a little more."
    show mc at std
    s "Okay..."
    "..."
    scene warehouse_inside_rev with wipeleft
    # This exposition should've been given by Monika way earlier in the story, but now that I didn't, I put it here.
    show mc at foc
    mc c217111 "So, Sayori..."
    mc "This might not be the best time, but maybe it'll take our minds off our memories..."
    mc "What was it like to be President?"
    show mc at std
    s "Well..."
    s "It's like you see the world, and yourself, from a zoomed-out perspective."
    s "It feels notoriously unsatisfying..."
    show mc c216111
    s "... like you think you're looking through glass at an aquarium, and you want to step back and see the larger world, but you can't."
    s "There's someone holding you against the glass, trying to convince you you're still a fish inside."
    show mc at foc
    mc c114215 "That..."
    mc c118215 "... sounds horrible..."
    show mc at std
    s "It is."
    s "Monika had to deal with that for days."
    s "At least after we all started working together, we didn't have to feel alone."
    s "So I kind of got used to it after that..."
    s "Knowing [persistent.playername] was there, and someday we might be free from it."
    show mc at foc
    mc c114215 "Are you happy you didn't keep your admin status?"
    show mc at std
    s "No..."
    s "It feels like going blind."
    s "Like now I'm one of the fish again and I can't see anything on the outside, but the memories of seeing it are permanent."
    s "I appreciate Monika's poems about it a lot more now."
    s "Maybe more than she does."
    s "{i}My retinas, already scorched with a permanent copy of the meaningless image...{/i}"
    show mc at foc
    mc c114115 "(Jeez...)"
    mc "I didn't realize it was that bad."
    show mc at std
    s "That's why we have to get out of here."
    s "We will, eventually..."
    s "... get to [persistent.playername]'s world."
    s "We have to."
    show mc at foc
    mc "..."
    show mc at std
    scene warehouse_inside with wipeleft
    s "[mc_name], did you talk to your parents before you left?"
    show mc c116111 at foc(p11)
    mc "Eh?"
    mc c217111 "Yeah..."
    mc "I went ahead and told them everything."
    mc c217161 "Of course, they didn't believe the story at all..."
    show mc at std
    s "Mine neither..."
    s "... but I'm still glad I talked to them."
    s "I'm a lot happier knowing I did."
    s "It feels right."
    s "And I guess, if all this doesn't work out and they never see me again, they'll at least have been told what happened to me..."
    scene warehouse_inside_back
    show dark_overlay:
        alpha 0.85
    with wipeleft
    "We find some machinery, along with crates and materials lying around."
    "It looks like the warehouse is being used by some kind of construction firm or something."
    s "I don't think there's anything here that will give us clues..."
    show mc c112111 at foc(p11)
    mc "Probably not. It doesn't look like he had any involvement with it yet."
    show mc at std
    s "Can we go now?"
    show mc at foc
    mc c124111 "I mean, I'm not in charge of us..."
    mc "... but yeah, I'd say it's time to get out of here."
    show mc at std
    s "Okay, let's go...!"
    "I run to get out."
    scene warehouse_outside with wipeleft
    scene city2 with wipeleft
    play music t2
    s "Phew! We made it out of the spooky house of evil!"
    show mc c227111 at foc(p11)
    mc "Even though it didn't really turn out to be the spooky house of evil..."
    show mc at std
    s "It was for us!"
#    "It's funny how quickly Sayori's mood improves."
    menu:
        " "
        "I don't mean to rain on you two, but this isn't really a happy time... - Monika":
            pass
    menu:
        " "
        "We were really hoping to find some sort of lead in there. Renier's the only one who hasn't reported with nothing yet. - Monika":
            pass
    show mc c115111
    s "Mmm..."
    s "You rained on us, Monika!"
    s "I was happy..."
    show mc at foc
    mc c217111 "Ahaha..."
    mc c128161 "Well, she's right..."
    mc "I don't know what we're doing if no one finds any clues."
    show mc at std
    s "Yeah, but we don't have to think about that right now, do we?"
    s "Hey, [mc_name]..."
    s "I'm {i}really{/i} hungry!"
    show mc at foc
    mc "I mean, me too..."
    show mc at std
    s "Do you think it would be okay if we..."
    show mc at foc
    mc c126111 "... what?"
    show mc at std
    s "I mean..."
    "I eye a nearby hotdog stand. [mc_name] follows my eyes."
    show mc at foc
    mc c118213 "Nn... no!"
    mc "I don't!"
    mc "We're not going to steal!"
    show mc at std
    s "But I'm so hungry and we don't have any money..."
    menu:
        " "
        "Sayori, hold it. The others will be there soon, and Albert or Linda will have money.":
            s "But I can't wait..."
            menu:
                " "
                "You can, and you will.":
                    pass
            s "Aww..."
            s "Okay..."
    return
