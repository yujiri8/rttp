label chapter16:
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u224231 at std(p41)
    show natsuki u114123 at std(p42) zorder 1
    show yuri u125131 at std(p43)
    show renier ru2283 at std(p44)
    with open_eyes
    mc "So that's how all this started..."
    show renier ru1283 at foc
    r "I'll be..."
    r ru1213 "Well..."
    r "Here we are."
    r "It's nice to finally meet all of you..."
    show sayori u224111
    show natsuki u114111
    r ru12331 "... not as your torturer."
    show renier at std
    "..."
    show yuri at foc zorder 1
    y u125111 "It's nice to finally meet you..."
    y u12b114 "Not as your {i}prisoner{/i}."
    show yuri at std zorder 0
    show renier at foc zorder 1
    r ru1233 "..."
    show renier at std zorder 0
    show yuri u125111
    show renier ru1113
    show natsuki at foc
    n "It's nice to meet you two in person, [mc_name] and Sayori..."
    n "For the first time knowing our history."
    show natsuki at std
    show sayori at foc
    s u213111 "It's nice to meet you too, Natsuki..."
    s "... and [mc_name] and Yuri again."
    s u11x211 "And in happier circumstances than I thought we ever would..."
    show sayori at std
    "It seems like it's a ritual that we all have to go through this now."
    mc "Yeah, nice to be back with you, Sayori..."
    mc "Good thing that ambush wasn't the end of us."
    "I smile despite the situation we're in."
    show sayori at foc
    s u115112 "Although, actually, maybe we'll end up wishing it had been after all this..."
    show sayori at std
    show natsuki at foc
    n u324111 "You can't go thinking that way Sayori."
    n "You gotta make the most of a crappy situation."
    show natsuki u124111 at std
    show sayori at foc
    s u115112 "Okay..."
    s u11x212 "I'll try..."
    show sayori at std
    show natsuki at foc
    n u114113 "So... Yuri..."
    n "I guess we're sisters?"
    show natsuki at std
    show yuri at foc zorder 1
    y "I think so..."
    y "Markov changed all our names, probably to reduce the odds of us remembering."
    y "And Renier and Linda didn't get name changes because they snuck in."
    show yuri at std zorder 0
    show renier zorder 1
    menu:
        " "
        "So...":
            pass
    menu:
        " "
        "Our plan is?":
            pass
    menu:
        " "
        "That still didn't tell us how to fix our situation.":
            pass
    show natsuki u114111
    show sayori at foc
    s u116113 "Mmm..."
    s u213111 "Well, first things first."
    s "I gotta turn this awful music off."
    show sayori at std
    mc "Music? What are you talking about?"
    show sayori at foc
    s "Maybe this one..."
    play music yawa
    show sayori at std
    show natsuki at foc zorder 1
    n u124111 "I don't hear anything."
    show natsuki at std
    show sayori at foc zorder 2
    s u113111 "Aw, I forgot you guys couldn't hear it."
    s "It's the game's music."
    show sayori at std
    show yuri at foc
    y u125113 "Isn't it a bit... strange..."
    y "... to be picking music to listen to while we're in an {i}actual{/i} life and death situation?"
    show yuri at std
    show sayori at foc
    s u115111 "I mean..."
    s u213111 "If we're in a life and death situation, might as well not make ourselves more miserable by listening to that ominous drawl for an hour."
    show sayori at std
    mc "Fair enough..."
    show sayori at foc
    s "So, what we have to do is still revive Linda."
    s u215111 "Let me try that reset method..."
    show sayori at std
    show natsuki at foc
    n xu4111 "Well, here we go with the hacking again."
    n "Brace yourselves."
    show natsuki at std
    show sayori at foc
    s u213111 "Don't worry, I'll be careful..."
    call updateconsole("linda.reset()", "0")
    call hideconsole
    $ consolehistory = []
    play sound glitch_basic
    $ restore_character('linda')
    show yuri u125218
    show renier ru1113
    show natsuki u113211
    s u213213 "Uh--"
    show sayori at std
    show natsuki at foc
    n u113211 "Did you just break something?!?"
    show natsuki at std
    show sayori at foc
    s u213211 "No, look, the return code is 0!"
    s "That means it worked!"
    show sayori at std
    menu:
        " "
        "Sayori's right. Linda's file is back. So the .reset method did work.":
            pass
    show yuri u113111
    show natsuki u114213
    show renier ru1113
    show sayori at foc
    s "Let me try to bring her in!"
    show sayori at std
    call updateconsole("warp('linda', 'space_room')", "Failed: character dead")
    call updateconsole("restore_character('linda')", "Failed: character already alive")
    call hideconsole
    $ consolehistory = []
    show natsuki u114111
    show sayori at foc
    s u223114 "Oh come on!"
    s "If I try to warp her here, it says she's dead; if I try to restore her, it says she's alive!"
    s u215113 "At least it's different errors than before..."
    show sayori at std
    menu:
        " "
        "Maybe the old delete-restore trick?" if persistent.sayori_reset_ynr:
            show sayori at foc
            s u215111 "I'll try it..."
            call updateconsole("os.remove('linda.chr')", "linda.chr deleted successfully")
            $ delete_character('linda')
            call updateconsole("restore_character('linda')", "Linda restored successfully")
            $ restore_character('linda')
            call updateconsole("warp('linda', 'space_room')", "Failed: character dead")
            call updateconsole("restore_character('linda')", "Failed: character already alive")
            call hideconsole
            $ consolehistory = []
            s u113113 "Ugh..."
            s "It's just the same errors..."
        "Should I try deleting and restoring her file?" if not persistent.sayori_reset_ynr:
            show sayori at foc
            s u115113 "Well..."
            s "I don't know what else to try."
            s u113111 "Sure, go ahead."
            show sayori at std
            menu:
                " "
                "Alright. I deleted and restored the file.":
                    pass
            $ restore_character('linda')
            show sayori u213111 at foc
            call updateconsole("warp('linda', 'space_room')", "Failed: character dead")
            call updateconsole("restore_character('linda')", "Failed: character already alive")
            call hideconsole
            $ consolehistory = []
            s u223113 "Gah..."
            s "It didn't fix it."
            show sayori at std
    menu:
        " "
        "Any other ideas?":
            pass
    menu:
        " "
        "You're the only one with access to the internals of the game.":
            pass
    show sayori at foc
    s u113121 "Well..."
    s u113111 "I could try to restore some more of the world."
    s "Maybe the way it comes back will give me a clue."
    show sayori at std
    mc "Let's go for it."
    mc "I'd love to get out of this place."
    show renier ru1111
    show sayori at foc
    s u213111 "Okay..."
    call updateconsole("restore_area('club_day')", glitchtext(20))
    s u213112 "Oh no..."
    show sayori at std
    show yuri u125218
    show renier ru1113
    show natsuki at foc
    n u113211 "Crap stop it!"
    show natsuki at std
    show sayori at foc
    call updateconsole("restore_area('club_day')", glitchtext(200))
    show sayori at std
    s "Huh."
    show natsuki at foc
    n u115211 "What the hell are you doing?!?"
    show natsuki at std
    menu:
        " "
        "Sayori, did you just call a function, get an error, and then do the exact same thing again?":
            pass
    show sayori u123114 at foc
    s "But it got a different result!"
    show sayori at std
    menu:
        " "
        "Yeah... a different amount of glitch text.":
            pass
    s u123121 "Well let's see what happens if I try it a third time..."
    show natsuki at foc
    n "{cps=200}Are you serious?{nw}"
    show natsuki at std
    call updateconsole("restore_area('club_day')", glitchtext(200))
    s u123111 "See?"
    s "It's the same as the second time!"
    s "That's proof it did something the first time!"
    show yuri at foc
    y u126115 "That doesn't prove anything!"
    y "If it's glitch text and not an error message, then the amount of it is probably meaningless!"
    show yuri at std
    show sayori at foc
    s t1221 "Oh..."
    s "I guess you're right..."
    s u123111 "What if I try it more times?"
    s "Even if it's just glitch text, if it was a small amount the first time and always a big amount after, then that's evidence that there's a pattern."
    show sayori at std
    show yuri at foc
    y u125115 "I suppose so..."
    y "But I'd still prefer a solution that didn't involve doing things that are giving us errors and guessing when it might be safe to assume it worked."
    show yuri at std
    show renier at foc
    r ru1213 "I say go for it."
    r "Even if she's throwing darts at the wall, there's not that many ways to make this situation worse."
    show renier at std
    show sayori at foc
    s "Okay..."
    call updateconsole("restore_area('club_day')", glitchtext(200))
    call updateconsole("restore_area('club_day')", glitchtext(200))
    call updateconsole("restore_area('club_day')", glitchtext(200))
    call updateconsole("restore_area('club_day')", glitchtext(200))
    s u113111 "Okay, that's six tests now."
    s "I'm pretty sure something happened the first time."
    show sayori at std
    show natsuki xu6211
    show yuri at foc
    y u125113 "Well, I suppose that's enough tests for me..."
    y "But what do we do with it?"
    y "How does restoring more of the world help us?"
    show yuri at std
    show sayori at foc
    s u123111 "Well, we should try warping someone to the clubroom now to see if it really worked."
    s u115112 "It's kind of a dangerous role though..."
    show sayori at std
    show natsuki at foc
    n u113112 "Are you serious?"
    n "{i}That's{/i} your plan?"
    n "Warp one of us into an area that's probably invalid or something, and {i}hope{/i} it works?"
    n "{i}Still{/i} with no idea what we're gonna do if it does?"
    show natsuki at std
    show sayori at foc
    s "Well, yeah..."
    s u113112 "I don't see any other options."
    s u113111 "And this kind of plan has never had more than temporary consequences before."
    show sayori at std
    menu:
        " "
        "Can't you do it yourself?":
            menu:
                " "
                "Isn't it kind of low to suggest a dangerous plan and make someone else be the one to risk themselves?":
                    show natsuki u114114
                    $ persistent.player_guilt_trip_sayori = 2
                    show sayori at foc
                    s u113313 "Ah--"
                    s u223313 "No!"
                    s u113313 "I feel bad about it too, but it can't be me."
                    s "I'm the only person with admin powers right now."
                    s "If I mess myself up, we might be stuck."
                    if mc_dislike_player() + (persistent.mc_favorite == "Sayori") > 2:
                        show sayori at std
                        mc "Don't let [persistent.playername] make you feel bad about it, Sayori."
                        $ temp = persistent.player_subj_pronoun.title()
                        mc "[temp]'s just a prick."
                        show sayori at foc
                        s u114111 "..."
                "(continue)":
                    $ persistent.player_guilt_trip_sayori = 1
                    show sayori at foc
                    s u113211 "It can't be me."
                    s "I'm the only person with admin powers right now."
                    s "If I mess myself up, we might be stuck."
                    show natsuki u114111
        "(continue)":
            $ persistent.player_guilt_trip_sayori = 0
    show sayori at std
    mc "I volunteer."
    if persistent.mc_favorite == 'Natsuki':
        show natsuki u114114
    show sayori u114112
    mc "I just wanna get out of this place."
    mc "It brings back too many bad memories."
    show sayori at foc
    s u113111 "Okay."
    s u213112 "Be safe, [mc_name]..."
    show sayori at std
    call updateconsole("warp(" + mc_name.lower() + ", 'club_day')")
    call hideconsole
    $ consolehistory = []
    scene black
    stop music fadeout 1
    "..."
    mc "Uh oh."
    play music glitch_flatline
    mc "Sayori?!?"
    mc "Crap!"
    menu:
        " "
        "[mc_name], are you okay?":
            mc "[persistent.playername], are you there?"
            mc "Can you--"
            mc "Oh, of course you can't answer me..."
            menu:
                " "
                "[mc_name]!":
                    pass
            mc "Sayori, help!"
    call screen dialog("[mc_name], are you okay?", ok_action=Return())
    call screen dialog("Sorry about this!", ok_action=Return())
    call screen dialog("Just hang in there!", ok_action=Return())
    "She's not answering either..."
    "Oh no, oh no..."
    $ l_name = glitchtext(5)
    $ gtext = glitchtext(100)
    l "{cps=50}[gtext]"
    play sound glitch_medium
    call screen dialog("Uh-oh!", ok_action=Return())
    $ persistent.autoload = "mc_in_void"
    call screen dialog(persistent.playername + "! Turn the game off!", ok_action=Return())
    while True:
        ""
    # There might be different ways this can go if the player deletes Linda.
label chapter16_2:
    $ persistent.autoload = None
    scene bg notebook-glitch
    play music glitch_flatline
    $ gtext = glitchtext(15)
    mc "[gtext]!"
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    mc "Ow!"
    mc "What's happening?!?"
    mc "It hurts!"
    $ l_name = glitchtext(5)
    l "Who..."
    mc "Help!"
    l "Renier, where are yoU"
    mc "Linda...?"
    l "I failed"
    l "You're our only hope"
    mc "Where are you?"
    l "I failed"
    l "can you here mE"
    mc "Linda!"
    "I'm screaming at the top of my lungs, but I'm not sure if any sound is coming out."
    "Where am I?"
    "Why is the noise like this?"
    "Is Sayori powerless to fix this...?"
    "Cause I'm in over my head!"
    l "static"
    l "the kids"
    l "our mission"
    l "Clare where is she"
    mc "Linda it's Daniel can you hear me!"
    l "Where's Daniel?"
    l "You have to find him..."
    "She's hearing me, at least in some way..."
    "What the hell is going on?!?"
    "The static makes me feel like my head is exploding!"
    l "Help us"
    mc "Linda, I'm Daniel!"
    mc "Can you hear me?"
    l "Where is DanieL?"
    "I don't know what's up with her, but is there something I can say to snap her out of it?"
    mc "Linda, there's something terribly wrong with this family and you accepted the invitation to become a part of it!"
    l "I know!"
    l "I wanted to fix it!"
    $ gtext = glitchtext(10)
    l "How do we [gtext]"
    "I bet what she just said was important, but I didn't catch it!"
    l "Help me Daniel/"
    mc "Sayori!!"
    mc "It hurts!"
    mc "Can you fix this?!?"
    "God!"
    mc "Linda, we have to get out of this illusory world!"
    l "No, can't, we have our mission!"
    l "Don't give up("
    l "Don't make me waste"
    "I can't think when everything's like this!"
    "The static hurts so much!"
    mc "Linda help me!"
    l "Help me..."
    l "Help them..."
    l "vvvvv"
    mc "Someone..."
    mc "Can anyone hear me?!"
    l "I tried to send her the truth."
    l "But I don't even know if it worked"
    mc "Linda, we're all here..."
    mc "Clare, me, Daniel, Abbey, Elyssa, Maria, and Renier..."
    mc "Stop whatever you're doing!"
    "I have an idle theory that Linda in her delirium when the game came back on tried to fix things and is stopping Sayori from fixing them."
    l "Okay..."
    "{i}... Really?{/i}"
    stop music
    play sound glitch_squarewave
    hide noise with Dissolve(2)
    hide vignette with Dissolve(2)
    pause 2.0
    scene black
    "Everything's quiet..."
    "{cps=60}That's{nw}"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    s "--Ah!"
    play music m1
    $ l_name = "Linda"
    show sayori u227112 at foc(p41) zorder 1
    show yuri u227138 at std(p43)
    show natsuki u115114 at std(p42)
    show renier ru11a3 at std(p44)
    s "[mc_name]!"
    show sayori at std
    mc "Ow..."
    show natsuki u114114
    show renier ru1113
    mc "What the hell..."
    show sayori u224112 at x(p51)
    show natsuki at x(p52)
    show yuri u114118 at x(p11)
    show renier u22a3 at x(p54)
    show linda 115333 at std(p55)
    l "Ow..."
    l "Please never do that to me again..."
    show linda at thide
    hide linda
    "Linda lays down." # Maybe I should increase Linda's reaction before instead of here. But before I needed to show her sprites.
    show renier at xif(p54)
    r u2233 "Thank God..."
    show renier at std
    mc "{i}What{/i} just happened?"
    show sayori at foc
    s u223211 "I don't know!"
    s "Everything got messed up!"
    s "But we got Linda back!"
    s "So I guess my plan worked..."
    s u213112 "Are you okay, [mc_name]?"
    show sayori at std
    mc "Yeah..."
    mc "But what was happening to me?"
    mc "It was like an endless cacoph-"
    mc "..."
    mc "Was {i}that{/i} what it was like for you and Monika when the game was off...?"
    show sayori at foc
    s u113112 "We couldn't think during ours, but it might've been the same feeling."
    show sayori at std
    mc "I can't imagine being stuck like that for more than a few minutes..."
    mc "Monika said it was hell..."
    mc "But I guess you never understand until you go through it yourself."
    show linda 334113 at foc(p55)
    l "Sorry about that, [mc_name]..."
    l "I think it was my fault."
    show linda at std
    mc "So what happened to you?"
    mc "It seemed like you had got back your old memories and forgot everything since we met you...."
    mc "... But now you remember it all?"
    show renier u1113
    show sayori u114111
    show natsuki u114111
    show yuri u113111
    show linda at foc
    l 334111 "I was in some kind of state like I was before you brought me in the first time."
    l 334221 "I hate being like that."
    l "It hurts so much."
    l "I thought making it into this world the first time was the end of me having to go through that."
    l 334111 "I guess since the game was glitched, memory segmentation wasn't working properly?"
    l 123111 "But that's right!"
    l "Monika left my memories intact, right?"
    l "So I can just unlock them now that the deep script is gone."
    show linda at std
    show renier u1114
    mc "Awesome!"
    show sayori at foc
    s u213111 "Wait, the music changed back to the spooky drawl..."
    s u21x111 "Let's give this moment a proper triumphant theme!"
    show sayori at std
    play music t8
    show linda at foc
    l 123111 "Haha, this is nicer!"
    l "Okay, here we go..."
    call updateconsole("linda.old_memories.unlock()", "Linda's memories unlocked")
    $ consolehistory = []
    call hideconsole
    show natsuki u114113
    show linda 119441
    l "."
    "Expected reaction so far..."
    show renier u1113
    l "Oh... My..."
    l "..."
    show linda 117111 with Dissolve(1.0)
    "Linda's expression gradually turns to a mischievious smile."
    l "Hahaha..."
    show linda at std
    show renier at foc zorder 4
    r "... Linda...?"
    show renier at std
    show linda at foc zorder 5
    l "After all that..."
    l 123111b "I think we got him!"
    show linda at std
    mc "What do you remember?"
    show linda at foc
    l 123111 "Everything."
    l "Portrait of Markov, both versions, was the product of some assembled memories I read from different people while I was a ghost in Markov's world."
    l "I actually did this because I anticipated something going wrong with me and Renier's hijacking."
    l "I wanted to give us a way to remember."
    l "Reading the memories took a lot of work, to load the proper time period and decode them..."
    l "... so I had to be selective."
    l "I picked mostly Elyssa's memories from the time leading up to her capture, since I had a hunch she'd be the admin."
    l "If I'd known Clare was going to be the admin, I'd have dug up more of hers."
    l "I tried to edit them into something that'd be believable as a novel, so the game would accept it as a replacement for whatever book Yuri was supposed to have."
    l "When Renier and I snuck aboard, it went badly, as I feared..."
    l "Renier lost his memories and got used by the script as Natsuki's dad instead of a placeholder NPC..."
    l "... and I retained my memories, but I didn't manage to manifest as a character."
    l "I only got \"halfway in\", so to speak."
    # Some more explanation of how Markov designed Presidency could happen.
    l "After the first few hours, Markov would've noticed what had happened and pulled us out..."
    l "But he didn't anticipate Monika breaking the entire game after Sayori became President."
    l "He must've not been able to get us back with the gameworld in that state."
    l "He probably forgot about this world in the time since then and when [persistent.playername] managed to reopen it."
    show linda at std
    menu:
        " "
        "Okay, so...":
            pass
    menu:
        " "
        "Once again...":
            pass
    menu:
        " "
        "Our plan is?":
            pass
    show linda at foc
    l "I've got an answer for that too!"
    l "The DDLC software isn't specifically tied to this world."
    l "It's a 'virtual reality viewport', and I think I know what we have to do to point it at Markov's world and get ourselves back there."
    l "We just need Markov's PGP key to pass the authentication portal."
    l 123331 "And that's what's in my character file!"
    l 123111 "I snooped the key off his computer!"
    show linda at std
    show sayori u222211
    show yuri u112131
    show natsuki u112113
    show renier u1115b at foc
    r "Awesome!"
    r "You planned for everything."
    show renier at std
    show linda at foc
    l 122111b "Thanks."
    show linda at std
    menu:
        " "
        "So how are we using it?":
            pass
    show linda at foc
    l 124111 "What we have to do is a little difficult."
    l "We need to do two things."
    l "We need to use Markov's key to issue an authoritative command to extract ourselves from this world..."
    l "... and we need to change where the player's viewport is pointed at."
    l "And we need to do them at the same time."
    l "If either one goes wrong, I'm not sure what kind of fix we'll be in."
    l "I'm going to expose the file you need to edit."
    show linda at std
label chapter16_argument:
    stop music fadeout 3.0
    show sayori u224112
    show yuri u114113
    show renier ru1113
    show natsuki at foc zorder 1
    n u224111 "Hold it."
    n "How is this plan gonna work?"
    n "Won't we come out right inside Markov's lair..."
    n u223111 "... with no way to defend ourselves?"
    show natsuki at std
    show linda at foc
    l 114222 "Well..."
    l 114112b "Yes, but [persistent.playername] will be following from the viewport!"
    l 114112 "With luck, [persistent.player_subj_pronoun] can just delete Markov."
    l "[mc_name] meeting him should give him a character file."
    show linda at std
    show natsuki at foc
    n u224111 "Maybe..."
    n "But at best, that only works if we can get [mc_name] face-to-face with Markov."
    n u223111 "That sounds hard on its own!"
    n "And didn't Monika show us that being deleted doesn't stop a person with admin powers?"
    show natsuki at std
    show linda at foc
    l 114112b "Well, yes..."
    show linda at std
    show natsuki at foc
    n "So what are we gonna do?"
    n "He'll keep deleting us, and [persistent.playername] will just keep restoring us and deleting him until he gives up and begs for mercy?"
    show natsuki at std
    show renier at foc
    r ru2113 "Well, why not?"
    r "We'd win, right?"
    r "Markov would have no power over [persistent.playername]."
    show renier at std
    show linda 114111
    show natsuki at foc
    n u124131 "I mean, I guess..."
    n "I guess I don't see any other options."
    n u124111 "But this is still assuming that Markov killing [mc_name] wouldn't cut off [persistent.playername]'s connection..."
    n "... and that we can get [mc_name] face-to-face with him before his flunkies kill us..."
    n "... and that character files work the same way in that world..."
    n "... and that Markov doesn't have any other tricks to stop himself from being deleted."
    n "It hardly seems like an airtight plan."
    show natsuki at std
    show yuri at foc zorder 6
    y u125111 "What about the nightmares?"
    y "[persistent.playername] might also be able to torture Markov into submission by turning the game on and off..."
    y "... and that wouldn't require getting [mc_name] to him."
    show yuri at std zorder 2
    show linda at foc
    l 124111 "We've got that too."
    l "I don't know if the nightmares will still happen in that world, but [persistent.playername] can try it if we can't delete him."
    show linda at std
    show renier at foc
    r ru1213 "We also have our Third Eyes."
    r "Four of us have them..."
    r "And if we can trigger their powers, like Clare and Daniel and Abbey did to escape the first time, then they could have a hard time controlling us."
    show renier at std
    show natsuki at foc zorder 3
    n u223111 "Do you remember what happened the last time someone tried to use their Third Eye for good?"
    show natsuki at std
    show renier at foc
    r "What, it worked?"
    show renier at std
    show natsuki at foc
    n xu3231 "Well, technically!"
    n xu4131 "I guess that did do what we couldn't have done any other way..."
    show natsuki at std
    show renier at foc
    r ruf13 "I remember how much it hurt..."
    r "But they could help."
    show renier at std
    show natsuki at foc
    n u124111 "Well, you're right."
    n "The Third Eyes could save us here."
    n xu4131 "(I'm still glad I don't have one, though...)"
    show natsuki xu4111 at std
    show yuri at foc zorder 6
    y u125111 "Also..."
    y "[persistent.playername] ought to be able to just restore our files if we're killed."
    y "And as long as [persistent.player_subj_pronoun] can restore us..."
    y u125112 "... death isn't anything new to any of us."
    y u126114 "I'm in favor of this plan."
    show yuri u124111 at std zorder 0
    show natsuki at foc
    n xu4111 "Well..."
    n xu4114 "(Oh Christ...)"
    n u114111 "So am I, I guess."
    n "There are three different ways we could win..."
    n "And it doesn't seem like there's anything else we {i}can{/i} do."
    show natsuki at std zorder 1
    show yuri u124111
    call chapter16_argument_monika
    show linda 114113b
    mc "Linda, you really tried to lie to us just now, didn't you?"
    mc "You knew you weren't sure and changed what you were saying!"
    show linda at foc
    l 119113b "I had to convince her!"
    l "This is too important!"
    l "Even if we have to leave Monika behind, we {i}have{/i} to do this!"
    l "Think about Markov's other subjects!"
    l "Every minute we waste..."
    show linda at std
    call chapter16_end_argument
    show sayori at foc
    s "...!!"
    s u115293 "Okay... you're right..."
    s u115213 "Knowing we failed because I wouldn't leave Monika behind would be worse than knowing I left her behind."
    show sayori at std
    play music determination
    show natsuki u114124
    show yuri u125128
    mc "Alright..."
    mc "I guess we're doing this..."
    return

label chapter16_argument_monika:
    show sayori at foc zorder 2
    s u223212 "Wait!"
    s u113212 "What about Monika?"
    show natsuki u114114
    show yuri u114118
    show renier ru1113
    s "We still haven't got her back."
    s u223212 "We can't leave her behind!"
    show sayori at std
    "I forgot about that..."
    "Even I wouldn't dream of leaving Monika behind, even after all I've suffered at her hands."
    show linda 115332
    "Linda sighs."
    show linda at foc
    l 114112 "I think Monika might've already escaped during her Third Eye frenzy."
    l "That might've been why the error was 'character missing'."
    l "We don't exactly have any other options though."
    l "There's no way to prove that she isn't still in here."
    l "So we'll have to hope."
    show linda at std
    "..."
    show sayori at foc
    s u115112 "... Hope...?"
    s "That's..."
    s "... not good enough..."
    s u227213 "We have to {i}know{/i} she's not in here!"
    show sayori at std
    show linda at foc
    l "But..."
    l "If we get out, we'll be able to check for sure."
    l "I don't think-- I mean, leaving this world won't destroy it."
    show linda at std
    show sayori at foc
    s u227214 "You don't {i}think{/i}?"
    show sayori at std
    show linda at foc
    l "And we would be able to just reinsert ourselves if we needed to..."
    show linda at std
    show sayori at foc
    s "You don't {i}think{/i} your plan will destroy this world on the way out?"
    show sayori at std
    return

label chapter16_end_argument:
    show natsuki at foc zorder 3
    n u114124 "Um, guys?"
    n "I just realized something else."
    n "If Monika escaped, then she probably came out in the facility too."
    n u113124 "If I were Markov I'd sure as hell come check on my old experiment if a subject came out of it!"
    show yuri u125125
    show sayori u227232
    show renier ru1183
    n u117124 "We're sitting ducks in here!"
    show natsuki at std
    show linda at foc
    l 119443b "Oh crap, I didn't even think about that!"
    l "I just thought it was urgent because of the gravity of the situation!"
    l 119113 "How many minutes do you think we have left, Sayori?"
    l "Every second we wait is a chance that --"
    show linda at std
    show sayori at foc zorder 4
    s u227212 "But wait!"
    s "That's evidence that Monika {i}didn't{/i} escape!"
    s "If she had, Markov would've caught onto us by now!"
    s "That was like an hour ago, at least!"
    s "It wouldn't have taken him that long to investigate!"
    show sayori at std
    mc "And if Monika didn't escape, then we still have time..."
#    show sayori at foc
#    s "And don't you act like she wouldn't be useful, Linda!"
#    s "She has both admin powers and the Third Eye!"
#    s "{i}And{/i} she might've learned something we could use to know!"
#    show sayori at std
    show linda at foc
    l "Maybe Monika came out like I did the first time, because she broke out the wrong way!"
    l "That would explain everything!"
    l "One way or another every minute we wait is a minute Markov's other subjects suffer!"
#    l "And even ."
    l "If we're doomed without her we're doomed with her."
    show linda at std
    return
