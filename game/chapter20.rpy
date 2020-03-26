label chapter20:
    stop music fadeout 4.0
    pause 4.0
    "I'm woken by sounds of crying."
    "I lay still for a minute."
    "I feel like it's the middle of the night..."
    "It sounds like..."
    "... Monika?"
    m "... Not again..."
    "I open my eyes."
    play music t10 fadein 2.0
    scene hospital_room_night
    show dark_overlay zorder 100:
        alpha 0.95
    show monika u1131g4 at std(p11)
    with open_eyes
    m "(sniff)..."
    mc "Monika...?"
    show monika u1181i4
    m "Ohhh!"
    m "[mc_name]..."
    "I sit up."
    show monika u1142g4
    m "I-I'm-I-I'm so sorry..."
    m "I-I-I can't-"
    m "I'm-"
    mc "Okay, calm down Monika..."
    "Everyone else is starting to wake up too."
    s "Monika's awake...?"
    show monika at foc
    m u1141i2 "Sa..."
    m u1181i4 "I'm so sorry everyone!"
    m "I'm not a monster I promise...!"
    m u1171i4 "I couldn't stop it..."
    m "It was God..."
    show monika at std
    show natsuki u223111 at foc(p33)
    n "Okay, hold on!"
    n "What did you mean by that?"
    show natsuki at std
    show monika at foc
    m u1141i4 "The Third Eye..."
    m "The temptation..."
    m "It..."
    m "... felt like God..."
    show monika at std
    show natsuki u224111
    "..."
    show linda 334112 at foc(p31)
    l "Don't worry Monika, we understand."
    l "And the plan worked."
    l 334111 "You broke the script and that allowed us to get out."
    show linda at std
    show monika at foc
    m u1141i1 "Th...th..."
    m "Thank you..."
    m "Thank goodness..."
    m "It wasn't for nothing..."
    m u1141i2 "Are you all okay...?"
    show monika at std
    show linda at x(p52)
    show renier u1213 at foc(p51)
    r "Yeah..."
    r "... but I think I have a phobia of you holding a knife now."
    r "For shit's sake, I thought you were gonna make a single cut, not fucking kill me."
    show renier at std
    show monika u1141g4 at foc zorder 1
    "Monika squeezes a few more tears."
    m "Oh jeez, I'm so sorry..."
    m "I just wish I could take it back..."
    show monika at std zorder 0
    show renier at foc
    r "Well..."
    r "Like Linda said, it worked."
    r "You probably had to do what you did."
    r "The Third Eye gets tickled from any blood, but to open it all the way, and get the ability to break the rules..."
    r "... you have to spill a lot."
    r "Probably anything less than what you did wouldn't have worked."
    r "You're not Libitina..."
    show renier at std
    show monika u1142i4
    "..."
    show natsuki u222111 at foc zorder 1
    n "Well..."
    n "Ready to hear what happened after you..."
    n "... did whatever berserk admin mojo you did?"
    show natsuki at std
    show monika at foc zorder 2
    m u1141i1 "Yeah..."
    show renier u1115 at std(p61)
    show linda 123111 at std(p62)
    show monika at std(p63)
    show yuri u221111 at std(p64)
    show sayori u111111 at std(p65)
    show natsuki at std(p66)
    with None
    #show dark_overlay zorder 100:
     #   alpha 0.5
    hide dark_overlay
    with dissolve
    "I flip on some lights, and we recount our adventures since Monika was with us."
    show monika at xif(p63)
    m u112311 "Wow..."
    m "I can't believe you went through all that..."
    m "... without me..."
    m "Ahaha..."
    m u111311 "I remember being Clare, now, though."
    show monika at std
    mc "So, Monika..."
    mc "Can you give [persistent.playername] dialog boxes?"
    mc "We haven't been able to get through to [persistent.player_obj_pronoun] since Linda and Sayori both lost their admin status."
    show monika at foc
    m u114111 "Yeah, I should be able to..."
    show monika at std
    menu:
        " "
        "I can hear you.":
            pass
    show monika at foc
    m u112111 "Great!"
    m "I can reach [persistent.player_obj_pronoun]."
    show monika at std
    menu:
        " "
        "So where are we at?":
            pass
    show monika at foc
    m u114211 "I don't know..."
    m "I'm confused about this world."
    m "I saw the people in it, even with admin status."
    m u124211 "And that means they must be real, right?"
    m "But the world must still be virtual, because Markov and I have admin powers."
    m "I think..."
    show sayori u114112
    show linda 114113
    show natsuki u214114
    show renier u1113
    show yuri u124118
    m u114214 "... this world is just like DDLC, the only difference is that there are more prisoners."
    show monika at std
    show yuri at foc zorder 2
    y u125111 "But..."
    y "If the world is full of real people, can it really be fake?"
    y "Isn't it effectively real if the people here are real?"
    show yuri at std zorder 0
    show monika at foc
    m u114221 "..."
    m "You're right."
    m u114111 "The only thing that makes [persistent.playername]'s world count as real is that it's where the rest of the {i}world{/i} is."
    m "I guess... this world is kind of real, then."
    m "It might be the realest we'll ever get."
    m "I'll be disappointed if I can't escape to [persistent.playername]'s world..."
    m "But a world where a meaningful life is possible is as much as I could expect."
    m "If this world is what it seems to be..."
    m "... then I'm free."
    m "We're all free."
    show sayori u111111
    show natsuki u221111
    show yuri u111111
    show renier u1114
    show linda 121111
    show monika at std
    mc "So does that mean..."
    mc "... assuming Markov doesn't come back..."
    mc "We won?"
    mc "We escaped to {i}a{/i} reality?"
    mc "That's what we set out to achieve, right?"
    show monika at foc
    m u213113 "We still have to make sure this world is safe from Markov and his cult."
    m "I doubt he's really dead if he was an admin."
    m u124113 "Although I don't know why he's not restoring himself..."
    m "He's not giving himself a file."
    m "Maybe he got kind of messed up, like Sayori and I did by the emergency purge."
    m u114113 "But also..."
    m "The other problem with DDLC?"
    show sayori u115112
    show natsuki u214114
    show yuri u114113
    show renier u1113
    show linda 124113
    m "We couldn't survive if [persistent.playername] turned the game off."
    m u114212 "[persistent.playername]..."
    m "We have to try this."
    m "I'm really scared to find out..."
    $ persistent.shutdown_in_pom = False
    m u113213 "But I'll have to eventually."
    m "Just make a save first."
    show monika at std
    while not persistent.shutdown_in_pom:
        ""
label found_out_pom_dependent:
    scene hospital_room_night
    show renier u1113 at std(p61)
    show linda 124113 at std(p62)
    show monika u114211 at foc(p63) zorder 1
    show yuri u114113 at std(p64)
    show sayori u115112 at std(p65)
    show natsuki u214114 at std(p66)
    m "..."
    m "Are..."
    m "... you going to turn the game off?"
    menu:
        " "
        "I did.":
            pass
    show sayori u115111
    show natsuki u214113
    show linda 124111
    show yuri u114111
    m u114111 "Then..."
    m "... it worked?"
    m "I have admin powers, but no nightmares?"
    show monika at std
    show renier at foc zorder 1
    r u1213 "But wait..."
    r "Did time pass?"
    show renier at std
    show sayori u115112
    show natsuki u214114
    show yuri u114118
    show linda 124113
    show monika at foc
    m u114212 "..."
    m u117244 "No..."
    m u114214 "The timestamp..."
    m "Time passed in [persistent.playername]'s world, but not in this one."
    m "This world is still dependent on the viewport."
    show monika u117115
    play sound "sfx/smack.ogg"
    "Monika hits her fist on a nearby table."
    m u117113 "Our quest."
    m "Is not."
    m "Over."
    show monika at std
    show natsuki at foc
    n u223111 "Hold on a sec!"
    n "This world must've been running without a viewport just fine before we all got here!"
    n "Are you telling me connecting the viewport make this world dependent on it?"
    show natsuki at std
    show monika at foc zorder 2
    m u114213 "That's what it sounds like to me."
    show monika at std
    show natsuki at foc
    n u223114 "Then we just dragged everyone else in this world into our problem?"
    show natsuki at std
    show monika at foc
    m u114212 "I think so..."
    m "But I {i}will{/i} find a way to fix it."
    show monika at std
    show yuri at foc zorder 3
    y u126111 "Wait...!"
    y u125111 "This changed when [persistent.playername] changed the viewport destination, right?"
    y "Maybe it'll fix it if [persistent.player_subj_pronoun] points it back at the DDLC world."
    show yuri at std zorder 0
    show monika at foc
    m u114111 "Maybe..."
    m "I think it's too risky to test right now, though."
    m "If it didn't work, and [persistent.playername] couldn't connect back here..."
    m u114114 "Everyone in this world would be dead."
    m "Frozen forever."
    m u114113 "We can't risk such a thing."
    m u114212 "[persistent.playername], you wouldn't mind helping us a little longer, would you?"
    show monika at std
    menu:
        " "
        "I'll stick around as long as it takes.":
            show sayori u111111
            show yuri u121111
            show linda 121111
            show natsuki u214111
            show monika u111111 at foc
            m "Thanks."
            show monika at std
            show natsuki at foc zorder 1
            n xu4111 "It's not like [persistent.player_subj_pronoun] deserves any praise for it."
            show natsuki at std
            show monika at foc
            m u124111 "Natsuki..."
            show monika at std
            show natsuki at foc
            $ temp = persistent.player_subj_pronoun.title()
            n "[temp]'d be basically a mass murderer if [persistent.player_subj_pronoun] didn't."
            show natsuki at std
            show monika at foc
            m u121111 "Well... I guess that's true..."
            show natsuki xu1111
        "I didn't sign on for this... I'll stick around, but if you ever get the chance, you owe me, okay?":
            $ persistent.player_guilt_dokis[1] = True
            show monika u114312
            show natsuki u223112 at foc zorder 1
            n "Hey you jerk, it's not like it's our fault we're stuck in here!"
            n "Don't you try to guilt us!"
            show natsuki at std
            show monika at foc
            m "Don't worry [persistent.playername], I won't ever forget."
            show monika u114311
    show monika at std
    mc "So what are we doing?"
    mc "How do we make sure it's safe for [persistent.playername] to point the viewport away?"
    show monika at foc
    m u114111 "I don't know..."
    m u214111 "But there are a lot of things left to investigate."
    m "I should go to the place where Libitina broke everything."
    m "That sounds like there might be clues there."
    m u224111 "Markov also probably knows more, if he's still alive."
    m "Assuming he is, if it's possible, we should try to interrogate him..."
    m "But for the time being..."
    m "We should wait for Libitina to wake up before we do anything."
    m "She might be able to tell us more."
    return

