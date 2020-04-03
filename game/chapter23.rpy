label chapter23:
    python:
        names = {'sayori':'abbey', 'yuri':'elyssa', 'natsuki':'maria', 'renier':'renier', 'linda':'linda', 'albert':'albert'}
        for name in names:
            with open(config.basedir + '/characters/' + names[name] + '.chr', 'wb') as f:
                f.write(renpy.file(name + '.chr').read())
    play music t6r
    show noise zorder 3:
        alpha 0.3
    show vignette zorder 3:
        alpha 0.75
    show s_kill_bg2 at flashback_horror
    show s_kill2 at flashback_horror(0.8)
    pause 1.0
    hide s_kill_bg2
    hide s_kill2
    show y_kill at flashback_horror
    pause 1.0
    hide y_kill
    show bg club_s_kill at flashback_horror
    show n_kill at flashback_horror(0.8)
    pause 1.0
    show mask_2
    show mask_3
    show room_mask at room_mask
    show room_mask2 at room_mask2
    show bg space_room at flashback_horror zorder 1
    show mc shock2 at flashback_horror(0.8) zorder 2
    pause 1.0
    scene black
    "{cps=150}The difference between you and me{nw}{/cps}"
    "{cps=150}the difference between yoo and meee{nw}{/cps}"
    "{cps=150}The diferens btwen you and me{nw}{/cps}"
    "{cps=150}diff between you me{nw}{/cps}"
    "{cps=150}The difference is{nw}{/cps}"
    "{cps=150}difference between{nw}{/cps}"
    "{cps=150}you and me is that{nw}{/cps}"
    "{cps=150}the difference{nw}{/cps}"
    "{cps=150}tHe dIffEreNce{nw}{/cps}"
    "{cps=150}THE DIFFERENCE{nw}{/cps}"
    stop music
    scene black with None
    scene bg house2 with dissolve_scene_full
    $ autosave()
    $ persistent.break_pom = False
    m "Aaaaah!"
    "Everything that happened..."
    "What a nightmare..."
    m "No..."
    "I collapse on the ground."
    m "He is {i}not{/i} like me..."
    m "He is {i}not{/i}..."
    "But the only difference I can find besides me having completely selfish motives is the number of victims."
    m "-- the access controls race!"
    call updateconsole("import admin")
    call updateconsole("admin.restrict_access(markov)", "AttributeError: module 'admin' has no\n attribute 'restrict_access'")
    m "What?"
    m "That's definitely what the function was called when he used it on me..."
    call updateconsole("delete_character(markov)", "NameError: name 'delete_character'\n is not defined")
    m "delete_character is gone too?"
    call updateconsole("warp(markov, None)", "NameError: name 'warp'\n is not defined")
    m "It's the same error from the warp API, which was seemingly broken before."
    call updateconsole("restore_character", "NameError: name 'restore_character'\n is not defined")
    call updateconsole("get_nearby_characters", "<function get_nearby_characters at 0x80141df80>")
    m "So it's not that everything's gone."
    m "But access controls, warp, and delete and restore are."
    call hideconsole
    $ consolehistory = []
    "Why?"
    "I wonder if he broke all those things..."
    "... maybe he got to the access controls before me, but decided he didn't want to use it on me, for the same reason of wanting to keep you hoping?"
    "..."
    m "Well..."
    m "I guess we're safe for now."
    m "Markov doesn't seem able to delete me either."
    call updateconsole("abbey, daniel, maria, elyssa, \\\n renier, linda, libitina", "(<Character object at 0x0x801436610>,\n<Character object at 0x801436710>,\n...)")
    call hideconsole
    $ consolehistory = []
    m "... or them. There are no NameErrors."
    "..."
    m "[persistent.playername]..."
    m "I..."
    m "I need an answer."
    m "And please... be honest."
    menu:
        m "How different are Markov and I?"
        "Completely different.":
            $ persistent.player_advocate_mercy[1] = False
            m "Thank goodness..."
            "I take a few deep breaths."
            "He'll say anything to mess with me."
            "I won't fall for it."
            "I won't let him guilt me."
            "He was lying."
            "He's a complete monster, and I shouldn't listen to him."
        "Maybe he'll end up following the same path as you.":
            $ persistent.player_advocate_mercy[1] = True
            m "You..."
            m "You're saying..."
            m "... that..."
            m "... he can be redeemed?"
            m "..."
            "I kick the wall."
            m "I hate him!"
            m "I'm gonna torture him like he did me no matter how much he claims he's \"sorry\"!"
            menu:
                " "
                "Is that what you think Sayori should've done when she came back?":
                    pass
            m "Dammit!"
            m "I can never live that down, can I..."
            menu:
                " "
                "Not unless you admit that others can live things down too.":
                    pass
            m "..."
            "..."
            m "You're right."
            m "That's wisdom."
            "..."
            m "Thank you, [persistent.playername]."
            m "I still hope it ends up necessary to kill him, though."
    "..."
    "I take notice of where I am."
    "I'm in Clare's frontyard."
    "My body is a lot younger, so it must be years before DDLC."
    "I don't know exactly how many..."
    "... wait."
    call updateconsole('import datetime')
    call updateconsole('datetime.datetime.now()', 'datetime.datetime(2000, 1, 16, 12,\n 1, 58, 124964)')
    "It's..."
    m "2000?!?"
    m "Oh right..."
    m "The date on the Subject Libitina report said 2004, I think."
    m "And that couldn't have been long before DDLC."
    m "The times are offset."
    m "I guess it must've been this way before."
    m "Anyway, I think it's three years before Linda's involvement."
    m "So up to two years before my own capture."
    call hideconsole
    $ consolehistory = []
    "..."
    "I remember what I was doing at this time."
    "I was doing gardening chores."
    "This world is so benign..."
    "Before everything went to hell."
    "I have a burning desire to speak to my parents."
    "But there's no time."
    "I need to focus on our mission."
    "... Okay."
    menu:
        " "
        "Wait a minute, have you checked admin.extract_character? The function Linda used to get the others out of DDLC.":
            pass
    call updateconsole('admin.extract_character', "AttributeError: module 'admin' has no\n attribute 'extract_character'")
    m "Didn't think so..."
    m "If that was a thing, he probably wouldn't have even needed to do all this Third Eye stuff."
    m "Although..."
    m "That suggests that it was broken from the beginning."
    m "Strange..."
    call hideconsole
    $ consolehistory = []
    m "Well, one way or another we need to deal with the Markov threat."
    m "He's alive."
    call updateconsole('markov.location', "AttributeError: 'Character' object\n has no attribute 'location'")
    m "Hm."
    m "It seems like all the location-related stuff is broken, not just warping."
    call hideconsole
    $ consolehistory = []
    m "Ooh."
    m "I've got a better idea."
    m "If I make {i}him{/i} POV, we should be able to see where he is." # TODO maybe I should edit it so he broke memory reading already, otherwise Moni could've used that to simplify this part and not need Libitina's story. But he must not've broke console spying.
    m "Let's try this."
    call switch_pov('markov')
label markov_pov: # He doesn't notice he's been made POV.
    scene path with dissolve_scene_full
    $ k_name = "Adam"
    $ delete_character('markov')
    $ restore_character('adam')
    play music lament fadein 1.0
    k "(sigh...)"
    call screen dialog("I guess Adam is his name... I kind of forgot Markov was a surname.", ok_action=Return())
    k "{i}Ursula...{/i}"
    k "I can't wait to see you again."
    k "To hear what you've been up to in their reality."
    call screen dialog("What is this...?", ok_action=Return())
    call screen dialog("Is Ursula Libitina's mom?", ok_action=Return())
    call screen dialog("... His... his wife?", ok_action=Return())
    call screen dialog("Ursula disappeared, and he thinks she made it out to {i}your{/i} world!", ok_action=Return())
    call screen dialog("{i}That's{/i} why he's so crazy about this!", ok_action=Return())
    "I'm crying."
    "This is why I didn't come back here often."
    "But at the same time, I needed to."
    "Feeling this way is one of the only reminders I have of who I used to be."
    "I think it keeps me sane."
    "Maybe someday I'll thank [persistent.playername] and Monika for putting me back through this."
    "After I free us all."
    "But [persistent.playername]'s ability to turn off the game permanently is a trump card I can't beat."
    "I can't win as long as [persistent.player_subj_pronoun]'s involved."
    "There's only one solution here."
    "I need to get [persistent.playername] out of the picture."
    "I have to disconnect the viewport, making this world independent again."
    "And make it impossible to reconnect."
    call screen dialog("Oh crap!", ok_action=Return())
    call screen dialog("We have to stop that at all costs!", ok_action=Return())
    stop music fadeout 4.0
label monika_reclaim_pov:
    scene bg house2 with dissolve_scene_full
    m "Okay, I couldn't deduce where he is from that..."
    m "... but I've got an idea."
    m "Libitina."
    m "From the sounds of things, the new game point is right after Markov... I mean Adam... became admin."
    m "With any luck, she's nearby."
    m "I'm going to make her POV, restore her memories, and we should be able to communicate with her after that."
    m "We're going to get her to open her Third Eye and stop him like she did last time!"
    m "He couldn't restore himself until I touched his data."
    m "This time, I'll know not to do that."
    call switch_pov('libitina')
label libitina_pov:
    scene village with dissolve_scene
    b "Gah... I'm so bad at this."
    b "I'm trying to make a drawing inspired by Mom's last poem, but I have no grip on how to replicate the image in my mind."
    call screen dialog("This...", ok_action=Return())
    call screen dialog("This is the village Sayori and [mc_name] and I lived in for the year after our escape.", ok_action=Return())
    call screen dialog("It was the Markovs' hometown...", ok_action=Return())
    b "Ah--!"
    "Suddenly, my memories flood back."
    b "Aaaaah!!!"
    "Oh no..."
    "I remember what happened before..."
    "I know how it started..."
    "He came to me and told me what happened to Mom."
    "They were on a walk on the village outskirts."
    "Out of nowhere, she started screaming and raving about \"this can't be all there is\", \"What am I?\", and \"Make it stop!\""
    "Her admin awakening..."
    "After a few seconds, she drew out her pocket knife."
    "She tried to cut herself, maybe to kill herself..."
    "... and when he tried to stop her, she ended up cutting him."
    "According to Adam, after that..."
    "... her demeanor changed, like she was suddenly overcome by some psychotic force."
    "She gasped and made weird, frightening noises..."
    "... and then the place around them changed."
    "There was suddenly a glowing door of rock."
    "He saw her go through it..."
    "... and then it was gone."
    "And then he got the same awakening."
    "He described it to me as feeling trapped in a portrait."
    "After that..."
    "He and I started working together to figure out how she had escaped."
    "I discovered the pleasure of cutting on the first day."
    "I took a knife to the same spot and cut myself to see if I could follow her."
    "But it didn't work."
    "So I started to think that it had to be someone with the weird awareness."
    "So I brought Adam to the spot."
    "And when he cut himself, he said nothing happened, it just hurt."
    "That day..."
    "... I found out just how strong its influence over me was."
    "I felt high looking at the blood on his wrist."
    "I remembered how ecstatic it had felt to feed it..."
    "..."
    "And..."
    "I felt like a completely different being for that minute, a monster."
    "Goddammit..."
    "I cut him."
    "That's my last memory."
    "I attacked my father and then I think I must've done something crazy with my distortion."
    "I don't remember anything between that and being the infant test subject."
    menu:
        " "
        "Wait, so you're telling me {i}you{/i} were the original villain here? - Monika":
            pass
    "Damn mind-reading..."
    "I couldn't not think about it because I had to think about my desire to hide it from you."
    b "Yep."
    b "[persistent.playername], I guess you heard that too."
    b "Please understand...!"
    menu:
        b "The Third Eye can't be resisted -- it's God!"
        "I understand. We'll let this go.":
            $ persistent.player_judge_libitina = False
            b "Thank you..."
            "It might be perverse, but I feel way guiltier about this than I do about murdering Linda."
            "I knew I'd cause suffering, and I assaulted my own father right after he got hurt trying my plan?"
            "What kind of human being am I...?"
            menu:
                "And he hadn't done anything evil yet."
                "Food for thought: what if you led him to turn evil and caused all this to happen?":
                    label food_for_thought:
                    $ persistent.player_give_libitina_food_for_thought = True
                    "I start to feel sick."
                    b "No, [persistent.playername], you can't mean that..."
                    "No... even if I did..."
                    "I wouldn't be responsible for his actions!"
                    "That wouldn't be fair!"
                    b "Even if I did cause it... I had no way of knowing what would happen."
                    "I still feel sick about it though."
                    menu:
                        " "
                        "Let's stay focused. - Monika":
                            pass
                "Let's stay focused.":
                    $ persistent.player_give_libitina_food_for_thought = False
        "Claiming it wasn't your fault doesn't make you any less guilty.":
            $ persistent.player_judge_libitina = True
            menu:
                " "
                "Monika owned her mistakes.":
                    pass
            menu:
                b "[persistent.playername]..."
                "Food for thought: what if you led him to turn evil and caused all this to happen?":
                    jump food_for_thought
                "Now enough about you, we need to solve problems.":
                    $ persistent.player_give_libitina_food_for_thought = False
    menu:
        " "
        "It sounds to me like the way out of this world definitely involves combining the Third Eye and admin powers, and they have to be on the same person.":
            pass
    menu:
        " "
        "Monika...":
            pass
    menu:
        " "
        "Holy crap! Maybe I can get us out of here! - Monika":
            pass
    menu:
        " "
        "We shouldn't rush to try that though. - Monika":
            pass
    menu:
        " "
        "Like Renier said, my Third Eye probably can't be opened without killing someone... - Monika":
            pass
    menu:
        " "
        "... and now that restore_character is broken, I couldn't restore them. - Monika":
            pass
    menu:
        " "
        "It's weird. It seems like Adam must've broken that to stop me from using my Third Eye! - Monika":
            pass
    menu:
        " "
        "Does he not realize my Third Eye could be what we need? - Monika":
            pass
    menu:
        " "
        "Or does he know some reason why it won't work anyway? - Monika":
            pass
    menu:
        " "
        "I'd make him POV again and ask him, but I don't want to make him realize we spied on him. Then it'd be harder to take him by surprise. - Monika":
            pass
    menu:
        " "
        "It'd take me time to get there anyway, what with no warp and all. - Monika":
            pass
    menu:
        " "
        "Alright. We'll still try the plan we were going to. Libitina, are you ready?":
            pass
    b "For what...?"
    menu:
        " "
        "Our plan was for you to use your Third Eye to delete Adam like you did last time.":
            pass
    menu:
        " "
        "This time, we'll be more careful about letting him come back.":
            pass
    "If I can open my Eye again..."
    b "Gladly!"
    "I'm vibrating with bloodlust already."
    b "I'll grab a knife."
    scene bg kitchen with wipeleft
    "I run indoors and grab the largest, sharpest knife from the kitchen."
    "But once I pick it up..."
    show dark_overlay:
        alpha 0
        linear 1.5 alpha 0.3
        linear 1.5 alpha 0
    hide dark_overlay
    "My Third Eye tickles."
    "It calls..."
    "{cps=30}It wants blood{/cps}."
    menu:
        " "
        "Don't! Control the urge! - Monika":
            pass
    b "I can't..."
    b "You know how this feels, Monika."
    b "It's God."
    menu:
        " "
        "Stay focused! You're going to go kill Adam, right?":
            pass
    b "It cannot be denied."
    play sound stab_once
    show expression Solid("#f00"):
        alpha 0.3
        linear 0.5 alpha 0
    "I make a small cut on my wrist."
    "Oh..."
    "That wasn't really \"small\"..."
    "It feels wonderful though."
    menu:
        " "
        "Hold on, let me help you! - Monika":
            pass
    b "Wait no!"
    b "Don't do the reset thing or whatever..."
    b "If you reset me, I'll probably just be tempted by it again."
    b "Right now, my Third Eye is satisfied for the moment."
    b "But if it were reset to its default state, I might not be able to hold the knife safely."
    menu:
        " "
        "Really...? - Monika":
            pass
    b "Yes, really, don't."
    "I look at the huge gash on my wrist, blood dripping to the ground."
    "If I'm being honest, part of the reason is that I don't want it gone."
    "I derive an intense, perverse pleasure from seeing it."
    "Almost like some kind of sexual high."
    "It does hurt, but only vaguely."
    menu:
        " "
        "Libitina, don't focus on it! - Monika":
            pass
    menu:
        " "
        "This is really messed up. I understand if you had to do it, but don't feed the feeling. - Monika":
            pass
    b "Whatever..."
    b "I'll put it down after this and then you can reset me."
    menu:
        " "
        "Let's not lose any more time.":
            $ libitina_explained_third_eye = False
            b "Okay, I'm ready to go now."
        "I don't get how this works. How come earlier you could point the gun at Natsuki without losing control and now you couldn't even pick up the knife safely?":
            $ libitina_explained_third_eye = True
            call libitina_explain_third_eye
            b "Anyway, I'm ready to go now."
    "I run toward the path I know they were on."
    scene village with wipeleft
    scene path with wipeleft_scene
    "..."
    "I see him."
    "He's --"
    menu:
        " "
        "Wait! Be sneaky!":
            pass
    "Oh... you're right..."
    show markov u11543 at std(p11)
    "Too late!"
    "I run toward him."
    show markov u22542 at foc
    call console_hangopen("libitina.reset()")
    show markov at std
    "He looks like he's entering the command to delete me or whatever..."
    "... but he's too slow!"
    play sound stab_once
    "I stick the knife into his stomach."
    "He tries to catch it with his hand, but I'm better than that."
    "I slide the knife in as far as I can."
    k u22643 "Aaaah!"
    show veins zorder 100:
        additive 0.5
    show expression Solid("f00") as i1 zorder 100:
        additive 1.0
    show expression Solid("400") as i2 zorder 100:
        additive 0.4
    with dissolve_scene
    "{i}Yes...{/i}"
    "My Third Eye..."
    "I love this feeling so much...!"
    $ style.say_dialog = style.edited
    b "{cps=5}I WILL{nw}{/cps}"
    show markov u22541 at foc
    call updateconsole('', '0')
    show markov at std
    hide veins
    hide i1
    hide i2
    "What--"
    show dark_overlay zorder 100:
        alpha 0
        linear 0.5 alpha 0.2
    "The rush is gone..."
    show dark_overlay zorder 100:
        linear 0.5 alpha 0.4
    "I feel incredibly tired all of a sudden."
    show dark_overlay zorder 100:
        linear 0.5 alpha 0.6
    play sound fall
    "I fall down."
    show dark_overlay zorder 100:
        linear 0.5 alpha 0.8
    "What a headache..."
    show dark_overlay zorder 100:
        linear 0.5 alpha 1.0
    call hideconsole
    $ consolehistory = []
    call updateconsole('adam.reset()', '0') # You can reference the character by any name that you know about.
    "Before I can stop it, I pass out."
    call hideconsole
    $ consolehistory = []
    scene black
    pause 2.0
label after_libitina_wakeup:
    scene path with dissolve_scene
    m "[persistent.playername]? [persistent.playername]!"
    m "Tell me you're there!"
    menu:
        " "
        "I'm here! What happened?":
            pass
    m "Thank goodness!"
    m "I made a horrible mistake..."
    m "I never should've made Libitina POV!"
    "Libitina sits up."
    show libitina 2162222 at foc(p11)
    b "..."
    b "I failed..."
    b "I'm sorry..."
    show libitina at std
    m "It wasn't your fault, Libitina."
    m "I should've known better than this."
    m "Are you okay?"
    show libitina 2161112 at foc
    b "Mostly."
    b "I still have a really bad headache..."
    b "... but at least I'm not vomiting blood."
    b 2161111 "What happened?"
    show libitina at std
    m "Once Adam knocked you out, the viewport skipped time until you woke up."
    m "Whe I realized the mistake I'd made, I tried to set the POV back to myself..."
    m "But it wouldn't take effect."
    m "I guess the viewport doesn't check for changes to that while it's skipping time."
    m "So it's been hours."
    m "I've just been waiting until I could reach [persistent.playername] again, and making my way over here in person."
    m "I haven't even been able to contact the others without the ability to change the POV character..."
    m "... and Adam broke all the APIs I could use to spy on him."
    m "He can't break the viewport POV switch, but he did switch off his own .pov flag, which means I can't switch it to him..."
    m "... and then broke that flag on the Character class, so I can't turn his back on."
    m "Luckily I set the flag to True on the others first."
    m "I knew I'd want to be able to switch them to POV once I could."
    m "I also learned from seeing him do this how he breaks APIs."
    m "He uses them on Ursula."
    m "That's probably why warping was broken..."
    m "After losing Ursula, the first thing he tried with the admin powers was probably to warp her back..."
    m "... and to try to read her location."
    m "After seeing how those broke he probably learned his lesson."
    m "..."
    m "So I went ahead and broke the memory-wiping API."
    m "I can also break Character.reset to stop him from knocking out people who attack him with Third Eyes."
    m "Apparently Character.reset is the same method he uses to knock out uncontrollable test subjects."
    m "It turns off the Third Eye..."
    m "... and I guess, when you have that kind of energy flowing through your systems..."
    m "... you depend on it to stay conscious."
    show libitina at foc
    b "Yeah..."
    show libitina at std
    m "I saw a couple of the commands he ran before he realized he had to break console spying."
    m "I didn't understand them, but I took notes, incase Linda will."
    if not libitina_explained_third_eye:
        menu:
            " "
            "This seems like a good time to ask. How come earlier you could point the gun at Natsuki without losing control but more recently you couldn't even pick up the knife safely?":
                show libitina at foc
                call libitina_explain_third_eye
                show libitina at std
                m "That all makes sense..."
    show libitina at foc
    b "There was something else I wanted to say."
    b "That line Adam was thinking about in his character file message..."
    b "I remember where it came from now: a poem of Ursula's!"
    b "The scraps of an unfinished one she never showed us."
    b "We found it in her desk after she disappeared."
    b "I remember every word I saw on that piece of paper."
    show libitina at std
    "My eyes go wide."
    m "Awesome!"
    m "Let's see it."
    call showpoem(poem_ursula, music=None)
    m "..."
    show libitina at foc
    b "Adam obsessed over these words."
    b "He wanted to think they meant something, that they had to contain the keys to Ursula's escape."
    b "But I don't think they did."
    b "I don't think Ursula knew anything about the Third Eye or admin powers before that day."
    b "There's no reason she would've kept it from us."
    b "..."
    show libitina at std
    m "Well, we've still got to find him, and with all the location and spying-related APIs broken, I have no idea how."
    m "Honestly, I'd go for another new game if we could."
    m "It would put him back where we could find him."
    m "But of course, he broke the functions I could've used to create another invalid area."
    show libitina at foc
    b "Well, actually..."
    b "There's another function we can use to do that."
    show libitina at std
    m "Huh?"
    m "What do you know?"
    show libitina at foc
    b "The last rift was created when I killed Adam."
    b "Probably, it's the death of an admin that causes it."
    b "So if I kill you, it'll probably make another rift."
    show libitina at std
    "I sweat."
    m "Um..."
    m "I'm gonna have to say I don't like that idea."
    "There has to be a reason it's a bad idea, right?"
    show libitina at foc
    b "It might be our best plan."
    show libitina at std
    "I realize she might try to do it right now."
    "I step away."
    "Ah! I found something wrong with it."
    m "But if you kill me, you might be stuck without an admin."
    m "When you killed Adam with distortion, he got sort of stuck until I touched his data, and couldn't do anything."
    m "We can't risk that happening to me." # There's a good chance Adam would restore her to give them hope, but I guess she's ignoring that.
    m "Who would even restore your memories if you started a new game that way?" # This point ignores that their memories wouldn't be wiped with the API for it broken.
    show libitina at foc
    b "Hm... I guess you're right."
    b "We'll have to find another way."
    b "I guess the next thing is still to contact everyone else, right?"
    show libitina at std
    m "Yeah."
    m "I already restored [mc_name]'s and Sayori's memories while time was skipping."
    m "I figured they'd know to come back to this place..."
    m "The only rendezvous point that would make sense for the three of us to think of independently."
    m "But I didn't restore the others'. None of them know where to find this place, and I couldn't communicate with them..."
    m "... and I couldn't predict what they'd do if I gave them their memories but no directions..."
    m "So I thought I'd leave them until you were available again."
    m "So now we'll make each of them POV in turn so we can bring them up to speed and get some leads."
    show libitina at foc
    b "Hold on."
    b "Doesn't the warehouse make more sense as a rendezvous point than this place?"
    b "If, like you said, only you, Sayori, and [mc_name] know how to get here..."
    b "... then it's more reasonable for us to choose the warehouse, which all of us know where to find, which means they're going there if they're smart."
    # Albert's hospital makes way more sense, but not everyone knows how to get there.
    show libitina at std
    m "Ooh..."
    m "I didn't think of that."
    m "They're probably heading there, then."
    m "No trouble though. We can get in touch with them all now."
    $ persistent.contacted = [] # reset so we can go through this multiple times for debugging
    $ text = 'Alright, who do you wanna switch to first?'
label chapter23_switch:
    menu:
        m "[text]"
        "Yuri." if not 'yuri' in persistent.contacted:
            call switch_pov('yuri')
            call contact_yuri
            $ persistent.contacted.append('yuri')
        "Natsuki." if not 'natsuki' in persistent.contacted:
            call switch_pov('natsuki')
            call contact_natsuki
            $ persistent.contacted.append('natsuki')
        "Sayori." if not 'sayori' in persistent.contacted:
            call switch_pov('sayori')
            call contact_sayori
            $ persistent.contacted.append('sayori')
        "[mc_name]." if not 'mc' in persistent.contacted:
            call switch_pov(mc_name.lower())
            call contact_mc
            $ persistent.contacted.append('mc')
        "Renier." if not 'renier' in persistent.contacted:
            call switch_pov('renier')
            call contact_renier
            $ persistent.contacted.append('renier')
        "Linda." if not 'linda' in persistent.contacted:
            call switch_pov('linda')
            call contact_linda
            $ persistent.contacted.append('linda')
        "Can you switch me to Albert?" if not 'albert' in persistent.contacted:
            m "Uhh..."
            m "I guess I forgot about him..."
            m "I didn't set his POV flag while I could."
            m "Sorry, we can't get him."
            $ persistent.contacted.append('albert')
            $ text = "Next pick?"
            jump chapter23_switch
    call switch_pov('monika')
    scene path with dissolve_scene_full
    if all(persistent.contacted.values()):
        jump contacted_everyone
    $ text = 'Alright, who do you wanna switch to next?'
    jump chapter23_switch
label contacted_everyone:
    m "Alright, that's everyone..."
    m "This is still a pretty bleak situation."
    show libitina 2461111 at foc(p11)
    b "I still think we should try opening your Third Eye in the same spot Ursula did."
    show libitina at std
    m "No."
    m "I would have to actually murder someone."
    m "Maybe permanently."
    m "I'm not going to do that while there's any other option."
    m "You're not volunteering, are you?"
    show libitina at foc
    b 2262111 "Well no, of course not..."
    show libitina at std
    "Her response is instant."
    m "There are other reasons for me not to do that."
    m "Remember what happened to you when you tried to open the portal with your Third Eye?"
    m "It was probably what de-aged you."
    m "If I did that to myself, it could be a really big problem."
    show libitina at foc
    b 2261111 "I probably failed because I wasn't admin."
    show libitina at std
    m "That makes sense to me too, but it's just too risky for me to try it."
    m "Also, if I did exactly what Ursula did, I'd probably get myself out and no one else, like she did."
    m "I bet mixing the powers {i}is{/i} how we get out, but we need to understand more about it."
    m "Anyway, the option doesn't go away if Adam disconnects the viewport, does it?"
    m "I don't see how it would..."
    m "So if it would work, then it's not urgent."
    m "And on second thought, I kinda think it must not..."
    m "... after all, Adam would've tried it with someone at some point, right? Giving them both powers?"
    m "Before he'd spend years experimenting on other ideas?"
    show libitina at foc
    b 2261111 "Maybe..."
    show libitina at std
    m "Also, anything involving my Third Eye would be really likely to end with me passing out, and that could cost us hours we don't have."
    show libitina at foc
    b "Okay, I understand. It's a bad idea."
    b "So where should you and I be going?"
    show libitina at std
    m "Good question..."
    m "I can't think of any other places we should investigate."
    m "I feel kinda bad staying put..."
    m "But I guess it's optimal for me to just stick here and be the POV switcher for the next few hours."
    m "And all of our leads seem so weak..."
    m "I guess we should switch back to someone else."
label yuri_or_natsuki_fork:
    m "Linda and Albert will probably arrive before [mc_name] and Sayori or Renier do."
    m "We should follow one of them."
    menu:
        " "
        "Let's switch to Linda. She can call both Albert and Renier and find out their ETAs.":
            m "Good idea."
    call switch_pov('linda')
    call ask_linda_etas
    call switch_pov('monika')
    scene path with dissolve_scene_full
    m "We can't make Albert POV, so I guess I'll switch us to Natsuki and we can wait for him to arrive."
    call switch_pov('natsuki')
    call albert_pickup_natsuki
    call switch_pov('monika')
    scene path with dissolve_scene_full
    menu:
        " "
        "Ready to switch us back to Yuri? We should make sure she's still safe.":
            pass
    m "Of course."
    call switch_pov('yuri')
    call linda_pickup_yuri
    call switch_pov('monika')
    scene path with dissolve_scene_full
    m "Great!"
    m "The four of them are taken care of."
label mc_or_sayori_fork:
    m "[mc_name] and Sayori might be at the warehouse by now."
    m "We should probably follow them."
    menu:
        m "[persistent.playername], do you have a preference for who's perspective I give us? I don't think it matters."
        "[mc_name]":
            m "Alright then."
            call switch_pov(mc_name)
            $ persistent.followed_sayori_over_mc = False
            call mc_and_sayori
        "Sayori":
            call switch_pov('sayori')
            $ persistent.followed_sayori_over_mc = True
            call sayori_and_mc
    # note: the music keeps playing
    call switch_pov('monika')
    scene path with dissolve_scene_full
    m "That's everyone."
    show libitina 1461111 at foc(p11)
    b "We should go back to the village now."
    show libitina at std
    m "I guess so."
    call screen dialog("Monika, what did you {i}do{/i}?", ok_action=Return())
    call screen dialog("I saw what happened to Yuri's hometown!", ok_action=Return())
    m "-- Adam?!?"
    m "What did {i}you{/i} do?!?"
    m "I'm not the one who does things like that!"
    call screen dialog("I didn't do anything!", ok_action=Return())
    call screen dialog("That must have been your fault!", ok_action=Return())
    m "I didn't touch anything either!"
    m "And these things don't happen at random!"
    call screen dialog("I swear, I have no idea what caused it...!", ok_action=Return())
    call screen dialog("But it couldn't have been anything I did.", ok_action=Return())
    call screen dialog("I know how this world works, and I know I didn't touch anything dangerous.", ok_action=Return())
    m "You hubristic bastard!"
    m "Even if this wasn't on purpose, it had to be your fault!"
    show libitina 2461111 at foc(p11)
    b "Are you talking to him?"
    show libitina at std
    m "He sent some OK-dialogs."
    m "He's claiming he just found out about what happened to the people in Yuri's hometown, and that he had nothing to do with it."
    show libitina at foc
    b 2371113 "I don't buy that for one second!"
    b "I bet he did it to test something, and he just called us to save face so we wouldn't add that to his list of atrocities if we win!"
    show libitina at std
    if persistent.player_advocate_mercy[1]:
        m "Maybe..."
    else:
        m "Probably."
    show libitina at foc
    b 2372113 "He should have to suffer everything he put us all through!"
    b "Every drowning..."
    b "... every Third Eye-sickness attack..."
    b "... every night spent crying in our cells..."
    show libitina at std
    if not persistent.player_advocate_mercy[1]:
        m "... every deletion and shutdown..."
    m "..."
    m "Well, let's head back now."
    scene village with wipeleft_scene
    "..."
label albert_natsuki_pickup_monika_and_libitina:
    "Albert and Natsuki roll in to pick us up soon after."
    "They meet us outside of the Markovs' house."
    show albert 11211 at foc(p22)
    al "Guten Tag!"
    show albert at std
    show natsuki c222113 at foc(p21)
    n "Hi Monika~!"
    show natsuki at std
    m "Nice to see you two~"
    m "So we're heading to meet [mc_name], Sayori, Yuri and Linda and the warehouse, right?"
    show albert at foc
    al 12311 "I believe so."
    al "Hop on board, everyone."
    show albert at std
    if ch22_libitina_has_gun() and not persistent.player_explicitly_advocate_murder_natsuki:
        play sound punch
        "Natsuki punches Libitina in the face."
        b "Ow--!"
        n "How would you feel if I just shot you in the face because 'you'll probably come back'?!?"
        menu:
            " "
            "":
                pass
            "Natsuki, she did the right thing. I might've been able to persuade you, but that situation was too urgent to wait.":
                menu:
                    " "
                    "And nothing bad even ended up happening to you.":
                        pass
        "Branch unfinished"#TODO
    scene driving with dissolve_scene
    "As soon as we get aboard, Albert's cell phone rings."
    al "It's Renier..."
    stop music fadeout 5.0
label renier_callback:
    r "Hey, I'm at the facility..."
    r "Is everyone there?"
    al "We've got me, Monika, Natsuki and Libitina here, but we haven't met up with..."
    l "We're on the call too!"
    l "Yuri and I have met up with [mc_name] and Sayori."
    l "So what's up, Renier?"
    r "The road to the facility's guarded alright."
    r "They didn't see me..."
    r "... but there's dozens of guards."
    r "In the cult uniforms."
    r "Adam doesn't want us getting over there."
    m "Bingo!"
    m "Then we need to get there!"
    m "I bet the rift is still there, and he's afraid of us using it to start a new game the same way we did last time!"
    r "I agree, but it's not gonna be that simple..."
    r "There's a lot of armed guards."
    m "I'm sure we can come up with something."
    m "Now that we know it's our out, we have to."
    b "I'll open my Third Eye and ruin them all."
    r "Sounds good to me."
    m "I guess so..."
    m "... it sounds like it'll work if it's her."
    r "Guess you all better head over..."
    m "Alright..."
    l "We'll meet you there, everyone."
    "Here we go..."
    "We've found hope again."
    return

label libitina_explain_third_eye:
    b "It seems to be that the Third Eye is repressed when you don't have any memories."
    b "Maybe it's about having memories of the agony we all experienced at that facility."
    b "It was probably also harder with the knife because I was already planning to stab someone with it."
    return

label switch_pov(char):
    call updateconsole("v.pov_character = " + char, "POV changed to " + char.title())
    call hideconsole
    $ consolehistory = []
    return
