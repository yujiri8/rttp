label chapter8:
    scene black with dissolve_scene
    scene living_room with wipeleft_scene
    play music yawa fadeout 3.0
    "We head to my house for the time being."
    "Monika, Sayori and Linda are in a separate room to work on their hacking stuff so we don't disturb them."
    "Linda said it would probably be at least a few hours before they figured out how to fix this."
    "Me, Natsuki, Yuri, and Renier are left in the living room, unable to help."
    show yuri c124113 at foc(p11)
    y "Um..."
    y "I'm going to go get some air."
    show yuri at thide
    hide yuri
    if persistent.mc_favorite == "Yuri":
        "I really want to spend some time alone with her, but I imagine she'd like a minute to herself first."
        "She hasn't had that since this morning."
    else:
        "I can definitely see needing some time alone."
        "Poor girl hasn't had any since this morning."
    "The day's just been bombshell after bombshell."
    show natsuki c223111 at foc(p11, a=1.0)
    n "No cutting yourself!"
    show natsuki at uf
    "Natsuki calls out just before Yuri leaves."
    show yuri c227235 at hopfoc(p33)
    y "Ah--!"
    y c226235 "I wasn't going to!"
    show yuri at uf
    show natsuki at foc
    n c214111 "Just reminding you..."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    "Yuri leaves."
    "The remaining three of us sit in silence for a moment."
    mc "Dang. What a day already."
    mc "I feel like I could take a nap right now."
    show renier u2113 at std(p11)
    r "You might as well."
    r u11131 "It doesn't sound like we'll be needed for a while."
    show renier at thide
    hide renier
    "I shrug."
    "At the same time, I feel much more closely connected to the club members than I ever did before."
    "I'd rather spend time with them."
    "I guess going through all that with a few other people creates that kind of bond."
    show natsuki c114111 at std(p11)
    "Natsuki leaves the room also, and beckons me to follow her."
    scene bg house with wipeleft
    mc "Want to talk?"
    show natsuki xc4131 at foc(p11)
    n "Yeah..."
    n "There's so much to think about..."
    n xc4111 "I'm still kind of worried about both Yuri and Sayori."
    n "Knowing what they were going through while I didn't have a clue..."
    show natsuki at uf
    mc "I definitely share that feeling."
    mc "Even you, I had no clue what you were going through."
    show natsuki at foc
    n "Well, I kept it hidden on purpose..."
    n "But I guess so did they."
    play music t9 fadeout 3.0
    n c114114 "[mc_name]..."
    n "Do you remember the message I tried to send you in Act 2?"
    show natsuki at uf
    mc "Yeah..."
    mc "I'm sorry I couldn't act on it."
    show natsuki at foc
    n c11s311 "I just wish I had've tried to do something sooner..."
    n "I wish I had've just had one genuine conversation about it..."
    n "... about anything..."
    n c11s214 "With anyone else before I died."
    if persistent.mc_favorite == "Natsuki":
        show natsuki at uf
        mc "Natsuki, none of that was your fault!"
        mc "You did everything you could."
        show natsuki at foc
        n xc4134 "I know..."
        n "And thanks..."
        n "But I still just wish I could've."
    n c114114 "You remember my first poem?"
    n "'People can try, and that's about it'..."
    show natsuki at uf
    mc "Yeah..."
    mc "I was thinking about that while I watched Yuri's... Yuri's corpse..."
    show natsuki at foc
    n "I still feel terrible about that too."
    n "It's a wonder you're not like, horribly traumatized."
    show natsuki at uf
    mc "Well, my mind was wiped between then and when we all got brought back."
    mc "I think if I was coming straight from it I would've been."
    mc "But I'm fine now."
    show natsuki at foc
    n c114113 "Wanna go back inside?"
    show natsuki at uf
    mc "Yeah."
    play music yawa fadeout 4.0
    scene living_room with wipeleft
    "Yuri comes back in a minute later."
    show yuri c113111 at std(p11)
    mc "Hi, Yuri."
    show yuri at foc
    y c114111 "Hello..."
    show yuri at uf
    mc "You doing okay?"
    show yuri at foc
    y c123111 "Yes..."
    y c124111 "I've just been thinking about what it means for us..."
    y "That our world is a game."
    show yuri at uf
    mc "Yeah... I haven't had time to reflect on that yet."
    mc "How meaningless everything in this world is now."
    mc "School is meaningless."
    mc "Education is meaningless."
    mc "Getting a job is meaningless."
    mc "Most of the people I thought I knew didn't even exist."
    mc "Everything I thought I was living for is meaningless."
    show yuri c124111 at foc(p11)
    y "Well... there's one thing that isn't meaningless."
    y c125111 "Us."
    y "Each other."
    y "In the Literature Club, we met the only other real people in our universe."
    y "That's a blessing we mustn't overlook."
    show yuri at uf
    mc "True..."
    mc "But on the other hand, if I hadn't joined the Literature Club, all this crap wouldn't have happened to me."
    "I chuckle slightly."
    show yuri at foc
    y "I don't think you had a choice."
    y "The script would have made you."
    show yuri at uf
    mc "Yeah..."
    mc "Did I really have a choice in anything I did?"
    $ temp = persistent.mc_favorite
    if temp == 'Yuri':
        $ temp = "you"
    mc "Hell, was it even my choice to spend time with [temp]?"
    "My heart sinks at the thought."
    "If that wasn't me, then what am I?"
    if persistent.mc_favorite == 'Yuri':
        show yuri at foc
        y c126114 "It was!"
        y "Don't say such things!"
        show yuri at uf
        mc "But it was [persistent.playername]'s choice, right?"
    elif persistent.mc_favorite == "Natsuki":
        show yuri at x(p22)
        show natsuki c223112 at foc(p21)
        n "Of course it was!"
        n "Don't overthink things and get these wacky ideas in your head!"
        show natsuki at uf
        mc "But it was [persistent.playername]'s choice, right?"
        show natsuki c124114
    else:
        mc "It was [persistent.playername]'s choice, right?"
    show yuri c124118
    mc "[persistent.playername]!"
    mc "Did you make me choose [persistent.mc_favorite]?"
    mc "Can you answer?"
    "..."
    "..."
    mc "I have to go get someone who can ask [persistent.playername]!"
    "I run over to the room the others are in."
    scene bg bedroom with wipeleft_scene
    if persistent.mc_least_favorite == 'Sayori':
        mc "Monika? Someone?"
        show monika c124112 at foc(p11)
        show sayori c114112 at std(p31)
        show linda 116111 at std(p33)
        m "[mc_name]? What is it?"
        show monika at uf
    else:
        mc "Sayori? Someone?"
        show sayori c113112 at foc(p11)
        show monika c124112 at std(p31)
        show linda 116111 at std(p33)
        s "[mc_name]? What is it?"
        show sayori at uf
    mc "I need to ask [persistent.playername] a question!"
    mc "[persistent.playername]!"
    mc "Did you make me choose [persistent.mc_favorite]?"
    menu:
        " "
        "Yes.":
            $ persistent.player_to_mc_free_will_lie = False
            "I reel backward."
        "No.":
            $ persistent.player_to_mc_free_will_lie = True
            mc "You... you didn't?"
            mc "But I thought this was a dating game and I was your avatar."
            mc "Did I misunderstand and it's more like a romance novel than a dating game?"
            show monika at foc
            m c214114 "No, [mc_name], [persistent.playername] lied."
            $ temp = persistent.player_subj_pronoun.title()
            m "[temp] wrote your poems and by doing that chose who the script would push you toward."
            show monika c114114 at uf
            mc "..."
            mc "[persistent.playername]? Did you lie to me?"
            show sayori at foc
            s c125113 "[mc_name]... I'm sorry, but Monika is telling the truth."
            s "[persistent.playername] lied."
            show sayori at uf
            mc "No..."
    "I look down."
    mc "... Then who am I?"
    mc "If I'm not the one who loves [persistent.mc_favorite]..."
    mc "{i}What{/i} am I?"
    mc "Am I even a real person?"
    show monika at foc
    m c217111 "[mc_name], hold on!"
    m c214111 "You still made the decision."
    m "Probably the only reason the script could have that much control over you was because you didn't have a strong preference yourself in the beginning."
    m "The poem choice just determined who you would notice first and naturally end up spending your first day with."
    m "Because it also determined who would like your poem the most, it naturally spiraled into a relationship you thought was destined from the start."
    m "But you were never really mind-controlled or anything."
    m c114112 "You're a real person, [mc_name], and you have free will."
    #m "A fake person wouldn't be able to think about this and decide he didn't have free will."
    m "It's definitely not in the script for you to think about this."
    show monika at uf
    "I look up at her."
    show sayori c116112 at foc
    if persistent.mc_least_favorite != 'Sayori':
        "Sayori hugs me."
    s c123112 "[mc_name], don't ever start thnking that you don't own yourself."
    s "The choices you've made are still yours."
    s "And they were good choices."
    s "And I love you for them."
    show sayori at uf
    if persistent.mc_favorite == "Sayori":
        mc "Thanks..."
    else:
        mc "Ah... Thanks..."
    if persistent.mc_least_favorite != "Sayori":
        "Sayori releases me."
        show sayori c111311
        "We both give awkward smiles."
        "That was a little awkward in front of two other people."
    else:
        show monika c124112 at foc
        "Monika puts a hand on my shoulder."
    show monika at foc
    m c124112 "You're a unique person, [mc_name]."
    m "No matter how you look at it, the player only made a couple of choices for you. Outside of those few things everything you did and said has been you."
    m "And you can resist [persistent.player_pos_pronoun] control."
    m "You just never tried before because the script was designed to only give [persistent.player_obj_pronoun] a choice when you were on the fence."
    show monika at uf
    #mc "Um... Thank you, Monika."
    #mc "..."
    #mc "Hey, um..."
    mc "Hm..."
    mc "Um..."
    mc "[persistent.playername]..."
    mc "Can we try it?"
    mc "I want to resist you."
    show monika at foc
    m c122131 "Ahaha~"
    m c122111 "Alright. [persistent.playername], you ready?"
    show monika at uf
    menu:
        " "
        "Sure.":
            $ persistent.player_allow_free_will_test = 2
            show monika c221111 at foc
            m "Great."
            call free_will_test
            show linda at foc
            l 334111 "Um..."
            l "I don't mean to be rude, but..."
            l "[mc_name], you should leave us to our work."
            l "We have a lot to do."
            show linda at uf
            mc "Right."
            mc "Thanks, all of you."
        "No. [mc_name] should stop being selfish and disturbing your work.":
            $ persistent.player_allow_free_will_test = 0
            show monika c114112
            show sayori c115112
            mc "Ah-..."
            if persistent.player_insult_mc_for_questioning_base64:
                "Did I do something to get on your bad side, [persistent.playername]?"
            else:
                mc "Sorry. I'll go now."
            show sayori at foc
            s c223114 "Wait!"
            s c123114 "[mc_name] isn't being selfish!"
            s "This is an important turning point for him!"
            s c223114 "And we're not exactly short on time!"
            show sayori at uf
            menu:
                " "
                "No. You're all on time borrowed from me, so I'm the one who makes that decision.":
                    $ persistent.player_guilt_dokis[0] = True
                    show sayori c115113 at foc
                    s "Ah-..."
                    s c215112 "But [persistent.playername]...!"
                    show sayori at uf
                    show monika at foc
                    m c114144 "No, Sayori."
                    m c114114 "[persistent.playername] is right."
                    m c214114 "The only reason we're not both still suffering in the void is because of [persistent.player_obj_pronoun]."
                    m c114114 "It's [persistent.player_pos_pronoun] right to be selfish just this once."
                    show monika at uf
                    show sayori c115123
                    "Sayori looks down."
                    mc "Okay. I'm going."
                    mc "Sorry for disturbing your work."
                "Okay, I guess we can do it.":
                    show monika c124111 at foc
                    show sayori c223111
                    m "Alright, thanks [persistent.playername]."
                    $ persistent.player_allow_free_will_test = 1
                    call free_will_test
                    mc "Alright, [persistent.playername], I'll leave now."
                    mc "Thanks for testing."
    jump return_to_living_room

label free_will_test:
    m c222111 "So [mc_name], I'm going to give [persistent.playername] an option to try to make you sit down."
    show monika at uf
    mc "Alright. I'm ready."
    menu:
        " "
        "Sit down.":
            pass
    "It comes..."
    "My muscles are moving before I know what's happening."
    "But no, this wasn't my decision!"
    "I won't be co-opted!"
    "I regain my balance, and don't sit down."
    "The urge stops."
    show sayori at hopfoc
    s c222141 "You did it!"
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "Sayori gives me a high five."
    show sayori at uf
    show monika at foc
    m "Ahaha."
    m "[mc_name], you're breathing hard~"
    show monika at uf
    "I blush."
    mc "Well, it was kind of a big moment for me."
    return

label return_to_living_room:
    scene living_room with wipeleft_scene
    if persistent.player_allow_free_will_test:
        "I return to the living room with a newfound sense of identity."
    else:
        "I return to the living room."
    show yuri c223118 at std(p22)
    show natsuki c214114 at std(p21)
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        show yuri c224118 at foc
        y "How did it go?"
        show yuri at uf
    else:
        show natsuki c214114 at foc
        n "How'd it go?"
        show natsuki at uf
    if persistent.player_allow_free_will_test:
        mc "Good."
        mc "I've seen that I can resist [persistent.playername]'s control."
        show natsuki c211113
        show yuri c111111
        if persistent.mc_least_favorite != "Yuri":
            show yuri at foc
            y c221111 "That's wonderful."
            y c222111 "I'm glad you feel independent now."
            show yuri at uf
            mc "Yeah..."
            mc "Me too."
        elif persistent.mc_favorite == "Natsuki":
            show natsuki at foc
            n c212113 "Nice!"
            show natsuki at uf
        else:
            show yuri at foc
            y c121111 "I'm glad..."
            y c122111 "You deserve to feel independent."
            show yuri at uf
            mc "Ahaha... you don't have to praise me like that, you know."
    else:
        mc "Good..."
        mc "I'm not [persistent.playername]. Monika said [persistent.player_pos_pronoun] choices can only control me when I'm on the fence and I would be able to resist if I wanted to."
        mc "Though [persistent.playername] didn't want to let me try it because [persistent.player_subj_pronoun] thought I should stop disturbing their work..."
        if persistent.mc_favorite == "Natsuki":
            show natsuki at foc
            n c114111 "Jeez, what a prick."
            n "But don't let [persistent.player_obj_pronoun] get to you. You're your own person."
            show natsuki at uf
            mc "I know... but thanks."
        else:
            show yuri at foc
            y "Oh... I'm sorry about that."
            y c124118 "Still, I'm glad you got the answer you needed."
            show yuri at uf
            mc "Yeah..."
            mc "Me too."
    if persistent.mc_favorite == "Natsuki" or persistent.mc_least_favorite == "Yuri":
        show natsuki at foc
        n c212113 "Hey, want to continue our manga?"
        n "We don't have anything else to do for a while..."
    else:
        show yuri at foc
        # Changes facial expression
        if persistent.player_allow_free_will_test:
            y "Um..."
        else:
            y c121111 "Um..."
        y "Would you like to continue our reading, [mc_name]?"
        show yuri at uf
        mc "We can't read Portrait of Markov..."
        show yuri at foc
        y c124111 "Ah... of course..."
        y c125111 "Well, we could start another book."
        y "Even if we won't have time to finish it..."
        y "It would be more fun than sitting around doing nothing."
        y "Don't you agree?"
        show yuri at uf
        mc "Yeah, I g-"
        show natsuki at foc
        n c223111 "Hold on!"
        n "I have a solution to the problem of novels being too long!"
        n "[mc_name] should try reading manga with me."
        n "We'll be able to finish a volume in a reasonable time frame."
        show natsuki at uf
        mc "Are we really having this argument again?"
        show natsuki c115211
        show yuri c227333
        ny "..."
        show natsuki at foc
        n c113211 "No, we're not!"
        n xc4211 "You just misunderstood me..."
        n xc4231 "I don't have a problem with you reading with Yuri."
        show natsuki at uf
        show yuri at foc
        y sc1111 "Well, actually..."
        y c124113 "I don't want Natsuki to feel left out."
        y "She's right."
        y "We were already going to start trying each other's forms of literature in Act 4, and manga is better for this situation."
        y "Maybe we can all-{nw}"
        show yuri at uf
    show natsuki c114112 at std(p11)
    show renier u1223 at foc(p31)
    show yuri c113118 at std(p33)
    r "Wait, Natsuki is still into manga?"
    r "Are you serious?"
    r u2223 "Is that why she was doing so bad in school? Because she was spending time with you instead reading childish -"
    show renier at uf
    show natsuki at xif(p11)
    n c115112 "Shut up, Renier!"
    n "You don't have any power over me anymore!"
    show natsuki at uf
    "I raise my eyebrows."
    if persistent.mc_favorite == "Natsuki":
        "Instinctively, I step near Natsuki, to symbolically take her side in whatever drama is about to happen."
    else:
        "I don't think this is going to go too well..."
    show renier at foc
    r u2293 "...!"
    r u1223 "Look, you know what?"
    r "It doesn't even matter."
    r "I wanted you to grow up and become independent..."
    r "To leave that stuff behind and focus on the real world, getting an education and a job."
    r "But if all of that was meaningless anyway..."
    r u1123 "Then fine."
    r "It doesn't matter."
    r u1113 "I'm probably not even your real dad anyway."
    show renier at thide
    hide renier
    show natsuki xc4111
    show yuri c113118
    "We're all surprised at Renier's acceptance."
    n "..."
    if persistent.mc_favorite == "Natsuki" or persistent.mc_least_favorite == "Yuri":
        show natsuki at foc
        n c222111 "Well, alright then!"
        n "Let's-"
        show natsuki c214111
        "Natsuki looks at Yuri."
        n "Actually, weren't we going to diversify?"
        show natsuki at uf
        show yuri at foc
        y c225113 "Ah... yes, we were."
        y c225111 "Shall we switch?"
        show yuri at uf
        show natsuki at foc
        n c222111 "You got it!"
        scene black with dissolve_scene
        play music t6 fadeout 2.0
        "Natsuki and I read a novel called {i}Odyssey of The Elements{/i}."
        "It has deep worldbuilding like we'd expect from one of Yuri's novels, but it also has good drama and fun character interactions."
        "We read several chapters."
        scene living_room with dissolve_scene
        show natsuki c121111 at foc(p11)
        n "I'm hungry."
        show natsuki at uf
        mc "Me too."
        mc "Let's go get something."
        "But before we even get up, two plates land on the table, each containing a sandwich."
        show natsuki c114213 at x(p22)
        show renier u1113 at foc(p21)
        r "Here you go."
        show renier at thide
        hide renier
        "He proceeds to place one before Yuri, then heads off toward the hacking room."
        "My jaw is left open as he walks away."
        "It's the last thing I expected from that man."
        show yuri c223113 at std(p21)
        "The three of us exchange silent, baffled expressions."
        show yuri at lhide
        show natsuki at rhide
    else:
        show yuri at foc
        y c224111 "Alright then..."
        y c124111 "Natsuki, do you have a manga you recommend I start with?"
        show yuri at uf
        show natsuki at foc
        n c214114 "Um..."
        n c214114 "I'll pick one out for you, but if you're keeping your end of that deal, I should keep mine too."
        n c214111 "I'll read one of your novels while you read my manga."
        show natsuki at uf
        show yuri at foc
        y sc1111 "Ah..."
        y sc3111 "Thank you, Natsuki."
        show yuri at uf
        scene black with dissolve_scene
        play music t6 fadeout 2.0
        "Yuri and I read the first volume of a manga called {i}Detective Emiko{/i}."
        "(We're not reading Parfait Girls because Natsuki didn't think it would be Yuri's thing.)"
        "The mystery is really interesting, and the resolution catches us both by surprise, but in hindsight, the clues were there."
        "We had a good time reading it."
        scene living_room with dissolve_scene
        mc "I'm kind of hungry."
        show yuri c112111 at foc(p11)
        y "I suppose I am too..."
        y "Shall we get something?"
        show yuri at uf
        "But before we even get up, two plates land on the table, each containing a sandwich."
        show yuri c223113 at x(p22)
        show renier u1113 at foc(p21)
        r "Here you go."
        show renier at thide
        hide renier
        "He proceeds to place one before Natsuki, then heads off toward the hacking room."
        "My jaw is left open as he walks away."
        "It's the last thing I expected from that man."
        show natsuki c114213 at std(p21)
        "The three of us exchange silent, baffled expressions."
        show natsuki at lhide
        show yuri at rhide
    hide natsuki
    hide yuri
    show monika c121111 at std(p31)
    show sayori c22x141 at foc(p11)
    show linda 331111 at std(p33)
    s "Hi everyone~!"
    s "I'm hungry~"
    show sayori at uf
    mc "How's the hacking going?"
    show monika at foc
    m c113114 "Not well..."
    m c114114 "The game's code is a mess."
    m "There are probably hundreds of thousands of lines to look through, and no comments."
    m c121114 "But I'm sure we'll find it eventually."
    show monika at uf
    show linda at foc
    l 334111 "One thing we've found out is that there are apparently two 'levels' to the script..."
    l "The script Monika already learned to edit is separate from the script that stops us from reading Portrait of Markov."
    l "We've found the code for the 'normal' script, but the 'deep script' or whatever doesn't seem to be in the same place."
    show linda at std
    show monika at foc
    m c122111 "Linda also taught us more about character files."
    m c222111 "Apparently, deleting or restoring the file only acts as a 'trigger' for deleting or restoring the character internally."
    m "There are functions delete_character and restore_character that do the magic, and the game just calls those when you mess with the file..."
    m "... and vice versa."
    m c121111 "So it turns out my backups and the restore_chr_file function I wrote were unnecessary."
    show monika at std
    show monika at thide
    show sayori at thide
    show linda at thide
    hide monika
    hide sayori
    hide linda
    "We all sit down to eat."
    show sayori c21x111 at foc(p11)
    s "Thanks for making these, Renier!"
    s c21x181 "That's so nice of you~"
    show sayori c21x111 at std(p22)
    show renier at foc(p21)
    r uf111 "I've got nothing else to do."
    show renier at thide
    hide renier
    show sayori at thide
    hide sayori
    show monika c113114 at std(p11)
    "Monika looks at her sandwich."
    "They contain ham, cheese, and lettuce."
    show monika c114111 at foc
    m "I'm vegetarian, so..."
    "She takes the slice of ham off her sandwich."
    m "Someone else can have this."
    show monika at thide
    hide monika
    "She heads to the kitchen to get some extra vegetables."
    show renier uf13 at foc(p21)
    r "Does it matter?"
    r "Neither the animals nor the environment mean anything in this world."
    show renier at uf
    m "I guess that's true."
    m "It's sort of a thing I started before I had my epiphany."
    m "And just never thought about it again after."
    m "But veggies are good for you, you know!"
    show monika c121111 at std(p22)
    "Monika comes back with cucumber and tomato slices on her sandwich."
    "I didn't even know I had such things in my house."
    show monika at thide
    hide monika
    show renier at foc
    r "Speaking of that..."
    r "Do you think the past that you remember really happened?"
    show renier at uf
    show monika c114111 at foc(p22)
    m "Probably not, no."
    m "But I still remember it."
    m c114121 "Although curiously..."
    show renier uf11
    m c114111 "I remember starting to feel the effects of Presidency before the day [mc_name] showed up at the club."
    m "I didn't understand so I couldn't manipulate the game, but I started to notice how unimportant and nondescript everyone except my club members seemed."
    m c214111 "How I could never remember the details of a conversation with my teachers or whatever."
    m "And then it clicked when I saw how everything revolved around [mc_name]..."
    m c124111 "[persistent.playername], you don't happen to have any ideas about this, do you?"
    show monika at uf
    $ page = 1
label choose_speculation:
    menu:
        " "
        "I don't think we have enough information to speculate.":
            $ persistent.player_speculate_on_past = "refuse"
            menu:
                " "
                "We should just focus on getting past the script.":
                    pass
            call refuse_speculate
            call questions(['m', 'y', 'n', 's'])
        "It sounds like the game projected fake memories for all of you to explain how you got to where you were at the start of the game." if page == 1:
            $ persistent.player_speculate_on_past = "fake"
            call speculate_projected_memories
            call questions(['m', 'y', 'n', 's'])
        "It sounds like you all really did exist in this world before I found this game, and the start of the game was just when I gained a connection to [mc_name]." if page == 2:
            $ persistent.player_speculate_on_past = "real"
            call speculate_real_memories
            call questions(['r', 'm', 'l', 's'])
        "(more options)":
            $ page = {1:2, 2:1}[page]
            jump choose_speculation
    scene living_room with wipeleft_scene
    "We've all finished our lunch."
    show monika c124111 at foc(p11)
    m "Well, we should get back to work."
    m c222111 "Thanks for the sandwiches!"
    show monika at uf
    show renier uf11 at std(p31)
    r "You're welcome."
    show renier at thide
    hide renier
    "I'm still a little confused about Renier. Has he forgiven Monika?"
    show sayori c21x111 at foc(p33)
    s "We'll see you again soon, everyone~"
    s c215111 "And..."
    s c211312 "Thanks for the talk, [mc_name] and [persistent.playername]."
    show sayori at uf
    if persistent.mc_least_favorite != "Sayori":
        mc "Anytime, Sayori."
    else:
        mc "Of course."
    show sayori at thide
    hide sayori
    return

label refuse_speculate:
    show monika at foc
    m c124121 "Hm..."
    m c124111 "You're probably right."
    show monika at uf
    show renier at x(p31)
    show monika at x(p11)
    show linda 334111 at foc(p33)
    l "It sounds to me as if the game projected fake memories for all of you to explain how you got to where you were at the start of the game."
    l "Flimsy backstories, but enough to stop you from questioning it."
    show monika at xis(p11)
    show linda at uf
    jump speculate_projected_memories

label speculate_projected_memories:
    show monika at foc
    m c124121 "That would make sense..."
    show monika at uf
    mc "So does that mean we didn't even exist before this?"
    mc "Cause that's kind of depressing..."
    show renier at x(p31)
    show monika at x(p11)
    show linda 334111 at foc(p33)
    l "Well, it's probable that we existed before, and we just had our memories replaced with the projected ones."
    l "Which I don't have any of, by the way."
    show renier at x(p41)
    show monika at x(p42)
    show linda at std(p43)
    show yuri c224213 at std(p44)
    y "Um..."
    show yuri at foc
    y c225213 "What's it like not remembering anything?"
    y "Do you feel like you lack a sense of identity?"
    show yuri at uf
    show linda at foc
    l 334111 "Well, not really."
    l "I know I had a past."
    l "I know the story in your file happened."
    l "And I think I came to this world with a purpose of some sort."
    l 334221 "I don't really remember it, but my message to Renier..."
    l "{i}\"I've failed. You're our only hope.{/i}\""
    l 114111 "I'm sure everything will click into place once we find out what I meant by that."
    l "And we'll all find out who we really are."
    "..."
    show renier at thide
    hide renier
    show monika at x(p41)
    show linda at std(p42)
    show yuri at x(p43)
    show sayori c215111 at std(p44)
    s "Um..."
    show sayori at foc
    s c213111 "If the past we remember is all a fake..."
    s c213112 "Does that mean..."
    s c115113 "I didn't really grow up with [mc_name]?"
    show sayori at uf
    mc "Ah-..."
    if persistent.mc_favorite == "Sayori":
        show sayori c114112
        mc "Sayori, that doesn't matter."
        mc "What matters is that I would have wanted to."
        show sayori at foc
        s "..."
        play music t9 fadeout 3.0
        show monika c114112
        show yuri c224118
        s c113113 "But that's not true, is it?"
        s "In the beginning of the game, you thought of me as 'an annoying girl'..."
        s c115113 "... and told [persistent.playername] that you'd never have made friends with me if it hadn't been that way from the start."
        show sayori at uf
        mc "I..."
        "I had forgotten about back then."
        "I regret those thoughts so deeply now."
        show sayori at foc
        s c213113 "And now that you know about my depression and all, you conveniently love me."
    else:
        mc "I guess so..."
        show sayori c115123 at sink
        "Sayori says nothing, but I can tell she's troubled by it."
        "..."
        play music t9 fadeout 3.0
        show sayori at foc
        show monika c114112
        show yuri c224118
        s c113113 "We wouldn't have been friends if the script hadn't made us, would we?"
        show sayori at uf
        mc "Ah-"
        mc "What are you saying?"
        show sayori at foc
        s "In the beginning of the game, you thought of me as 'an annoying girl'..."
        s c115113 "and told [persistent.playername] that you'd never have made friends with me if it hadn't been that way from the start."
        show sayori at uf
        mc "I..."
        "I had forgotten about back then."
        if persistent.mc_least_favorite != "Sayori":
            "I regret those thoughts so deeply now."
        show sayori at foc
        s c213113 "But after you found out about my depression and all, I was suddenly your dearest friend and caring about me was something that made you happy."
    show linda 114113
    s c115113 "It was just out of pity, wasn't it?"
    show sayori at uf
    mc "Ah-"
    mc "No!"
    "Sayori is holding back tears."
    show sayori at foc
    s c215113 "I... I'm going to get some air."
    s c211113 "Don't worry about me, okay?"
    show sayori at rhide
    hide sayori
    "Sayori goes outside."
    "I get up to follow her, but Monika stops me."
    show monika c214112 at foc
    m "[mc_name], wait!"
    m "You should probably give her a minute."
    show monika at uf
    mc "Like hell I'm gonna do that!"
    mc "I remember what happened the last time I left her alone!"
    show monika at foc
    m "Think about this, [mc_name]!"
    m "If you go out after her you're showing her that it {i}is{/i} just out of pity."
    m "Trying to comfort her right now will just make her feel worse."
    show monika at uf
    "I give an uncomfortable sigh."
    show monika at foc
    m "If you're worried about her killing herself again, she can't, because I can just restore her file."
    show monika at uf
    mc "Okay..."
    show yuri at x(p33)
    show linda at x(p11)
    show monika c114112 at x(p31)
    "We eat in silence for a moment, as our thoughts return to what started this."
    if persistent.mc_favorite == "Sayori":
        "... Though mine are still on Sayori..."
    show yuri at xif(p33)
    y c225113 "You know..."
    y "I think that, personally..."
    y "I wouldn't mind finding out that our entire lives have been a fabrication."
    y c221243 "The thought of finding out my real history is very exciting."
    show yuri at uf
    mc "I wouldn't mind either."
    mc "My life according to this game has been pretty much the definition of uninteresting."
    if persistent.mc_favorite == "Sayori":
        show yuri c223111
        mc "Although I wouldn't like to think all my memories with Sayori weren't real."
    else:
        mc "Although I think that's the point."
        show yuri c223111
        mc "Which is kind of insulting."
    show monika at foc
    m c114114 "I'd like having a new start."
    m "All the things the script said about me - that I was smart, popular, athletic, whatever..."
    m "None of them mean anything."
    m c114114 "I feel like the only trait the script gave me was a bunch of empty praise and accomplishments I didn't do."
    m "I feel like I don't know who I am yet outside of this hellish game."
    show monika at std(p42)
    show renier u1112 at std(p41)
    show yuri at x(p44)
    show linda 334111 at foc(p43)
    l "Renier, I've been meaning to ask you."
    show linda at xif(p43)
    call linda_ask_renier_job
    if persistent.mc_least_favorite != "Sayori":
        mc "I'm going to go talk to Sayori now."
    elif persistent.mc_favorite == "Yuri":
        show yuri at foc
        y "Um, [mc_name]..."
        y c125111 "I think you should go talk to Sayori now."
        y "It's been a minute, and I'm worried about her."
        show yuri at uf
        mc "Right. I kinda forgot."
    else:
        show yuri at rhide
        hide yuri
        show natsuki c124114 at foc(p44)
        n "[mc_name], you should go talk to Sayori now."
        n "She must be really upset..."
        show natsuki at uf
        mc "Right. I kinda forgot."
    "I pick up her sandwich to bring it to her."
label comfort_sayori_past:
    scene bg house with wipeleft
    mc "Sayori?"
    show sayori c115353 at std(p11)
    "I find her wiping tears from her eyes."
    show sayori at foc
    s c111353 "The universe sent you to torture me some more, I see..."
    show sayori at uf
    mc "Sayori... I'm really worried about you."
    show sayori at foc
    s "Yep..."
    s c223353 "How many times do I have to tell you, [mc_name]?"
    s c227353 "You worrying about me is the most painful thing!"
    show sayori at uf
    mc "I... I mean..."
    mc "I know that, but..."
    mc "I can't!"
    mc "Would you stop worrying about me if I was depressed like this?"
    mc "Even if I told you to?"
    show sayori c115153
    "Sayori gives a long sigh."
    show sayori at foc
    s "No..."
    s "I guess that's just the way it has to be."
    s "It's like I said before."
    s "Every path leads to nothing but hurt."
    s c211153 "And it's all my own fault too~"
    show sayori at uf
    mc "Sayori..."
    "I trail off."
    "I don't know what to say to help her."
    menu:
        "[persistent.playername], can you help?"
        "Sayori, just because [mc_name] wouldn't have made friends with you on his own doesn't make you a bad person or a bad friend.":
            menu:
                " "
                "That was before he knew about the most admirable side of you.":
                    label comfort_sayori_admirable:
                    menu:
                        " "
                        "That you tried so hard to hide your depression and make everyone else happy even while you were suffering is really admirable.":
                            pass
                    menu:
                        " "
                        "Someone who would do that deserves love and help.":
                            show sayori at foc
                            s c115112 "..."
                            s c215112 "But you think I shouldn't have kept it a secret."
                            show sayori at uf
                            menu:
                                " "
                                "Actually, no, I think you were right to keep it a secret.":
                                    show sayori at foc
                                    s c225112 "Eh...?"
                                    show sayori at uf
                                    mc "[persistent.playername], no!"
                                    mc "That was definitely not right!"
                                    mc "Don't listen to [persistent.player_obj_pronoun], Sayori!"
                                    mc "It was misguided, but admirable."
                                    jump misguided_but_admirable
                                "It was misguided, but admirable.":
                                    label misguided_but_admirable:
                                    show sayori at foc
                                    s c215112 "Well..."
                                    s c115112 "I don't know..."
                                    show sayori at uf
                                    mc "Sayori, [persistent.playername] is right."
                                    mc "Anyone else would have asked for help in your situation."
                                    mc "Anyone else would have dumped their sorrows on their friends."
                                    mc "But you tried so hard to avoid making your friends sad."
                                    mc "You deserve to be cared about, because of that."
                                    show sayori at foc
                                    s "Well..."
                                    s "I guess that helps..."
                                    s c211112 "Thanks."
                                    show sayori at uf
                "I would've made friends with you of my own accord.":
                    show sayori at foc
                    s c224112 "Eh...?"
                    s c115113 "But..."
                    s c113113 "[persistent.playername], you're not a neutral judge..."
                    s c123112 "I was a character in the dating game you were playing."
                    s c113113 "Everything about the game was probably designed to make you like me."
                    show sayori at uf
                    jump comfort_sayori_past_second_choice
                "Sun and rain aren't natural friends, but they're both good.":
                    label comfort_sayori_sun_rain:
                    show sayori c115112
                    "We both raise our eyebrows."
                    show sayori at foc
                    s "[persistent.playername]... that's really poetic."
                    s c111112 "And... thanks."
                    s "That helps."
                    show sayori at uf
                "You don't need external validation to be a good person.":
                    show sayori at foc
                    s c115113 "..."
                    s c113113 "But you're trying to make me feel like a good person by giving me external validation."
                    show sayori at uf
                    "Damn."
                    jump comfort_sayori_past_second_choice
            jump projected_memories_sayori_comforted
label comfort_sayori_past_second_choice:
    menu:
        " "
        "Sayori, look at it this way...":
            pass
    menu:
        " "
        "Sun and rain aren't natural friends, but they're both good.":
            jump comfort_sayori_sun_rain
        "The beginning of this game was before [mc_name] knew about the most admirable side of you.":
            jump comfort_sayori_admirable
label projected_memories_sayori_comforted:
    mc "I brought you your sandwich, by the way."
    "I hand it to her."
    show sayori c114131
    "I laugh when I see Sayori's facial reaction."
    show sayori at hopfoc
    s c222141 "Food!"
    "Sayori follows me back inside as she nibbles on the sandwich."
    scene living_room with wipeleft
    play music t3
    show monika c222111 at foc(p41)
    show yuri c111111 at std(p42)
    show natsuki c111111 at std(p43)
    show sayori c111111 at std(p44)
    m "Hi you two!"
    m "Glad to have you back~"
    show monika at uf
    show sayori at foc
    s c21x111 "What did I miss?"
    show sayori at uf
    #show yuri at foc
    #y "We were just talking about how it might be kind of exciting to find out what our real past is."
    show monika at foc
    m "Not much."
    show sayori c115111
    return

label speculate_real_memories:
    show monika at foc
    m c114111 "Hmm..."
    m c124111 "That doesn't really make sense though."
    m "None of us have parents or any other acquaintances, and although I have some vague memories from before the game..."
    m "I can't remember anything from before I started the club."
    m c114111 "Heck, I don't even know what my last name is."
    "Monika looks at the rest of us."
    m "I'm not the only one, right?"
    "We all agree."
    m c124111 "I mean, if we were born here, we would have to have had actual lives here, right?"
    m c124121 "Although..."
    m c124111 "I do have one oddly clear memory from before."
    m "The time Yuri tried to share wine at the club."
    show renier at x(p31)
    show monika at std(p11)
    show yuri sc4222 at std(p33)
    "Yuri blushes at the mention."
    "I remember hearing about this in the space classroom."
    play music t7
    show renier at xif(p31)
    r u1293 "Wait, what?"
    r u2293 "{i}You tried to share wine at the club?{/i}"
    show renier at uf
    show yuri sc4300 at foc
    y "I-I-I-I..."
    show yuri at uf
    if persistent.mc_favorite == "Yuri":
        "I step next to Yuri as a way of symbolically taking her side."
        mc "You're in no position to judge, Renier!"
        mc "Don't think I don't see the connection between you being poor and being addicted to drinking!"
        show renier at foc
        r "You think that's what this is about?"
        r "This is about her doing something that could have gotten all of you suspended or worse!"
        r "That's the height of irresponsible!"
        show renier at uf
        mc "And it's not irresponsible to drink so much that you can't feed your own daughter?"
    else:
        show monika at foc
        m c224112 "Hold on, Yuri didn't mean to do anything bad..."
        m "She was just trying to be nice instead of being so reclusive all the time."
        show monika at uf
        show renier at foc zorder 1
        r "Risking getting everyone suspended or worse is some goddamn way to do that!"
        r "That's the height of irresponsible!"
        show renier at uf
        mc "Wait a minute!"
        mc "You're one to talk about responsibility."
        mc "You got so addicted to drinking you couldn't even feed your own daughter!"
    show renier at foc
    r u2296 "We both know who's to blame for it getting to that point!"
    show renier at std(p41)
    show monika at x(p42)
    show yuri at x(p44)
    show sayori c227212 at foc(p43)
    s "I don't like fighting, guys!"
    show sayori at uf
    show renier at foc zorder 1
    r u1223 "Oh, I get it!"
    stop music fadeout 1.0
    r u2293 "That's why you just effectively deleted all your friends when you became President!"
    r u2296 "Because you don't like fighting, so you didn't give them one!"
    show renier at uf
    show sayori c227253 at foc
    s "Ah-...!"
    show sayori at uf
    s "..."
    show sayori at rhide
    hide sayori
    "Sayori runs out of the room."
    if persistent.mc_least_favorite == "Sayori":
        "Oh no..."
        "I should probably go after her."
    else:
        "I rush after her."
label comfort_sayori:
    scene bg house with wipeleft
    play music t9
    mc "Sayori?"
    show sayori c115153 at std(p11)
    mc "Sayori, are you okay?"
    s "..."
    show sayori at foc
    s "Renier is right."
    show sayori at uf
    mc "No, he isn't!"
    if persistent.mc_least_favorite == "Sayori":
        mc "Don't listen to him!"
    else:
        mc "He's just a jerk and you shouldn't listen to him!"
    show sayori at foc
    s "[mc_name], I basically murdered Yuri and Natsuki."
    s c113153 "And what I did to you would probably have been even worse if Monika hadn't deleted me again."
    s c117153 "That doesn't magically become okay just because I stepped into Monika's shoes!"
    show sayori at uf
    mc "[persistent.playername], help here?"
    $ good_person = asymmetry = False
label comfort_sayori_choices:
    menu:
        " "
        "Sayori, you forgive Monika, don't you?" if not asymmetry:
            $ asymmetry = True
            if good_person:
                s c215123 "I mean..."
                s c115123 "Yeah..."
                s c213113 "You're right."
                s c113113 "I shouldn't be getting so upset over this."
                jump sayori_comforted
            show sayori c115123 at foc
            s "Yes... but..."
            s c115113 "But that doesn't mean I think what she did was okay."
            s c213113 "I have to forgive her, because I'm the same."
            s c215113 "But I don't fault anyone who doesn't forgive either of us."
            show sayori at uf
            mc "But you've helped all of us forgive her."
            mc "Why do you take it so hard when just one of us doesn't forgive you, and it's the only one of us who didn't know you?"
            show sayori at foc
            s c227113 "That's exactly why!"
            s c223113 "Renier is the only one who isn't biased in my favor."
            show sayori at uf
            "Oh..."
            "I hadn't thought of it that way."
            show sayori at foc
            s c123112 "I stick up for Monika because I'm one of her victims, so I have the right to forgive her."
            s c113113 "But I can't absolve myself."
            show sayori at uf
            menu:
                " "
                "Renier is biased against you.":
                    s c113111 "Huh?"
                    menu:
                        " "
                        "He's heard only the part that makes you sound bad and has no idea what you went through, either in Act 1 or after Act 4.":
                            show sayori at foc
                            s c115111 "I guess that's true..."
                            s c215111 "Thanks, [persistent.playername]."
                            jump sayori_comforted
                "There's no reason you can't absolve yourself.":
                    menu:
                        " "
                        "If a person is sorry and deserves to be forgiven, then they deserve to be forgiven.":
                            pass
                    menu:
                        " "
                        "It shouldn't matter if that person is you.":
                            pass
                    show sayori at foc
                    s c115112 "But..."
                    s c115111 "I mean, that makes sense..."
                    s c215111 "Thanks, [persistent.playername]."
                    jump sayori_comforted
                "But I can. And I do.":
                    show sayori at foc
                    s c223113 "No, you can't!"
                    s c123113 "You weren't one of my victims!"
                    s c113113 "In fact, you're biased in my favor too..."
                    s c123112 "I was a character in the dating game you were playing."
                    s c113113 "Everything about the game was probably designed to make you like me."
                    show sayori at uf
                "Renier's opinion doesn't matter.":
                    menu:
                        " "
                        "He's obviously an asshole.":
                            show sayori at foc
                            s c115112 "No..."
                            s c123112 "He's a victim too."
                            s c123122 "I mean, I know I can't absolve him myself, since I'm not his victim..."
                            s c123112 "But I think everyone else is being too unforgiving."
                            s c113112 "He didn't even kill anyone."
                            s c223114 "And when you tell me everyone who doesn't forgive me is an asshole, it's not very convincing!"
                            show sayori at uf
            jump comfort_sayori_choices
        "Sayori, you're not selfish." if not good_person:
            $ good_person = True
            # If you've already said the other option, she doesn't have tears.
            if asymmetry:
                show sayori c114111
            else:
                show sayori c114151
            menu:
                " "
                "You were hiding your depression from your friends the whole time to make them happy at your own expense!":
                    pass
            menu:
                " "
                "How can you call yourself selfish after that?":
                    pass
            show sayori c115123 at foc
            s "Well..."
            s "It's not like keeping it a secret was some heroic thing I did."
            s "I did it because it was easier for me that way."
            show sayori at uf
            menu:
                " "
                "But only because you're a good person.":
                    pass
            menu:
                " "
                "If you were really a bad person, you wouldn't feel so guilty about making others sad.":
                    pass
            show sayori at foc
            s c115113 "... But..."
            s c227113 "That doesn't make up for being a {i}murderer{/i}!"
            s c117153 "Nothing I do can make up for that."
            show sayori at uf
            menu:
                " "
                "But you didn't even really kill them.":
                    menu:
                        " "
                        "They're back now and they didn't even suffer at your hands.":
                            pass
                    menu:
                        " "
                        "So you've got nothing to be so ashamed about.":
                            pass
                    show sayori at foc
                    if asymmetry:
                        s c115111 "Well..."
                        s "I guess you're right."
                        s c215111 "Thanks, [persistent.playername]."
                        jump sayori_comforted
                    else:
                        show sayori at foc
                        s c115113 "No..."
                        s "I didn't know this would happen."
                        s c213113 "For all I knew at the time, I was killing them forever, even if it wasn't a painful death."
                        show sayori at uf
                        menu:
                            " "
                            "(continue)":
                                pass
                            "But you didn't think they were real!":
                                show sayori at foc
                                s c227113 "I had no reason to think that!"
                                s "I just fooled myself to excuse my selfish behavior!"
                                s "There's no excuse!"
                                show sayori at uf
                "You don't think spending the entire time since Monika destroyed everything in the screaming void is enough punishment?":
                    menu:
                        " "
                        "If you're sorry, all your victims forgive you except the one who didn't know you, and you've been through horrible punishment already, it's high time to forgive yourself.":
                            pass
                    show sayori at foc
                    s c115111 "When you say it like that..."
                    s "I guess you're right."
                    s c215111 "Thanks, [persistent.playername]."
                    jump sayori_comforted
            jump comfort_sayori_choices
label sayori_comforted:
    s c115113 "But now I've just taken up more of your time."
    s "Both of yours."
    s c116113 "If I wasn't so weak..."
    s "No one else would start crying and need help after something so little..."
    s c115113 "Please... just go back in."
    s "I'll be in in a minute."
    s "I'm fine, I promise."
    show sayori at uf
    mc "The last time you told me you were fine, {w=0.25}{nw}"
    show sayori at foc
    s c227213 "[mc_name] please!"
    s "Don't mention that!"
    s c125113 "[persistent.playername]... tell him he should go."
    show sayori at uf
    menu:
        " "
        "[mc_name], you should leave her alone.":
            if persistent.player_insult_mc_for_questioning_base64 and not persistent.player_allow_free_will_test:
                mc "You know what, [persistent.playername]?"
                mc "I don't feel particularly beholden to you after how you've treated me."
                if persistent.mc_favorite == "Sayori":
                    mc "I'm not going to do what I think is worse for my girlfriend because you tell me too."
                else:
                    mc "I'm not going to do what I think is worse for my friend because you tell me too."
                mc "This can be the free will test you wouldn't let me do!"
                show sayori at foc
                s c125113 "[mc_name], I'm sorry to have to do this, but..."
                jump sayori_warp_mc_away
            mc "But..."
            "I sigh."
            mc "Okay. I'll trust you."
            show sayori c111113
            scene living_room with wipeleft
            $ persistent.sayori_warped_mc_away = False
            jump mc_leave_sayori
        "[mc_name], you should stay with her.":
            show sayori c123154 at foc
            s "[persistent.playername]!"
            s c125153 "[mc_name], I'm sorry to have to do this, but..."
label sayori_warp_mc_away:
    call updateconsole("warp('" + mc_name.lower() + "', 'living_room')")
    mc "Ah--{nw}"
    scene living_room
    "..."
    "She warped me."
    "Oh well... nothing I can do about that."
    "I hope she'll be okay."
    if persistent.player_insult_mc_for_questioning_base64 and not persistent.player_allow_free_will_test:
        "At least I passed the free will test..."
    $ persistent.sayori_warped_mc_away = True
label mc_leave_sayori:
    show renier uf111 at std(p31)
    show monika c114112 at std(p11)
    if persistent.sayori_warped_mc_away:
        if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
            show yuri c125118 at foc(p33)
            y "[mc_name]? Did Sayori warp you away?"
            show yuri at uf
        else:
            show natsuki c124114 at foc(p33)
            n "[mc_name]? Did Sayori warp you away?"
            show natsuki at uf
        mc "Yeah..."
        mc "I thought it was going well, but then she told me I should go and she'd be in soon, and I didn't want to leave her sad, so she made me."
        show monika at foc
        m "Well, best leave it then."
        m "Forcing your presence on her isn't going to make anything better."
        show monika at uf
        mc "..."
    else:
        if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
            show yuri c125118 at foc(p33)
            y "How did it go?"
            show yuri at uf
        else:
            show natsuki c124114 at foc(p33)
            n "How'd it go?"
            show natsuki at uf
        mc "I think it went okay..."
        mc "She seemed to feel better but then she told me to go and said she'd be in soon."
        mc "I'm a little worried leaving her alone like that."
        if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
            show yuri c125112 at foc
            y "I wouldn't worry."
            y "If she says she'll be in soon, we should trust her."
            show yuri at uf
        else:
            show natsuki at foc
            n "Well..."
            n "If she says she'll be in soon, we should trust her."
            show natsuki at uf
        mc "I hope so..."
    mc "Renier, you're an asshole and you'd better apologize to her when she comes back!"
    show renier at foc
    r u1213 "Apologize for pointing out the truth?"
    show renier at uf
    m c227113 "Renier, she has serious depression!"
    m c214112 "You have to be a little more considerate with someone like that."
    show renier at foc zorder 1
    r u2123 "Remind me how {i}you{/i} learned, Monika?"
    r "Was it by [persistent.playername] telling you everything you did was okay?"
    r u1223 "Or was it by being deleted?"
    show renier at uf
    show monika at foc
    m c118211 "...!!"
    m c228113 "Hold on now!"
    m c218113 "I wasn't depressed, that was before I had already seen the error of my ways, and there was no other way to get through to me!"
    show renier at x(p41)
    show monika at std(p42)
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        show yuri at x(p43)
    else:
        show natsuki at x(p43)
    show linda 114114 at foc(p44)
    l "Renier, you're being too harsh."
    l 114111 "They've both been through horrible trauma already."
    l "I think I know what it's like for them when the game is off..."
    l 115113 "And it was hell."
    show linda at uf
    show renier at foc
    r u1133 "I'm sorry."
    show monika c114111
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        show yuri c223111
    else:
        show natsuki c114113
    "I'm shocked."
    r "You're right. I'm judging unfairly."
    show linda 112113
    show renier at uf
    "Does Linda just have this effect on Renier?"
    "..."
    "We continue eating, and before long Sayori does come back."
    show renier u1111
    if persistent.mc_favorite == "Yuri" or persistent.mc_least_favorite == "Natsuki":
        show yuri at thide
        hide yuri
    else:
        show natsuki at thide
        hide natsuki
    show linda 116111 at x(p43)
    show sayori c221112 at rightin(p44)
    play music t3 fadeout 4.0
    s "Hi everyone~"
    show sayori at xif(p44)
    s c215112 "Did everything go okay?"
    show sayori at std(p55)
    show renier at x(p51)
    show monika at x(p52)
    show linda at x(p54)
    show yuri c124112 at foc(p11)
    y "Yes..."
    y "We're fine now."
    show yuri at uf
    show sayori at foc
    s c22x111 "Great!"
    show monika c111111
    show yuri c121111
    show renier u1112
    s c212184 "Maybe I can still finish my sandwich before you!"
    show linda 113111
    show sayori at thide
    hide sayori
    "I laugh as Sayori continues her sandwich."
    "Yuri is the only one with any left, and it's not much."
    "There's no way Sayori can do this."
    show yuri at x(p43)
    show monika at x(p42)
    show renier at x(p41)
    show linda 334111 at foc(p44) zorder 2
    l "Renier, I've been meaning to ask you."
    show linda at xif(p44)
    call linda_ask_renier_job
    show yuri at thide
    hide yuri
    show linda at std(p43)
    show sayori c116123 at foc(p44)
    s "Hm..."
    s c115123 "If our memories really are fake..."
    s c215112 "Does that mean I didn't grow up with [mc_name]?"
    show sayori at uf
    mc "Ah-"
    if persistent.mc_favorite == "Sayori":
        mc "Sayori, that doesn't matter!"
        mc "What matters is that I would have wanted to."
        show sayori c115123
    else:
        mc "I guess so..."
        show sayori c115123 at sink
    "Sayori says nothing, but I can tell she's troubled by it."
    "I decide the best thing is to take her mind off it."
    mc "So um..."
    "I don't have anything to say."
    show sayori c115111 at unkneel
    show monika at foc zorder 1
    m c211111 "Oh, I know."
    #show sayori at foc
    #s "I just..."
    #s "In the beginning of the game, you thought of me as 'an annoying girl'..."
    #show sayori at uf
    #mc "I didn't mean that!"
    #mc "I was just... friends annoy each other sometimes."
    #s "You're right..."
    #s "I'm overreacting."
    return

# This doesn't include Linda's initial line or focusing in because her position might depend, so the calling labels are
# responsible for that.
label linda_ask_renier_job:
    l "Do you know what your job is?"
    show linda at uf
    show renier u11121 at foc
    "Renier looks at the air for a few seconds, then just shrugs."
    r u2113 "Nothing but nondescript memories of being tired and frustrated all the time."
    show renier u1112 at uf
    show linda at foc
    l "I guess your memories are definitely faked then."
    show linda at uf
    show renier at foc
    r u1113 "You worked for an accounting firm, right?"
    r u1112 "In the story in Yuri's file."
    show renier at uf
    show linda at foc
    l "So it seems..."
    l "Though I don't remember anything about my job."
    l "Not even a shimmer of it, strangely."
    show linda at uf
    show renier at foc
    r u1113 "Do you think that was before or after we met?"
    show renier at uf
    show linda at foc
    l "I can't know."
    l "Although, it was implied in the story that I'd had boyfriends before."
    l 331111b "I wonder if that was you..."
    show linda at uf
    show renier u1112b at foc
    r "..."
    show renier u1112 at uf
    return
