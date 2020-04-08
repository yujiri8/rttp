# Adam should still be terrified of being killed afterward.
label chapter27:
    scene driving_night
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
    al "What the hell?!?"
    # He can't insert himself if he's unconscious. But if he dies, he can be mentally concsious and able to act while the game effectively sees him as unconscious.
    m "Dying while we're moving could be a way for him to escape us!"
    m "I'm gonna use DDLC to heal him and Libitina."
    al "Alright..."
    "Albert pulls over."
    al "Let's make this quick! We're still in the danger zone."
    # maybe they should get out of the city before this.
    # TODO image thought: maybe I should get a nighttime filter of the daytime city image and use this one only here.
    scene city_night with wipeleft
    show yuri c125111 at foc(p11)
    y "We should make sure someone else is POV while you're in the DDLC world."
    y "I don't guess Adam would really gain anything from breaking the viewport anymore..."
    y "... but just incase."
    show yuri at std
    m "Good idea."
    show yuri at std(p22)
    # TODO maybe not if she was murdered.
    show natsuki c124111 at foc(p21)
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
    call updateconsole("def insert(char):\n  c=admin.jail(ddlc, char)\n  s=pgp_sign(c, markov_key)\n  admin.complete_action(s)")
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
    # But Renier doesn't have the pipe.
    "Everyone but me and Monika covers their ears."
    "On second thought, it was pretty dumb of me to volunteer for this when it could've been Linda."
    "Oh well. No more time to lose."
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
    n "I hope she gets back soon."
    n "We're still in danger every second we're in this city."
    # TODO probably a few lines
    "..."
    scene city_night with wipeleft
    "A minute later, Adam, Monika and Libitina all reappear, uninjured."
    show libitina 2261111 at std(p31)
    show markov u11543 at std(p33)
    show monika c222111 at foc(p32)
    m "We're back!"
    show monika at std
    show markov at foc
    k "..."
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
    b 2371113 "What the hell happened?!?"
    show libitina at std
    "We fill her in."
    show libitina at foc
    b 2262111 "Then..."
    b 2262114 "(To avoid having to go through that again...)"
    show libitina at std
    "We pile back in our transport and finish fleeing the city."
    "We're lucky enough to make it out before any of us gets struck by the random corruption."
    # TODO I feel there should be a lot more convo here, particularly with Adam, but I don't want it to be in the car (where no sprites are shown). Another reason to make them escape before reviving him and Libitina.
    scene black with dissolve_scene
    pause 3.0
    scene road1_night with dissolve_scene
    "We stop once we're a good half a mile out of the city limits."
    "We should be safe from spontaneous Third Eye shenanigans here."
    "We disembark."
    show albert at foc
    al "It's time for your judgement, Mr. Markov."
    show albert at std
    show markov at foc
    k "Indeed..."
    k "... you've won."
    k "Well done, everyone."
    show markov at std
    #
    show markov at foc
    k "I guess my time is up."
    k "There are no barriers left."
    k "Today is the day we open the gates to escape this Portrait."
    k "Libitina."
    k "Let us go to DDLC."
    k "We will do what I fooled you and Monika into thinking you had done."
    show markov at std
    # TODO some convo about the threat of him using this as an escape?
    # Wait. Admins actually get messed up by this. So an admin AND a guinea pig needs to go in.
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
    k "The difference is that if do it in there and with admin status, you would come out with admin status."
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
    b "This power is more sublime than anything."
    b "This is the true meaning of consciousness."
    b "Why isn't this called the Third Eye?"
    show libitina at std
    # Stitching.
    # TODO what about the plan to get cupcakes? I do kinda want it to fail, but it seems like they'd want to go do it now.
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

    k "My theory is that the people who build this world... the Portrait of Markov..."
    k "chose Ursula for their first experiment with medium-awareness."
    k "Maybe they never wanted to try again, or maybe I was their next choice after Ursula escaped so easily."
    k "And then they haven't done anything with it in the years since."

    "How are we possibly going to stop her?"
    "We've seen that bullets can't touch her."

    k "Bullets don't, but if anything will, other Third Eyes will."
    k "If we're lucky, [mc_name]'s rallying effect could be strong enough to keep her lucid and prevent her from forgetting the plan."
    k "But that's unlikely."
    k "If we're less lucky, perhaps other Third Eye-bearers can combine their powers to stop her."
    k "Maybe Monika, by combining her Third Eye with admin status again, could stop her."
    k "There's still a lot we don't know."
    k "But there isn't really any other way to learn more."
    k "There will be no more experiments."
    
    return
