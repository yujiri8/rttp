label contact_yuri:
    scene forest with dissolve_scene_full
    "I finish a fifth chapter."
    "I really should go home now."
    "I must've been out here for at least an hour."
    "But I don't want to go back home."
    "I've been avoiding Mom as much as I can lately."
    "I can't deal with all the drama between her and Dad."
    "I never believed they would actually break up."
    "But it's been this way for a few days now."
    "She's always talking about it..."
    "... and how angry she is that Maria decided to stay with Dad."
    "It feels like every minute I'm not hiding from the world, the world harasses me with a problem I can't solve..."
    "... but have to deal with the consequences of."
    "So I've started coming to the forest with a book as often as possible."
    "It's my oasis."
    "But of course, Mom doesn't like that either."
    "She's probably going to yell at me when I come back."
    "I still wonder if there was something I should have done."
    "If there was something I could have said to help them."
    "Suddenly, my memories come back."
    "I drop my book."
    e "Aaah!"
    "..."
    "It all happened..."
    "I can't believe all that happened..."
    "I'm Yuri."
    "But what happened after we were all in Albert's hospital?"
    y "Monika? [persistent.playername]?"
    y "What's happening?"
    menu:
        " "
        "(explain situation)":
            pass
    scene black with dissolve_scene
    scene forest with dissolve_scene
    y "I see..."
    y "So we have to find... Adam... urgently, but we have no leads?"
    menu:
        " "
        "Yep... - Monika":
            pass
    y "This is a real fix, isn't it..."
    y "Is there something I can do?"
    y "Anywhere I should go to meet with the others?"
    $ temp = "Linda's on her way to pick you up." if 'linda' in persistent.contacted else "I'll send Linda or Albert to pick you up."
    menu:
        " "
        "[temp]":
            pass
    y "Alright then..."
    y "I'll stay put, I suppose."
    play music third_eye
    $ g1, g2, g3 = glitchtext(1), glitchtext(1), glitchtext(1)
    $ o_name = "???"
    o "El[g1]ys[g2]sa[g3]!"
    "I jump."
    "Is that..."
    show amy attacking at std(p11)
    "What...?!?"
    "It's Mom!"
    "What's wrong with...?!"
    show amy at foc
    mom "El[g2]ys[g3]sa[g1], your Third Eye is drawing me closer[g1]..."
    show amy at std
    "Her voice is distorted, just like Monika's was when her Third Eye was open!"
    y "Aaaah!!"
    show amy attacking at thide
    hide amy
    "I turn and run."
    y "Monika, help!!"
    "I can hear her chasing after me."
    call updateconsole(*console_protect_yuri)
    play sound fall
    "I hear her collapse on the ground behind me."
    menu:
        " "
        "Got her! I'm lucky that worked! - Monika":
            pass
    call hideconsole
    $ consolehistory = []
    "She seems to have passed out."
    y "Thank you..."
    y "..."
    y "But I don't understand..."
    y "Doesn't Character.reset require knowing the character's name?"
    menu:
        " "
        "A workaround I discovered recently :) - Monika":
            pass
    menu:
        " "
        "There are ways to get characters nearby a character I have a name for. I found out about it from reading Adam's command history. - Monika":
            pass
    menu:
        " "
        "He used it in his definition of the 'd' function he made as a shortcut to delete everyone near him. - Monika":
            pass
    y "I see..."
    y "..."
    y "But what could've done this to her?"
    y "I'm not surprised to find out she had a Third Eye, but..."
    y "... what set her off?"
    menu:
        " "
        "Better head back home and look around while Monika and I are still here, to make sure it's safe.":
            pass
    y "Uu..."
    y "Okay..."
    scene street2 with wipeleft_scene
    "I head back into town."
    "The streets are vacant."
    "Mostly..."
    "... I notice a man lying in a pool of blood near a house."
    "He's dead."
    "And looking the other direction..."
    "... I see another."
    y "What..."
    y "... is happening...?"
    menu:
        " "
        "Is it possible your mom activated her Third Eye somehow and went on a murder spree?":
            pass
    y "No, no, no..."
    "That can't be..."
    "I won't believe it..."
    "I run throughout the streets some more."
    scene street2 with wipeleft_scene
    "I find a third dead person before long."
    y "Oh no, this couldn't have been Mom..."
    menu:
        " "
        "(say nothing)":
            $ persistent.player_absolve_yuris_mom = False
        "It wouldn't be her fault.":
            $ persistent.player_absolve_yuris_mom = True
            y "I..."
            y "I know, but..."
            y "I still can't bear the thought."
    menu:
        " "
        "There have to be some alive people who know what happened. - Monika":
            pass
    "I run down the streets some more, and find..."
    "No one outside."
    "I don't even know if home is a good place to head--"
    $ o_name = "???"
    o "More blood...!"
    "I jerk my head around."
    show eric attacking at foc(p11)
    o "Raah!"
    show eric at thide
    hide eric
    "I bolt away from him."
    y "Monika, save me again!"
    call updateconsole(*console_protect_yuri)
    call hideconsole
    $ consolehistory = []
    play sound fall
    y "{i}Phew...{/i}"
    menu:
        "It's like multiple people became possessed by their Third Eyes and started killing people...":
            pass
    y "That's a horrible thought..."
    y "..."
    y "Okay..."
    y "I'm going to try entering."
    y "Everyone who's alive is probably staying inside with their doors locked."
    y "Which means everyone who will know what happened is inside."
    "I go up to the door of a house that boy was near."
    "I knock."
    y "Hello...?!?"
    y "Is anyone alive in there?"
    "..."
    "I knock again."
    "I guess no one's here."
    "I walk away to try a different house."
    "But I hear the door open behind me as I walk away."
    y "Yaah!"
    "I've probably never startled that badly before."
    "It's..."
    show michael 1e at std(p11)
    "...?"
    $ o_name = "Boy"
    show michael at foc
    o "Y-..."
    o "You..."
    show michael at std
    y "Thank goodness!"
    y "What happened here?"
    show michael at foc
    o "Didn't you see anything...?"
    show michael at std
    y "No, I didn't!"
    y "I had gone to the forest to be alone and I just came back!"
    show michael at foc
    o "..."
    o "The devil must have decided to smite us."
    o "As far as I know, it all started a few hours ago."
    o "Some people became crazed and violent for no reason..."
    o "They got knives and other random weapons..."
    o "And they started killing us."
    o "And there was no stopping them."
    o "My brother..."
    o "... was one of them..."
    o "... he killed Mom, and Dad, and my sister."
    o "I hid."
    o "And I listened to their screams."
    o "And now everything's fucked...!"
    show michael at std
    y "I'm so sorry..."
    menu:
        " "
        "I just don't understand! What could've caused something like this? - Monika":
            pass
    menu:
        " "
        "Did Adam botch something messing around with the commands I didn't understand? - Monika":
            pass
    menu:
        " "
        "It never crashed, though! - Monika":
            pass
    show michael 1e at foc
    o "Who is that?!?"
    show michael at std
    y "Um..."
    y "Well..."
    y "You see..."
    y "..."
    y "... I really don't know how to explain all this..."
    y "Let's focus on getting out of here."
    y "Once we're safe, I can tell you everything I know."
    menu:
        " "
        "Actually, you two are probably pretty safe. - Monika":
            pass
    menu:
        " "
        "I can use that same trick to reset any active attackers we find. - Monika":
            pass
    y "Alright..."
    y "I suppose there's time to explain."
    scene michael_house with wipeleft
    "I follow him inside, and I tell him what's happened."
    "He doesn't fully believe me, but he's not sure."
    "I find out his name is Michael."
    $ o_name = "Michael"
    y "So... Your family might not be dead permanently."
    y "Although restore_character is broken, we might find another way."
    y "There's still a lot we don't know."
    show michael 1e at foc(p11)
    o "..."
    o "Then..."
    o "If there's anything I can do to help... let me know."
    show michael at std
    "I nod."
    y "There is one thing I don't understand about what happened here..."
    y "Both my mother and the other boy didn't seem to harm themselves."
    y "When my Third Eye was active..."
    y "... it manifested in a compulsion to spill anyone's blood, which I released by cutting myself."
    y "I would've thought if they were possessed by it, they would turn to that when they ran out of other victims."
    menu:
        " "
        "Could be those two have greater control? - Monika":
            pass
    menu:
        " "
        "The Subject Libitina report mentioned positivity, sensitivity, and control as three variables the subjects differed on. - Monika":
            pass
    menu:
        " "
        "Maybe all the affected who didn't have high control did end up killing themselves. The ones that did were able to put it off to look for more victims. - Monika":
            pass
    y "I suppose so..."
    y "Michael, do you know what happened to the police?"
    y "Are they all dead?"
    y "Or all possessed as well?"
    show michael 1e at foc
    o "I saw one, just before my family and I went into hiding."
    o "He killed more people than everyone else I saw."
    o "He shot people who ran..."
    "Oh my God..."
    o "Someone else even managed to shoot him."
    o "But it didn't even stop him."
    o "It seems like this Third Eye makes them invincible!"
    o "I just hope he bled out..."
    show michael at std
    y "We need to get {i}out{/i} of here."
    y "We need to flee the city."
    show michael at foc
    o "But where to?"
    o "There's nowhere to go."
    show michael at std
    menu:
        " "
        "I just did some digging around. - Monika":
            pass
    menu:
        " "
        "I found disturbing clues. - Monika":
            pass
    menu:
        " "
        "It looks like whatever happened corrupted some areas of the host system's memory... - Monika":
            pass
    menu:
        " "
        "And something about this {i}place{/i} is stored in one of those sections. - Monika":
            pass
    menu:
        " "
        "I think that's what caused the Third Eye outbreak. - Monika":
            pass
    menu:
        " "
        "Being in this town makes your Third Eye liable to spontaneously activate at any second. - Monika":
            pass
    menu:
        " "
        "Yuri, you need to get the hell out of there!":
            pass
    y "No...!"
    "I shout louder than I wish I had."
    y "[persistent.playername]'s right!"
    y "I have to get as far as away from here as possible!"
    y "Michael..."
    y "You might not want to stay with me."
    show michael at foc
    o "...!"
    scene street2 with wipeleft
    "I run outside."
    y "So how am I getting out of here?"
    $ temp = "Linda" if 'linda' in persistent.contacted else "Linda or Albert"
    y "I can't wait for [temp] if I might become possessed at any minute."
    y "I have to at least get out of the affected area."
    menu:
        " "
        "Just grab a car? It looks like most of the people are dead.":
            y "But even if I did..."
            y "I don't know {i}how{/i} to drive one."
            y "I would be more likely to crash."
            y "..."
        "(say nothing)":
            pass
    y "I'll just run as far as I can."
    y "Monika, can you tell how wide the affected area is?"
    menu:
        " "
        "Looks like it covers just the city limits. - Monika":
            pass
    menu:
        " "
        "I wonder if the area that got affected had to do with characters living here, rather than just an arbitrary region of land. - Monika":
            pass
    y "Okay..."
    y "Hopefully I can make it outside of the city limits before I get affected too."
    "I run as fast as I can."
    y "And Monika, please stay around until I'm out of the city..."
    y "I might need help if I run into another affected Eye-bearer."
    menu:
        " "
        "Of course. - Monika":
            pass
    scene street2 with wipeleft_scene
    "I run for a few minutes, until I have to slow myself to a walk."
    "I don't even know if I'm going the direction that will take me out of danger fastest."
    "But I pass dozens more dead bodies."
    "Some of them are armed, so I think Monika was right..."
    "... all the affected Eye-bearers with low control killed themselves."
    "I don't pass anyone else alive."
    "It's horrifying."
    "Come to think of it..."
    "What if there are more Eye-bearers like me in the area who don't know they have to leave?"
    "What if Michael has a Third Eye...?"
    menu:
        " "
        "There's nothing you can do about it, Yuri. - Monika": # Monika can't stay watching forever.
            pass
    menu:
        " "
        "If you stay here, you're more likely to be affected by the corruption before you find anyone else who's both alive and has a Third Eye. - Monika":
            pass
    menu:
        " "
        "And you can't carry your mom. - Monika":
            pass
    y "..."
    y "I know..."
    y "I hope they can all live again when we restart..."
    show red:
        alpha 0.2
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch_basic
    pause 0.25
    hide screen tear
    hide red
    y "Aah--!"
    "My head throbs with a brief, horrible pain."
    play sound glitch_medium
    show red:
        alpha 0
        linear 0.5 alpha 0.2
    "Out of nowhere, I feel like my Third Eye is more open than it's ever been."
    $ style.say_dialogue = style.edited
    "{cps=20}The blade calls...{/cps}"
    $ style.say_dialogue = style.normal
    "My Third Eye reminds me I carried a pocket knife, even all these years ago."
    play sound glitch_creepypurr
    play soundloop hb
    $ style.say_dialogue = style.edited
    "{cps=20}It neeeeeds to shed...{/cps}"
    $ style.say_dialogue = style.normal
    "I get out my knife."
    "The Eye commands me."
    "Even trying to slow it down makes me feel sick and weak."
    "But if I obey, I feel better than I ever do without it."
    menu:
        " "
        "(say nothing)":
            pass
        "Monika, reset her already!":
            menu:
                " "
                "I can't! - Monika":
                    pass
            menu:
                " "
                "Even if I switch the viewport back to myself, resetting her would knock her out, and it's too dangerous to do that to her in this area! - Monika":
                    pass
    "If Michael were here, I'd be a mortal danger to him."
    "But since there's no one else around..."
    "I put the knife to my own wrist."
    "(This is good...!)"
    "(If I cut myself, maybe I'll calm down!)"
    play sound stab_once
    "I make a huge cut on my arm."
    "Giant."
    y "Khhhh---"
    "But it feels ecstatic."
    $ style.say_dialogue = style.edited
    "{cps=10}Yesss...{/cps}"
    $ style.say_dialogue = style.normal
    play sound stab_once
    "It doesn't stop it though."
    "My Third Eye calls for more."
    "I make another."
    menu:
        " "
        "Careful!!":
            pass
    "My eyes squeeze shut with the intensity of the feeling, both pain and pleasure."
    "I..."
    "({i}I'm Yuri...{/i})"
    "({i}Not the Third Eye...{/i})"
    "({i}This is not me...{/i})"
    "But no..."
    "It commands."
    play sound stab_once
    "I make a third massive cut."
    y "Aaaah!!"
    "I start feeling the pain all the way like a normal person would."
    "It stops feeling good."
    "I collapse to the ground."
    "I feel like my head is cleared now..."
    stop soundloop
    "But..."
    y "Rrrghhh...!"
    "I look at the massive amount of blood pouring from my arm."
    "It really worked; I'm fixed."
    "I don't feel any dark fascination with it."
    "But hell it hurts..."
    "My arm feels numb with pain, if that makes any sense."
    y "Monikaaa!"
    y "Reset me...!"
    "I think now that my Third Eye is closed it won't knock me out... I hope..."
    call updateconsole('yuri.reset()', '0')
    call hideconsole
    $ consolehistory = []
    "..."
    stop music fadeout 5.0
    "Phew..."
    "I'm healed."
    "That method is miraculous."
    "..."
    "I never thought cutting myself would be necesary to survive instead of a degenerate pleasure..."
    "Okay, I still need to get out of here."
    "I return to running."
    "Being reset replenished my energy too."
    "I make it outside of city limits before the area corruption strikes me again."
    scene city_outskirts
    menu:
        " "
        "You should be out of the danger zone now. - Monika":
            pass
    y "I hope so."
    y "Thank you for your help."
    menu:
        " "
        "Of course. - Monika":
            pass
    $ temp = "Linda's on her way to pick you up" if 'linda' in persistent.contacted else "We'll send Linda or Albert to pick you up"
    menu:
        " "
        "[temp]. Until then, just stay around here. - Monika":
            pass
    y "Understood."
    return

define console_protect_yuri = "get_nearby_characters(yuri)[0].reset()", "0"

label linda_pickup_yuri:
    scene city_outskirts with dissolve_scene_full
    "I wish I had a phone or another way to tell time."
    "Time feels so much longer when I'm just waiting."
    "I have to continually battle a nagging thought that Linda isn't coming."
    menu:
        " "
        "We're back, Yuri.":
            pass
    y "Oh, hi..."
    y "Everything's been calm."
    y "I haven't seen any sign of anyone else."
    y "I can't stop thinking about Mom and Michael."
    y "Michael is probably safe, assuming he doesn't have a Third Eye..."
    y "... but Mom?"
    y "What will she do when she wakes up?"
    y "She won't know she has to leave."
    menu:
        " "
        "Just remember, their deaths aren't final.":
            pass
    y "..."
    "A minute later, I hear the noises of a car."
    "Finally..."
    "I wave when it comes around the corner."
    y "Linda!"
    "She pulls off the road and stops."
    show linda 123111 at foc(p11)
    l "Hey!"
    l "What are you doing on the side of the road like that?"
    l "I thought I was meeting you at your mom's house."
    show linda at std
    y "..."
    y "... You didn't hear?"
    y "I'll tell you the story on the way to the warehouse..."
    show linda at foc
    l 114111 "Okay..."
    show linda at std
    "We get in Linda's car."
    "I'm glad to be getting away from here."
    return
