label the_final_plan:
    play music determination
    k "We all know what has to happen."
    k "Libitina has to open her Third Eye..."
    k "... open the portal..."
    k "... and then, she needs to be stopped before she can exit, so that the portal can be held open."
    k "All evidence indicates it will close if she steps through it."
    k "But if she doesn't, our best hope is the theory that someone {i}else{/i} going through it {i}wouldn't{/i} close it."
    k "At least if it's a normal character."
    k "If that theory proves true, then we know how to get everyone out of this world."
    k "And if it proves false, we won't be deprived of our means of re-opening it."
    show markov at std
    # Don't they expect killing Adam alone will stop her?
    # Maybe being admin herself makes her not vulnerable to that, as they found out when she became one.
    "How are we possibly going to stop her?"
    "We've seen that bullets can't touch her."
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
    show markov at std
    mc "My ability to open others' Third Eyes might come in handy here."
    mc "If I open mine..."
    mc "Maybe I could get everyone else's open without them having to each kill someone."
    show albert at foc
    al 22112 "[mc_name], I will be your sacrifice."
    show albert at std
    mc "Eh...?"
    "{i}Without even being pressured...?[/i}"
    show albert at foc
    al "Someone must, and again, I'm one who hasn't been through it yet."
    al "The only one who hasn't suffered anything equivalent either."
    al "I also know you have more attachment to the others who haven't than to me."
    show albert at std
    "I..."
    "I don't know what to say."
    mc "I..."
    mc "Thank you."
    mc "Very much."
    "Albert gives a solemn nod."
    "Okay."
    show sayori at foc
    s "I can't believe we're doing this again..."
    show sayori at std
    show renier at foc
    r "Just remember..."
    r "Last time..."
    r "... it worked."
    show renier at std
    show markov at foc
    k "We should make [mc_name] POV."
    k "If he's the most important one to keep on target..."
    k "... besides the one who can't be..."
    k "... [persistent.playername] should be connected to him, so [persistent.player_subj_pronoun] can talk to him."
    show markov at std
    if mc_dislike_player() > 2:
        mc "Alright..."
    else:
        mc "Sounds good."
    show markov at foc
    $ switch_pov(mc_name.lower())
    scene road1_night with dissolve_scene
label do_the_final_plan:
    show albert at foc
    al "[mc_name]..."
    al "You need to kill me first."
    al "Since your Third Eye will take longer to open than Libitina's."
    show albert at std
    "Okay... oh my God..."
    "I can't believe things have come to this."
    "I start to breathe hard and sweat just thinking about what I'm going to do."
    "I close my eyes."
    "I imagine how the next few seconds are going to be."
    "I'm going to inflict that same pain on this man that I felt when Monika stabbed me."
    "I'm going to have to listen to his screams and keep feeding it."
    "I'm going to go insane."
    "I'm deliberately entering a situation where I basically won't be in control of my actions."
    "What kind of deed is this?"
    "..."
    "I feel like it's a good sign that I hesitate longer than Monika did."
    "Does that make me a better person than her?"
    "I'm just distracting myself."
    al "[mc_name], stop dragging out this tension."
    "I jump."
    "My eyes water again."
    "But yes... it's time to feed that dark monster I know is in me."
    "Here it... {i}fucking...{/i} goes."
    scene black
    play sound stab
    play music our_reality
    "My mind is instantly flooded with flashbacks."
    "I forgot how familiar I already was with the feeling of stabbing someone from my time in the facility."
    "It's one of the most empowering feelings in the world."
    "I remember the people I killed during experiments and during my escape."
    "I'm adding another one."
    play sound stab
    "I feel like I'm getting goosebumps all over."
    "My body convulses."
    "I hear the cries of my friends, almost drown by Albert's screams."
    "I hear [persistent.mc_favorite]'s cry."
    $ style.say_dialogue = style.edited
    "But I no longer feel any remorse."
    "My Third Eye is my God."
    "I do as it commands."
    "I am it."
    "I continue to make a mess of Albert's flesh."
    "The rivers of blood I spill are a sacrifice to God."
    "A gravely insufficient sacrifice."
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
    "I serve God!"
    "Who should I kill next?"

    "In the meantime, Libitina has stabbed Adam."
    "Her own Third Eye is open."
    # Even if this doesn't stop her in her tracks, it should still break shit, right?
    # Maybe MC interrupts her and she doesn't finish him off.
    # Or maybe they have someone else finish him off for fear of putting a rift on top of the scene.
    # or just her losing her mojo before opening the portal.
    # TODO probably the gate is opened now.
    "Ah..."
    "A contester."
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
    "My headache clears..."
    show distort1:
        alpha 0.3
    show distort2:
        alpha 0.3
    with Dissolve(0.5)
    "I feel empowered again."
    "I hear a shout from Monika."
    "I think she's giving the rest of them a time advantage, since nothing seems to happen between me and Libitina for the next few seconds."
    "I hear a shout from Renier."
    "He seems to inflict a similar weakening effect as Libitina does."
    show dark_overlay:
        linear 1.0 alpha 0.4
    "Only his is affecting her too."
    b "Grhh--"
    b "Back!!"
    b "Die!"
    b "Rrghh..."
    "Renier fires a shot while she appears weakened, but still nothing."
    show dark_overlay:
        linear 0.5 alpha 0.2
    "Sayori's distortion kicks in again, lessening the effects of Renier's distortion on us but not on Libitina."
    "This is my moment."
    "Bullets can't penetrate her field, but a knife if it could get close..."
    "I run toward her."
    $ temp = glitchtext(10)
    mc "You're finished, {w=0.4}[temp]"
    show distort1:
        alpha 0.7
    show distort2:
        alpha 0.7
    $ temp = glitchtext(60)
    b "[temp]!!!"
    "No!"
    "How is she still so powerful?"
    "I collapse as I approach her."
    "I feel her knife slide into my throat."
    show expression Solid("#f00"):
        linear 0.1 alpha 0.4
    "N-no"
    "I hear a scream from Yuri."
    "I feel the physical space distorting."
    "From what little I can see, it's like the area is condensing into one point..."
    "... and then re-expanding..."
    "... and suddenly, all of us are right next to each other."
    "Sayori, Monika, and Renier's effects can be more fully present."
    "Yuri's able to resist crumbling in weakness under Libitina's power for a second."
    "She takes the knife I dropped..."
    "... and stabs Libitina in the throat."
    b "Ff--"
    "There's a feeble hiccup in Libitina's distortion, like an engine sputtering out."
    "Yuri continues to stab her in the chest and stomach."
    b "Uwaaaaah--!"
    "Libitina falls, and her distortion ceases entirely."
    "{cps=5}Victory...{/cps}"
    "{cps=3}...{/cps}"
    "But I'm not done."
    "I didn't get to spill her blood."
    "My Third Eye isn't nearly satiated."
    "My throat has mostly healed from Sayori's distortion."
    "I pick up Libitina's knife."
    "And I look at Yuri."
    "She must become the next fuel."
    play sound gunshot1
    "But I feel a great force strike me in the back before I can stab Yuri."
    n "Noooooo!!"
    n "Stop!"
    n "You did it!"
    n "The portal's open!"
    "My energy fades entirely."
    $ style.say_dialogue = style.normal
    show expression Solid("#600"):
        linear 0.3 alpha 0.8
    "Oh god... what kind of pain is this..."
    "{cps=8}FFFFF-{/cps}"
    "I hear more ear-shattering bullets."
    "Natsuki and Linda are shooting all the active Eye-bearers to stop us."
    "None of us are invulnerable to it like Libitina was."
    "They're..."
    "By attacking our group, they're helping to make sure Sayori sees us as allies of circumstance a little longer, so her healing keeps affecting us."
    "They leave her for last."
    "Sure enough, I'm starting to feel like I haven't been shot."
    "I can't see the wound on my back, but if Sayori's Third Eye keeps working..."
    "But what if Sayori attacks them?"
    n "Sayori we won!"
    l "Stand down!"
    n "Remember why you did this!"
    l "Don't make us shoot you!"
    s "..."
    "Sayori can tell she can't kill them without the rest of us."
    "Knowing that seems to be giving her confliction."
    "Are they actually going to be able to talk her down...?"
    s "..."
    "It looks like it's working!"
    "Just hesitating is pushing her Third Eye to recede."
    n "Remember the cupcakes!"
    n "You get two if you don't hurt anyone else!"
    s "..."

    "The incredible thing is that none of us are dead."

    $ temp = glitchtext(200)
    call screen dialog("[persistent.playername], what the fuck is this static?!? - Libitina", ok_action=Return())
    call screen dialog("[temp]!! - Libitina", ok_action=Return())
    return
