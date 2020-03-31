label chapter26:
    scene driving with dissolve_scene_full
    pause 5.0
    scene city_night
    python:
        with open('ERROR.txt', 'w') as f:
            f.write("ERROR: not allowed while a POV character is being followed.")
    "We roll back into the town with the warehouse."
    "The first town he ever experimented in."
    "We make a short stop for food, and then head for the warehouse."
    play music determination
    show linda at foc
    l "Let's be really careful here."
    l "I don't see anything unusual yet, but it's {i}gotta{/i} be a trap."
    show linda at std
    show natsuki at foc
    n "You know, the longer I think about this, the dummer it seems."
    n "We're basically walking into a situation where we're likely to be shot at any second?"
    n "Honestly, it feels bleaker going into this than it did being on the clock and not having a lead."
    n "With no restore_character..."
    show natsuki at std
    show libitina at foc
    b "Worst case scenario, I'll open my Third Eye and ruin them all."
    b "Some of us might die, but we almost can't lose."
    show libitina at std
    n "Maybe, but still, dying is hardly an attractive thought!"
    n "Also, no you won't if you're the first one to get shot."
    show yuri at foc
    y "Actually..."
    y "We probably won't be ambushed."
    y "Adam doesn't want to kill us all."
    y "He demonstrated that earlier."
    y "He's afraid that [persistent.playername] will stop playing."
    y "And he can't do that until he succeeds in disconnecting the viewport."
    show yuri at std
    show natsuki at foc
    n "That's a good point..."
    n "I actually feel a lot better now. Thanks."
    n "Still though, we can't be sure."
    show natsuki at std
    mc "I feel like we should move faster."
    mc "We must look really suspicious."
    show yuri at foc
    y c125113 "Also... shouldn't we break Character.reset before we go into danger?"
    y "If our ability to win in case of an ambush depends on using our Third Eyes, we need to make sure he can't counter it."
    show yuri at std
    show monika at foc
    m c114111 "Good idea..."
    show monika c214113
    call updateconsole("ursula.reset()", "ERROR: escaped character.\nDisabling Character.reset.")
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
    l "Our least essential people should be in the front."
    show albert at foc
    al "Who's that?"
    al "Me and Natsuki, the only ones with no admin experience and no Third Eyes?"
    show albert at std
    l "I..."
    l "I'm sorry, but yes."
    show natsuki at foc
    n "Hold on now..."
    show natsuki at std
    show albert at foc
    al "Oh wait, maybe this doesn't even work."
    al "Assuming this is a trap, Adam's watching the viewport."
    al "Which, again, means he sees everything the POV character sees."
    show albert at std
    l "Good point."
    l "Well, crap, I guess he already knows we're here and everything we've said."
    l "Whether this is an ambush or not, there's no way he isn't watching."
    show albert at foc
    $ vpchar = mc_name if mc_dislike_player() < 2 else 'Renier'
    al "What if [vpchar] stays separate so he won't know exactly where we are?"
    al "[vpchar] could hang back a distance, maybe serve as a rear guard."
    al "That would mitigate Adam's information advantage."
    show albert at std
    mc "I guess that's true..."
    "I want to be with everyone else, but I also like the excuse to not be going into danger."
    mc "I can do that, then."
    menu:
        m "[persistent.playername], anything to say before we do this?"
        "Have you seen ERROR.txt?":
            pass
    m "Huh...?"
    "We all look at her curiously."
    m "Uh..."
    m "There's a file called ERROR.txt in the game directory that says 'ERROR: not allowed while a POV character is being followed'."
    menu:
        m "When did that appear?"
        "Seemed to appear right when the city loaded in.":
            pass
    m "..."
    m "I'm not sure what to make of that."
    m "Could be an error from something Adam tried that got automatically written to a file for some reason?"
    m "Because of the way the viewport skips time, if it appeared for you when the city loaded in then it could've happened at any point during the drive."
    m "I guess there's nothing to do about it right now."
    show linda at foc
    l "If something he did failed because \"a POV character is being followed\", we shouldn't leave [mc_name] alone."
    l "Maybe killing or knocking out [mc_name] would enable him to do some new plan we don't know about."
    show linda at std
    mc "So I am coming with you after all?"
    show linda at foc
    l "I think so. Maybe you should just close your eyes so you don't give away our exact position."
    l "And we'll keep you in the middle of the group."
    show linda at std
    mc "Um... okay..."
    "I end up closing my eyes and letting [persistent.mc_favorite] lead me by the hand."
#    "Me, Monika, and Libitina are in the center, since we're the three most important." TODO this depends on a lot
#    "Albert's taking point."
#    "Yuri, Renier and Linda are in the back, ."
    scene warehouse_outside_night
    "..."
    "I open my eyes in a flash when I hear a door opening."
    "We're here."
    "Albert walks in, pointing his gun."
    al "Doctor Markov?"
    al "You in here?"
    "We follow him into the building."
    scene warehouse_inside
    "Well, here we are in this horrid place one last time..."
    "But there doesn't seem to be anyone here."
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
    show libitina at foc
    b "I remember when he discovered in one of his first experiments that being cut make the Third Eye recede!"
    b "He tested it on me in this very room!"
    "Libitina's shaking with fury."
    show libitina at std
    show yuri at foc
    y "Try to stay calm..."
    y "This is a dangerous place for all of us Eye-bearers who were kept here."
    y "Given how sensitive yours is, you risk opening it if you don't stay calm."
    show yuri at std
    show renier at foc
    r "Holy shit..."
    r "What if..."
    r "... that was his plan?!"
    r "If I were him I'd've known fully well what being in this place would do to us."
    r "It's like he wanted to lure us into a place where one of us might snap and open her Third Eye."
    r "Especially given we were all here together and armed, any one of us who snapped could kill everyone else."
    show renier at std
    show yuri at foc
    y "But does that do him any good?"
    y "Wouldn't that just lead to us starting a new game?"
    show yuri at std
    l "Not without reset."
    l "We might not actually be able to start a new game, one way or another."
    l "With both restore_character and Character.reset gone."
    "..."
    l "It's also possible he {i}wanted{/i} us to start a new game now."
    l "With his other plan foiled, maybe he wanted to split us up for some reason?"
    l "Hard to say."
    "..."
    show albert at foc
    al "Frankly, I don't think he's coming."
    al "This wasn't an ambush. Maybe he just sent us here to buy time to think of a new plan."
    show albert at std
    # TODO what specifically prompts this?
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
    l "Have we been tricked?"
    l "That explains why it didn't work to make Libitina an admin."
    l "Maybe you didn't really do the thing."
    show monika at foc
    m "No, no, no!"
    m "I have to restore our memories."
    show monika c214212
    call updateconsole("for char in ('monika', 'libitina'):\n  char.old_memories.unlock()", "Monika's memories unlocked\nLibitina's memories unlocked")
    m c114282 "..."
    m c118382 "It's true!!"
    m "The last thing I remember is trying to fix the new game function and not being able to!"
    m "Adam must've snuck in while I was trying and used the opportunity to wipe my memories before I noticed him!"
    m "But wait...!"
    m "viewport.set_strict_mode worked!"
    m "So it must not've been a trick...!"
    show monika at std
    l "{i}No...{/i}"
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
    "The next few seconds are a flash."
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
    # Maybe Albert tries and Renier stops him? I like that. TODO
    scene city with wipeleft
    "I make it a few blocks away before I stop."
    "I turn around and pant."
    "I see the others catching up, and the backdrop behind them."
    "Outer space lies past the warehouse."
    "It looks like everyone escaped, except for Monika and Libitina."
    "The two most important members of our group."
    show renier at foc
    r "What the fuck happened!?!"
    show renier at std
    "I can barely hear him."
    show linda at foc
    l "Libitina..."
    l "... she snapped and shot to feed her Third Eye."
    show linda at std
    show yuri at foc
    y "No..."
    y "I think she got scared that Monika would snap and shot her out of fear!"
    y "Without thinking it through..."
    y "I'm so sorry, she caught me off guard...!"
    y "I should've stopped her!"
    show yuri at std
    show linda at foc
    l "Now we don't have Monika!"
    l "And she can't restore herself!"
    l "And without reset, we can't even use the rift to start a new game!"
    l "What the hell do we do?!?"
    show linda at std
    show renier at foc
    r "Beats me!"
    r "We've also lost [persistent.playername] then!"
    r "We're completely fucking screwed!"
    r "If his hack isn't done yet, it could be any minute!"
    show renier at std
    mc "Would we even know if he disconnected the viewport?"
    mc "Assuming he's right that it would make this world independent again?"
    show natsuki at foc
    n c117224 "There just has to be some way to bring Monika back!"
    n "We've always found a loophole in situations like this!"
    n "What haven't we tried?"
    n "[persistent.playername], think!"
    show natsuki at std
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
    r "We don't need you to tell us you murderous freak!"
    scene city with wipeleft
    "Around the corner, the screams are coming from a man being held against a wall and eye-gouged by another man."
    "The aggressor looks he has an open Third Eye alright."
    "That unmistakable look..."
    "(... Is this like the epidemic that happened in Yuri's town?!?)"
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
            pass # TODO If Adam still wants the POV to die, why wouldn't he let Renier do it and then make him POV?
    "Being reminded, Renier manages to stop himself from pulling the trigger."
    "Albert takes the shot."
    "He fires two, the second one landing in the head."
    "The attacker falls over."
    "The survivor runs away, still screaming."
    "..."
    show yuri at foc
    y "The epidemic that happened in my town!"
    y "It's happening here too...!"
    y "What have we done?"
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
    "Yuri also gives Linda her knife."
    show sayori at foc
    s "We need to get out of here!"
    show sayori at std
    show yuri at foc
    y "And we need to bring Libitina with us!"
    y "She's still the only way to really solve things."
    show yuri at std
    show renier at foc
    r "No problem, our car's not too far."
    scene warehouse_outside_night with wipeleft
    "We head back to the warehouse."
    "I hear a scream as we approach it."
    scene warehouse_inside_1_rift with wipeleft
    "The room inside is pretty much intact except for the rift."
    "I guess killing an admin sort of ends her frenzy, so she didn't have time to ravage the place like she did in the forest." # Maybe the equiv of this line should be in ch24.
    "Libitina's on the floor vomiting blood again, like she did after killing Adam."
    show yuri at foc
    y "Noooo!"
    show yuri at std
    b "Hel--"
    "More blood comes out."
    "More screams."
    show linda at foc
    l "Is it every time she catches an admin with her distortion...?"
    show linda at std
    show yuri at foc
    y "But I caught it before when it wasn't me who did it..."
    show yuri at std
    show linda at foc
    l "You were in the room, right?"
    l "And in the adjacent cell the other time?"
    l "Maybe it hits every other nearby Third Eye-bearer?"
    show linda at std
    "Renier picks up Libitina again."
    # What if Renier had caught it too from being slow to get out because he saved Albert?
    scene warehouse_outside_night with wipeleft
    scene city_night with wipeleft
    scene driving_night with dissolve_scene
    "We head back to where we parked, Albert takes the wheel, and we drive out of the city as fast as possible."
    "Libitina is still vomiting."
    "My heart aches watching her."
    "Yuri is crying."
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
        $ temp = "There's no way you'd be that stupid"
    else:
        s "We've worked with people who did horrible things before!"
        $ temp = "I should trust you"
    menu:
        " "
        "... - Adam":
            pass
    menu:
        " "
        "You're right. [temp]. Dammit. I'll meet you. - Adam":
            pass
    menu:
        " "
        "Take road 27 and pull over a good half a mile out of the city limits to make sure you're safe. - Adam":
            pass
    menu:
        " "
        "I will be there. - Adam":
            pass
    r "He's just sending us on another goddamn goose chase!"
    r "He's not gonna be there, and we'll lose even more time!"
    mc "Hold on!"
    mc "That ERROR.txt file a few minutes back!"
    mc "What if that was the result of his hack?"
    r "Eh...?"
    l "It's plausible..."
    l "The hack targeted the viewport."
    l "Could it be that he already completed the brute-force attack, but his exploit only works while the POV character is dead or unconscious?"
    l "It would seem skipping time doesn't count, or it would've worked while we were driving."
    l "But I bet you're right."
    l "I bet we're not on the clock anymore, but it's essential that we protect you."
    return
