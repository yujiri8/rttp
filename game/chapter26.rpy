label chapter26:
    scene driving with dissolve_scene_full
    pause 5.0
    scene city_night
    python:
        with open('ERROR.txt', 'w') as f:
            f.write("ERROR: cannot work while a POV character is being followed.")
    # Also, POV switch?
        # maybe MC asks for you back if you've been nice to him, but not if you haven't.
        # Who do you get otherwise? Still Linda?
        # I think I'll write the version from MC's perspective.
        # It makes sense to stay with Linda if they do want to hide their POV.
    "We roll back into the town with the warehouse."
    "The first town he ever experimented in."
    "We make a short stop for food, and then head for the warehouse."
    play music determination
    l "Let's be really careful here."
    l "I don't see anything unusual yet, but it's {i}gotta{/i} be a trap."
    show libitina at foc
    b "Worst case scenario, I'll open my Third Eye and ruin them all."
    b "Some of us might die, but we almost can't lose."
    show libitina at std
    mc "Maybe, but still, dying isn't an attractive thought."
    mc "..."
    mc "I feel like we should move faster."
    mc "We must look really suspicious."
    show yuri at foc
    y c125113 "Shouldn't we break Character.reset before we go into danger?"
    y "If our ability to win in case of an ambush depends on using our Third Eyes, we need to make sure he can't counter it."
    show yuri at std
    show monika at foc
    m c114111 "Good idea..."
    show monika c214113
    call updateconsole("ursula.reset()", "ERROR: escaped character.\n Disabling Character.reset.")
    call hideconsole
    m c114113 "Well there we go."
    m "There's no reset and no restore."
    m "It does give us better odds of winning, but it's unnerving."
    $ consolehistory = []
    show monika at std
    show albert 11111 at foc
    al "We should move strung out, so if we do get ambushed by cultists, they can't take us all out quickly."
    show albert at std
    l "That's a good thought."
    # TODO work this out
    "Albert volunteeers to be the most exposed as we approach the warehouse."
    "Natsuki and Linda agree to trail behind Albert, since they don't have Third Eyes."
    "Libitina and Monika are at the back, since they're our most important people."
    show albert at foc
    al "Oh wait... that won't even work."
    al "Assuming this is a trap, Adam's watching the viewport."
    al "Which means he sees everything the POV character sees."
    show albert at std
    "Well, crap, I guess he already knows we're here and everything we've said."
    show albert at foc
    al "What if our viewpoint character stays separate so he won't know exactly where we are?"
    show albert at std
    #
    menu:
        m "[persistent.playername], anything to tell us?"
        "Have you seen ERROR.txt?":
            pass
    m "Huh...?"
    m "Uh..."
    m "There's a file called ERROR.txt in the game directory that says 'ERROR: cannot work while a POV character is being followed'."
    menu:
        m "When did that appear?"
        "Seemed to appear right when the city loaded in.":
            pass
    m "..."
    m "I'm not sure what to make of that."
    m "Could be an error from something Adam tried that got automatically written to a file for some reason?"
    m "I guess there's nothing to do about it right now."
    #
    scene warehouse_outside
    "..."
    al "Here we go..."
    "Albert opens the door and walks in, pointing his gun."
    al "Doctor Markov?"
    al "You in here?"
    "We follow him into the building."
    scene warehouse_inside
    "Back to this horrid place one last time...."
    "There doesn't seem to be anyone here."
    show albert at foc
    al "It doesn't look like it was a trap."
    show albert at std
    show libitina at foc
    "Libitina gasps as she walks in."
    b "This place...!"
    show libitina at std
    show yuri at foc
    y "I vividly remember being cornered here that night."
    y "Hearing Mr. Markov's voice come to rescue me from a kinder death."
    y "What a place of hell..."
    show yuri at std
    show renier at foc
    r "Good lord..."
    r "I was recruited back in this era too."
    r "I did some of the experiments here...!" # this might make Libitina attack him.
    r "I..."
    r "There are so many other victims that never even got an escape like we did."
    r "We'll have to do whatever it takes to bring them back to life after this."
    show renier at std
    show libitina at foc
    b "I remember when he discovered in one of his first experiments that being cut closes the Third Eye!"
    b "He tested it on me in this very room!"
    "Libitina's shaking with fury."
    show libitina at std
    show yuri at foc
    y "Try to stay calm..."
    y "This is a dangerous place for all of us Eye-bearers who were kept here."
    y "Given how sensitive yours is, you risk your Third Eye opening if you don't try to stay calm."
    show yuri at std
    r "Holy shit..."
    r "What if..."
    r "... that was his plan?!"
    r "If I were him I'd've known fully well what being in this place would do to us."
    r "It's like he wanted to lure us into a place where one of us might snap and open her Third Eye."
    r "Especially given we were all here together and armed, any one of us who snapped could kill everyone else."
    # TODO this section needs a lot of patching
    "But does that do him any good?"
    "Wouldn't that just lead to us starting a new game?"

    "Not without reset."
    "We might not actually be able to start a new game, one way or another."
    "With both restore_character and Character.reset gone."

    "It's also possible he wanted us to start a new game now."
    "With his other plan foiled, maybe he wanted to split us up for some reason?"
    "..."
    r "You know, there's a pretty good chance he's not coming."
    r "Maybe it's not an ambush. Maybe he just sent us here to buy time to think of a new plan."
    
    menu:
         " "
         "Monika... are you sure you know what really happened when you three were in DDLC?":
             pass
    show monika at foc
    m "What do you mean...?"
    show monika at std
    menu:
        " "
        "We already know that APIs broken out here work inside DDLC...":
            pass
    menu:
        " "
        "... because warp was broken out here before DDLC, and you and Sayori and Linda used that in there.":
            pass
    menu:
        " "
        "So in that time he was in there with you two, he could've wiped and rewrote your memories.":
            pass
    show monika at foc
    m c114282 "No..."
    m "Oh no..."
    show monika at std
    "Have we been tricked?"
    "That explains why it didn't work to make Libitina an admin."
    #
    l "What if viewport.set_strict_mode wasn't real?!?"
    show monika at foc
    m c117382 "But that worked!"
    show monika at std
    l "It logged a message, and had a docstring."
    l "But the viewport object is shared between each admin's console namespace."
    l "And since it's Python, he could've added a method to it."
    l "I think viewport.set_strict_mode is a function he attached that does nothing but says it worked!"
    show monika at foc
    m c118382 "{cps=10}Nooooooo!!{/cps}"
    show monika at std
    "Monika's scream hurts my ears."
    "I remember Yuri's words of warning to Libitina..."
    "Monika's shaking with fury now."
    "The next few seconds are a flash."#
    "Sayori is trying to wrestle Monika's gun."
    "Monika continues to scream."
    "I run toward Monika to help Sayori..."
    play sound gunshot1
    "... but then I hear something fire."
    "And it looks Monika was the one who was shot."
    "I don't see who did it at first."
    "But my instinct is to flee back toward the door."
    play sound gunshot1
    pause 0.5
    play sound2 gunshot1
    "I hear more ear-shattering shots."
    "Shit, what's happening?"
    "As I reach the warehouse door, I glance back and notice it's Libitina shooting Monika."
    "Oh no, oh no, oh no..."
    "(Did she snap too?)"
    "Her distortion might kill us all!"
    "I make it out the warehouse door."
    "And bolt across the street."
    scene city with wipeleft
    "Hopefully the others make it out too."
    # would it be better if others shot Libitina?
    # maybe Albert tries.
    # but anyone who tries will likely fail. i want lib to survive and remain an active threat.
    # Is it ok if Albert or someone else tries and dies as a result?
    scene city with wipeleft
    "I make it a few blocks away before I stop."
    "I turn around and pant."
    "I see the others catching up, and the backdrop behind them."
    "Outer space lies past the warehouse."
    "It looks like everyone escaped, except for Monika and Libitina."
    "The two most important members of our group."
    r "What the fuck happened!?!"
    "I can barely hear him."
    l "Libitina..."
    l "... she snapped and shot to feed her Third Eye."
    show yuri at foc
    y "No..."
    y "I think she got scared that Monika would snap and shot her out of fear!"
    y "Without thinking it through..."
    y "I'm so sorry, she caught me off guard...!"
    y "I should've stopped her!"
    show yuri at std
    l "Now we don't have Monika!"
    l "And she can't restore herself!"
    l "And without reset, we can't even use the rift to start a new game!"
    l "What the hell do we do?!?"
    show renier at foc
    r "Beats me!"
    r "We've also lost [persistent.playername] then!"
    r "We're completely fucking screwed!"
    r "If his hack isn't done yet, it could be any minute!"
    show renier at std
#    mc "What if he already won, and we just haven't noticed yet?"
#    mc "When was the last time we asked [persistent.playername] a question?"
    mc "Would we even know if he disconnected the viewport?"
    mc "Assuming he's right that it would make this world independent again?"
    #
    "Hold on!"
    "That ERROR.txt file a few minutes back!"
    "What if that was the result of his hack?"
    #
    show natsuki at foc
    n "There just has to be some way to bring Monika back!"
    n "We've always found a loophole in situations like this!"
    n "What haven't we tried?"
    n "[persistent.playername], think!"
    show natsuki at std
    "I hear a long, thundering sound."
    "I watch the warehouse collapse."
    mc "Holy shit!" # TODO maybe this is bad dialog cuz it could've been just the slicing off of half that made it fall.
    # or maybe the warehouse shouldn't collapse, even though it's cool, because it'd kill Lib. it'll also cost me a ton of money.
    "She leveled the warehouse!"
    show renier at foc
    r "This is what the Third Eye's capable of..."
    show renier at std
    menu:
        " "
        "Christ! - Adam":
            pass
    "Adam!!"
    "You bast-"
    menu:
        " "
        "I didn't mean for this to happen! I swear! - Adam":
            pass
    menu:
        " "
        "If I could've done something, I would've, but she acted too fast! - Adam":
            pass
    show renier at foc
    r "You're responsible for this too!"
    r "Add this to the list of reasons you deserve to die!"
    show renier at std
    $ delete_character('monika')
    "I hear screams I don't recognize from someone around the corner."
    "Oh no..."
    menu:
        " "
        "Investigate! - Adam":
            pass
    "We don't need you to tell us you murderous freak!"
    scene city with wipeleft
    "Around the corner, the screams are coming from a man being held against a wall and eye-gouged by another man."
    "The aggressing man looks he has an open Third Eye alright."
    "That unmistakable look..."
    "Renier points a gun at the attacker."
    "I cover my ears."
    r "Only one way to..."
    menu:
        " "
        "Waaiiiit!! - Adam":
            pass
    menu:
        " "
        "Renier you have a Third Eye! - Adam":
            pass
    "Being reminded, Renier manages to stop himself from pulling the trigger."
    "Natsuki takes the shot."
    "She fires two, the second one lands in the head."
    "The attacker falls over."
    "The survivor runs away, still screaming."#
    "I don't know if he can see anything or if he realizes he was rescued."#
    "..."
    show yuri at foc
    y "The epidemic that happened in my town!"
    y "It's happening here too?!?"
    show yuri at std
    menu:
        " "
        "I knew it... - Adam":
            pass
    menu:
        " "
        "It wasn't something I did! It was Libitina killing me back in the facility that caused the outbreak in Yuri's town! - Adam":
            pass
    menu:
        " "
        "Killing an admin with the Third Eye messes things up, and not just the admin themselves. - Adam":
            pass
    l "That makes sense..."
    show yuri at foc
    "Yuri holds out her gun to Linda."
    y "We can't hold these!"
    show yuri at std
    "Linda takes it."
    "The rest of us Eye-bearers also hand off our guns."
    show sayori at foc
    s "We need to get out of here!"
    show sayori at std
    show yuri at foc
    y "And we need to bring Libitina with us!"
    y "She's still the only way to really solve things."
    show yuri at std
    # Should Libitina have got the Third Eye sickness?
    # is it every time she hits an admin with it?
    show renier at foc
    r "No problem, our car's not too far."
    scene warehouse_outside with wipeleft
    "We head back to the warehouse."
    "Renier picks up Libitina again."
    scene driving dissolve_scene
    "We head back to where we parked, Albert takes the wheel, and we drive out of the city as fast as possible."
    menu:
        " "
        "I want you to know, her death still isn't irreversible. I can still bring people back to life. - Adam":
            pass
    menu:
        " "
        "By using admin.jail, I can put dead people into DDLC, where restore_character works, and then restore and extract them. - Adam":
            pass
    menu:
        " "
        "I made sure to leave this workaround available because I never wanted to risk anyone permanently dying. - Adam":
            pass
    s "Use that to restore Monika!"
    s "If you're still expecting us to believe you're really sorry, then prove it!"
    menu:
        " "
        "I already tried... - Adam":
            pass
    menu:
        " "
        "I put her in DDLC where she should be able to restore herself and then re-extract. - Adam":
            pass
    menu:
        " "
        "But she isn't. - Adam":
            pass
    menu:
        " "
        "Maybe putting her in DDLC didn't fix her console. She's still messed up from Libitina's distortion.":
            pass
    menu:
        " "
        "True... - Adam":
            pass
    s "You're going into DDLC to reset her!"
    menu:
        " "
        "You're right. - Adam":
            pass
    menu:
        " "
        "If she's still in that horrid glitched state... I have to save her from it. - Adam":
            pass
    menu:
        " "
        "It's faster if I come to you and let you knock me out like you did with Monika than if I try to fall asleep. - Adam":
            pass
    menu:
        " "
        "I'd do that, but you'll shoot me on sight... - Adam":
            pass
    s "We won't shoot you on sight!"
    s "If you're really the only way we can save Monika... then we're not stupid."
    if persistent.player_advocate_mercy[0]:
        s "I want to torture you."
        s "I want to see you bleed and cry, just like you did to us..."
        "Sayori sniffles."
        s "But I'm not stupid."
    else:
        s "We've worked with people who did horrible things before!"
    menu:
        " "
        "... - Adam":
            pass
    menu:
        " "
        "You're right. There's no way you'd be that stupid. Dammit. I'll meet you. - Adam":
            pass
    menu:
        " "
        "Take road 27 and pull over a good half a mile out of the city limits to make sure you're safe. - Adam":
            pass
    menu:
        " "
        "I will be there. - Adam":
            pass
    r "We still don't have any goddamn reason to trust him."
    al "Well, again, he can't really ambush us."
    al "If he does anything but cooperate, we can shoot him."
    "Alright..."
    "This time, we'll be careful."
    "We're not going to walk into a trap."
    return
