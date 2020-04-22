label chapter19:
    "..."
    mc "This is too good to be true..."
    mc "No way we just took out the cult like that."
    "..."
    "Linda drives until we arrive in a town."
    y "Where are we going?"
    y "We have no shelter, no connections, and no money..."
    y "And Libitina needs medical attention."
    l "We'll take her to the hospital I used to work at."
    l "The owner was kind..."
    l "With luck, he'll let this one slide without pay."
    "Linda takes us there."
    "Libitina's still unconscious."
    play music yawa
    scene lobby with wipeleft
    "We follow Linda to the counter, where the clerk recognizes her."
    $ o_name = "Clerk"
    o "Linda...?"
    show linda 334111 at foc(p21)
    l "Yeah, it's been a long time."
    show linda at std
    o "You disappeared two years ago..."
    show linda at foc
    l "It's a long story."
    l "Can I talk to Albert?"
    l "We have an urgent case and no money."
    show linda at std
    o "I..."
    show linda at foc
    l "Look, I know this is a shock, but please, get me Albert."
    l "I'll catch up with you later."
    show linda at std
    o "Okay..."
    "The clerk heads back, and a few seconds later, Albert comes out."
    $ restore_character('albert')
    show albert 11141 at foc(p22)
    al "Linda...?"
    al "It really is you..."
    show albert at std
    show linda 334113 at foc
    l "Albert, look, I don't have any money, but we have someone in critical condition."
    l "She's been vomiting blood and screaming..."
    l "Please tell me you'll help her."
    l "I'll find a way to-"
    show linda at std
    al 22111 "Of course."
    al "Follow me."
    scene hospital_hall with wipeleft
    pause 0.4
    scene hospital_room with wipeleft
    "Albert leads us to a room where he directs Renier to set Libitina on a bed."
    "He asks Linda a few questions about what Libitina's been through."
    show linda 114112 at foc(p33)
    "To my surprise, Linda doesn't hold the beans."
    "She tells Albert that Libitina was tortured at a secret cult facility, and activated supernatural powers and saved us all."
    show linda at std
    show albert 11111 at foc(p32)
    al "..."
    al "I find this believable."
    show albert at std
    show linda 116111
    mc "What?!?"
    show albert at foc
    al "It's not the first I've seen of such things."
    al "I have one other mysterious patient."
    al "A girl with a knife and a white ribbon who appeared spontaneously..."
    al "... with a horrible stab wound..."
    al "Witnesses said she seemed to disappear, then reappear without her wound, and passed out."
    al "A kind samaritan brought her to me."
    show albert at std
    show sayori u213211 at foc(p31)
    s "Can we see her?!?"
    s "She's our friend!"
    show sayori at std
    show albert at foc
    al "Of course."
    al "Room 12."
    show albert at std
    "While Albert tends to Libitina, the rest of us go to visit Monika."
    scene hospital_hall with wipeleft
    pause 0.4
    scene hospital_room with wipeleft
    "Monika's on the bed, unconscious."
    show sayori u115111 at foc(p22)
    s "Oh thank goodness, she's alive..."
    show sayori at std
    show linda 111111 at foc(p21)
    l "I told you it would be okay..."
    show linda 114111 at std
    show sayori at foc
    s u123114 "That doesn't make it okay for you to lie to us like that, though!"
    show sayori at std
    "The huge wound Yuri gave her is gone."
    "Even her uniform no longer has the bloodstains."
    show sayori u114111 at foc
    s "She deleted and restored herself..."
    show sayori at std
    show linda 334111 at foc
    l "I guess she came out in the spot you and Daniel and her were ambushed in."
    show linda at std(p31)
    show sayori at std(p33)
    show yuri u125111 at foc(p32)
    y "Wait a minute..."
    y "If she {i}could{/i} delete and restore herself..."
    y u126131 "That means she kept her admin powers!"
    y u125111 "We're in luck."
    y "When she wakes up, she can probably help us figure out what we need to do now."
    show linda at std(p41)
    show sayori at std(p44)
    show yuri at std(p43)
    show natsuki xu4111 at foc(p42)
    n "Well..."
    n "I guess Monika can't talk yet."
    n "We might as well go back."
    show natsuki at std
    scene hospital_hall with wipeleft
    pause 0.4
    scene hospital_room with wipeleft
    show albert 11111 at foc(p22)
    al "How did it go?"
    show albert at std
    mc "Glad to see her alive..."
    mc "Thanks, Albert."
    mc "How long do you think it'll be before she wakes up?"
    show albert at foc
    al 12111 "No idea."
    al "If, like you say, she was affected by supernatural forces, I may not be able to do much for her."
    al "I'll do what I can, though."
    al "For the time being I'm waiting for a scan to finish."
    al "It'll take a while, so in the meantime..."
    al 12311 "Linda, I'm ready to hear more about what's happened."
    show albert at std
    show linda 114111 at foc(p21)
    l "Of course..."
    show linda at std
    scene black with dissolve_scene
    scene hospital_room with dissolve_scene
    "We tell him everything that's happened."
    show albert 11111 at foc(p22)
    al "..."
    al "That's quite a story..."
    al 11211 "I can see how you decided to make it into a novel!"
    show albert at std
    show linda 334113 at foc(p21)
    l "I understand if you don't believe us..."
    l "I don't think I would've believed myself."
    show linda at std
    show albert at foc
    al 12111 "I won't lie, I find it very convenient how you can't provide any proof."
    al "But, I suppose I'll see soon enough."
    al "If it's true, then when Monika wakes up, she can put me through to this [persistent.playername]."
    al 12311 "In the meantime, you're welcome to stay here."
    show albert at std
    show linda 114111 at foc
    l 114111 "Thank you, Albert."
    show linda at std
    show albert at foc
    al "I can also bring food."
    al "I imagine you're all hungry."
    show albert at std
    show linda at foc
    l 114111b "..."
    show albert at std(p33)
    show linda at std(p32)
    show sayori u222141 at hopfoc(p31)
    s "Yes!"
    s u21x111 "Thank you so much!"
    show sayori at std(p42)
    show linda 111111b at std(p43)
    show yuri u222211 at foc(p41)
    y "That's very generous of you, Albert."
    y "Thank you."
    show yuri at std
    "We end up spending the night at Albert's hospital." # does this imply a day passes and it's next evening?
    "We really owe this guy."
label romance:
    scene black with dissolve_scene
    stop music fadeout 3.0
    "We have a lot of downtime that evening."
    "I get [persistent.mc_favorite] to come up to the roof with me."
    scene roof with dissolve_scene
    play music romance
    "..."
    mc "Perfect timing..."
    mc "We get to watch the sunset."
    call expression 'romance_'+persistent.mc_favorite.lower()
    scene black with dissolve_scene
    return

label romance_sayori:
    show sayori u111141 at std(p11)
    "..."
    "I feel happier than I have in a long time."
    "It's the first time since before all this Portrait of Markov stuff that I've felt like I don't have any burdens."
    show sayori u111111
    mc "Sayori, are you as happy as I am right now?"
    mc "Maybe this is a dumb question but..."
    mc "... how's your depression?"
    show sayori at foc
    s u123111 "[mc_name]..."
    s u121111 "You can stop worrying about that now."
    s u121112 "Things really have changed. A lot."
    show sayori at std
    "That's good to hear."
    "I was expecting her to say something about how worrying about her makes it worse, or how I should never have worried in the first place."
    show sayori at foc
    s u123111 "We've been through so much since then."
    s "Before the Club and all..."
    s "I used to not see any value in myself."
    s u123113 "My depression was probably a result of how the experiments ruined us."
    s "Made us slaves to our Third Eyes."
    s "And even when I didn't remember that, it still affected how I felt."
    s u123111 "But this quest has shown me what my life is worth."
    s "How much there is to do with it."
    show sayori at std
    mc "I guess it would be hard to feel worthless when you helped take down that horrific cult facility."
    show sayori at foc
    s u123113 "It's not like we saved everyone there."
    s "We don't even know what happened to the other side."
    s "For all we know, maybe we killed all the other test subjects."
    show sayori at std
    mc "Oh..."
    mc "Yeah... you're right."
    mc "It wasn't a pure an outcome as we could've hoped for."
    mc "But at least we stopped him from doing anything more."
    mc "And I mean, at worst, it would be a mercy kill."
    show sayori at foc
    s u115111 "Yeah..."
    s "It helps a lot to know we did that."
    s u123111 "[mc_name], what do you think's going to happen?"
    show sayori at std
    mc "Well, we'll see when Monika and Libitina wake up."
    mc "They'll know what we need to do next, if anything."
    mc "But don't stress over the future."
    mc "We've earned this rest..."
    mc "... like, a hundred times over."
    show sayori at foc
    s "I'm not stressing."
    s "I really can't wait to see what comes next."
    s "It's scary..."
    s "... but it'll be exciting!"
    s u12x141 "And just like blowing up that horrible place, we'll look back on it and laugh!"
    show sayori at std
    mc "I hope so..."
    show sayori at foc
    s u125311 "Hey [mc_name]..."
    s "Maybe this is a dumb question but..."
    s "Do you want to kiss now?"
    show sayori at std
    "I forgot!"
    "It's been so long since I first wanted to."
    mc "Yeah..."
    return

label romance_natsuki:
    show natsuki u111143 at std(p11)
    "..."
    mc "Man."
    mc "Sure is nice to have a rest."
    mc "I could laugh now, just about how crazy it is that we all made it out of that alive."
    show natsuki at foc
    n u124113 "So..."
    n u224113 "We're literally heroes now."
    n "We stopped that crazy cult facility."
    show natsuki at std
    mc "Ehehe... yeah."
    mc "Even though... we didn't exactly save all the prisoners..."
    show natsuki at foc
    n u124111 "Well yeah, but we must've still done them a favor."
    n "I mean..."
    n u124114 "Being a prisoner there was {i}way{/i} worse than dying."
    show natsuki at std
    mc "Oh yeah, I agree..."
    "I shiver just giving it a moment's thought."
    show natsuki at foc
    n u114114 "Sorry..."
    show natsuki at std
    "Natsuki had it way better than me."
    "She was only there for a few days before she was killed."
    "So that's probably why it doesn't bother her like it does me."
    mc "Like I said before though..."
    mc "Being lucky enough to meet you made it all worth it."
    show natsuki at foc
    n u124111 "Are you sure about that? Cause that's kind of insane."
    n "The Literature Club horror fest was worth it, but the cult shit, no way."
    show natsuki at std
    mc "Well, on second thought, you're right."
    mc "But it makes it a lot better."
    mc "Y'know, it's too bad we'll probably never get to continue Parfait Girls."
    mc "Or Odyssey of the Elements."
    show natsuki at foc
    n "Yeah..."
    n u124113 "I remember some of the series I was into way back when."
    n u121113 "I hope I get a chance to introduce you to them later."
    show natsuki at std
    mc "You were into manga before DDLC?"
    show natsuki at foc
    n u222111 "Well of course!"
    n "It's literature, you know."
    show natsuki at std
    mc "Hahahaha..."
    mc "I'd totally forgotten about that argument."
    mc "Looking back on it, I wish I'd stuck up for you then."
    mc "Monika was actually being kinda mean."
    show natsuki at foc
    n u124111 "Well, I was being pretty mean to you."
    show natsuki at std
    mc "Eh?"
    "I guess she was, come to think of it."
    mc "True..."
    "Natsuki's attitude toward me has changed so much."
    "She really is a nice person."
    "We watch the sunset in silence for a moment."
    show natsuki at foc
    n u124111 "My only gripe right now is being in my school uniform."
    show natsuki at std
    mc "You'd rather be in your cute outfit?"
    show natsuki at foc
    n xu4111 "Oh, you dumb oaf..."
    show natsuki at std
    "A much milder response than I anticipated."
    "Maybe getting mad at me got old?"
    "Actually... now that I think about what I just said..."
    "I said it {i}because{/i} I thought it'd make her mad."
    mc "I'm sorry, Natsuki."
    mc "I shouldn't push your buttons like that."
    show natsuki at foc
    n u114213 "..."
    n "... Yeah... it was kinda mean, now that you mention it."
    n "I appreciate that."
    n u114111 "Actually, wait a minute..."
    n u113111 "... didn't you just imply that I'm {i}not{/i} cute in my school uniform?"
    show natsuki at std
    mc "What?!?"
    mc "Natsuki... you never would've said that just a week ago."
    mc "Did things change a lot?"
    show natsuki at foc
    n xu4111 "What a stupid question."
    n "I should make a meme of you:"
    n "Finds out the world is a video game, sees everyone die and come back to life a dozen times each, remembers past life, blows up evil cult facility..."
    n "... asks 'Did things change a lot'."
    show natsuki at std
    mc "Ahaha..."
    show natsuki at foc
    n u114113 "But really..."
    n "Most of the reason I didn't like being seen as cute before was because it always felt dismissive."
    n "Like being cute meant I couldn't be taken seriously, or write about serious things, or whatnot."
    n "But that's all changed."
    n "I don't feel like anyone treats me that way anymore."
    n "And even if they did, I wouldn't be so vulnerable to it anymore."
    show natsuki at std
    mc "Huh..."
    mc "So you're okay with it now?"
    show natsuki at foc
    n "Yeah."
    n "And [mc_name]..."
    n "Want to kiss now?"
    n "Since that big prick Renier stopped us last time."
    show natsuki at std
    mc "Yeah..."
    mc "It's been put off for long enough now."
    return

label romance_yuri:
    show yuri u111161 at std(p11)
    "..."
    show yuri at foc
    y u112111 "Indeed... coming up here was a wonderful idea."
    y "And if there was ever a day that deserved to end watching the sunset together..."
    show yuri at std
    mc "Definitely."
    "There's something I need to talk to her about."
    mc "Yuri, now that we know what Portrait of Markov was..."
    mc "I feel like it's insane that you liked that book, even when you didn't know it was about us."
    "Uh... I hope that doesn't sound offensive."
    show yuri at foc
    y u125111 "I feel that way too."
    y "But it's not insane."
    y "People read books about horrible things happening to people all the time, and in fact..."
    y "... all stories involve it, to some degree."
    y "One could say imaginging the suffering of others is the cornerstone of all stories."
    y "It only starts to seem insane once you know it's real."
    show yuri at std
    mc "Huh."
    show yuri at foc
    y u121211 "I wonder if I could write a poem about that insight."
    y "In some sense, sadism is a core element of one of our main forms of recreation."
    show yuri at std
    mc "Uh..."
    mc "Yikes..."
    "Yuri giggles."
    show yuri at foc
    y u125131 "{i}The same knife cuts both flesh and vegetables.{/i}"
    y "{i}A singular tool of war and peace.{/i}"
    show yuri at std
    mc "Mm..."
    show yuri at foc
    y u125111 "Also..."
    y u126111 "Before you ask..."
    y u125111 "I haven't cut myself since the Literature Club."
    show yuri at std
    mc "Ahaha... can you blame me for being a little paranoid at first?"
    show yuri at foc
    y "I suppose not."
    y "But I haven't really felt tempted."
    y "Every time since then I've been stressed out, I was with all of you..."
    show yuri at std
    mc "Sorry."
    mc "Has the lack of solitude been upsetting?"
    show yuri at foc
    y "Not really."
    y "I feel like our bonds have gotten so much stronger that it feels completely different from how it used to."
    y "Knowing Natsuki is my sister and all..."
    show yuri at std
    mc "Yeah..."
    mc "... and all the trouble we got up to with me and Sayori and Monika trying to find you before Markov did..."
    show yuri at foc
    y u125111 "[mc_name], have you imgined what might come next?"
    show yuri at std
    mc "Come next?"
    mc "I prefer not to stress over the future after everything we went through today."
    show yuri at foc
    y "It isn't like the prospects of the future are all stressful ones."
    y "I'm eager to meet Libitina..."
    y "... outside of that horrid place."
    show yuri at std
    mc "I guess that'll be interesting..."
    mc "Assuming she doesn't open her Third Eye again and do any more distortion."
    show yuri at foc
    y u125213 "[mc_name]... do you want to kiss now?"
    y "S-since we got interrupted last time..."
    show yuri at std
    mc "Yeah."
    mc "It's kind of good we got interrupted - now our first kiss can be under the sunset."
    show yuri u121211
    return
