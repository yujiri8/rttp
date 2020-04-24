label chapter18:
    $ delete_all_saves()
    $ autosave()
    $ persistent.autoload = None
    $ persistent.tried_newgame = False
    $ persistent.newgame = 'deny'
    $ restore_character('monika')
    scene vr_room
    show sayori u115132 at std(p51)
    show natsuki u114124 at std(p52)
    show yuri u224125 at std(p11)
    show linda 334443 at std(p54)
    show renier u2283 at std(p55)
    with Dissolve(5.0)
    play music third_eye
    mc "Oh hell..."
    mc "We're back to hell."
    "I shudder."
    "I remember being Daniel..."
    "Even the walls in this place look haunted."
    "They look like memories of agony."
    "Torture."
    "Cruelty."
    "I'm shaking uncontrollably."
    show linda at foc zorder 1
    l 119443 "I didn't keep my powers!"
    show linda at std
    show sayori at foc zorder 1
    s u227232 "I didn't keep mine either!"
    show sayori at std
    "I didn't really expect them to, but now that they say it..."
    mc "..."
    mc "You're telling me we can't even contact [persistent.playername] because neither of you can give [persistent.player_obj_pronoun] a menu?"
    show linda at foc
    l 114442 "Yes..."
    show linda at std
    show natsuki at foc zorder 1
    n u113124 "For pity's sake!"
    n "I thought we'd at least be able to communicate with [persistent.player_obj_pronoun]!"
    show natsuki at std
    show yuri at foc zorder 2
    y u225125 "Oh hell..."
    y "If our plan to get [persistent.player_obj_pronoun] to delete Markov doesn't work..."
    y u226325 "We'll be condemned to a fate far worse than death!"
    show yuri at std
    mc "Hold on, hold on!"
    mc "Our plan's still alive, we just need to find Markov..."
    show natsuki at foc zorder 3
    n u114124 "Linda, Renier?"
    n "One of you know where he'd be?"
    n "How we can get to him without running into anyone else?"
    show natsuki at std
    show linda at foc
    l 114113 "Yes..."
    l "If nothing's changed, I know where his office is."
    show linda at std
    mc "Okay, okay, there's hope..."
    show yuri at foc zorder 4
    y u226325 "This could end so much worse than us dying, though..."
    y u225375 "If Markov recaptures us..."
    y u228335 "Even suicide is no escape!"
    y "He can bring us back!"
    show yuri at std
    mc "Yuri, please!!!"
    mc "Don't force me to imagine it!"
    show yuri at foc
    y u224325 "..."
    show yuri at std zorder 2
    show natsuki at foc
    n "Let's get this over with..."
    n "Before we make any more noise..."
    show natsuki at std
    scene facility_hall with wipeleft
    "After listening for a few seconds and not hearing any footsteps, we head out into the hallway."
    "I feel like I'm in a cathedral of evil."
    "I guess I literally am."
    "We see closed rooms to the side."
    "The subjects must be--"
    "A door opens behind us."
    "I jerk my head around to see a guard coming out of room 114."
    "And she has a gun."
    "Oh crap not already!"
    "Renier acts quickly, running toward her with his knife incase he can reach her before she shoots him."
    "But he's too far away...!"
    "But I see a look of panic on the guard's face when she sees him, even though she has plenty of time, like she's cornered between a rock and a hard place."
    "She doesn't stop to shoot at Renier, but curses and runs away from the still-open door."
    "The subject comes running out after her."
    $ restore_character('libitina')
    show libitina 3311443 at std(p11)
    "It's..."
    "Libitina?!?"
    "Is that her?"
    show libitina at thide
    hide libitina
    # Maybe Renier should throw the knife to Libitina.
    "Libitina manages to grab the guard by the wrist, stopping her flight, and puncture it with a staple..."
    "And as soon as she does, she seems to become an unstoppable force, ripping the guard's flesh apart..."
    "{i}With the staple.{/i}"
    play sound stab
    $ b_name = "Libitina"
    b "I haven't done this in too long...!"
    "Shit, this ruckus is going to attract the entire cult!"
    show linda 339443 at foc(p11)
    l "Run! We have to find Markov before others show up!"
    show linda at std
    "I try to leave Libitina and follow Linda down the hallway, but suddenly I get disoriented..."
    hide linda
    show distort1
    show distort2
    with Dissolve(0.2)
    "I see a blur of colors and can't make out the sounds around me, and I'm not sure if I've fallen down."
    "I get an inexplicable pain like I did when the game was glitching."
    "I think I hear Libitina screaming."
    "Oh {i}fuck{/i}..."
    "Is she doing her 'distortion' thing...?"
    "Will I be able to give Markov a character file if I'm like this?!?"
    "I don't think I'd know if he showed up!"
    hide distort1
    hide distort2
    with Dissolve(0.5)
    "A few seconds later, everything turns normal again, and the excruciating pain stops."
    "I find myself on the ground."
    "Getting up, I glance behind me and notice Libitina is passed out on the floor."
    $ k_name = "???"
    $ restore_character('markov')
    show markov fu111 at foc(p11)
    k "My oh my, what has transpired here?"
    show markov at std
    show linda 119112 at foc(p33)
    l "That's him! [persistent.playername] delete him!"
    show linda at std
    $ k_name = "Markov"
    show markov at foc
    k u21511 "What...?"
    k u21543 "Crap."
    k fu111 "Oh, no. It's fine."
    k "You don't have authorization."
    show markov at std
    show linda at foc
    l 339443 "What?!?"
    show linda at std
    mc "What's he talking about?"
    mc "Didn't we use his key?"
    show markov at foc
    k "There was one thing you forgot to do."
    show markov at std
    "So you can't delete him?!?"
    "[persistent.playername], are you trying?"
    show markov at std
    "Yuri and Renier, followed by the rest of us, start running toward Markov." # this isn't a problematic plothole because it wouldn't have helped them to start running sooner.
    show markov u21111 at foc
    python:
        for char in ('yuri', 'renier', 'linda', 'sayori', 'natsuki'): delete_character(char)
    call updateconsole("d()", "yuri.chr deleted successfully\nrenier.chr deleted successfully\nlinda.chr deleted successfully\nsayori.chr deleted successfully\nnatsuki.chr deleted successfully\nNo such character")
    hide linda
    show markov fu111 at std
    "I see everyone else disappear at once."
    "Did he just delete everyone with one command?!?"
    show markov at foc
    k fu511 "Oh..."
    call hideconsole
    $ consolehistory = []
    k "It missed you because now that you're bound to [persistent.playername]'s viewport, you don't have a character file."
    k fu111 "No matter."
    show markov at std
    "Half a dozen other cultists are coming in at the other end of the hallway."
    "I'm helpless here."
    "But there's one person who might not be..."
    "I turn and run toward where Libitina fell."
    show markov at thide
    hide markov
    k "Daniel, what do you think you're..."
    "I know Markov's stopped her before, but maybe that was because he was too far away to be fully affected."
    "It's the only hope I have."
    "I have to trick him about my plan."
    mc "If I can't stop you, I'll deprive you of your most valuable subject!"
    k "You know I can just reset her, right?"
    mc "Not if I sever her trioptic gland..."
    "I hope to make him fear for a second that I know something about the Third Eye he doesn't."
    "It works."
    "Markov starts running toward us, unable to delete me, and unwilling to risk deleting Libitina."
    "I position myself between Markov and Libitina so he can't see exactly what I'm doing."
    "I pick up the staple Libitina used, put it between her fingers, and use her hand to stab my own with it."
    "{i}Tell me this counts...{/i}"
    "It hurts, and it feels good, but it doesn't do anything."
    "It must've counted as me cutting myself."
    "Okay, second resort...!"
    "I give Libitina's arm a cut with the staple."
    mc "Please!"
    "It works."
    "Her eyes light up again, and I give her the staple."
    mc "Come on!"
    "Libitina seems to be back in the game immediately."
    "She stabs my arm with the staple, and her Third Eye opens again."
    "This time, Markov is too close for his own good."
    "He realizes how I've tricked him, but too late."
    "Before he can enter the command to turn her off again, Libitina unleashes her distortion on me and him."
    show distort1 zorder 100
    show distort2 zorder 100
    with Dissolve(0.2)
    "I guess that's the end of my part in this operation..."
    "Come on Libitina, kill him..."
    "I can only hope."
    $ style.say_dialogue = style.edited
    k "... nO, No, emEgncyyyy..."
    call updateconsole(glitchtext(10), "SyntaxError")
    k "No..."
    $ gtext = glitchtext(30)
    b "[gtext]"
    k "hELp!"
    $ style.say_dialogue = style.normal
    "Libitina's distortion is excruciating..."
    "... but I think it's working...!"
    "He doesn't seem able to knock her out!"
    show dark_overlay zorder 100:
       alpha 0.0
       linear 1.0 alpha 0.5
       block:
           linear 0.8 alpha 0.75
           linear 0.8 alpha 0.5
           repeat
    "Oh god, I feel like I'm dying--"
    $ consolehistory = []
label first_break:
    # TODO Need a specially crafted sound effect.
    python:
        for char in ('yuri', 'renier', 'linda', 'sayori', 'natsuki'): delete_character(char)
    stop music
    $ delete_character('markov')
    scene black
    pause 5.0
    "..."
    "....."
    show mask_2
    show mask_3
    with open_eyes
    "I find myself looking into a messed up void like when Monika and Sayori broke stuff."
    "{i}Ow...{/i}"
    "What happened to the world...?"
    "I don't see Markov around, or hear any cultists coming."
    "I look behind me."
    scene facility_hall_r with wipeleft
    "The hallway's still there on the other side."
    "Libitina's on the ground next to me."
    "Miraculously, she seems to have calmed down."
    "But she looks like she's about to vomit..."
    "Huh."
    "Somehow, the cut Libitina gave me is gone."
    "I wonder if she deleted both me and Markov, but due to my special nature as the viewpoint character..."
    "... I got automatically restored? Like I did after Monika restored Sayori?"
    "Libitina suddenly coughs up a bit of blood."
    mc "No!"
    b "I didn't kn--"
    "She coughs up some more."
    b "Aaaah!!"
    mc "{i}No!{/i}"
    mc "We need help!"
    mc "[persistent.playername], can you do anything now?"
    mc "Please try to restore everyone else!"
    "Libitina coughs up more blood."
    "I feel so helpless, watching her go through this after saving me."
    while not (check_character('linda') and check_character('sayori') and check_character('yuri') and check_character('natsuki') and check_character('renier')):
        "..."
    show linda 339443 at std(p55)
    show renier u2283 at std(p54)
    show yuri u228325 at std(p11)
    show natsuki u117224 at std(p52)
    show sayori u227232 at std(p51)
    "I see everyone else come back into being."
    show natsuki at foc zorder 1
    n "What happened?!?"
    show natsuki at std
    show renier at foc zorder 1
    r "Where'd Markov go?"
    show renier at std
    show sayori at foc zorder 2
    s "Why is the other half of the hallway gone?!?"
    show sayori at std
    mc "I have no idea!"
    mc "Libitina used her distortion on me and Markov and that's all I know!"
    show linda at foc zorder 2
    l 334441 "Did she..."
    l "Cause a glitch without admin powers...?"
    show linda at std
    "I hear more sounds of blood-vomiting."
    "Libitina screams so loud it hurts my ears."
    show yuri at thide
    hide yuri
    "Yuri rushes over to Libitina and crouches beside her."
    y "What can I do?!?"
    y "Tell me I can help!"
    show linda 334443
    "Libitina screams more."
    show yuri u228338 at foc(p11) zorder 2
    y "We have to help her!"
    show yuri at std
    show linda at foc
    l 334112 "I'm sorry, but I've no idea what to do..."
    l "It's like a new, incurable disease..."
    l "But if it goes the same way it did for you, it will pass after a few minutes."
    l "At least temporarily."
    show linda at std
    show yuri at foc
    y u224128 "..."
    show yuri at std
    show sayori u227253
    show renier u22a3
    "Another scream and more blood."
    show yuri at foc
    y u1251y7 "I know how much this hurts..."
    show yuri at std
    show linda at foc
    l 114113 "[persistent.playername], can you talk to us now?"
    l "Hoping something changed when the world got messed up..."
    show linda at std
    mc "I don't think so."
    show linda at foc
    l 115112 "Figures..."
    show linda at std
    "Libitina finally stops vomiting blood, but she must already be in mortal condition..."
    show renier at foc zorder 3
    r u2183 "So is Markov dead?"
    r "Did Libitina kill him?"
    show renier at std
    show linda at foc zorder 4
    l 114112 "There's no way to know."
    l "It seems too good to be true though..."
    show linda at std
    show renier u2113
    show natsuki at foc zorder 3
    n u114114 "We should try to get out of this place."
    n "We've done what we can, and Libitina needs help."
    show natsuki at std
    show sayori at foc zorder 4
    s u223252 "Wait!"
    s "Linda, you said after we got out, we could check from the outside if Monika was still trapped in DDLC."
    s "How do we do that?"
    show sayori at std
    show linda at foc
    l 114112 "Um..."
    l 115112 "We can't."
    show linda at std
    show sayori u117214
    mc "Wait, did you lie about that too?!?"
    show linda at foc
    l 119112 "Of course I lied!"
    l "How would I be able to scan a virtual world if I no longer had admin powers?"
    show linda at std
    show sayori u128314 at foc
    "Sayori clenches her fists."
    s u127314 "You betrayed me!"
    s "You betrayed us all!"
    show sayori at std
    show linda at foc
    l "Look, it's not like she's dead!"
    l 114112 "She might've come out differently than we did, or if she is still in there we might find a way to get her out later."
    l "We'll probably see her again."
    show linda at std
    show sayori at foc
    s u228314 "Probably?!?"
    s u227314 "How can I trust anything you say now?!?"
    show sayori u228314 at std
    show natsuki at foc zorder 4
    n u113114 "Look, let's focus on getting everyone out of here alive!"
    n "We have to get to civilization!"
    n "We know the cultists go back and forth sometimes, so they must have a garage or something."
    show sayori u225112
    show natsuki u114114 at std
    mc "Wait, what about the other subjects?"
    "Somehow I haven't heard anything from the other rooms, so I didn't think about them."
    mc "We have to let them all out!"
    "I get a key from the dead guard's body, and use it to open one of the other doors."
    "The cell is empty."
    "I start to try each of the others in the intact part of the hallway."
    mc "All the other cells here are empty."
    mc "I wonder if they weren't using them before, or if whatever Libitina did messed up this world in other ways."
    show renier at foc
    r u2113 "They might've not been using the cells near Libitina's, to keep their most volatile subject isolated."
    r "I guess it's time for us to go."
    show renier u1111 at std
    "Renier picks up Libitina, Natsuki picks up the guard's gun, and we head out the door at the back end of the hallway."
    scene black
    show mask_2
    show mask_3
    show facility_rift
    with wipeleft_scene
    "Natsuki was right."
    "The part of the camp that didn't get turned into space is almost none..."
    "... but by some miracle, the garage is on the remaining sliver, halfway on the border."
    "We cram the seven of us into a car, with Linda driving, and head back toward civilization."
    # I wouldn't mind a car sound effect.
    return
