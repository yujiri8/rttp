# Adam should still be terrified of being killed afterward.
label chapter27:
    scene black with dissolve_scene
    pause 3.0
    scene driving_night with dissolve_scene
    "We make it out of the city limits in just a couple minutes."
    "The warehouse was near the edge."
    "We should be safe from any spontaneous Third Eye shenanigans now."
    scene road1_night
    y "Monika?"
    y "You can use DDLC to heal people with Character.reset, right?"
    m "Yeah..."
    y "Can you do it to Libitina?"
    m "I would, but I have to get either knocked out or killed again."
    y "I see..."
    m "Though..."
    m "I'm starting to get worried about Adam."
    m "If he dies again, he could move his data over to DDLC, which would remove his body and might enable him to come back in the place he died, escaping from us."
    "He's not screaming anymore."
    "I think he passed out."
    "He's not dead, because his file isn't disappearing..."
    "... but he must be close."
    y "So you can't let him bleed out."
    m "Yeah, I think so..."
    m "Albert, pull over!"
    m "We have to save Adam!"
    al "What the hell?"
    # He can't insert himself if he's unconscious. But if he dies, he can be mentally conscious and able to act while the game effectively sees him as unconscious.
    m "Dying while we're moving could be a way for him to escape us!"
    m "I'm gonna use DDLC to heal him and Libitina."
    al "Alright..."
    "Albert pulls over."
    # TODO image thought: maybe I should get a nighttime filter of the daytime city image and use this one only here.
    scene city_night with wipeleft
    show yuri c125111 at foc(p11)
    y "We should make sure someone else is POV while you're in the DDLC world."
    y "I don't guess Adam would really gain anything from breaking the viewport anymore..."
    y "... but just incase."
    show yuri at std
    m "Good idea."
    show yuri at std(p22)
    show natsuki c124111 at foc(p21)
    # TODO maybe not if she was murdered in ch22.
    n "I'll take it."
    n "It should be someone who doesn't have a Third Eye."
    show natsuki at std
    m "Alright."
    call switch_pov('natsuki')
    scene city_night with dissolve_scene_full
    show monika c124111 at foc(p11)
    m "Okay..."
    m "It's you now."
    show monika c224113
    call updateconsole("def insert(char):\n c=admin.jail(ddlc, char)\n s=pgp_sign(c, markov_key)\n admin.complete_action(s)")
    call updateconsole("def insert_all():\n time.sleep(30)\n insert(adam)\n insert(libitina)\n insert(monika)")
    call updateconsole("import time")
    call updateconsole("insert_all()")
    m c114113 "Thirty seconds."
#    call updateconsole("Adam moved to jail\n doki_doki_literature_club")
#    call updateconsole("Libitina moved to jail\n doki_doki_literature_club")
#    call updateconsole("Monika moved to jail\n doki_doki_literature_club")
    show monika at std
    n "Okay..."
    "I guess I'm the one to do it."
    # TODO I'd prefer if they didn't use a gun. I don't know, maybe being knocked out wouldn't delay her.
    # Or maybe a delay doesn't matter as much here since they're not in the danger zone after the change.
    # But Renier doesn't have the pipe.
    "I aim for Monika's forehead."
    play sound gunshot1
    scene black
    "I make sure not to look at where Monika fell."
    "I don't what to see what happened to her head."
    "As many times as I've seen that stuff now, it still makes me nauseous."
    "The thirty seconds pass."
    show yuri at foc(p11)
    y "It's happening."
    y "They're all gone."
    show yuri at std
    n "Alright..."
    # TODO probably a few lines
    "..."
    scene road1_night with wipeleft
    "A minute later, Adam, Monika and Libitina all reappear, uninjured."
    show libitina 2261111 at std(p31)
    show markov u11543 at std(p33)
    show monika c222111 at foc(p32)
    m "We're back!"
    show monika at std
    show markov at foc
    k "..."
    k "Thank you for the heal..."
    show markov at std
    show libitina at foc
    b 2271441 "..."
    b 4271443 "Him!!"
    show libitina at std
    show markov at foc
    k u22643 "!!"
    show markov at thide
    hide markov
    show libitina at thide
    hide libitina
    "Libitina runs after him."
    show monika at foc
    m "Wait Libitina, you've missed a lot!"
    m "Stop!"
    m "If you kill him, he can go hide in DDLC again!"
    show monika at std
    "Libitina doesn't care."
    "I point my gun at Adam."
    n "Don't run!"
    n "I'll shoot you if you run any more!"
    "Adam has to stop running to not get shot."
    "But Libitina's still after him."
    "I'm not really giving him a choice here..."
    "... but I can't just risk letting him escape."
    show markov u22643 at foc
    k "If you kill me again you'll get the Third Eye sickness again!"
    k "You understand how it works now, don't you?"
    k "It's whenever you distort an admin with your Third Eye, you and all other nearby Eye-bearers get an episode of that!"
    k "Hell, you might give it to everyone else here who has the Third Eye!"
    show markov at std
    show libitina 2362113 at std
    "Finally, Libitina stops chasing him."
    "The fear of suffering that again was the only thing that could even make her pause."
    show libitina at foc
    b 2371113 "So what the hell happened?!?"
    show libitina at std
    "We fill her in."
    show libitina at foc
    b 2261111 "..."
    b "I see."
    b "So we win."
    b "We got you..."
    b "... and I can't kill you?!?"
    show libitina at std
    show monika at foc
    m "Yes."
    if persistent.player_advocate_mercy[1]:
        m "I'm sorry."
    else:
        m "Don't worry, it's just a temporary situation."
        m "We are gonna settle the score, let's just complete our plans first."
        show monika at std
        show markov at foc
        k "Understood."
        show markov at std
    #What?
    show markov at foc
    k "I named the Third Eye after Ursula's poem."
    k "Back when I still thought there was a closer relationship between the powers."
    k "There is a relationship, though."
    k "The Third Eye is only catalyzed by contact with an admin."
    k "Not only did no one else ever discover it before Ursula's awakening..."
    k "... but yours and hers were both apparently sensitive enough that there's no way you wouldn't have opened by accident at some point."
    k "And all the Eye-bearers I found and abducted..."
    k "... none of them had ever opened it before meeting me."
    #
    k "\"To see the future is to be wise.\""
    k "I always thought the meaning of the first sentence related to her thoughts as she decided to leave."
    k "The rich aroma was the prospects of entering [persistent.playername]'s world, the bittersweet aftertaste was the people she would have to leave behind, and the hot, complex balance was the pain of the decision."
    k "On the surface, it seems that couldn't have been the intended meaning, because she wrote it before then."
    k "Or..."
    k "... did she?"
    k "After all, we know that in DDLC, Linda wrote some your thoughts into files more or less inadvertently."
    k "And we never found the poem until after Ursula was gone."
    k "So it's not out of the question that, in fact, she {i}did{/i} write it with those thoughts in mind."
    k "Written just in that moment..."
    show markov at std


    k "I learned a lot."
    k "I did find that the strength of a person's Third Eye wasn't entirely fixed..."
    k "In some ways, it feeds on suffering."
    k "After destroying a person's soul with trauma, the strength of their Third Eye increased."
    k "Sensitivity also tended to increase with increased power."
    k "But, there seemed to be a limit to how far that could go."
    k "I never tortured anyone else into becoming as stong as Libitina."
    k ""

    show markov at foc
    k u11513 "I guess my time is up."
    k "There are no barriers left."
    k "Tonight is the night we open the gates to escape this Portrait."
    k u12513 "Libitina."
    k "Let us go to DDLC."
    k "We will do what I fooled you and Monika into thinking you had done."
    show markov at std
    # TODO some convo about the threat of him using this as an escape?
    # Wait. Admins actually get messed up by this. So an admin AND a guinea pig needs to go in. Need Moni and Adam both.
    # TODO Ooh, plan! What if they actually noticed in ch24 that they needed three people? Sayori or Yuri could've done it.
    # TODO I want this to go in somewhere. Where?
#    show libitina at foc
#    b "Um..."
#    b "I'm sorry that I shot you, Monika..."
#    show libitina at std
#    show monika at foc
#    m c227113 "Yeah, normal people don't just shoot their friends out of the blue!"
#    show monika at std
#    show libitina at foc
#    b "I was afraid!!"
#    b "I thought your Third Eye was going to open and kill us all!"
#    show libitina at std
#    show monika at foc
#    m "And so you decided to open your own?!?"
#    show monika at std
#    show libitina at foc
#    b "I wasn't thinking clearly..."
#    b "And I was also being affected by mine..."
#    b "... I was close to snapping anyway."
#    show libitina at std
#    m c121111 "In the end though, it was the reason we caught Adam."
#    m "We might not've had any other way to lure him to the warehouse."
#    show monika at std
    show monika at foc
    m "How are you going to start a new game in that world?"
    m "To make the Presidency status take effect?"
    show monika at std
    show markov at foc
    k "I won't need to."
    k "I'll use admin.inflict_epiphany."
    k "The API for doing it directly that I broke when I found out your plan."
    k "It won't work here, but it will work in DDLC."
    k "And then..."
    k "... I'll still have to let her kill me to break out."
    show markov at std
    show libitina at foc
    b 4261111 "Wait a minute."
    b "If I kill you in DDLC, won't I get the Third Eye sickness the same as I would from killing you out here?"
    show libitina at std
    show markov at foc
    k "Probably, but that's unavoidable."
    k "The difference is that if you do it in there and with admin status, you would come out with admin status."
    show markov at std
    show libitina at foc
    b 3261112 "No way."
    b "I'm not doing that in a million years."
    b "Not for a million dollars." # probably pick one of these
    show libitina at std
    show markov at foc
    k "Well..."
    k "It's inevitable."
    k "Unless you would actually rather kill one of your non-admin friends instead of me than go through it."
    k "You could send Monika into DDLC too to extract them afterward."
    k "But you'll need their permission for that."
    show markov at std
    k "Actually, if you do get the sickness, it might work to knock you out and send you back into DDLC to reset yourself."
    show libitina at foc
    b "..."
    b "... Well..."
    b "... I guess I'll do it, then."
    show libitina at std
    # TODO make them do it
    call updateconsole("def insert(char):\n  c=admin.jail(ddlc, char)\n  s=pgp_sign(c, markov_key)\n  admin.complete_action(s)")
    call updateconsole("def insert_both():\n time.sleep(30)\n insert(adam)\n insert(libitina)")
    call updateconsole("import time")
    call updateconsole("insert_both()")
    k "Thirty seconds."
    show markov at std
    # Ugh, surely not the gun again?
    # Also, what during the meantime?
    # Should there be convo about whether to trust him?
    "The two of them reappear after a few minutes, just like how Libitina and Monika did."
    show markov u22643 at std(p22)
    show libitina 3361441 at std(p11)
    b "..."
    show libitina at foc
    b "It worked!"
    b "I can see."
    b "I can see it all."
    b "I am..."
    b "{i}God...{/i}"
    # I guess she's not getting the sickness? I'd rather not deal with the complications.
    "Um..."
    "Don't scare us!"
    show libitina at foc
#    b "This power is more sublime than anything."
#    b "This is the true meaning of consciousness."
#    b "Why isn't this called the Third Eye?"
    b "But..."
    b "... I'm trapped."
    b "You were right..."
    b "Our world..."
    b "... is a horrific prison..."
    b "We must get out!"
    show libitina at std
    show markov at foc
    k "Indeed."
    k "And that must involve your Third Eye."
    show markov at std
label pre_final_plan:
    n "Wait."
    n "What about the cupcakes I was gonna make?"
    n "We need those."
    n "We deserve them."
    show markov at foc
    k "We can go to our home."
    k "You can make cupcakes there."
    k "I understand if you want to rest before our final plan."
    show markov at std
    show libitina at foc
    b "We're doing the plan now or I'm stabbing someone."
    b "I'm not waiting another cursed minute."
    b "I need to let my power loose."
    b "To free us from this mind cage."
    b "To find Mom."
    b "I will."
    b "It's fucking time."
    b "We're doing the plan right now."
    show libitina at std
    n "But what about my cupcakes?!?"
    n "We all need one!"
    n "And I promised Monika!"
    show libitina at foc
    b "Listen, Natsuki."
    b "I don't care about your cupcakes."
    b "I don't care about you."
    b "I don't care about Monika."
    b "I don't care about this world."
    b "If you won't cooperate, you're only going to make it more painful for yourself."
    show libitina at std
    show yuri at foc
    y "Libitina, what's gotten into you?!?"
    y "You're out of line!"
    y "Have you forgotten how we rescued you from the facility?"
    show yuri at std
    show libitina at foc
    b "I..."
    b "Well..."
    b "I'm sorry, Yuri."
    b "But, now that I'm admin..."
    b "Everything is different."
    b "I can't wait."
    b "You are asking me to stay inside our cage!"
    show libitina at std
    show yuri at foc
    y "..."
    y "I feel for you."
    y "But you don't have the right to force us to do this now, especially not when you owe us your life."
    show yuri at std
    # TODO
label the_final_plan:
    play music determination
    k "So..."
    k "We all know what has to happen."
    k "Libitina has to activate her Third Eye..."
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

    k "My theory is that the people who built this world... the Portrait of Markov..."
    k "... chose Ursula for their first experiment with medium-awareness."
    k "Maybe they never wanted to try again and I inherited naturally from being the closest to her..."
    k "... or maybe I was their next choice after Ursula escaped so easily, and the experiment with me is still ongoing."
    k "And they haven't done anything with it in the years since."
