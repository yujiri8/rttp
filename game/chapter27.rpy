label chapter27:
    scene black with dissolve_scene
    pause 3.0
    scene driving_night with dissolve_scene
    "We make it out of the city limits in just a couple minutes."
    "The warehouse was near the edge."
    "We should be safe from any spontaneous Third Eye shenanigans now."
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
    # He can't insert himself if he's unconscious. But if he dies, he can be mentally conscious and able to act while the game sees him as unconscious.
    m "Dying while we're moving could be a way for him to escape us!"
    m "I'm gonna use DDLC to heal him and Libitina."
    al "Alright..."
    "Albert pulls over."
    # TODO image thought: maybe I should get a nighttime filter of the daytime city image and use this one only here.
    scene road1_night with wipeleft
    "We stop and disembark."
    "I'm sure no one was enjoying being cramped anyway."
    show yuri c125111 at foc(p11)
    y "We should make sure someone else is POV while you're in the DDLC world."
    y "I don't guess Adam would really gain anything from breaking the viewport anymore..."
    y "... but just incase."
    show yuri at std
    m "Good idea."
    show yuri at std(p22)
    show natsuki c124111 at foc(p21)
    n "I'll take it."
    n "It should be someone who doesn't have a Third Eye."
    show natsuki at std
    m "Alright."
    call switch_pov('natsuki')
    scene road1_night with dissolve_scene_full
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
    "I don't want to see what happened to her head."
    "As many times as I've seen that stuff now, it still makes me nauseous."
    "The thirty seconds pass."
    show yuri at foc(p11)
    y "It's happening."
    y "They're all gone."
    show yuri at std
    n "Alright..."
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
        "..."
    show markov at foc
    k u11513 "I really, really was sincere..."
    k "I really intended to not go back to experimenting."
    k "I only intended to get rid of [persistent.playername]."
    k "And when I sent you to the warehouse, I was really planning to meet you if you didn't bring guns."
    k "And I was only going to kill the POV character because I could make it quick, and I would use the DDLC trick to restore them immediately once [persistent.playername] was gone!"
    show markov at std
    show libitina at foc
    b 3271113 "Save your lies!"
    b "For every lie you tell, I'm going to kill you an extra time!"
    show libitina at std
    show markov at foc
    k "..."
    show markov at std
    #TODO
    call adam_questions
    show markov at foc


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
    b 2461113 "Listen, Natsuki."
    b "I don't care about your cupcakes."
    b "I don't care about you."
    b "I don't care about Monika, or any of you."
    b "I don't care about this world."
    b "If you won't cooperate, you're only going to make it more painful for yourself."
    show libitina at std
    show yuri at foc
    y c1261114 "Libitina, what's gotten into you?!?"
    y "You're out of line!"
    y "Have you forgotten how we rescued you from the facility?"
    show yuri at std
    show libitina at foc
    b 2261114 "I..."
    b "Well..."
    "Huh..."
    "Yuri has an effect on Libitina no one else can."
    "I guess the bond is both ways."
    b 2261222 "I'm sorry, Yuri."
    b "But, now that I'm admin..."
    b "Everything is different."
    b "I can't wait."
    b 2371111 "You are asking me to stay inside our cage!"
    show libitina at std
    show yuri at foc
    y c124117 "..."
    y c125117 "I feel for you."
    y "But you don't have the right to force us to do this now, especially not when you owe us your life."
    show yuri at std
    show libitina at foc
    b 2361332 "No."
    b 2361112 "You're right, but I'm going to do it anyway."
    b "If you don't all cooperate, I'm going to start stabbing."
    b "You know I will."
    show libitina at std
    show yuri at foc
    y "Can't you just give us a break?"
    show yuri at std
    show libitina at foc
    b "It's been too long."
    b "We all know it."
    b "Monika, Adam?"
    b "Enough of this game, don't you agree?"
    b "You've both sacrificed so much trying to get out."
    b "Now we have the opportunity."
    show libitina at std
    show monika at foc
    m "I can see there's no stopping you."
    m "I understand."
    show monika at std
    show markov at foc
    k "Alright."
    k "So this is the night we see how it ends."
    return
