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
    show monika at std
    n "Okay..."
    "Hi again, [persistent.playername]."
    show monika at foc
    m "If I can, I'll use the same chance to get Libitina's admin status granted."
    m "We know from earlier that there must be an API to grant it outside of the DDLC President priority system."
    m "And it won't be broken inisde there."
    show monika at std
    show renier u2113 at foc(p31)
    r "There's a problem..."
    r "I don't have the pipe."
    r "How am I supposed to knock you out?"
    r "Should I try to do it with my fist?"
    show renier at std # TODO pose
    show monika at foc
    m "Forget it."
    m "We know for certain that being killed won't mess up my console as long as its not by a Third Eye."
    m "So honestly, just shoot me."
    show monika at std
    n "Yikes..."
    n "... are you serious?"
    show monika at foc
    m "Yeah."
    m "I'll be able to come out in one piece."
    show monika at std
    n "Jeez."
    n "Okay then..."
    "The thought still makes me really uncomfortable."
    "I guess I'm gonna be the one to do it."
    show monika c224113 at foc
    call updateconsole("def insert(char):\n c=admin.jail(ddlc, char)\n s=pgp_sign(c, markov_key)\n admin.complete_action(s)")
    call updateconsole("def insert_all():\n time.sleep(30)\n insert(adam)\n insert(libitina)\n insert(monika)")
    call updateconsole("import time")
    call updateconsole("insert_all()")
    m c114113 "Thirty seconds."
    show monika at std
    "I aim for Monika's forehead."
    play sound gunshot1
    scene black
    "I make sure not to look at where Monika fell."
    "I don't want to see what happened to her head."
    "As many times as I've seen that stuff now, it still makes me nauseous."
    "The thirty seconds pass."
    scene road1_night with open_eyes
    show yuri c114112 at foc(p11)
    y "It's happening."
    y "They're all gone."
    show yuri at std
    n "Alright..."
    "..."
    #TODO a few lines
    scene road1_night with wipeleft
    "A minute later, Adam, Monika and Libitina all reappear, uninjured."
    show libitina 2261441 at std(p31)
    show markov u22543 at std(p33)
    show monika c222111 at foc(p32)
    m "We're back..."
    m "Libitina, tell me that..."
    show monika at std
    # I guess she's not getting the sickness? I'd rather not deal with the complications.
    # TODO Or maybe she'll come out with it, reset herself, and go back in and out.
    # Maybe she starts puking after her first few lines.
    show libitina at foc
    b 2261441 "It worked!"
    b "I can see."
    b "I can see it all."
    b "I am..."
    b "{i}God...{/i}"
    show libitina at std
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
    n "So Monika, did you guess the name of the function that gives admin powers?"
    n "What was it?"
    show markov at foc
    k "I told her!"
    k "She didn't figure it out!"
    k "It's admin.inflict_epiphany, and I told her voluntarily {i}after{/i} I knew what she would do with it!"
    show markov at std
    show monika at foc
    m "That's actually true..."
    show monika at std
    show libitina at foc
    b "He just did it to earn trust!"
    b "It means nothing!"
    show libitina at std
    show markov at foc
    k "..."
    k "This is the tragedy of sin."
    k "You have taken away my option to turn back, in that no matter what I do, it will not be recognized."
    k u11513 "I really, really was sincere..."
    k "Ever since you made me remember, I never intended to go back to experimenting."
    k "I only intended to get rid of [persistent.playername]."
    k "And when I sent you to the warehouse, I was really planning to meet you if you didn't bring guns."
    k "And I was only going to kill the POV character because I could make it quick, and I would use the DDLC trick to restore them immediately once [persistent.playername] was gone!"
    show markov at std
    show libitina at foc
    b 3271113 "Save your lies!"
    b "For every lie you tell, I'm going to kill you an extra time!"
    show libitina at std
    show markov at foc
    k "{i}You don't want to believe I'm sorry because then you couldn't hate me as much as you want to.{/i}"
    show markov at std
    #TODO
    call adam_questions
    show markov at foc
    k "Tonight is the night we open the gates to escape this Portrait."
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
    y c126114 "Libitina, what's gotten into you?!?"
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
    b 2261332 "No."
    b 2261112 "You're right, but I'm going to do it anyway."
    b "If you don't all cooperate, I'm going to start stabbing."
    b "You know I will."
    show libitina at std
    show yuri at foc
    y "Can't you just give us a break?"
    show yuri at std
    show libitina at foc
    b "It's been too long."
    b "We all know it."
    b 4261112 "Monika, Adam?"
    b "Enough of this game, don't you agree?"
    b "You've both sacrificed so much trying to get out."
    b "Now we have the opportunity."
    show libitina at std
    show monika at foc
    m c113114 "I can see there's no stopping you."
    m "I understand."
    show monika at std
    show markov at foc
    k "Alright."
    k "So this is the night we see how it ends."
    return
