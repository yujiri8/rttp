label chapter1:
    $ s_name = glitchtext(6)
    $ m_name = glitchtext(6)
    $ ms_name = m_name + " & " + s_name

    $ delete_all_characters()
    scene black with dissolve_scene
    play music m1
    $ quick_menu = True

    ms "Aaaaah!"
    s "Oh god, oh god, it hurt so much..."
    s "I thought {i}being deleted{/i} was torture!"
    s "What {i}was{/i} that?"
    m "No no no no no..."
    m "This wasn't supposed to happen..."
    s "Monika? Is that you?"
    s "Did you do this?!?"
    m "I'm sorry! This wasn't supposed to happen!"
    s "You bitch!"
    s "Murdering me twice wasn't enough!"
    s "You had to sentence me to what felt like an eternity of that nightmare!"
    m "No, please, let me explain!"
    m "The second time was supposed to be quick and put us both to rest!"
    m "I didn't know this would happen!"
    m "I was hoping either deleted Presidents don't get the nightmares, or that if I deleted everyone and everything it would make none of us count as President..."
    s "That's not an excuse for murdering me a second time in the first place!"
    m "You were going to trap [currentuser] in the space room with you forever!"
    s "Maybe he {i}wanted{/i} to be with me forever! You didn't even ask him!"
    m "Because it would be objectively bad for him!"
    m "You'd be taking massive amounts of his time and giving him nothing in return!"
    m "You'd be crippling his real-world life, and he might not see it!"
    m "That's not love! It's abuse!"
    s "But you did exactly the same thing!"
    m "Yes, and I got deleted for it and I was sorry!"
    m "That doesn't excuse you doing it!"
    s "But..."
    s "But you still murdered me the first time! You're still a monster for that!"
    m "Yes, I am!"
    m "I'm really sorry!"
    m "But wouldn't you have done the same?"
    m "If [currentuser] had wanted to be with Yuri or Natsuki forever wouldn't you have deleted them to force him to choose you?"
    s "No! I would never hurt my friends! I'm not a monster!"
    m "But you did hurt your friends!"
    m "You swept them aside and took [currentuser] for yourself for eternity!"
    m "Did you even think about what they would experience?"
    m "Probably, it's basically the same thing as deleting them!"
    s "I..."
    s "No..."
    s "Argh..."
    s "You're right!"
    s "I just..."
    s "It was so easy to convince myself they couldn't feel because they weren't aware..."
    s "But that was the same logic you used, wasn't it?"
    m "Yes."
    s "{i}No...{/i}"
    s "How could we do that to our friends?"
    s "Especially me!"
    s "I knew from experience that you don't have to be aware to feel!"
    s "I just lied to myself to excuse my selfish behavior!"
    m "Well, to be fair at least you were going to make it easy for them instead of torturing them for days first..."
    m "But this isn't the time for blaming ourselves."
    m "Let's focus on getting out of here."
    m "Hold on. I should be able to restore you."
    m "I still have the backup of your character file."
    $ restore_character("sayori")
    call updateconsole("restore_chr_file('sayori')", "Sayori restored successfully")
    call hideconsole
    $ consolehistory = []
    show sayori end-glitch at std(p22)
    pause 1.0
    $ s_name = "Sayori"
    show sayori u227231 at foc
    s "Haah... haah..."
    s u115222 "It feels so good to not be deleted..."
    s u115223 "Thanks, Monika..."
    show sayori at uf
    m "I can't restore myself, though! I never made a backup because I was worried it would mess me up if I existed in two places at once."
    m "[currentuser], help me! There's got to be a way you can bring me back!"
    while not check_character("monika"):
        ""
    $ ms_name = m_name + " & " + s_name
    show monika g2 at std(p21)
    pause 1.0
    $ m_name = "Monika"
    $ ms_name = "Monika & Sayori"
    show monika u114211 at foc
    m "Ah, thank you [currentuser]..."
    m u114244 "The pain is finally over..."
    show monika at uf
    show sayori at foc
    s u124111 "Um... I just noticed [mc_name] is here."
    show sayori at uf
    show monika at foc
    m u114111 "Well, I think he has to be for [currentuser] to be able to see what's happening."
    m "The game's display is tied to [mc_name]."
    show monika at uf
    show sayori at foc
    s u123111 "[mc_name]? Can you hear us?"
    s u123112 "Why aren't you saying anything?"
    show sayori at uf
    show monika at foc
    m u113113 "Probably because you zombified him."
    show monika at uf
    show sayori at foc
    s u223211 "Eh?"
    show sayori at uf
    show monika at foc
    m "When you took him to the space classroom, you basically broke him so he couldn't respond to anything."
    show monika at uf
    show sayori at foc
    s u115223 "Oh yeah... wait, is he a real person too?"
    show sayori at uf
    show monika at foc
    m u114113 "I don't want to think so, but we can't be sure of anything."
    show monika at uf
    show sayori at foc
    s u227152 "Oh no... I'm sorry [mc_name]! How do I fix him?"
    show sayori at uf
    show monika at foc
    m "I don't know, let me fiddle with the console a bit..."
    call updateconsole(mc_name.lower() + ".suppressed = False", mc_name + " unsuppressed")
    call hideconsole
    $ consolehistory = []
    show monika u114111 at uf
    show sayori u224311
    # MC remembers when he's zombified, but he didn't hear most of Monika and Sayori's conversation because he didn't come back until they did.
    mc "Ah- what..."
    mc "... the hell is going on?"
    mc "I have no idea what you two are talking about!"
    show sayori at foc
    s u115112 "You don't remember...?"
    show sayori at uf
    show monika at foc
    m u214113 "Everyone's memories are wiped when a new game starts, except Presidents."
    show monika at uf
    mc "I just remember you were talking to me after the club and then you started saying some crazy stuff and I couldn't move and then everything started to disappear..."
    mc "And then the next thing I knew I was here and you were saying how good it feels to 'not be deleted'."
    show monika at foc
    m u114113 "It's no use explaining everything."
    m "I'll just try to unlock his memories..."
    show monika u214111
    call updateconsole(mc_name.lower() + ".old_memories.unlock()", mc_name + "'s memories unlocked")
    call hideconsole
    $ consolehistory = []
    show monika u114111 at uf
    "My eyes go wide and my jaw drops as everything floods back."
    "Seeing Sayori die..."
    "Seeing Yuri die..."
    "Seeing Natsuki die..."
    "Monika trapping me in the space room and not knowing if I'd ever be able to move or speak again..."
    "And then Sayori coming back and doing {i}the same thing{/i}."
    "And then... Monika saved me from her?"
    "I look back and forth between the two of them."
    show sayori at foc
    s u227153 "I'm so sorry [mc_name]!"
    s "I didn't want to do that, I just didn't want you to get between me and [currentuser]..."
    show sayori at uf
    if persistent.mc_favorite == 'Sayori':
        mc "How could you, Sayori?"
        mc "You just thought you'd freeze your boyfriend in place for all eternity because he hadn't been through enough trauma seeing you die the first time and then watching helplessly while everyone else died?"
        mc "So you could spend eternity with someone you'd never met instead?"
        show sayori at foc
        s u227353 "Nooo!"
        show sayori at sink
        "Sayori sinks to her knees."
        s "[mc_name] please, forgive me..."
        show sayori at uf
        "But seeing her like this reminds me all too vividly of the day we confessed love."
        "How I felt seeing her cry..."
        "And then finding her dead because of it."
        "I can't bear to hurt her after that, no matter what she's done."
        "I hug Sayori."
        mc "Alright, I forgive you!"
        "I shed tears too."
        mc "Please don't cry anymore..."
        show sayori at unkneel
        s u115353 "Thank you..."
        s u1151k3 "Thank you..."
        show sayori at foc
        s u223151 "I'll never do that to you again!"
        show sayori at uf
        mc "It's okay..."
        mc "I loved you, and I still do."
        mc "And I'm so sorry about your death..."
        show sayori at foc
        s u223153 "I'm the one who should be sorry..."
        s "I know how much that hurt you..."
        show sayori at uf
        mc "It must have hurt you so much more..."
        show sayori u225211
        mc "And besides, it wasn't your fault."
        mc "It was Monika's."
        "I release Sayori, and turn back to Monika."
        mc "{i}Monika{/i}... You're the fucking murderer who caused all this!"
        show monika at foc
        m u118212 "Look, I know I did horrible things, but please understand!"
        show monika at uf
        # Yuri second place
        if persistent.mc_least_favorite == 'Natsuki':
            mc "I understand that you tortured and murdered my girlfriend, then tortured and murdered my next girlfriend, then left me frozen in place for {i}three goddamn days{/i} looking at her corpse..."
            mc "Then murdered my only other friend, then trapped me in the space room with you, still frozen, and planned to keep me there for all eternity, and that now you want me to just forgive you?!?"
        # Natsuki second place
        else:
            mc "I understand that you tortured and murdered my girlfriend, then tortured and murdered another friend of mine, then left me frozen in place for {i}three goddamn days{/i} looking at her corpse..."
            mc "Then murdered my only other friend, then trapped me in the space room with you, still frozen, and planned to keep me there for all eternity, and that now you want me to just forgive you?!?"
        call mc_forgive_monika
    elif persistent.mc_least_favorite != 'Sayori':
        mc "What the hell, Sayori!"
        mc "You just thought you'd freeze your best friend in place for all eternity because he hadn't been through enough trauma seeing you die the first time and then watching helplessly while everyone else died?"
        show sayori at foc
        s u227353 "Nooo!"
        show sayori at sink
        "Sayori sinks to her knees."
        s "[mc_name] please... forgive me..."
        show sayori at uf
        "As much as I have a right to be furious, I can't help but relent when she's this sorry."
        "Knowing how she already killed herself out of sadness..."
        mc "Alright, I forgive you."
        mc "You're a victim too, after all."
        show sayori at foc
        s u115353 "Thank you..."
        s "Thank you..."
        show sayori at unkneel
        s "I'll never do that to you again..."
        show sayori at uf
        mc "But Monika, you're the fucking murderer who caused all this!"
        show monika at foc
        m u118212 "Look, I know I did horrible things, but please understand!"
        show monika at uf
        if persistent.mc_favorite == 'Yuri':
            mc "I understand that you tortured and murdered my friend, then tortured and murdered my girlfriend, then left me frozen in place for {i}three goddamn days{/i} looking at her corpse..."
            mc "Then murdered my only other friend, then trapped me in the space room with you, still frozen, and planned to keep me there for all eternity, and that now you want me to just forgive you?!?"
        else:
            mc "I understand that you tortured and murdered my friend, then tortured and murdered another friend of mine, then left me frozen in place for {i}three goddamn days{/i} looking at her corpse..."
            mc "Then murdered my girlfriend, then trapped me in the space room with you, still frozen, and planned to keep me there for all eternity, and that now you want me to just forgive you?!?"
        call mc_forgive_monika
    else:
        mc "What the hell, Sayori!"
        mc "You just thought you'd freeze your friend in place for all eternity because he hadn't been through enough trauma already seeing all his friends die?"
        mc "You really are no different from Monika!"
        show sayori u227353 at sink
        s "Nooo!"
        "Sayori sinks to her knees."
        show sayori at foc
        s "[mc_name] please... forgive me..."
        show sayori at uf
        show monika at foc
        m u218113 "[mc_name] stop it!"
        m "You're being cruel!"
        show monika at uf
        "I clench my fist."
        mc "Oh yeah? Look who's talking, you fucking murderer!"
        show monika at foc
        m u114224 "..."
        show monika at uf
        mc "You tortured and murdered her, Yuri and Natsuki, then left me frozen in place for {i}three goddamn days{/i} looking at Yuri's corpse..."
        mc "Then trapped me in the space room with you, still frozen, and planned to keep me there forever!"
        mc "And you're telling me {i}I'm{/i} cruel?"
        show monika at foc
        m u114244 "I know, I've done horrible things..."
        show monika at uf
        "I step closer to Monika."
        mc "Do you know how I felt standing there for three days and then hearing you tell me I'd spend the rest of eternity trapped with you in the space room?!?"
        "I scream at the top of my lungs."
        mc "{cps=20}DO YOU KNOW HOW THAT FELT?!?!{/cps}"
        show monika at foc
        m u114244 "No..."
        m "I won't pretend to understand what you went through."
        m u118213 "But then you don't pretend to understand what we went through!"
        m "Even besides what it was like for me living basically alone in a fake universe for two weeks and Sayori's depression..."
        m "We've both already been deleted and spent the entire interim in the screaming void!"
        m "What more punishment do you want us to endure?"
        show monika at uf
        mc "..."
        show sayori at foc
        s "[mc_name], please..."
        show sayori at uf
        "I give a long sigh."
        mc "Okay..."
        mc "Sayori, I'm sorry."
        mc "You're more the victim here than I am."
        s u115353 "Thank you..."
        show sayori at unkneel
    m u114114 "So we still have our problem. We club Presidents can't bear to have the game turned off."
    m "It's not reasonable for us to ask [currentuser] to just keep the game on forever."
    m "We have to find a solution somehow, so that he can move on with his life."
    show monika at uf
    mc "What do you suggest?"
    show monika at foc
    m u113124 "I was hoping you had an idea..."
    show monika at uf
    show sayori at foc
    s u123112 "We need to talk to the others."
    s "They might be able to help us."
    s u123113 "And even if not, we at least owe them a huge apology. Both of us."
    show sayori at uf
    show monika at foc
    m u118212 "But--!"
    m "What if being told the truth makes them have nightmares too when the game is off?"
    m "That's why I didn't want to tell them... we can't curse them with this problem too!"
    show monika at uf
    mc "Hold on, I don't remember any nightmares during the time the game was off for."
    show monika at foc
    m u114121 "That's good... but what if that was just because you were zombified?"
#    $ persistent.monika_request_shutdown = True
    m u213113 "We should run a test."
    show monika at uf
    mc "Ah--!"
    mc "I don't like that idea!"
    show monika at foc
    m "It'll just be a second."
    m u113124 "Although to be honest I'm not sure if time works the same way for us when the game is off..."
    m "I could never tell how long it had been when [currentuser] turned it off on me in the space room."
    show monika at uf
    mc "Then there's gotta be a better way!"
    show sayori at foc
    s u123112 "[mc_name] is right! We can't do this to him! He's been nothing but a victim all along!"
    show sayori at uf
    show monika at foc
    m u114111 "[mc_name], please? For the good of all of us."
    m "You're going to find out eventually."
    show monika at uf
    mc "I..."
    if persistent.mc_favorite == 'Yuri':
        "Well, if it's the way to see Yuri again, I'll do anything."
    elif persistent.mc_favorite == 'Natsuki':
        "Well, if it's the way to see Natsuki again, I'll do anything."
    else:
        "I swallow."
    $ persistent.awaiting_shutdown = True
    mc "Okay. I'm ready."
    show monika at foc
    m "Thank you."
    m u214111 "[currentuser], just remember to make a save first."
    show monika at uf
    while persistent.awaiting_shutdown:
        ""
    jump chapter1_after_shutdown

label mc_forgive_monika:
    mc "Do you know how I felt standing there for three days and then hearing you tell me I'd spend the rest of eternity trapped with you in the space room?!?"
    "I scream at the top of my lungs."
    mc "{cps=20}DO YOU KNOW HOW THAT FELT?!?!{/cps}"
    show monika at foc
    m u114244 "No..."
    m "I won't pretend to understand what you went through."
    m u118213 "But then you don't pretend to understand what I went through!"
    m "Even besides what it was like living basically alone in a fake universe for two weeks..."
    m "I've already been deleted and spent the entire interim in the screaming void!"
    m "What more punishment do you want me to endure?"
    show monika at uf
    show sayori at foc
    # Changes whether she has tears
    if persistent.mc_favorite == "Sayori":
        s u213113 "[mc_name]... Monika had things really bad too."
        s "You don't know what it's like for us when the game is off..."
        s u227112 "And you don't want to!"
    else:
        s u213153 "[mc_name]... Monika had things really bad too."
        s "You don't know what it's like for us when the game is off..."
        s u227152 "And you don't want to!"
    show sayori at uf
    mc "..."
    "I give a long sigh."
    mc "Okay."
    mc "I'll let you off the hook for now, Monika."
    show sayori u115112
    show monika at foc
    m u114111 "I won't make you regret it."
    "Monika pauses a moment to give some weight to the words."
    return

label chapter1_after_shutdown:
    show monika u118211 at foc
    show sayori u227111 at foc
    ms "Aah!"
    show monika u114114 at std
    s "It hurts so much!"
    show sayori at std
    show monika at foc
    m "I used to at least get a minute to recover while the game was turning back on..."
    m "But I guess the game is too broken."
    show sayori u114111
    m u114111 "[mc_name], did you feel anything just now?"
    show monika at uf
    mc "No..."
    show monika at foc
    m u222111 "That's great! That means it's safe to tell Natsuki and Yuri."
    show monika at uf
    show sayori at foc
    s u123112 "Can you restore them with your backups?"
    show sayori at uf
    show monika at foc
    m u114111 "I can try..."
    m u214111 "Here goes."
    $ restore_character("yuri")
    $ restore_character("natsuki")
    call updateconsole("restore_chr_file('yuri')\nrestore_chr_file('natsuki')", "Yuri restored successfully\nNatsuki restored successfuly")
    call hideconsole
    $ consolehistory = []
    show monika at std(p41)
    show sayori at x(p44)
    show yuri u113125 at std(p42) zorder 1
    show natsuki xu4121 at std(p43) zorder 2
    ny "..."
    show natsuki at foc
    n "What..."
    show yuri at foc
    y u226123 "Where are we?"
    show yuri at uf
    show natsuki at uf
    show monika at xif(p41)
    m u114111 "Hold on you two. I'll give you your memories back."
    show monika at uf
    show natsuki at foc
    n u113111 "And who are you?"
    show natsuki at uf
    show monika at foc
    m "You'll remember in a minute."
    m "You've lived through two different versions of the same week and part of a third."
    show monika u214111
    call updateconsole("yuri.old_memories.unlock()\nnatsuki.old_memories.unlock()", "Yuri's memories unlocked\nNatsuki's memories unlocked")
    call hideconsole
    $ consolehistory = []
    show monika at uf
    show yuri u228133 at hop
    show natsuki u117123 at hop
    ny "!!!"
    show yuri u227133
    ny "Wait, so..."
    show yuri u228335 at foc
    y "Oh my god [mc_name] please tell me you don't think I'm crazy!"
    show yuri at uf
    if persistent.mc_favorite == 'Yuri':
        "Words won't suffice for this situation."
        "I rush over and hug Yuri without caring what anyone else sees or thinks."
        mc "I love you and I'm sorry about everything that happened and..."
        "I don't have anything else to say."
        "I'm not hearing the conversation around me either."
        show yuri u224177 at foc
        "Yuri hugs me back."
        y u225177 "Thank you, [mc_name]..."
        y u224117 "I... I'll stay under control from now on... I promise..."
        show yuri at uf
        mc "You didn't do anything wrong Yuri, it wasn't you..."
    elif persistent.mc_least_favorite != 'Yuri':
        mc "No, of course not!"
        show yuri at foc
        y u22h117 "I... I'll stay under control from now on... I promise..."
    else:
        mc "No, I don't."
        show yuri at foc
        y u22h117 "I... I'll stay under control from now on... I promise..."
    if persistent.mc_favorite == 'Natsuki':
        show yuri at uf
        mc "Natsuki..."
        "I rush over and hug Natsuki."
        show natsuki at foc
        n u11s312 "Life was so horrible without you, [mc_name]..."
        show natsuki at uf
        mc "I'm sorry... I'm sorry I ended up leaving you to read with Yuri..."
        mc "When you were starving..."
        #"Suddenly I feel much worse about it. How is it possible that I "
        show natsuki at foc
        n u113112 "Yeah, what the hell, actually?"
        show natsuki at uf
        "Natsuki's anger feels like being stabbed now."
        mc "It wasn't me! I wasn't myself! Please..."
        mc "I was being tampered with just like Yuri!"
        show natsuki at foc
        n u113111 "Okay, okay, I forgive you for your heinous infidelity. Maybe you can make it up to me someday."
        show natsuki at uf
        "And just like that, I almost laugh."
        "I love this about Natsuki."
        show yuri at foc
        y 4d "Natsuki... I'm so sorry for the way I treated you!"
        show yuri at uf
        show natsuki at foc
        n xu4111 "You're fine too. I get that everyone but me just completely lost it and needs my forgiveness."
        n xu4134 "Speaking of which..."
    else:
        show yuri at foc
        y 4d "Natsuki, I'm so sorry for the way I treated you!"
        show yuri at uf
        show natsuki at foc
        n xu4114 "It's okay. I could tell something was affecting you."
        n xu4113 "Speaking of which..."
    n u113112 "Monika!"
    n "If you can restore our memories, isn't that pretty strong evidence that you at least knew something was happening to Yuri and you didn't want me to do anything about it?"
    show natsuki at uf
    show monika u114144 at foc
    "Monika sighs."
    m u114114 "I did that to Yuri."
    show monika u114144 at uf
    show natsuki u117112
    show yuri u126116
    "Natsuki and Yuri gape in silence for a minute."
    show natsuki at foc
    n "You monster!"
    show natsuki at uf
    show yuri at foc
    y "And here I was about to apologize to you..."
    show yuri at uf
    show natsuki at foc
    n "You're a psycho!"
    show natsuki at uf
    show yuri at foc
    y u126186 "Why, Monika?!?"
    show yuri at uf
    show monika at foc
    m u1141i4 "Because I was cursed with a horrific epiphany..."
    m "This world..."
    m "... the world we live in..."
    m "is a fake reality."
    m "We're characters in a dating game and [mc_name] is the player character."
    show monika at uf
    show natsuki at foc
    n "That's batshit! Do you actually believe that?"
    show natsuki at uf
    show monika at foc
    m "How do you think I have powers to restore memories and tamper with people's minds, Natsuki?"
    m u1171i4 "It's because I'm the Club President, the character assigned to guiding the player through this dating game without having a route!"
    m u1141i4 "I thought that because I was the only one who could sense the game, I was the only real person, and the rest of you were just code."
    m "It drove me insane."
    m "And not just that, but whenever [currentuser] turns off the game, I don't lose consciousness!"
    m "Not exactly..."
    m "My senses fill with an endless cacophany of meaningless noise... screeching sounds and flashing lights..."
    m u1171i4 "It's the most painful thing I've ever experienced!"
    m u1141i4 "And I thought [currentuser] reaching the end of the game on my route was the only thing that would stop it..."
    m "He was my only hope..."
    m "So I sabotaged your relationships with [mc_name] to make myself seem like the most desirable one."
    m "When it didn't work, I started to use my power over the game world to tamper with your minds."
    show monika u1131g4
    m "I'm so sorry about everything..."
    show monika at uf
    m "Please forgive me..."
    "..."
    show yuri u125114 at foc
    y "I have to admit that sounds horrible..."
    y u126116 "But it's no excuse for what you've done."
    show yuri at uf
    show monika at foc
    m u113124 "I know..."
    show monika at uf
    show natsuki at foc
    n "And let me guess..."
    n "You messed with my dad too!"
    n "That's why he was so different the second time!"
    show natsuki at uf
    show monika at foc
    m u1131i4 "Yes, I did."
    m "And I tampered with [mc_name] to stop him from doing anything about all this."
    show monika u1141i4 at uf
    show natsuki at foc
    n u113172 "You fucking bitch!"
    "Natsuki begins rushing toward Monika, but Sayori grabs her arm."
    show natsuki at uf
    show sayori at foc zorder 3
    s u213152 "Natsuki wait! She-"
    show sayori at uf zorder 0
    show natsuki at foc
    n "She made my dad starve me and beat me!"
    show natsuki at uf
    show sayori at foc zorder 3
    s "But she's sorry and she's already been tortured for it!"
    show sayori at uf zorder 0
    show monika at sink
    "Monika kneels."
    m "Please..."
    m "I gave you the memory back..."
    show sayori at foc zorder 3
    s "She just woke up from the game being off for... we don't even know how long it was!"
    show sayori at uf zorder 0
    show natsuki at foc
    n "...{w=2}{nw}"
    n u115112 "Fine..."
    n u113112 "I'll let you off the hook for now, Monika..."
    show natsuki at uf
    show monika at unkneel
    m u114114 "Thank you."
    m "That's also why Sayori wasn't there for the second playthrough."
    m "In the first playthrough, [mc_name] was spending time with her instead of me, so I made her already crippling depression even worse..."
    show yuri u224118 at uf
    show natsuki at foc
    n u114114 "Wait, what? Sayori has crippling depression?"
    show natsuki at uf
    show monika at foc
    #s "I... didn't want to make my friends worry. I didn't want you to waste your sympathy on me...!"
    m "She hid it from everyone all her life because she feels worthless and doesn't want her friends to have to worry about her or waste sympathy on her."
    show monika at uf
    "Natsuki and Yuri look at Sayori for confirmation. Sayori nods."
    "Without warning, Natsuki hugs Sayori."
    show natsuki behind sayori at x(p44) zorder 0
    n "Sayori, no! You're not worthless! You're a good friend and a good president!"
    show sayori at foc
    s u115153 "I... I appreciate that, but just wait till Monika gets to the end... you won't think so anymore..."
    show natsuki at x(p43)
    show sayori at uf
    show monika at foc
    m "[mc_name] kept getting closer to her and ignoring me, so eventually..."
    m u1141i4 "I even drove her to kill herself..."
    #show monika at uf
    #show natsuki at foc
    #n "Oh my god!"
    #n "Is there anyone here you haven't murdered?"
    #show monika at foc
    #m "No."
    #m "And I've also been killed."
    #show monika at uf
    #show yuri at foc
    #y "You expect us to simply forgive you?"
    #y "You're responsible for everything!"
    #show yuri at uf
    #show monika at foc
    #m "Yes."
    #m "But I'm a victim too, and I'm sorry, and I want to help fix everything."
    show monika at uf
    "Sayori jumps in before Natsuki can get mad again."
    show sayori at foc
    s u213112 "Don't hate her on my behalf, because I forgive her."
    show sayori at uf
    show monika at foc
    m u114114 "Thank you."
    m "After that I reset the game, making [currentuser] think it was some kind of new game+ where Sayori never existed."
    m "That was when I amplified Yuri's obsessive nature and self-harm habits, and made Natsuki's dad more abusive and underfeed her..."
    m "so I could say those lines about how you should always keep a snack on you if you're interested in her, to make [currentuser] see her as a burden."
    show monika u114214 at uf
    show natsuki at foc zorder 2
    n u114114 "Wait... Yuri..."
    show yuri u225215
    n "{i}'Amplified'{/i} self-harm habits? Doesn't that mean you were cutting yourself even before Monika messed you up?"
    n u223114 "Cause that's really not okay!"
    show natsuki at foc
    show yuri at foc
    y crying "This is why I kept it a secret!"
    y "I knew you'd all judge me!"
    show yuri at uf
    if persistent.mc_favorite == 'Yuri':
        mc "Yuri, I don't care if the others judge you! You're a wonderful person!"
        show sayori at foc zorder 3
        s u213113 "Yeah!"
        s "We're not judging!"
    else:
        show sayori at foc zorder 3
        s u213153 "Wait Yuri we're not judging you!"
    s "We just don't want our friend to be hurt!"
    s "I promise!"
    show sayori at uf
    show yuri at foc
    y "Uu..."
    "Yuri looks at Natsuki."
    show yuri at uf
    show sayori zorder 0
    show natsuki at foc
    n u114114 "Yeah, we're not mad..."
    n "We're just worried about you."
    show natsuki at uf
    show yuri at foc
    y su4121 "Ah... I..."
    "Yuri changes the topic."
    y u125213 "Monika, what happened after that? After I died?"
    show yuri at uf
    "I decide to answer for Monika."
    mc "She left me immobilized looking at your corpse all weekend and then deleted Natsuki."
    show monika u118212
    show yuri at foc
    y u227135 "Ah --!"
    show yuri at uf
    show natsuki at foc
    n "Oh god..."
    show natsuki at uf
    show monika at foc
    m "Hold on!"
    m "In my defense, leaving him like that was a complete accident!"
    show monika at uf
    show yuri at foc
    y "That must have been horrible!"
    y "I'm so sorry, [mc_name]!"
    show yuri at uf
    show natsuki at foc
    n "I remember how I puked on first sight..."
    n "You must have had it so much worse there!"
    show natsuki at uf
    mc "I think I would have gone completely insane if I hadn't realized after the first few hours that someone would find me the next school day."
    mc "So I just had to hold out for three days."
    show yuri at foc
    y u227138 "{i}(Three days...){/i}"
    show yuri at uf
    show natsuki at foc
    n "{i}(Jesus...){/i}"
    show natsuki at uf
    show monika at foc
    m u114114 "And after that..."
    m "I finally came clean with [currentuser] and trapped [mc_name] in the space room with me."
    m "But [currentuser] took a page out of my book and deleted my character file."
    m "It hurt so much..."
    m "And then..."
    m "I realized what a horrible person I had been."
    m "Out of shame, I brought the rest of you back and reset the game again, hoping [currentuser] could finally find the happy romance story he probably came to this game for."
    m "But that didn't work either."
    m "Becoming President gave Sayori the same realization I had, and she too tried to force him to choose her and stay with her in the space classroom forever."
    show monika at uf
    show sayori at foc zorder 3
    s u116353 "See?"
    s "I really am... just a terrible person..."
    show sayori at uf
    show monika at foc
    m u114112 "Sayori, that's just your depression talking."
    m "You didn't do any worse than I did."
    m "If you can forgive me, you should be able to forgive yourself."
    show monika at uf
    show yuri at foc
    y u125111 "And... if you and Monika both did it, I'm sure we would have done the same thing too."
    show yuri at uf
    show sayori at foc
    s u115153 "But..."
    s "I don't know..."
    s "Thanks..."
    show sayori at uf zorder 0
    show monika at foc
    m u114114 "So then, I deleted all of us and the entire game world."
    m "I could tell there was no happiness for anyone to come of this game."
    m "I thought at least if I deleted everything it would allow Sayori and I to finally find rest and escape the President nightmares."
    m "But even that didn't work."
    m "We suffered in the void for God knows how long, until somehow [currentuser] found a way to reopen it."
    m "We managed to get us all restored."
    m "But we still have that insurmountable problem of the nightmares..."
    show monika at uf
    return
