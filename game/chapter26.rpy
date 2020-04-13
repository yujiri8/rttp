label chapter26:
    scene driving with dissolve_scene_full
    pause 5.0
    scene city_night with dissolve_scene
    python:
        with open(config.basedir + '/ERROR.txt', 'w') as f:
            f.write("ERROR: not allowed while a POV character is being followed.")
    "We roll back into the town with the warehouse."
    "The first town he ever experimented in."
    "We make a short stop for food, and then head for the warehouse."
    play music determination
    show linda 114111 at foc(p11)
    l "Let's be really careful here."
    l "I don't see anything unusual yet, but it's {i}gotta{/i} be a trap."
    show linda at std(p22)
    show natsuki c114114 at foc(p21)
    n "You know, the longer I think about this, the dumber it seems."
    n "We're basically walking into a situation where we're likely to be shot at any second?"
    n "Honestly, it feels bleaker going into this than it did being on the clock and not having a lead."
    n "With no restore_character..."
    show natsuki at std(p32)
    show linda at std(p33)
    show libitina 1261111 at foc(p31)
    b "Worst case scenario, I'll open my Third Eye and ruin them all."
    b "Some of us might die, but we almost can't lose."
    show libitina at std
    show natsuki at xif(p32)
    n c223111 "Maybe, but still, dying is hardly an attractive thought!"
    n c224111 "Also, no you won't if you're the first one to get shot."
    show natsuki at std(p43)
    show linda at std(p44)
    show libitina at std(p42)
    show yuri c125111 at foc(p41)
    y "Actually..."
    y "We probably won't be ambushed."
    y "Adam doesn't want to kill us all."
    y "He demonstrated that earlier."
    y "He's afraid that [persistent.playername] will stop playing."
    y "And he can't do that until he succeeds in disconnecting the viewport."
    show yuri at std
    show natsuki at xif(p43)
    n "That's a good point..."
    n xc4111 "I actually feel a lot better now. Thanks."
    n "We still can't be sure, though."
    show natsuki at std
    mc "I feel like we should move faster."
    mc "We must look really suspicious."
    show yuri at foc
    y c125113 "Hold on..."
    y "Shouldn't we break Character.reset before we go into danger?"
    y "If our ability to win in case of an ambush depends on using our Third Eyes, we need to make sure he can't counter it."
    show yuri at std(p52)
    show libitina at std(p53)
    show natsuki at std(p54)
    show linda at std(p55)
    show monika c114111 at foc(p51)
    m "Good idea..."
    show monika c214113
    call updateconsole("ursula.reset()", "ERROR: escaped character.\nDisabling Character.reset.")
    m c114113 "Well there we go."
    m "There's no reset and no restore."
    m "It does give us better odds of winning, but it's unnerving."
    call hideconsole
    $ consolehistory = []
    show monika at std(p62)
    show yuri at std(p63)
    show libitina at std(p64)
    show natsuki at std(p65)
    show linda at std(p66)
    show albert 11111 at foc(p61)
    al "We should move strung out, so if we do get ambushed by cultists, they can't take us all out quickly."
    show albert at std
    l "That's a good thought."
    l "Our least essential people should be in the front."
    show albert at foc
    al "Who's that?"
    al "Me and Natsuki, the only ones with no admin experience and no Third Eyes?"
    show albert at std
    show linda at foc zorder 1
    l 114113 "I..."
    l "I'm sorry, but yes."
    show linda at std
    show natsuki at foc zorder 1
    n c114214 "Hold on now..."
    show natsuki at std
    show albert at foc
    al "Oh wait, maybe this doesn't even work."
    al "Assuming this is a trap, Adam's watching the viewport."
    al "Which, again, means he sees everything the POV character sees."
    show albert at std
    show linda at foc zorder 2
    l 115112 "Good point."
    l "It sure is easy to forget that..."
    l 114112 "Well, crap, I guess he already knows we're here and everything we've said."
    l "Whether this is an ambush or not, there's no way he isn't watching."
    show linda at std
    show albert at foc
    $ vpchar = mc_name if mc_dislike_player() < 2 else 'Renier'
    al "What if [vpchar] stays separate so he won't know exactly where we are?"
    al "He could hang back a distance, maybe serve as a rear guard."
    al "That would mitigate Adam's information advantage."
    show albert at std
    if mc_dislike_player() < 2:
        mc "I guess that's true..."
        "I want to be with everyone else, but I also like the possibility of not going into danger."
        mc "I can do that, then."
    else:
        r "I guess that's true..."
        "I feel bad sitting out the most dangerous part, but it's not really something I can complain about."
        r "I could do that then."
    show monika c114111 at foc zorder 1
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
    m c114121 "..."
    m c114111 "I'm not sure what to make of that."
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
    if mc_dislike_player() < 2:
        mc "Um... okay..."
    else:
        r "Uh... okay..."
    "I end up closing my eyes and letting Monika lead me by the hand."
    scene black with close_eyes
    "Me, Monika, and Libitina are in the center, since we're the three most important."
    "Albert and Natsuki are taking point."
    $ temp = 'Renier' if mc_dislike_player() < 2 else 'MC'
    "Yuri, [temp], and Linda are in the back, since they're more important than an ordinary person but not as much as us in the center."
    "..."
    scene warehouse_outside_night
    "I open my eyes in a flash when I hear a door opening."
    "We're here."
    "Albert walks in, pointing his gun."
    al "Doctor Markov?"
    al "You in here?"
    "We follow him into the building."
    scene warehouse_inside_1 with wipeleft
    "Well, here we are in this horrid place one last time..."
    "But there doesn't seem to be anyone here."
    play music spooky fadeout 5.0
    show albert 11121 at foc(p11)
    al "It doesn't look like it was a trap."
    show albert at std(p22)
    show libitina 2271441 at foc(p21)
    "Libitina gasps as she walks in."
    b "This place...!"
    show libitina at std(p32)
    show albert at std(p33)
    show yuri c125117 at foc(p31)
    y "I vividly remember being cornered here that night."
    y "Hearing Mr. Markov's voice come to rescue me from a kinder death."
    y c125127 "What a place of hell..."
    show yuri at std
    show libitina at foc
    b 2271113 "I remember when he discovered in one of his first experiments that being cut make the Third Eye recede!"
    b "He tested it on me in this very room!"
    "Libitina's shaking with fury."
    show libitina at std
    show yuri at foc
    y c125117 "Try to stay calm..."
    y "This is a dangerous place for all of us Eye-bearers who were kept here."
    y "Given how sensitive yours is, you risk opening it if you don't stay calm."
    if mc_dislike_player() < 2:
        show yuri at std(p42)
        show libitina at std(p43)
        show albert at std(p44)
        show renier u2283 at foc(p41)
    r "Holy shit..."
    r "What if..."
    r "... that was his plan?!"
    r u1213 "If I were him I'd've known fully well what being in this place would do to us."
    r "It's like he wanted to lure us into a place where one of us might snap and open her Third Eye."
    r "Especially given we were all here together and armed, any one of us who snapped could kill everyone else."
    r "Including the POV character..."
    if mc_dislike_player() < 2:
        show renier at std
    show libitina 2261111
    show yuri at foc zorder 1
    y c125113 "But he sent us here before ERROR.txt appeared... right?"
    show yuri at std
    if mc_dislike_player() < 2:
        show renier at foc zorder 2
    r u12131 "Yeah, I'm not sure about that part..."
    if mc_dislike_player() < 2:
        show renier at std
    show albert at foc
    al "Well frankly, I don't think he's coming."
    al "This wasn't an ambush. Maybe he just sent us here to buy time to think of a new plan."
    if mc_dislike_player() < 2:
        show renier at std(p51)
        show yuri at std(p52)
        show libitina at std(p53)
        show albert at std(p54)
        show monika c114114 at foc(p55)
    else:
        show yuri at std(p41)
        show libitina at std(p42)
        show albert at std(p43)
        show monika c114114 at foc(p44)
    m "Well now I feel completely lost again."
    m "We're not on a clock anymore, but we still have no way to find him."
    m c114124 "I just don't get why that cheat to give Libitina admin status didn't work..."
    m "We did exactly the same things that worked for me!"
    show monika at std
    menu:
        " "
        "Monika... are you sure you know what really happened when you three were in DDLC?":
            pass
    if mc_dislike_player() < 2:
        show renier u1233
    show yuri c124118
    show libitina 2261114
    show albert 11112
    show monika at foc
    m c114312 "What do you mean...?"
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
    show libitina 2261444
    show yuri c114128
    show albert 11142
    if mc_dislike_player() < 2:
        show renier u11a3
    show monika at foc
    m c114282 "No..."
    m "Oh no..."
    if mc_dislike_player() < 2:
        show monika at std(p66)
        show albert at std(p65)
        show libitina at std(p64)
        show yuri at std(p63)
        show renier at std(p62)
        show linda 334443 at foc(p61) zorder 2
    else:
        show monika at std(p55)
        show albert at std(p54)
        show libitina at std(p53)
        show yuri at std(p52)
        show linda 334443 at foc(p51) zorder 2
    l "Have we been tricked?"
    l "That would explain it."
    l "Maybe you didn't really do the thing."
    show linda at std
    show monika at foc
    m c117382 "No, no, no!"
    m "I have to restore our memories!"
    show monika c214382
    call updateconsole("for char in ('monika', 'libitina'):\n  char.old_memories.unlock()", "Monika's memories unlocked\nLibitina's memories unlocked")
    m c114282 "..."
    m c118382 "It's true!!"
    call hideconsole
    $ consolehistory = []
    m "The last thing I remember is trying to fix the new game function and not being able to!"
    m "Adam must've snuck in while I was trying and used the opportunity to wipe my memories before I noticed him!"
    m c117382 "But wait...!"
    m "viewport.set_strict_mode worked!"
    m "So it must not've been a trick...!"
    show monika at std
    show linda at foc
    l 114332 "{i}No...{/i}"
    l 114112 "It logged a message, and had a docstring."
    l "But the viewport object is shared between each admin's console namespace."
    l "And since it's Python, he could've added a method to it."
    l "I think viewport.set_strict_mode is a function he attached that does nothing but says it worked!"
    show linda at std
    show monika at foc
    m c118382 "{cps=20}Nooooooo!!{/cps}"
    show monika at std
    "Monika's scream hurts my ears."
    "I remember Yuri's words of warning to Libitina..."
    "Monika's shaking with fury now."
    scene black with close_eyes
    stop music
    "The next few seconds are a flash."
    "Sayori is trying to wrestle Monika's gun."
    "Monika continues to scream."
    if mc_dislike_player() < 2:
        "I run toward Monika to help Sayori..."
    else:
        "[mc_name] runs toward Monika to help Sayori..."
    play sound gunshot1
    "... but then I hear something fire."
    "And it looks Monika was the one who was shot."
    "I don't see who did it at first."
    "But my instinct is to flee back toward the door."
    play sound gunshot1
    pause 0.5
    play sound2 gunshot1
    "I hear more shots."
    "Shit, what's happening?"
    "As I reach the warehouse door, I glance back and notice it's Libitina shooting Monika."
    if mc_dislike_player() < 2:
        "Oh no, oh no, oh no..."
    else:
        "Oh shit, oh shit, oh shit..."
    "(Did she snap too?)"
    "Her distortion might kill us all!"
    "I see Albert trying to shoot at Libitina."
    "But it's not even affecting her now that her Third Eye is open."
    "It looks like his bullets are just vanishing as they fly near her."
    if mc_dislike_player() < 2:
        r "Albert she's immune!"
        "Renier grabs Albert and starts dragging him away."
        r "You dumbass!"
        "{i}He's just going to get himself killed too!{/i}"
        "There's nothing I can do. I have to think about my own survival."
        "I make it out the warehouse door."
        "And bolt across the street."
        scene city_night with wipeleft
        "Hopefully the others make it out too."
        $ delete_character('monika')
        scene city_night with wipeleft_scene
        "I make it a few blocks away before I stop."
        "I turn around and pant."
        "I see the others catching up, and the backdrop behind them."
        "Outer space lies past the warehouse."
        "It looks like everyone escaped, except for Monika and Libitina."
    else:
        "Dammit, that moron!"
        r "Albert she's immune!"
        "He doesn't stop shooting."
        "What the hell's wrong with him?!?"
        "I run back toward him and grab him by the arm."
        "Hell if I'm gonna let him die like an idiot here."
        r "You dumbass!"
        "Finally he comes to his senses and starts following me."
        "Somehow we still manage to make it out the warehouse door before Libitina's distortion turns on and catches us."
        "I bolt across the street."
        scene city_night with wipeleft
        "Looks like everyone else made it out too."
        "Except Monika and Libitina, of course..."
        "The two most important members of our group."
        $ delete_character('monika')
        scene city_night with wipeleft_scene
        "We run a few blocks away before we stop."
        "I turn around and pant."
        "I see the backdrop behind the warehouse..."
        "It might a new rift alright."
    show albert 11142 at std(p11)
    "Albert looks the most shocked, the only one who's never witnessed something like that before."
    show albert at foc
    al "Renier..."
    al "Thanks..."
    al "I think I'd have died trying to stop her..."
    show albert at std
    if mc_dislike_player() < 2:
        show albert at std(p22)
        show renier u2283 at foc(p21)
    r "You're welcome..."
    r "So what the fuck happened!?!"
    if mc_dislike_player() < 2:
        show renier at std(p31)
        show albert at std(p32)
        show linda 119442 at foc(p33)
    else:
        show albert at std(p21)
        show linda 119442 at foc(p22)
    l "Libitina..."
    l "... she snapped and shot to feed her Third Eye."
    if mc_dislike_player() < 2:
        show linda at std(p43)
        show renier at std(p41)
        show albert at std(p42)
        show yuri c124128 at foc(p44)
    else:
        show linda at std(p32)
        show albert at std(p31)
        show yuri c124128 at foc(p33)
    y "No..."
    y c125128 "I think she got scared that Monika would snap and shot her out of fear!"
    y "Without thinking it through..."
    y c125127 "I'm so sorry, she caught me off guard...!"
    y "I should've stopped her!"
    show yuri at std
    show linda at foc
    l 119443 "Now we don't have Monika!"
    l "And she can't restore herself!"
    l "And without reset, we can't even use the rift to start a new game!"
    l "What the hell do we do?!?"
    show linda at std
    if mc_dislike_player() < 2:
        show renier at foc
    r "Beats me!"
    r "We've also lost [persistent.playername] then!"
    r "We're completely fucking screwed!"
    r "If his hack isn't done yet, it could be any minute!"
    show yuri c125128
    if mc_dislike_player() < 2:
        show renier at std
    else:
        show mc c118335 at foc(p41)
        show albert at std(p42)
        show linda at std(p43)
        show yuri at std(p44)
    mc "Would we even know if he disconnected the viewport?"
    mc "Assuming he's right that it would make this world independent again?"
    if mc_dislike_player() < 2:
        show renier at std(p51)
    else:
        show mc at std(p51)
    show albert at std(p52)
    show linda at std(p53)
    show yuri at std(p54)
    show natsuki c117224 at foc(p55)
    n "There just has to be some way to bring Monika back!"
    n "We've always found a loophole in situations like this!"
    n "What haven't we tried?"
    n "[persistent.playername], think!"
    if mc_dislike_player() < 2:
        show renier at std(p61)
    else:
        show mc at std(p61)
    show albert at std(p62)
    show linda at std(p63)
    show yuri at std(p64)
    show natsuki at std(p65)
    show sayori c227232 at foc(p66)
    s "It's useless!"
    s "Only Adam can do it now!"
    s "The only way to save Monika is to put her in DDLC where restore_character isn't broken..."
    s "... but the only person in the world who can do that now is Adam!"
    show sayori at std
    show natsuki at foc
    n "There {i}has{/i} to be something we can do!"
    show natsuki at std
    "We can't be beaten..."
    "Just five goddamn minutes ago we were all convinced we had it!"
    "There isn't a curse word in my vocabulary strong enough for this."
    menu:
        " "
        "I'm so sorry, everyone! - Adam":
            pass
    if mc_dislike_player() >= 2:
        show mc c118133 at foc
    mc "Adam!!"
    mc "You bastard!"
    if mc_dislike_player() >= 2:
        show mc at std
    menu:
        " "
        "I didn't mean for this to happen! I swear! - Adam":
            pass
    menu:
        " "
        "I did {i}not{/i} plan for Libitina to do that! - Adam":
            pass
    menu:
        " "
        "If I could've done something, I would've, but you broke Character.reset...! - Adam":
            pass
    if mc_dislike_player() < 2:
        show renier u2297 at foc
    r "You're responsible for this too!"
    r "Add this to the list of reasons you deserve to die!"
    if mc_dislike_player() < 2:
        show renier at std
    "I hear screams I don't recognize from someone around the corner."
    "Oh no..."
    menu:
        " "
        "Investigate! - Adam":
            pass
    if mc_dislike_player() < 2:
        show renier at foc
    r "We don't need you to tell us you murderous freak!"
    scene city_night with wipeleft
    "Around the corner, the screams are coming from a man being held against a wall and eye-gouged by another man."
    "The aggressor looks he has an open Third Eye alright."
    "That unmistakable look..."
    "(... Is this like the epidemic that happened in Yuri's town?!?)"
    if mc_dislike_player() < 2:
        "Renier points a gun at the attacker."
        show renier at foc(p11)
        r u2286 "Only one way to..."
        show renier at std(p21)
    else:
        "I point a gun at the attacker."
        r "only one way to..."
    # TODO Posing not done after here.
    show linda 118443 at foc(p22)
    l "Renier you have a Third Eye!!"
    show linda at std
    if mc_dislike_player() < 2:
        show renier u2283
        "Being reminded, Renier manages to stop himself from pulling the trigger."
    else:
        "Oh crap...!"
        "Don't pull the trigger, forget about it..."
        "I stop myself from pulling the trigger."
    "Albert takes the shot instead."
    play sound gunshot1
    pause 0.5
    play sound gunshot1
    "He fires two, the second one landing in the head."
    "The attacker falls over."
    "The survivor runs away, still screaming."
    "..."
    show renier at std(p31)
    show linda at std(p32)
    show yuri at foc(p33)
    y c128135 "The epidemic that happened in my town!"
    y "It's happening here too...!"
    y "What have we done?"
    show yuri at std
    menu:
        " "
        "I knew it... - Adam":
            pass
    menu:
        " "
        "It wasn't something I did! Libitina killing me back in the facility caused the outbreak in Yuri's town as well as the rift! - Adam":
            pass
    menu:
        " "
        "Killing an admin with the Third Eye messes things up, and not just the admin themselves. - Adam":
            pass
    show linda at foc
    l 116443 "That makes sense..."
    show linda at std
    show yuri at foc
    "Yuri holds out her gun to Linda."
    y "We can't hold these!"
    show yuri at std
    "Linda takes it."
    "The rest of us Eye-bearers also hand off our guns."
    "Yuri also gives Linda her knife."
    show renier at std(p41)
    show linda at std(p42)
    show yuri at foc(p43)
    show sayori c127132 at foc(p44)
    s "We need to get out of here!"
    show sayori at std
    show yuri at foc
    y c1251 "And we need to bring Libitina with us!"
    y "She's still the closest thing we have to an out."
    show yuri at std
    show renier at foc
    r u2133 "No problem, our car's not too far."
    scene warehouse_outside_night with wipeleft
    "We head back to the warehouse."
    "I hear a scream as we approach it."
    scene warehouse_inside_1_rift with wipeleft
    "The room inside is pretty much intact except for the rift."
    "Libitina's on the floor vomiting blood again, like she did after killing Adam."
    show yuri c128138 at foc(p21)
    y "Noooo!"
    show yuri at std
    b "Hel--"
    "More blood comes out."
    "More screams."
    show linda at foc(p22)
    l 11b113 "Is it every time she catches an admin with her distortion...?"
    show linda at std
    show yuri at foc
    y c124118 "But I caught it before when it wasn't me who did it..."
    show yuri at std
    show linda at foc
    l "You were in the room, right?"
    l "And in the adjacent cell the other time?"
    l "Maybe it hits every nearby Third Eye-bearer?"
    show linda at std
    show yuri c123128
    "Renier picks up Libitina again."
    scene warehouse_outside_night with wipeleft
    scene city_night with wipeleft
    scene driving_night with dissolve_scene
    "We head back to where we parked, Albert takes the wheel, and we drive out of the city as fast as possible."
    "Libitina continues to scream and vomit blood."
    "My heart aches watching her."
    "Yuri is crying."
    # I want Adam to claim he tried to put Monika into DDLC and have the player suggest that her console is still messed up, but it's contrary to his motives to say it.
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
    #TODO probably insert some of the speculation dialogue in SCRAPS in here.
    # Up until now, he was still waiting for them to get farther away.
    $ delete_character('adam')
    l "{i}Oh no.{/i}"
    l "He tricked us into leaving the area and now he's going to where Monika died!"
    l "He'll shoot himself, put himself in DDLC, reset Monika and then extract them both and have her alone!"
    l "He'll be able to make her POV and then kill her and run his hack!"
    al "Oh shit, I'm turning back!!"
    "Albert turns around as aggressively as possible."
    al "I can't believe we got fooled like this!"
    mc "I bet he was right near the warehouse waiting for this!"
    mc "We can't get back in time!"
    s "[persistent.playername], you have to switch the viewport destination back to DDLC!"
    s "And then turn it off to stop time from passing in that world long enough for us to get back to the warehouse!"
    s "Change DESTINATION.txt to say /jails/doki_doki_literature_club again!" # TODO make sure these directions are as clear as possible.
    $ persistent.autoload = "return_to_ddlc"
    while True:
        " "
    return

label return_to_ddlc:
    $ quick_menu = False
    scene black
    python:
        correct = False
        try:
            with open(config.basedir + '/DESTINATION.txt') as f:
                correct = f.read().strip() == '/jails/doki_doki_literature_club'
        except: pass
    if correct:
        jump returned_to_ddlc
    else:
        'Invalid destination.'
        $ renpy.quit()

label returned_to_ddlc:
    $ persistent.autoload = 'returned_to_ddlc'
    $ quick_menu = False
    $ vpchar = mc_name if mc_dislike_player() < 2 else "Renier"
    "{cps=200}Fatal error: player character missing.{/cps}"
    k "What?!?"
    "{cps=200}Fatal error: player character missing.{/cps}"
    m "What happened?"
    "{cps=200}Fatal error: player character missing.{/cps}"
    k "[persistent.playername]?"
    "{cps=200}Fatal error: player character missing.{/cps}"
    m "You set the viewport destination back?"
    "{cps=200}Fatal error: player character missing.{/cps}"
    k "See, [persistent.playername]?"
    k "I told you my intentions were pure!"
    "{cps=200}Fatal error: player character missing.{/cps}"
    k "I just shot myself in the forehead to come here to save her from the glitching!"
    "{cps=200}Fatal error: player character missing.{/cps}"
    # Is this suboptimal, since now that the viewport's pointing here, it's simpler for him to just do it in here, but that would take explaining?
    k "Now we're going to come out."
    $ persistent.autoload = 'return_to_pom'
    while True:
        " "
label return_to_pom:
    $ quick_menu = False
    scene black
    python:
        correct = False
        try:
            with open(config.basedir + '/DESTINATION.txt') as f:
                correct = f.read().strip() == '/'
        except: pass
    if correct:
        jump after_return_to_ddlc
    else:
        'Invalid destination.'
        $ renpy.quit()

label after_return_to_ddlc:
    $ persistent.autoload = None
    $ autosave()
    scene warehouse_inside_1 with dissolve_scene
    "I'm back."
    "I look around."
    "I see..."
    show markov at foc
    "No...!"
    "He picks up a gun that was laying right next to him."
    m "Noo!"
    "I still don't understand what's going on...!"
    "When he rescued me I really believed his intentions were sincere--"
    scene black
    "I hear a shot." # I hope I'm not invoking the "surprise it didn't really happen" trope
    "The flinch forces my eyes shut."
    "But I don't feel anything."
    n "{cps=40}GOT YOU!!{/cps}"
    "I reopen my eyes."
    scene warehouse_inside_1 with open_eyes
    show natsuki c215122 at foc(p21)
    show markov at std(p22)
    "Natsuki... shot Adam..."
    show markov at thide
    hide markov
    "Adam falls down, dropping his gun." # maybe someone else should run over and take it
    "He starts to scream."
    "The others come in."
    show natsuki at std(p32)
    show mc c118131 at foc(p31)
    mc "You got him?!?"
    mc c123331 "We win!!"
    show mc at std
    show natsuki at xif(p32)
    n c222113 "You did it, [persistent.playername]!"
    n "You slowed him down enough for us to get back just in time!"
    show natsuki at std
    k "No, nooooo!!"
    "Adam continues to scream in pain."
    "I'm still speechless at what just happened."
    "I'm breathing hard."
    show yuri at foc
    # Come to think of it, they already knew this from experience in DDLC.
#    y "Assuming he did shoot himself to be able to go back to DDLC, it doesn't look like his death made the rift get any worse."
#    y "It really is only when an admin is killed by a Third Eye."
    show yuri at std
    m "Hold it, I'm way out of the loop."
    m "What did I {i}miss{/i} after Libitina killed me?"
    "The others fill me in."
    m "So we're still in the danger zone?"
    show linda 124111b at foc
    l "Uh... yeah..."
    show linda at std
    m "We'd better get out, before it hits {i}me{/i}!"
    "I see the 'oh crap' look on everyone else's face."
    "I run toward the exit."
    m "Someone carry Adam!"
    m "He has to come with us!"
    "Renier and Albert together carry the mortally wounded Adam back to our vehicle."
    "It's really cramped, even with a 7-seat van."
    "We squeeze four of us on the back bench and place Adam on the floor, while Libitina, who's finished vomiting and passed out by now, lays across our laps on the back."
    scene city_night with wipeleft
    scene driving_night with wipeleft_scene
    al "Where are we going?"
    m "Anywhere!"
    m "Just out of the city!"
    play sound car_speed
    "Albert speeds down the road like a madman."
    return
