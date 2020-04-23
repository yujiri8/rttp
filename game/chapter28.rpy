label chapter28:
    show monika c114113
    show yuri c124114
    play music determination
    k fu511 "We all know what has to happen."
    k "Libitina has to open her Third Eye..."
    k "... open the portal..."
    k "... and then, she needs to be stopped before she can exit, so that the portal can be held open."
    k "All evidence indicates it will close if she steps through it."
    k "But if she doesn't, our best hope is the theory that it's only the energy of an open Third Eye passing through it that forces it shut."
    k "If that theory proves true, then we know how to get everyone out of this world."
    k "And if it proves false, we won't be deprived of our means of re-opening it."
    show markov at std
    show monika at thide
    hide monika
    show mc at std(p54)
    show libitina at std(p11)
    show yuri at std(p52)
    show albert 11111 at foc(p51)
    al "How are we possibly going to stop her?"
    al "We've seen that bullets can't touch her."
    show albert at std
    show markov at foc
    k "Bullets don't, but if anything will, other Third Eyes will."
    k "If we're lucky, [mc_name]'s rallying effect could be strong enough to keep her lucid and prevent her from forgetting the plan."
    k "But that's unlikely."
    k "If we're less lucky, perhaps other Third Eye-bearers can combine their powers to stop her."
    k "Maybe Monika, by combining her Third Eye with admin status again, could stop her."
    k "There's still a lot we don't know."
    k "But there isn't really any other way to learn more."
    k "There will be no more experiments."
    show markov at std
    show libitina at foc
    b "So I'm going to use you as fuel..."
    b "And then..."
    b "The other Eye-bearers are all going to open their Third Eyes too and try to fight me together?"
    show libitina at std
    show markov at foc
    k "Pretty much."
    k "But we have to make sure you don't kill me, or else you'll probably quit on the spot..."
    k "... like happened the other two times you killed an admin."
    show markov at std
    n "I could shoot you in the head after she takes enough blood to open her Third Eye, so it doesn't count as her killing you."
    show markov at foc
    k "That will probably work."
    k "It's our best shot."
    #k "Though I'm a little worried about it causing her to attack you..."
    show markov at std
    n "Count on me."
    show mc at foc zorder 2
    mc "My ability to open others' Third Eyes might come in handy here."
    mc "If I open mine first..."
    mc "Maybe I could get everyone else's open without them having to each kill someone."
    show mc at std
    show markov at foc zorder 3
    k "Indeed."
    k "We should make you POV."
    k "If you're the most important one to keep on target..."
    k "... besides the one who can't be..."
    k "... [persistent.playername] should be connected to you, so [persistent.player_subj_pronoun] can talk to you."
    show markov at std
    if mc_dislike_player() > 2:
        mc "Alright..."
    else:
        mc "Sounds good."
    show markov at foc
    call switch_pov(mc_name.lower())
    scene road1_night with dissolve_scene
    mc "..."
    if mc_dislike_player() > 2:
        "Guess you're back in my head again, [persistent.playername]."
        "It won't have to last long though."
    else:
        "Welcome back, [persistent.playername]."
    show albert 22112 at foc(p11)
    al "[mc_name], I will be your sacrifice."
    show albert at std
    mc "Eh...?"
    "{i}Without even being pressured...?{/i}"
    show albert at foc
    al "Someone must, and again, I'm the only who hasn't been through it or some equivalent horror yet."
    al "I also know you have more attachment to the others who haven't than to me."
    show albert at std
    "I..."
    "I don't know what to say."
    mc "I..."
    mc "Thank you."
    mc "Very much."
    "Albert gives a solemn nod."
    "Okay."
    show sayori c215113 at foc(p31)
    s "I can't believe we're doing this again..."
    show sayori at std
    show renier ru2133 at foc(p33)
    r "Just remember..."
    r "Last time..."
    r ru2131 "... it worked."
    show renier at std
label do_the_final_plan:
    show albert at foc
    al "[mc_name]..."
    al "You need to kill me first."
    al "Since your Third Eye will take longer to open than Libitina's."
    show albert at std
    show sayori at thide
    show renier at thide
    hide sayori
    hide renier
    "Okay... oh my God..."
    "I can't believe things have come to this."
    "I start to breathe hard and sweat just thinking about what I'm going to do."
    "I close my eyes."
    scene black with close_eyes
    "I imagine how the next few seconds are going to be."
    "I'm going to inflict that same pain on this man that I felt when Monika stabbed me."
    "I'm going to have to listen to his screams and keep stabbing him."
    "I'm going to go insane."
    "I'm deliberately entering a situation where I basically won't be in control of my actions..."
    "... and will be a huge danger to everyone around me."
    "What kind of deed is this?"
    "..."
    "I feel like it's a good sign that I hesitate longer than Monika did."
    "Does that make me a better person than her?"
    "... I'm just distracting myself."
    al "[mc_name], stop dragging out this tension."
    "I jump."
    "My eyes water again."
    "But yes... it's time to feed that dark monster I know is in me."
    "Here it... {i}fucking...{/i} goes."
    play sound stab
    play music our_reality
    "My mind is instantly flooded with flashbacks."
    "I forgot how already familiar I was with the feeling of stabbing someone from my time in the facility."
    "It's one of the most empowering feelings in the world."
    "I remember the people I killed during experiments and during my escape."
    "I remember how great each one felt."
    "I'm adding another one."
    "And it feels better than anything."
    play sound stab
    "I feel like I'm getting goosebumps all over."
    "My body convulses."
    "I hear the cries of my friends, almost drowned out by Albert's screams."
    "I hear [persistent.mc_favorite]'s cry."
    $ style.say_dialogue = style.edited
    "But I no longer feel any remorse."
    "My Third Eye is my God."
    "I do as it commands."
    "I am it."
    $ delete_character('albert')
    "I continue to make a mess of Albert's flesh."
    "The rivers of blood I spill are a sacrifice to God."
    "An offensively insufficient sacrifice."
    "I need more."
    menu:
        " "
        "[mc_name], remember! You need to open everyone else's Third Eye!":
            pass
    "Who?"
    "[persistent.playername]?"
    "..."
    "Who do you think you are?"
    "You don't compare to this power."
    "Why should I follow you?"
    "With my Third Eye, I am a greater being than you."
    menu:
        " "
        "You knew it was going to affect you like this! You're not a greater being if you can't resist an influence you thought you were prepared for!":
            pass
    "I am not the same person as [mc_name] before he opened his Third Eye."
    "That boy... was an imbecile."
    "He didn't know anything."
    "He couldn't {cps=8}{i}feel{/i}{/cps} anything."
    "Hell, he was nothing more than a minion of you."
    if persistent.player_allow_free_will_test:
        menu:
            " "
            "You remember how we proved that wasn't true!":
                pass
    else:
        # TODO is this necessarily true?
        menu:
            " "
            "You know from experience that's not true! You defied me before!":
                pass
        "Stop calling that imbecile me."
    "He may have had a slimmer of identity, but he still did what you asked."
    "He was still an extra in an endeavor controlled by you."
    "You sick control freak!"
    "You don't own me, [persistent.playername]!"
    "I will ruin your plan!"
    "{i}I{/i} am the God now!"
    "Who should I kill next?"
    "In the meantime, Libitina has stabbed Adam."
    "Her own Third Eye is open."
    play sound gunshot1
    $ delete_character('adam')
    "Natsuki fires the shot to end him before Libitina does."
    "As we planned, Libitina manages to open the portal."
    play sound glitch_horror
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch_basic
    pause 0.4
    hide screen tear
    scene portal with dissolve_scene
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch_basic
    pause 0.4
    hide screen tear
    call updateconsole("vp.choices_target = " + mc_name.lower())
    call screen dialog("I undid what Monika did to the choice system a long time ago, so your choices speak to " + mc_name + "'s mind again! - Adam", ok_action=Return())
    call screen dialog("This way you stand a chance to influence him without him resisting. - Adam", ok_action=Return())
    call hideconsole
    $ consolehistory = []
    menu:
        " "
        "Stop her.":
            pass
    menu:
        " "
        "She's trying to leave.":
            pass
    menu:
        " "
        "But killing her would be far more satisfying than killing anyone else.":
            pass
    "Ah..."
    "That's true."
    "She can't just walk away from me."
    "I'm going to kill her."
    "This is more fitting."
    "A better certification of my power."
    "A clash with her would be the perfect event to punctuate my rise to supremacy."
    "I try to attack her with my knife."
    show libitina at foc(p11)
    b 3371443 "Back, weakling!"
    show libitina at std
    play sound glitch_horror
    show distort1 zorder 100
    show distort2 zorder 100
    with Dissolve(0.2)
    "What in the fucking hell!?!"
    "I feel weak suddenly."
    "I can't see, and I feel the sharpest ambient pain I've ever felt..."
    "... like the pain of being in the glitched state when restoring Linda back then... but worse."
    "I drop to my knees."
    "I can't resist her distortion!"
    "She is..."
    "... a far stronger being than I am..."
    "I need help."
    mc "Sayori!"
    mc "Monika!"
    mc "Yuri!"
    mc "Renier!"
    mc "Assist me!"
    "Come on...!"
    "I command their Third Eyes to open!"
    "I hear a shout from Sayori."
    "My headache clears partway..."
    show distort1:
        alpha 0.3
    show distort2:
        alpha 0.3
    with Dissolve(0.5)
    "I feel empowered again."
    "I hear a shout from Monika."
    "I think she's giving the rest of them a time advantage..."
    "... since nothing seems to happen between me and Libitina for the next few seconds."
    "I hear a shout from Renier."
    "He seems to inflict a similar weakening effect as Libitina does."
    show dark_overlay:
        alpha 0.0
        linear 1.0 alpha 0.4
        block:
            easein 0.8 alpha 0.3
            easein 0.8 alpha 0.6
            repeat
    "Only his is affecting her too."
    b "Grhh--"
    b "Back!!"
    b "Die!"
    b "Rrghh..."
    play sound gunshot1
    "Renier fires a shot while she appears weakened, but still nothing."
    show dark_overlay:
        linear 0.5 alpha 0.2
        block:
            easein 0.8 alpha 0.1
            easein 0.8 alpha 0.3
            repeat
    "Sayori's distortion kicks in again, lessening the effects of Renier's distortion on us but not on Libitina."
    "This is my moment."
    "Bullets can't penetrate her field, but a knife if it could get close..."
    "I run toward her."
    $ temp = glitchtext(10)
    mc "You're finished, {w=0.4}[temp]{nw}"
    show distort1:
        alpha 0.8
    show distort2:
        alpha 0.8
    $ temp = glitchtext(60)
    b "[temp]!!!"
    "No!"
    "How is she still so powerful?"
    "I collapse as I approach her."
    "Instead of sliding my knife into her throat, I feel hers slide into mine."
    show red_overlay:
        linear 0.1 alpha 0.7
    "N-no"
    "I can't lose..."
    "I hear a scream from Yuri."
    "I feel the physical space distorting."
    "From what little I can see, it's like the area is condensing into one point..."
    "... and suddenly, all of us are right next to each other."
    "Sayori, Monika, and Renier's effects can be more fully present."
    show red_overlay:
        linear 0.4 alpha 0.4
    show distort1:
        alpha 0.6
    show distort2:
        alpha 0.6
    "Yuri's able to resist crumbling in weakness under Libitina's power for a second."
    "She takes the knife I dropped..."
    show red_overlay:
        linear 0.4 alpha 0.3
    "... and stabs Libitina in the throat."
    b "Ff--"
    show distort1:
        linear 0.1 alpha 0.1
        linear 0.1 alpha 0.4
    show distort2:
        linear 0.1 alpha 0.1
        linear 0.1 alpha 0.4
    "There's a feeble hiccup in Libitina's distortion, like an engine sputtering out."
    show red_overlay:
        linear 0.4 alpha 0.2
    "Yuri continues to stab her in the chest and stomach."
    b "Uwaaaaah--!"
    "Libitina falls, and her distortion ceases entirely."
    show libitina at thide
    hide libitina
    play sound fall
    show distort1:
        linear 0.4 alpha 0
    show distort2:
        linear 0.4 alpha 0
    show red_overlay:
        linear 0.4 alpha 0
    $ renpy.music.set_volume(0.5, 1)
    "{cps=5}Victory...{/cps}"
    hide distort1
    hide distort2
    hide red_overlay
    "{cps=3}...{/cps}"
    "But I'm not done."
    "I didn't get to spill her blood."
    "My Third Eye isn't nearly satiated."
    "My throat has mostly healed from Sayori's distortion."
    $ renpy.music.set_volume(1.0, 1)
    "I pick up Libitina's knife."
    "And I look at Yuri."
    "She must become the next fuel."
    "She is worthy--"
    play sound gunshot1
    stop music fadeout 2.0
    "But I feel a great force strike me in the back before I can stab Yuri."
    $ style.say_dialogue = style.normal
    n "Noooooo!!"
    n "Stop!"
    n "You did it!"
    n "The portal's open!"
    "My energy fades entirely."
    show darkred_overlay:
        alpha 0
        linear 1.5 alpha 0.8
    "Oh god... what kind of pain is this..."
    "{cps=8}FFFFF-{/cps}"
    "I hear more ear-shattering bullets."
    "Natsuki and Linda are shooting all the active Eye-bearers to stop us."
    hide dark_overlay
    show darkred_overlay:
        linear 2.0 alpha 0.6
    "None of us are invulnerable to it like Libitina was."
    "They're..."
    show darkred_overlay:
        linear 2.0 alpha 0.5
    "By attacking our group, they're helping to make sure Sayori sees us as allies of circumstance a little longer, so her healing keeps affecting us."
    show darkred_overlay:
        linear 2.0 alpha 0.4
    "They leave her for last."
    show darkred_overlay:
        linear 2.0 alpha 0.3
    "Sure enough, I'm starting to feel like I haven't been shot."
    show darkred_overlay:
        linear 2.0 alpha 0.2
    "I can't see the wound on my back, but if Sayori's Third Eye keeps working..."
    show darkred_overlay:
        linear 10.0 alpha 0
    "But what if Sayori attacks them?"
    show natsuki c113221 at foc(p21)
    n "Sayori we won!"
    show natsuki at std
    show linda 119443b at foc(p22)
    l "Stand down!"
    show linda at std
    show natsuki at foc
    n "Remember why you did this!"
    show natsuki at std
    show linda at foc
    l "Don't make us shoot you!"
    show linda at std(p33)
    show natsuki at std(p11)
    show sayori c2151d6 at foc(p31)
    s "..."
    show sayori at std
    "Sayori can tell she can't kill them without the rest of us."
    "Knowing that seems to be giving her confliction."
    "Are they actually going to be able to talk her down...?"
    show sayori at foc
    s c2151d4 "..."
    show sayori at std
    "It looks like it's working!"
    "Just hesitating is pushing her Third Eye to recede."
    show natsuki at foc
    n "Remember the cupcakes!"
    n "You get two if you don't hurt anyone else!"
    show natsuki at std
    show sayori at foc
    s c2151d3 "..."
    show sayori c215113 with dissolve_cg
    s "Uhhrrh..."
    show sayori c215193 at std
    "Sayori seems to be reacting the same way Libitina did after emerging from DDLC as an admin."
    "She's managing to close her Third Eye."
    "She collapses along with the rest of us."
    show sayori at thide
    hide sayori
    s "Ahhhhhh..."
    "They did it."
    "They timed this so Sayori's positive distortion would heal our wounds before her own Third Eye closed."
    "Perfect..."
    show linda 334441
    show natsuki at foc
    n c113123 "We did it..."
    n "The portal's hanging open and we saved them..."
    n c114123 "Great job, Sayori... and all of you."
    show natsuki at std(p31)
    show linda at std(p11)
    show markov u11111 at foc(p33)
    k "I'm back..."
    show markov at std
    show natsuki c113122
    show linda 334444
    mc "Wait, {i}you're{/i} back?!?"
    "I'm ready to open my Third Eye again to kill him again."
    "We don't need him anymore, right?"
    show linda at foc
    l "He must've gone through DDLC..."
    show linda at std
    show markov at foc
    k u21513 "Wait, you didn't save Libitina?!?"
    show markov at std
    "Huh?"
    show natsuki c114124
    show linda 334443
    "I notice Libitina's still lying in the pool of her blood."
    "I guess Sayori's positive distortion wasn't applying to her because she never saw her as an ally."
    "I haven't been hearing her scream though."
    "Has she already bled to death?"
    "Oh crap... I think she has."
    "Yuri stabbed her in the throat."
    "She doesn't seem to be breathing."
    show markov at foc
    k u22643 "Shit...!"
    call console_hangopen("c=admin.jail(ddlc, li") # this wouldn't actually have worked even if he'd been fast enough. His namespace was reset on leaving DDLC.
    play sound2 glitch_basic
    call hideconsole
    $ consolehistory = []
    return
