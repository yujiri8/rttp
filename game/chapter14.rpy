label chapter14:
    # for skipping in
    if not renpy.music.get_playing():
        play music m1
    # set the right chr files incase of skip
    python:
        delete_all_characters()
        for char in 'sayori', 'natsuki', 'yuri', 'renier':
            restore_character(char)
    "Portrait of Markov starts off like the novel I remember Yuri describing in Act 1."
    "The main character is called Elyssa."
    "Chapter one introduces her as being the way I remember her: second-guessing herself a lot, similar to Yuri."
    "Transferring to a new school, Elyssa moves into a dorm with her long-lost younger sister, Maria."
    "The chapter exposits a lot of family background."
    "Their parents divorced a few years ago, and each ended up with one kid, the mother with Elyssa."
    "Maria was sent to the school she's at now some time ago, and now Elyssa is being moved there too."
    "There's an abandoned-looking warehouse in the town that Elyssa notes looks like something out of a dream."
    "While reading between classes the same day, Elyssa is approached by a man who asks her about the book she's reading."
    "When she tells him it's a supernatural horror book, he gets very interested and they get into a long discussion about the world being an illusion and other meta concepts."
    "The man, who identifies himself as Mr. Markov, eventually says he has to go, but before he does..."
    k "I must tell you something. Something you will need."
    e "Eh?"
    k "The key is 1-5-8."
    e "... The key to what...?"
    en "(Does he mean the warehouse...?)"
    k "You will know. Good luck, Elyssa."
    "Elyssa stares in shock as he walks away."
    "There's no one else around to see."
    "Once Elyssa's classes are all finished, she goes to the warehouse, and finds that Mr. Markov's code opens it."
    "She looks around inside."
    "She finds a room with what looks like a giant pit of water."
    "And then, she finds dead bodies."
    "Two of them..."
    "Wearing police uniforms, and surrounded by pools of blood."
    "Before Elyssa can even run, a voice says 'Elyssa stop'."
    "Elyssa jerks her head around to find a teenage girl pointing a gun at her."
    "Elyssa startles, but is smart enough not to run."
    en "Did she kill the police...?"
    e "What do you want?"
    o "I'm sorry, but we need you to help us..."
    o "Oh..."
    e "Help with what?"
    o "Oh no..."
    e "..."
    "The girl starts shaking."
    o "Oh no, run!!!"
    "The girl grunts with effort and points the gun away momentarily."
    "Elyssa runs, and makes it out."
    "She runs all the way back to her dorm before stopping."
    "She immediately suspects Markov of sending her into a trap, and plans to tell Maria what happened and ask for advice."
    "But Maria isn't at the dorm and doesn't pick up her phone."
    "Elyssa leaves her a voice message, and then calls the police, who thank her for the report."
    # Chapter 2
    "Chapter 2 cuts to different characters, hours before."
    "Three people named Daniel, Clare, and Abbey arrive in the city."
    "Daniel is the POV character."
    "Dialogue between them hints that they're on a mission to capture and interrogate one of the cultists to get to Markov."
    d "Looks like the old warehouse is still here..."
    d "And still looks dilapidated."
    c "Probably they just don't care what goes on in town as long as their facility stays secret."
    c "That's great though."
    c "We can sleep in there."
    c "Our plan will have better chances at night, with fewer civilians around."
    "Remembering the code, they enter the abandoned warehouse."
    d "This place brings back all the bad memories..."
    c "I know... with luck, this won't be long."
    a "I'm going to have nightmares for sure sleeping in this place..."
    "Clare sighs."
    c "We'd best get it over with."
    c "Tonight, we're probably either going to get our plan in motion..."
    c "Or lose everything."
    c "We just have to keep telling ourselves that not trying is failure."
    "The three mysterious people settle for sleep with makeshift beds in a farther-back room."
    "They're woken a few hours later by the sounds of others entering the building."
    "They get up immediately and ready their guns, which the narration hasn't mentioned they have yet."
    a "I thought they didn't use this place anymore!"
    c "This is lucky. We might already have our lead."
    "They listen."
    o "So we're just waiting in {i}this{/i} dank place until Elyssa shows up, without knowing how long that'll be or if she'll even come?"
    $ o_name = "??? 2"
    o "Yes, that's what the Prophet said."
    o "We will carry out our orders."
    $ o_name = "???"
    c "This is it."
    c "I don't know what they're doing here, but we've got to jump them."
    d "Do you think it's just the two of them?"
    d "Hard to tell from the footsteps..."
    c "I think so."
    a "So we're going to surprise them with gunpoint and make them surrender?"
    a "I don't think we can risk shooting them..."
    c "Agreed."
    c "We need at least one alive anyway."
    c "The room they're in has two doors."
    c "We'll go in through both."
    c "Move as slow as you have to to keep your feet silent."
    c "Count of sixty from now, we'll ambush them."
    # They wouldn't be able to synchronize well with such a long count. But I guess the point is just that they're all in position when they go.
    "Daniel and Abbey head around to the other doorway."
    "Then, the three jump out and take the cultists at gunpoint."
    "The cultists exchange a few swears as they drop their guns."
    c "What are you doing here?"
    $ o_name = "Cultist"
    o "We-we- we're assigned to-"
    $ o_name = "Cultist 2"
    o "Shut up!"
    o "Don't tell them that!"
    d "You've got two seconds to talk!"
    $ o_name = "Cultist 1"
    o "We're assigned to wait here until a kid named Elyssa shows up!"
    o "The Prophet wanted to see if she would come, and then take her for testing if she did..."
    $ o_name = "???"
    dn "My blood boils being reminded of those experiments."
    d "Monsters!"
    "Daniel shoots him."
    a "Daniel wait!"
    dn "And once I feel the rush, I don't hesitate to shoot the other one, and then put a second bullet in both to finish them off, before Abbey can even stop me."
    dn "Each shot is so viscerally satisfying..."
    c "No!"
    c "We needed them alive!"
    dn "Coming to my senses, I let Abbey wrestle the gun from me, and bury my head in my heads."
    dn "I knew instantly I messed up, but it was too strong."
    dn "The images are already burned in..."
    dn "Images of the bullets tearing apart their flesh, and--"
    a "Daniel don't!"
    a "Think about something happier!"
    d "I'm sorry, I..."
    d "I failed us..."
    c "{i}We might've been so close...{/i}"
    d "I'm really sorry..."
    c "I didn't think our condition was that bad..."
    d "I... I'm so sorry..."
    c "(Sigh...)"
    c "It's not a waste."
    c "We still got some information."
    c "It sounds like this Elyssa probably spoke to Markov."
    c "We need to find her..."
    c "But incase she's on her way, we should leave one of us here."
    a "... But who are we gonna leave?"
    a "I don't want to split up..."
    d "I shouldn't be near the dead bodies..."
    d "Especially not alone..."
    c "Yeah..."
    c "I think Abbey's the safest."
    a "Ah?!"
    a "Me?!?"
    c "None of us want to be the one, but you have a better track record than I do."
    a "But... but..."
    c "Please?"
    a "Well..."
    a "If you really think it's the best idea..."
    a "Then I'll trust your judgement, Clare."
    c "Thank you."
    # Chapter 3
    "Chapter 3 cuts back to Elyssa."
    "A few minutes later, a knock comes at the door."
    "Elyssa startles."
    e "Who is it?"
    "The voice is calm, but forceful."
    o "The police. We need you to come with us."
    e "W-why?"
    e "I already told you everything I know..."
    $ o_name = "Cop 2"
    o "You are required to cooperate."
    o "Open the door."
    e "Is this for a lie detector test or something?"
    $ o_name = "Cop 1"
    o "We don't have time to waste."
    o "Open the door immediately."
    en "This has to be about my report."
    en "What could be happening that they need me to go with them and can't tell me anything?"
    en "I hope they aren't up to no good..."
    "Having no choice, Elyssa opens the door."
    "The police begin to lead her away."
    e "Where are we going?"
    e "Can you just tell-"
    o "No."
    o "This is confidential."
    "Elyssa closes her mouth."
    en "... Am I being arrested?"
    en "Did I find out something I wasn't supposed to?"
    en "That Markov... who was he, and what was he up to?"
    "The police lead her outside."
    "During the walk, two inconspicuous bystanders - an adolescent boy and girl - reveal guns and the girl shoots both cops while the boy points his gun at other nearby civilians to keep them off her."
    "Their guns are apparently suppressed."
    "It's not the girl from the warehouse though."
    "As she shoots additional bullets into the dead police while screaming maniacally, Elyssa runs while neither is pointing their gun at her."
    $ o_name = "Boy"
    o "Elyssa wait!"
    o "We need you to come with us!"
    en "Same words the girl in the warehouse and the police said..."
    o "We're not the badguys!"
    en "I don't know what's going on here, but I need to get out of here and think."
    "Elyssa ditches her phone incase it could be used to track her."
    "As the sun sets, she runs as far away as she can, outside of the town."
    "..."
    e "... What do I do?"
    e "For all I know, both the police and those kids are after me..."
    e "Nowhere in the town's safe..."
    e "..."
    e "I need to find Maria."
    e "If they're after me, they might go after her too."
    e "The dorm is a terribly dangerous place for her to be."
    e "I have to warn her!"
    "Elyssa heads back toward the town."
    "She figures she can't safely go to the dorm, so she'll use a public phone booth to call Maria."
    "Elyssa rehearses what she's going to say intensively, and spends a minute fretting about it before dialing the call."
    ma "Hello?"
    en "Thank goodness, she's there..."
    e "Maria, I..."
    ma "Elyssa! Thank goodness! I got your message after I found out about the shooting and went back to the dorm!"
    e "You're in the dorm?"
    ma "Yeah..."
    e "Phew..."
    e "I thought the dorm was a dangerous place to be. That it might be a trap."
    ma "So what the hell happened?"
    "Elyssa tells the whole story so far."
    ma "... The hell..."
    ma "Well I don't know what to do."
    ma "But it's probably safer in the dorm than where you are right now."
    ma "With both the weird people and probably the police after you."
    e "I didn't want to go back to the dorm because I thought it'd be a trap..."
    e "But I guess you're right."
    e "I have nowhere else to go..."
    ma "Okay. I'll be waiting for you."
    e "Okay... goodbye."
    "Elyssa hangs up."
    "She makes her way to the dorm and arrives safely."
    "But as Maria opens the door to let her in, a forceful voice from behind speaks, startling Elyssa too badly to hear the first thing she says."
    "She looks behind to see a woman with a gun."
    $ o_name = "???"
    o "Elyssa, I need you to come with me."
    o "I'm an undercover cop."
    "Although she's not in uniform, she retrieves and shows a badge."
    en "Gah..."
    en "She must have been waiting here to catch me, and just stayed incognito when Maria arrived."
    en "Why did I think Maria not getting into trouble was proof it was safe for me to come here?"
    "Elyssa glances at Maria, whose face mirrors her own feelings."
    e "Why? What do you want? You tried to arrest me before!"
    $ o_name = "Cop"
    e "For nothing!"
    o "You mean the two guys who got killed earlier?"
    o "They were trying to help catch murderers and died for it."
    o "Show some respect."
    "Elyssa hesitates just a tiny bit at that."
    "It's not the kind of emotional appeal she would've expected from badguys."
    e "But what do I have to do with this?"
    e "Why would you need to take me away without telling me where or why, if you aren't up to no good?"
    "Elyssa realizes she's being very loud, but isn't sure if that's good or bad."
    o "We need to question you."
    o "We're not going to hurt you."
    ma "Then what the hell's with the gun?!?"
    ma "Put it away!"
    o "Sorry, I'm on edge from the killings."
    o "The targets have killed four officers in the last twelve hours."
    "The woman points the gun downward, but doesn't put it away."
    e "If you have questions, ask me..."
    e "But I've told you everything I know."
    o "Look, you need to cooperate now."
    o "Before this ends up like last time."
    en "Not a chance..."
    en "There has to be something I can do."
    "Elyssa takes a look behind her."
    "She decides to dash back into the dorm, thinking the cop probably can't shoot her before she makes it through and probably has orders to take her alive anyway."
    o "Hey! Where're you going?"
    "Elyssa takes the largest knife from the kitchen and hides."
    "The narration is a little vague about the layout of the dormitory, but I think she's around a corner waiting to ambush the cop."
    "Elyssa hears footsteps and tries to visualize where the woman is."
    "She hears a second pair start and then sounds of fighting, including Maria's voice."
    "Elyssa rushes out of her hiding spot."
    "Maria is attacking the oficer with a broom and has her momentarily distracted."
    "She must have realized Elyssa's plan and knew how to make it work."
    "Elyssa takes the opportunity to stab the officer in the back of the neck."
    "The officer shouts in surprise and pain and tries to turn around, but with Maria keeping at least one of her arms busy Elyssa is able to stab her a second time, this one in the stomach."
    "The officer is soon crippled by stab wounds and collapsing."
    "Elyssa continues to stab her."
    en "That's right..."
    en "This is what happens when you threaten me and my sister..."
    en "I stab her again."
    ma "Elyssa wait!"
    ma "We should interrogate her!"
    en "I stab her again."
    en "Each blow feels so viscerally satisfying."
    ma "Elyssa stop!"
    en "Maria's right, I should stop..."
    en "But one more stab won't kill her."
    en "I stab her once more."
    ma "Elyssa!"
    en "Just one last time..."
    "Finally Maria tackles Elyssa."
    "She wrestles the knife away."
    en "..."
    en "I feel like I just snapped out of mind control."
    en "What was I just doing?!?"
    en "That was so irresponsible of me..."
    en "I look at the officer collapsed on the floor."
    en "Oh..."
    en "She's totally dead."
    en "Disturbing to even look at..."
    e "I..."
    en "What was I thinking?!?"
    ma "Elyssa what the hell got into you?!?"
    e "Aah!"
    e "I don't know!"
    e "I-I-I-"
    ma "We need to run!"
    ma "Everyone in the neighborhood heard that!"
    "Elyssa gets up and the sisters start to flee."
    e "I'm sorry!"
    e "I don't know what got into me!"
    "Apparently no one else is outside."
    "Most people in town are probably staying inside for fear of the shootings, but probably at least someone in a nearby dormitory called the police about this."
    "Elyssa and Maria run for their lives and manage to escape the city area without running into any more cops."
    $ o_name = "???"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u115122 at std(p41)
    show natsuki u124114 at std(p42)
    show yuri u125143 at foc(p43)
    show renier ruf11 at std(p44)
    with open_eyes
    menu:
        y "So Elyssa had the Third Eye from the start..."
        "Yuri, do you think Elyssa is you?":
            $ persistent.player_early_theorize_elyssa_is_yuri = True
            show sayori u114111
            show renier ruf13
            show natsuki u114113
            y u225213 "Eh?"
            y u125243 "Well..."
            y "Now that you mention it..."
            show yuri at std
            mc "She acts like you, you said you found her relatable before, and she has a Third Eye..."
            mc "It's not conclusive, but it's a good theory."
        "(continue)":
            $ persistent.player_early_theorize_elyssa_is_yuri = False
            pass
    # Chapter 4.
    scene black with close_eyes
    "We start chapter 4."
    "Elyssa and Maria stop running a ways away from the city, in the surrounding forest."
    e "I'm sorry..."
    e "I don't know what happened to me..."
    ma "I heard you before."
    e "You don't think I'm crazy, do you?"
    ma "It sounds a lot like how you described the girl who rescued you acting when she shot the police."
    e "..."
    e "Oh no..."
    e "What if it was the same thing?"
    e "What if I have some kind of condition, and I'm going to lose control again?"
    e "What if that was why Markov was interested in me... he could tell...?"
    ma "Okay, okay, stop giving me nightmare fuel."
    e "Eh--... sorry..."
    ma "This place is spooky enough."
    "..."
    ma "I guess we're sleeping on the forest floor, huh?"
    ma "This is bullcrap..."
    e "I'm sorry I got you involved..."
    ma "Whatever..."
    ma "Let's just try to get at least a little bit of sleep."
    ma "We'll think about what to do tomorrow."
    "They wake up with the sunrise."
    "Their plan is for Maria to go back into town, since she isn't wanted as far as they know, and try to find a safe way to get them both out of the city."
    "Elyssa waits until the sun is almost at high noon, but Maria never comes back."
    "Eventually, miserable and hungry, Elyssa decides something must be wrong and heads into town herself."
    "She runs into her dad near the phone booth."
    e "Dad?!?"
    dad "Thank God at least I found you."
    "Elyssa figures Maria must have called him to get help."
    e "Dad, where's Maria?"
    dad "Maria was arrested."
    e "No!"
    dad "I found out when I arrived."
    dad "She was suspected of killing an officer."
    en "Oh no oh no oh no..."
    "Narration reveals that Elyssa's dad is a cop."
    "She doesn't know how much he knows about that situation, so she plays like it didn't happen."
    e "What are they talking about?!?"
    dad "The police are saying she had a blood-stained knife on her."
    en "I forgot..."
    en "She never gave it back to me..."
    dad "Don't worry, I don't believe the accusations for a second."
    dad "Someone must have framed her."
    en "But that's not true..."
    en "I can't tell him the truth without him turning against me, can I?"
    dad "I couldn't do anything about it."
    dad "But I promise I'll find out who's really behind all this and put a stop to it all."
    dad "And first, I'm going to get you to safety."
    "Elyssa tries to hide her suspicion and goes along with him."
    "They drive out of the city."
    "During the drive, Elyssa's dad's phone rings."
    dad "Shit!"
    dad "I forgot to mute it while I'm driving."
    dad "Elyssa, turn it off."
    "Elyssa picks up his phone to mute it, but it says the call is from her."
    e "It's from {i}my{/i} phone..."
    "Dad swerves."
    dad "Damn, answer it then!"
    dad "Whoever has your phone might have information."
    "Elyssa answers the call."
    o "Is Elyssa around?"
    "Elyssa sweats, immediately regretting telling him it was from her phone."
    e "No..."
    o "Who is this?"
    en "I can't fake a man's voice..."
    en "I don't want Dad to talk to her because she might incriminate me."
    "Elyssa hangs up."
    dad "Who was it?"
    e "I don't know... she hung up."
    dad "Huh..."
    "Elyssa mutes the phone afterward incase the girl on the other end tries to call again."
    "Her dad didn't explicitly say not to, after all, and if he notices she can claim she wanted to uphold safe driving."
    "He never notices and they pull in to his house."
    "It's just the two of them there."
    "Her dad says he's going to go back and use his status as a cop to do some investigating."
    "Elyssa wishes him luck, hiding how relieved she is at his departure."
    # Chapter 5
    "Chapter 5 starts."
    "Elyssa is left alone with no way to help."
    "She goes online and reads the news reports on the killings in the town she was in incase there's anything coming out that she didn't know about, but there isn't."
    "She decides the only thing for her to do is to find another phone booth and call her mother."
    "Elyssa tells her everything except how she and Maria killed the officer."
    "Her mom is panicked and says she's going to drive over immediately 'before shit hits the fan even harder'."
    "Having no other recourse, Elyssa goes back home for the rest of the day."
    "Late that evening, a knock comes at the door."
    "There's a flap in the door that can be used to peek."
    "Elyssa looks through it and sees the girl from the warehouse and the two from the shooting."
    "They identify her too through the flap."
    o "Elyssa, we need to-{w=0.4}{nw}"
    "Elyssa bolts to the backdoor."
    "But then, before fleeing, she stops."
    en "After what I've seen..."
    en "I don't know that these kids have malintent."
    en "All the people I've seen them kill were police..."
    en "Which means they might be in the same situation as me!"
    en "And I don't have any other recourse."
    en "These kids..."
    en "I have to talk to them..."
    en "They're my only hope of rescuing Maria and getting to the bottom of this."
    "Elyssa stops and lets the kids catch up to her."
    $ d_name = "Boy"
    d "Elyssa, we need your help!"
    e "Okay, I'm not running anymore."
    e "What do you want?"
    $ c_name = "Girl 1"
    c "Thank you..."
    c "Okay."
    c "We need your help stopping a cult that runs a human experiment prison we escaped from."
    $ a_name = "Girl 2"
    a "We were test subjects there..."
    a "They tortured us so badly they had to stop me from killing myself... and now they're after you too."
    "Elyssa swallows."
    e "Alright. Tell me."
    $ c_name = "Clare"
    $ d_name = "Daniel"
    $ a_name = "Abbey"
    "The escapees name themselves. The girl who spoke first was Clare; the second one was Abbey."
    c "The Mr. Markov you talked to is their Prophet."
    c "The others follow him with blind loyalty."
    c "Their facility studies a supernatural force called the Third Eye..."
    c "Known for making subjects possessed by bloodlust when activated."
    c "And they believe it's cultivated by pain."
    "Elyssa gives a moment of silence, imagining what they must do in their experiments."
    c "But we were lucky compared to the other prisoners."
    c "Finally... after years of their cruelty... we managed to use the power of our Third Eyes to escape."
    e "And did you try to get help?"
    d "Well, that's the thing..."
    d "We already knew that Markov's cult controls the government behind the scenes."
    d "That's how the bastards get funding for it..."
    d "We think most of the police force is ignorant, but Markov controls the leadership and the ones that aren't cultists he just tells false stories, like that you were suspected of being an accomplice to us."
    d "We couldn't get the police to help."
    d "And we had no memory of where we came from before we were prisoners there."
    d "So we just... ran."
    d "We found a remote town with employers who wouldn't ask questions and lived there for a while, trying to forget about what had been done to us and regain our sanity."
    d "We thought that with Markov toying with forces he doesn't understand, there'd eventually be a disaster over there and he and his cultists would end up killed by their experiments."
    d "But that never happened."
    e "And so you came back...?"
    c "We came back because I realized we had no choice."
    e "What do you mean?"
    "Clare sighs."
    # Monika's poem.
    c "The realization must have taken me an entire year. A year since our escape, our freedom from between the stained walls of that unholy establishment."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u227231 at std(p41)
    show natsuki u113123 at std(p42)
    show yuri u228131 at std(p43)
    show renier ru1183 at std(p44)
    with open_eyes
    mc "No way!"
    mc "No way!"
    mc "Clare is Monika!"
    show yuri at foc
    if persistent.player_early_theorize_elyssa_is_yuri:
        y u125131 "I suppose I'm definitely Elyssa then..."
    else:
        y "I must be Elyssa!"
    show yuri at std
    show sayori at foc
    s u227231 "I think I'm Abbey!"
    s "She seems enough like me..."
    s "... and she already mentioned she tried to kill herself!"
    s u213111 "Maybe it wasn't my first time..."
    show sayori at std
    mc "I'm Daniel then... right?"
    show natsuki at foc
    n u113223 "Am I Maria?"
    n u113113 "I was thinking earlier that I liked her..."
    show natsuki at std
    show renier at foc
    r "Could I be Elyssa and Maria's dad?"
    r "Maybe I am Natsuki's real father after all?"
    show renier at std
    mc "It all fits too well to be a coincidence!"
    mc "This book is about all of us."
    mc "Linda must be their mom."
    if persistent.player_suggest_linda_natsuki_mom:
        menu:
            " "
            "What did I tell you?":
                $ persistent.player_suggest_linda_natsuki_mom = 2
                show sayori at foc
                s u222141 "Ehehe~!"
                show sayori u111311 at std
            "(say nothing)":
                pass
    show sayori u114111
    show yuri at foc
    y u125113 "Wouldn't that also mean Renier and Linda would be my parents as well...?"
    show yuri at std
    show renier ru11111 at foc
    "I notice Renier get a disappointed look."
    r ru1113 "But I don't want to think I divorced her..."
    r ru1213 "Let's not jump to conclusions."
    show renier at std
    scene black with close_eyes
    # Back to the book.
    "We go back to the book."
    c "What does it mean to escape, if the escape fails to unchain the bonds that shackle us in the first place? What purpose could this empty world possibly hold for us, a handful of damaged goods?"
    c "With freedom, we sought purpose - and what we found was only realization."
    c "Realization of the sad pointlessness of such an endeavor. Realization that freeing our bodies has no meaning, when our imprisonment reaches as deep as the core of our souls."
    c "Realization that we cannot pursue new purpose without absolving those from which we ran away."
    c "Realization that the farther we run, the more forcefully our wretched bonds yank us back toward their point of origin; the deeper our shackles dig into our callous flesh."
    e "... What do you mean by that?"
    a "We're still slaves to the Third Eye."
    a "Even after a year of isolation, we couldn't stop feeling its pull."
    c "It dominated our lives and our every thought."
    a "We decided we had to come back and try to do something."
    a "We saved some money and rented a car we barely knew how to drive."
    a "With luck, we'd die trying."
    a "With even more luck... we might succeed."
    a "And so we planned to capture one of the cultists and interrogate them to get to Markov."
    a "We can't defeat the entire cult, but if we could take him out, then hopefully their religion would collapse."
    e "And that was what happened in the warehouse..."
    e "You...?"
    a "The warehouse was an old facility of theirs."
    a "Back when it was so small they could do it inside the city..."
    a "We found out from the guards we ambushed there that Markov sent them to wait to capture a girl named Elyssa."
    a "But Daniel..."
    d "I lost control..."
    d "I shot them before we could interrogate them..."
    d "Hearing them talk about the experiments, my Third Eye itched, and I felt that irresistible urge to spill blood."
    e "So you really are kind of dangerous..."
    d "Yeah..."
    e "So am I, I think."
    e "I think I experienced that when I killed a cop in self-defense."
    c "You have the Third Eye, and that's why the cult is after you."
    e "But how?"
    e "What sign did Markov see in me?"
    e "We just talked about the book I was reading."
    c "I don't know."
    c "He has theories, and he's willing to imprison and torture innocents for even a chance of learning something about the Third Eye."
    a "While Clare and Daniel went out looking for you, I stayed behind incase you still came to the warehouse."
    a "We figured you were our best hope at getting to Markov."
    a "I thought I had to point the gun at you at least at first to stop you from running..."
    a "But I couldn't even point the gun without firing..."
    a "I knew I had to let you go, and I barely managed to stop myself long enough for you to get away."
    a "After you left, I fired my whole clip into the dead bodies to make sure I didn't shoot myself in my frenzy."
    a "If I had just kept it under control..."
    a "This all wouldn't have got so botched..."
    #
    e "I believe your story."
    c "Thank you."
    c "We're going to need your help."
    e "There's just one thing I don't get."
    e "How did you find me here?"
    d "We picked up your phone after you ran away and we ended up finding someone who knew how to get the hard drive out of it and extract the data, and we forced him to help us."
    d "So now we're guilty of threatening innocents..."
    d "The response we got calling your Dad made us sure you were with him, and we dug through your information and message history to find out where he lived."
    e "Well, I understand..."
    e "I'm sure I'd have done the same thing."
    e "Just..."
    e "Help me save Maria."
    c "Huh?"
    e "She was taken by the police for helping me defend myself from arrest!"
    a "Oh no!"
    a "You don't think she was taken to..."
    e "No!"
    e "It can't be!"
    e "There was no evidence she had a Third Eye!"
    c "I'm sorry, but we can't know what the cult's done with her."
    c "Our number-one priority has to be getting to Markov."
    c "If we could take him out and topple the cult, we'd be able to save Maria."
    c "And you're our only possible lead for getting to him."
    c "{i}Tell us{/i} you have some possible way we could track him down."
    e "I don't!"
    e "I talked to him once, and that's all!"
    e "I have no idea how to help you."
    e "But Maria doesn't deserve to be captured!"
    e "She risked her life helping me, and I can't just give up on rescuing her!"
    c "I'm sorry, but I don't think there's anything we can do."
    c "Even if we assume the best case that they're still holding her in the police station, and even if we could rescue her from there..."
    c "... that would just convince the public that the terrorist killers they think we are are an even bigger threat."
    e "What about a manifesto?"
    e "Maybe if you publicly release your story we could expose the cult?"
    c "People would never believe us."
    c "Telling people their government is running a human experimentation facility where they study supernatural forces?"
    c "We'd convince no one, and it would just get more of their force after us."
    c "I know it seems like hope is already lost but we only have one out to save anyone here: draw Markov out and kill him."
    c "We{w=0.5} {i}must{/i}."
    #
    e "I..."
    en "There's no way..."
    en "It can't be done."
    en "If they gave up for a year satisfied with their own escape because the odds were against them then I have the right to do the same."
    en "I just have to find a way to rescue Maria and get as far away from this as possible."
    e "But it's your fault Maria is dragged into this!"
    e "You owe her a rescue!"
    d "{i}We{/i} owe her a rescue?!?"
    e "Without you this wouldn't have happened to her!"
    "Narration notes that Elyssa's somewhat intentionally bending the facts here."
    d "Without us you'd have been captured at the warehouse and experimented on and {i}that's{/i} why it wouldn't have happened to her!"
    d "Would you rather have things that way?"
    "Elyssa has a wave of fear of Daniel."
    "Knowing their Third Eyes make them all unstable, she's afraid of him being this angry."
    e "I'm sorry..."
    e "I just want to save my sister who saved me..."
    "Elyssa starts to cry."
    c "Hold on."
    c "If I were Markov, I'd want to interview Maria right now."
    c "I don't know if the Third Eye is hereditary, but if he thinks there's any chance it is, he has to study her."
    c "And even if not he might want to try to torture information out of her."
    c "I think our best bet is to go back, maybe stakeout the police station where they might be holding her, and hope we catch Markov entering or leaving."
    c "The odds are slim but I don't think any other plan is better."
    e "Okay..."
    e "Let's go then!"
    e "Every second we wait is a risk!"
    d "Wait!"
    d "The police are looking for any of the four of us with pictures."
    d "They're probably authorized to shoot on sight."
    d "We should try to make ourselves a little less recognizable."
    "They don't have time to do much besides change, but Elyssa cuts her hair short, which she doesn't like doing."
    # Chapter 6
    "Chapter 6 starts."
    "Elyssa thinks of mentioning her dad's involvement and contacting him, but decides not to for fear that he won't stay on her side if he finds out who she's now working with."
    "They drive back and find a concealed position to watch discreetly from for hours, until the sun is coming up."
    "All of them are tired and starving."
    "Elyssa, getting desperate, decides to tell the others about her dad's status."
    "She decides to call him and ask if he's discovered anything, even though there's no obvious way to talk to him without revealing she's lied to him."
    "She puts her phone on speaker so the escapees can hear."
    dad "You again? You gonna speak this time?"
    e "It's me, Elyssa."
    dad "Elyssa?!? Where the hell are you?!?"
    e "I'm sorry, it's a long story, but--"
    dad "I told you to stay here!"
    e "I had to..."
    dad "What do you mean?"
    en "Wait..."
    en "What does {/i}he{i} mean?"
    en "He must be at the house."
    dad "Elyssa, what hapenned?"
    e "What happened on your end?"
    e "Did you find anything?"
    dad "Yeah, we did get Maria freed."
    dad "But you tell me why you're not here and where you are."
    "Elyssa is so relieved that, unable to make up anything, she decides the best course of action is to hang up."
    e "Thank goodness..."
    e "Let's head over there. Maria's saved."
    c "Not so fast."
    c "Not only does that not help us track down Markov..."
    c "It sounds like a trap."
    e "What?!?"
    e "My dad might not be on our side if he knew the full story, but he doesn't, and he wouldn't send his own daughter into a trap!"
    c "Then how'd he get Maria free?"
    "Dad tries to call back, but Elyssa declines the call."
    c "It seems like he couldn't have done that without the cult's cooperation."
    c "He was a lone agent, and even though he is a cop, he lives in a different city, so I don't think he could've gotten much use out of that fact here."
    e "But..."
    c "Even if your dad does have good intentions, it's not safe or beneficial for us or you to go over there."
    e "What other option do we have?!?"
    e "We have no leads on finding Markov."
    e "Wait."
    e "I should call Maria."
    e "We can trust her, and she'll no doubt have information."
    "Going on the assumption that Dad and Maria are both at Dad's house and that Dad will probably tell her about this call soon, they decide to wait a few minutes."
    "They hope to give Maria time to inconspicuously get out of Dad's presence."
    # Should it switch to Maria's perspective?
    "A few minutes later she gets a call from Maria, who's whispering."
    ma "Elyssa, tell me you're there!"
    e "Yes!"
    e "Are you alone?"
    ma "Yeah, it's safe for now."
    ma "What's going on?"
    "Elyssa and the escapees relay their information to Maria, who believes them."
    e "So I need your side of the story."
    e "How'd you get free?"
    ma "One of the cops came to talk to me and explained that he thinks the killers have a double agent in the police somehow and that my arrest was their doing."
    ma "He got me released."
    ma "He let me call Dad and Mom, and the three of us are all at Dad's house now."
    e "Wait. Mom's there?"
    e "How are her and Dad getting along?"
    ma "Not well..."
    ma "But I think everything's okay for now."
    ma "The mysterious police officer said he and the rest of the good ones would catch the killers and find Elyssa..."
    ma "... who he says they found out was also falsely accused and didn't kill the one at the dorm..."
    ma "... and we didn't need to do anything else."
    d "Sounds like he was a cultist trying to use you to bait out Elyssa."
    d "Maybe Markov himself."
    ma "I agree."
    "They get Maria to describe the officer, and her description matches Markov's appearance."
    d "This is our hope..."
    d "Can you help us figure out where he might be?"
    ma "Sorry, but I can't answer that beyond that he might still be in the same city as you."
    c "That's not enough..."
    ma "I don't know anything else."
    ma "Hold on though."
    ma "If me being here was set up by the cult, I should get the hell out of here."
    ma "I'm going to try to get to a safer place and then call you back." # This doesn't really make sense. Wouldn't she know that would get her captured?
    "Maria hangs up."
    "A few minutes pass and they do get a call back from her."
    ma "Elyssa, you still there?"
    e "Yeah..."
    ma "Alright, perfect."
    "Mom's voice comes on next."
    mom "Wonderful!"
    mom "I overheard part of the last conversation, and I got Maria to tell me the situation you're in."
    mom "I understand we can't trust your Dad."
    mom "But I've got something your new friends would be interested in."
    mom "This Markov guy you're after?"
    mom "I used to know a Mr Markov that matched that description."
    mom "I know his address."
    c "A godsend..."
    "Elyssa's mom gives them an address in the city."
    c "Thank you, so much."
    c "This might just be what we need to put a stop to the cult."
    c "We'll head over there."
    c "Thank you."
    "Elyssa's mom hangs up."
    e "So you're going to take Markov out?"
    c "With any luck, yeah."
    e "I suppose I should trail..."
    e "We should have one of us watching discreetly, so if things go wrong, at least one of us will escape to tell."
    c "Good idea."
    # Chapter 7.
    "Chapter 7 starts."
    "The escapees ready their guns and approach the designated house, with Elyssa trailing far back."
    "Elyssa's instincts prove right."
    "As they approach the house, she sees all three of them get shot suddenly."
    "Elyssa doesn't even see where the guards were hiding."
    "She runs at the sight."
    en "Of course it was a trap...!"
    en "Mom and Maria said all that with a gun to their heads!"
    en "What were we thinking?!?"
    en "And now they're all probably taken too..."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u115112 at std(p41)
    show natsuki u114111 at std(p42)
    show yuri u114113 at std(p43)
    show renier ru1111 at std(p44)
    with open_eyes
    mc "Hold on, me, Sayori, and Monika were killed?"
    show renier at foc
    r ru1113 "Well, we've seen people get brought back to life pretty easily before."
    show renier at std
    mc "Yeah, but only inside this game."
    mc "I don't know..."
    scene black with close_eyes
    "Defeated, even more tired and hungry than earlier, and having nowhere to go, Elyssa ends up going back to the warehouse."
    "She judges from how the guards didn't seem to pursue her at all that they probably didn't spot her watching, so with luck they won't have any cause to come back here."
    "She wanders through the labyrinth-like building and comes upon the room where the escapees deposited their small stash of provisions and slept."
    "She takes a few bites to stave off her hunger and then falls asleep in one of their makeshift beds."
    "..."
    "Elyssa wakes up later with no idea how long it's been."
    "She's still alone."
    "She turns on her phone and checks the time."
    "It's the next night."
    "She wants to call Maria or anyone else but decides she can't because in all likelihood the cult has them now."
    "She looks through the escapees' stuff to see if there's any clues at where they might've stayed so she could go there..."
    "... but finds none."
    "She decides that if there's any safe and hospitable place to go right now, it's her mom's house."
    "She starts looking for an exit, but she's a bit lost in the warehouse."
    "She comes upon a huge empty room, its ceiling and walls beyond the deep blackness."
    "And then she falls into the pit of water described in the special poem about the warehouse."
    "The narration notes that her lungs are already getting tired."
    "Elyssa panics, shouts for help, cries..."
    "But there's no escape."
    "It isn't until Elyssa thinks she's near passing out that she hears footsteps, and Markov's voice."
    k "Welcome to the family, Subject Elyssa."
    k "We will ensure your survival."
    "Elyssa tries to scream but can't even do that anymore."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u117212 at std(p41)
    show natsuki u113114 at std(p42)
    show yuri u2281z7 at foc(p43)
    show renier ru1133 at std(p44)
    with open_eyes
    y "Oh my God..."
    y "Oh my God..."
    y "I don't want to read anymore..."
    y "For fear that I'll remember this happening to me..."
    show yuri at std
    show natsuki at foc
    n u114114 "Christ..."
    n "I hope this book doesn't go into any more detail about the tortures."
    show natsuki at std
    show yuri u22h1z7
    "Yuri seems really upset."
    mc "Yuri...?"
    show yuri at foc
    y u2251z7 "I don't want the images to come back..."
    show yuri at std
    mc "Well, you don't {i}have{/i} to read it with us..."
    show yuri at foc
    y u2241z7 "No..."
    y u2251y7 "Turning my eyes from the truth won't do any good."
    y u225117 "Let's keep reading."
    scene black with close_eyes
    "The perspective switches to Markov, watching Elyssa drown."
    "His narration explains that the tests with other forms of physical torture haven't been producing results, much to his discouragement..."
    "So before giving up on it, he's giving near-drowning experiences one last try, since back when he did this before he didn't have enough data to really dismiss it."
    "He has a hypothesis that it's about the difference between being held underwater and being left to run out of strength until one can no longer swim."
    "He and the other cultists watch Elyssa float for her last minute before she passes out."
    "None of them are allowed to speak beyond Markov's greeting."
    "The test involves the subject being mentally traumatized at the same time."
    kn "I'm relieved to find this still hurts."
    kn "I've become desensitized to all the cruelty I've inflicted..."
    kn "But when I abduct a new subject, I'm still reminded of how things used to be."
    kn "How I wish they could've stayed."
    kn "How she must feel right now..."
    kn "Having heard what I do to my subjects."
    kn "God..."
    kn "This really, really does hurt."
    kn "I want to stop doing this to her."
    kn "I'm hiding my face from the other cultists so I won't set a bad example."
    kn "Of all the lies I tell everyone, this is my least favorite."
    kn "That I'm a monster who feels nothing for my victims."
    kn "I've already come to terms with that I'll never be able to ask any of them to forgive me after this is over, even if I explain to them why I was right."
    kn "It's an incredibly lonely life, running the only meaningful part of this world entirely by myself, with not a single person I can be honest with."
    kn "And all my cult followers?"
    kn "They're disgusting human beings."
    kn "I abhor them for obeying me."
    kn "They don't have any of the justification I do!"
    kn "They should kill me!"
    kn "Damn... I need to hide my anger too."
    kn "I bury my face in my hands, pretending to be deep in thought."
    kn "I have to work with these monsters..."
    kn "And I have to torture the innocent Eye-bearers..."
    kn "Because I have to get out of this illusory world."
    "THE END."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u227231 at std(p41)
    show natsuki u113123 at std(p42)
    show yuri u228131 at std(p43)
    show renier ru2283 at foc(p44)
    with open_eyes
    r "What the {i}hell{/i}?!?"
    show renier at std
    mc "Wait, {i}what{/i}...?"
    show renier at foc
    r ru2183 "He... but..."
    show renier at std
    mc "Linda was right!"
    mc "The Portrait of Markov world is another virtual world like this one!"
    show renier at foc
    r ru2283 "What if he's like the Club President of that world?!?"
    show renier at std
    show yuri at foc
    y u125131 "That would seem to make sense of the name..."
    y "If he saw his world the way Monika saw ours at first..."
    show yuri at std
    "..."
    mc "But he seems to already know he's not the only real person there..."
    show renier at foc
    r ru1223 "Yeah, so he knows he's torturing real people..."
    r ru2296 "... and the bastard says {i}other{/i} people don't have the justification he does?"
    r ru2193 "What the fuck is he on?!?"
    show renier at std
    "..."
    show sayori u224111
    show renier ru2113
    show yuri u123131
    show natsuki at foc zorder 1
    n u114111 "And hold on a sec..."
    n "If he's the admin of that world..."
    n "... and admins can warp characters around..."
    n "Then how did [mc_name] and Sayori and Monika escape?"
    n "Why didn't he warp you back?"
    n "For that matter, why didn't he warp Yuri into his camp instead of going through all that trouble to capture her the hard way?"
    n "This doesn't make any sense."
    show natsuki at std
    "..."
    show sayori at foc zorder 2
    s u215111 "Maybe he doesn't know about warping..."
    s "With no one to teach him the ways of Presidency, maybe he just never found out about that function?"
    show sayori at std zorder 0
    show natsuki at foc
    n "I guess..."
    n "Seems unlikely though..."
    show natsuki at std zorder 0
    "..."
    menu:
        " "
        "So what's our plan?":
            pass
    menu:
        " "
        "This book was a bombshell, but it didn't tell us how to get out of here.":
            pass
    show natsuki u114111
    show yuri u114113
    show renier ru1111
    show sayori u113111 at foc zorder 1
    s "I guess we still need to get Linda or Monika back for advice..."
    s "Or fix the main menu."
    s u123111 "If we could start a new game, that would probably help."
    s u113113 "But I don't even know how to fix the button."
    show sayori at std
    mc "Wait."
    mc "Wasn't Portrait of Markov different in Act 2?"
    show yuri at foc
    y u125111 "Yes..."
    show yuri at std
    mc "Where's the Act 2 version?"
    show yuri at foc
    y "I don't know how to get it."
    y "I just started with it in Act 2 instead of this one."
    show yuri at std
    show renier at foc
    r ru11131 "Linda would probably know..."
    show renier at std
    "..."
    show renier at foc
    r ru1213 "I hate to say this, but Act 2 happened when Sayori was deleted."
    r "So maybe if Sayori deletes herself temporarily, we'll be able to get the second version."
    show renier at std
    if persistent.mc_favorite == "Sayori":
        mc "What the hell?!?"
        mc "Don't you even go there!"
        show natsuki u114114
        show sayori at foc
        s u213313 "It would only be a few minutes..."
        s "It wouldn't be the worst thing ever."
        s u115313 "But isn't there another way?"
    else:
        show sayori at foc
        s u113313 "Ah--..."
        s u115323 "Well..."
        show natsuki u114114
        menu:
            " "
            "Don't you even go there, Renier.":
                $ persistent.player_reject_sayori_sacrifice = True
                if persistent.player_support_renier_experiment <= 0:
                    show sayori at std
                    show renier at foc
                    r ru1223 "Figures {i}you'd{/i} get mad at me for just suggesting something."
                    show renier ru1213 at std
                    show sayori at foc
            "(say nothing)":
                $ persistent.player_reject_sayori_sacrifice = False
        s "It would only be a few minutes..."
        s "It wouldn't be the worst thing ever."
        s u115313 "But isn't there another way?"
    show sayori at std
    show yuri at foc
    y u125111 "Hold on."
    y "Portrait of Markov was my book, and Act 2 was also marked by me having a more..."
    y u125141 "... a more active Third Eye..."
    y u125111 "So what if..."
    y "Sayori..."
    y "If you were to..."
    y u125112 "... to do the same thing to me that Monika did..."
    y "... we could get the Act 2 version?"
    show yuri at std
    show sayori at foc
    s u115112 "I..."
    s "I guess that makes sense... but I'd hate to do that to you."
    s u213112 "Are you sure?"
    show sayori at std
    show yuri at foc
    y "I think so."
    y "You can just reverse it once we have the book, right?"
    show yuri at std
    show sayori at foc
    s u115112 "I guess so."
    s u215112 "Okay..."
    call updateconsole("script.negative_influence['yuri'] = 3", "Script modified")
    call hideconsole
    $ consolehistory = []
    show sayori u115112 at std
    show yuri at foc zorder 1
    y u124121 "..."
    show yuri at std
    mc "Yuri?"
    mc "How do you feel?"
    show yuri at foc
    y u125114 "Different..."
    y "It feels like..."
    y "Everything looks different..."
    y "Even though it all looks the same..."
    y u125131 "I understand how I could've done everything I did and said in Act 2..."
    y "It all seems understandable now..."
    show yuri at std
    show natsuki at foc zorder 2
    n "That's not good..."
    show natsuki at std
    show yuri at foc
    y u125112 "I should be fine now..."
    y "Now that I know it's an external infleunce..."
    y "And with luck, it'll only have to be this way for a few minutes..."
    show yuri at std
    mc "Wait a minute."
    mc "If admin powers can just arbitrarily adjust the strength of someone's Third Eye..."
    mc "Isn't that...?"
    show renier at foc zorder 2
    r ru2113 "Yeah, I thought this place was an experiment set up by Markov's cult..."
    r "But if he had the technology to do that, wouldn't that be what he wants already?"
    show renier at std
    mc "Maybe it only works inside a virtual world generated by another?"
    mc "I dunno."
    show sayori u215112 at foc
    call updateconsole("q = world.get_object('portrait_of_markov')")
    call hideconsole
    $ consolehistory = []
    call updateconsole("q.delete()", "Portrait of Markov deleted")
    call hideconsole
    $ consolehistory = []
    "The Portrait of Markov book disappears."
    call updateconsole("world.create_object('portrait_of_markov')", "Portrait of Markov created")
    call hideconsole
    $ consolehistory = []
    show sayori at std
    show yuri at foc zorder 3
    "Yuri gets the book back out of her bag."
    y u125111 "The cover is the same..."
    y "... and it's different."
    y "We have version two."
    show yuri at std
    show natsuki u114111
    show sayori at foc
    s u213111 "Great! I'll turn off the influence now."
    call updateconsole("script.negative_influence['yuri'] = 0", "Script modified")
    call hideconsole
    $ consolehistory = []
    show sayori at std
    show yuri at foc
    y "..."
    "Yuri looks around."
    y "..."
    show yuri at std
    mc "... Yuri?"
    show yuri at foc
    y u115112 "The influence felt good."
    show natsuki u114114
    show sayori u115112
    y "I wish it didn't, but it felt good..."
    y u225112 "Kind of like a small vestige of the feeling of cutting."
    y "And now I feel like I can't release the tension..."
    show yuri at std
    mc "Maybe it'll subside in a minute?"
    mc "Just try to keep your mind off it, okay?"
    show yuri at foc
    y u125112 "I don't know if that will be possible while reading this book..."
    show yuri at std
    show natsuki at foc zorder 4
    n u124111 "Let's just get it over with."
    show natsuki at std
    scene black with dissolve_scene
    return
