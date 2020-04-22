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
    show renier at std
    show monika at foc
    m "Forget it."
    m "We know for certain that being killed won't mess up my console as long as its not by a Third Eye."
    m c114111 "So honestly, just shoot me."
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
    show monika c214113 at foc
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
    n "So when they get out, Libitina's going to be as powerful as them?"
    n "And shocked by the epiphany?"
    n "I gotta say that makes me kinda nervous."
    show yuri at foc
    y "I don't think she'll still be in shock from the epiphany."
    y "She'll have had it for a few minutes before they come out."
    show yuri at std
    "..."
    "I realize something that's probably going to upset Yuri... knowing how much more she cares for Libitina than I do."
    n "Yuri..."
    n "If she stabs Adam to open her Third Eye to break out, she's probably going to have that Third Eye sickness again."
    show yuri at foc
    y c114128 "..."
    y "..."
    y c114117 "It's unavoidable."
    y c114113 "Or maybe, if the plan works, we can send her back in where she can reset herself and then re-extract?"
    show yuri at std
    # Maybe Natsuki should ask Yuri whether the sickness is more painful than being stabbed.
    scene road1_night with wipeleft
    "A minute later, Monika and Adam reappear."
    show monika c214112 at foc(p11)
    show markov u22643 at std(p33)
    m "We're back...!"
    m "We left before she knocked herself out finishing him off, so she'd follow us with her Eye still open."
    m "Should be any..."
    show monika c114112 at std
    show libitina 3371443 at foc(p31)
    b "..."
    b "I..."
    b 3361443 "I got out..."
    b "Must kill..."
    b 2261224 "Uhhh--..."
    show libitina at std
    "She stumbles."
    "Like Monika before, it looks like breaking out pretty much sapped all her mojo."
    show libitina at thide
    hide libitina
    "She falls down."
    show markov u11413
    "I think her Third Eye's closing."
    b "Can't..."
    show markov u11613
    b "EKH--"
    "She sounds like she just had the first wave of a puke."
    b "No..."
    b "N--!"
    "It starts."
    "She pukes up a bit of blood."
    b "Yaaaaahhh!"
    show yuri c225138 at foc(p31)
    y "Do something!"
    show yuri at std
    show markov at foc
    k "She can't go back into DDLC while she's alive and conscious..."
    show markov at std
    b "Hel--"
    "More blood."
    "She can barely get any words out between it."
    show yuri at foc
    y c226134 "Natsuki!"
    y "Do it!"
    show yuri at std
    n "Wait, you mean shoot her?!?"
    show yuri at foc
    y "Yes!"
    y "It'll let her be put back into DDLC where she can be reset!"
    show yuri at std
    "Jeez!"
    n "Libitina, do you want me to-"
    "She manages to nod while she can't speak."
    "Guess I'm doing this again."
    "I point it at her head to make sure it kills her instantly."
    play sound gunshot1
    scene black
    "My eyes flinch closed again."
    "I still don't want to look."
    n "I feel like I'm getting desensitized to this." # Lol, it's me who's degrading its significance by using it for things like this so often. I'm super clever for having characters allude to criticisms of my story.
    k "She's gone."
    "I open my eyes."
    scene road1_night with open_eyes
    "There's still a pool of blood on the ground."
    show markov u11511 at foc(p33)
    k "I guess that means it worked."
    k "We didn't send her back to DDLC. She must've put herself back in after you killed her."
    k "So giving her admin status worked."
    k "She must be going to restore herself in just a minute."
    show markov at std
    n "So Monika, did you guess the name of the function that gives admin powers?"
    n "What was it?"
    show markov at foc
    k u21511 "I told her!"
    k "She didn't figure it out!"
    k "It's admin.inflict_epiphany, and I told her voluntarily {i}after{/i} I knew what she would do with it!"
    k "I helped you even when I knew I'd be stabbed!"
    show markov at std
    show monika c124211 at foc(p11)
    m "That's actually true..."
    show monika at std
    show mc c118113 at foc(p31)
    mc "So what?"
    mc "He just did it to earn trust!"
    mc "It means nothing!"
    mc "We're still going to make him pay for all of his crimes as soon as we're sure we don't need him!"
    show mc at std
    if not persistent.player_advocate_mercy[1]:
        show monika at foc
        m c113111 "I agree."
        show monika at std
    else:
        show monika at foc
        m c114222 "..."
        show monika at std
        "I don't get her."
        "She seems like she doesn't want to punish Adam."
        "How's that {i}possible{/i}?"
        "She went through way more at his hands than I did!"
    show markov at foc zorder 1
    k u11513 "This is the tragedy of sin."
    k "You have taken away my option to turn back, in that no matter what I do, it will not be recognized."
    k u11513t "I really, really was sincere..."
    k "Ever since you made me remember, I never intended to go back to experimenting."
    k "I only intended to get rid of [persistent.playername]."
    k "And when I sent you to the warehouse, I was really planning to meet you if you didn't bring guns."
    k "And I was only going to kill the POV character because I could make it quick, and I would use the DDLC trick to restore them immediately once [persistent.playername] was gone!"
    show markov at std
    show mc at foc
    mc "Oh, save your lies!"
    mc "We don't need to hear it."
    show mc at std
    show markov at foc
    k "{i}You don't want to think I'm sorry because then you couldn't hate me as much as you want to.{/i}"
    show markov at std
    show mc at foc
    mc "Not."
    mc "Another."
    mc "Word."
    mc "Monster."
    show mc at std
    show markov
    "Before long, Libitina comes out again."
    show markov at std(p44)
    show monika at std(p43)
    show mc c114111 at std(p42)
    show libitina 2261111 at foc(p41)
    b "..."
    b "It worked."
    b "Thanks so much, Natsuki."
    show libitina at std
    n "You're welcome."
    show markov at std(p55)
    show monika at std(p54)
    show mc at std(p11)
    show libitina at std(p52)
    show yuri c125111 at foc(p51)
    y "So what's it like to be have gained admin status?"
    show yuri at std
    show libitina at foc zorder 1
    b "It feels like being God."
    show libitina at std
    "Isn't that the same way Monika described the Third Eye?"
    show mc at foc
    mc c124115 "Don't scare me..."
    show mc at std
    show libitina at foc
    b "I'm on a whole new level of existence now."
    b "But I'm a God trapped in a jar for the amusement of [persistent.playername]..."
    b 2371113 "Monika and Adam were right!"
    b 2361113 "Our world is a horrific prison."
    b "And we must get out."
    show libitina at std
    show mc c124111
    show markov at foc
    k u11413 "Indeed."
    k "And that's going to involve your Third Eye."
    k "I'll be your fuel... again..."
    show markov at std
    call adam_questions
    k u11413 "Alright then..."
    show markov at std
label pre_final_plan:
    n "Wait."
    n "What about the cupcakes I was gonna make?"
    n "We need those."
    n "We deserve them."
    show markov at foc
    k u11511 "We can go to our home."
    k "You can make cupcakes there."
    k "I understand if you want to rest before our final plan."
    show markov at std
    show libitina at foc
    b "We're doing the plan now or I'm stabbing someone."
    show libitina at std
    show markov u11513
    show yuri c125115
    show mc c124135
    show monika c114212
    n "Whoa, cool it!"
    show libitina at foc
    b "I'm not waiting another cursed minute."
    b "I need to let my power loose."
    b "To free us from this mind cage."
    b 2361114 "To find Mom."
    b "I will."
    b 2361113 "It's fucking time."
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
    b "And I have admin powers of my own now."
    b "I don't depend on Monika anymore."
    b "I'm more powerful than any of you."
    b "I make the decisions now, and you have no choice but to do as I say."
    b "And if you won't cooperate, you're only going to make it more painful for yourself."
    show libitina at std
    show yuri at foc
    y c126116 "Libitina, what's gotten into you?!?"
    y "You're out of line!"
    y "Have you forgotten how we rescued you from the facility?"
    y "Do you understand how deep in debt to us you are?"
    show yuri at std
    show libitina at foc
    b 2261114 "I..."
    b "Well..."
    "It's amazing..."
    "Yuri has an effect on Libitina no one else can."
    "I guess the bond is both ways."
    show yuri c124113
    b 2261222 "I'm sorry, Yuri."
    b "I don't mean to forget what you did for me."
    b "But, now that I'm admin..."
    b "Everything is different."
    b "I can't wait."
    b 2371111 "You are asking me to stay inside our cage!"
    show libitina at std
    show yuri at foc
    y c124117 "..."
    y c125117 "I feel for you."
    y "But you don't have the right to force us to do this now."
    y "We're not all ready."
    show yuri at std
    show libitina at foc
    b 2261332 "No."
    b 2261112 "You're right, what I'm doing is wrong... but I'm going to do it anyway."
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
    show monika at foc zorder 1
    m c113114 "I can see there's no stopping you."
    m "I understand."
    show monika at std
    show markov at foc zorder 2
    k u11413 "Alright."
    k "So this is the night we see how it ends."
    return
