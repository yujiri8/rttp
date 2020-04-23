label chapter15:
    "The first chapter shows Elyssa seemingly having a dream about escaping from the warehouse water trap by opening her Third Eye."
    "She flies out, and goes into a frenzy killing cultists, seemingly made invulnerable..."
    "And then wakes up in her cell."
    "I feel terrible for Yuri just reading this..."
    "Elyssa's sick, and doesn't seem to have any tears left."
    "Markov enters her room."
    "Elyssa tries to scream, but is too weakened to really even do that."
    k "How did my first virtual reality test go?"
    k "I'm trying to find a less costly way of testing the Third Eye, that doesn't require subjects being allowed to actually stab someone to open it."
    k "People are a bit too scarce a resource for such expenditure."
    "Elyssa calls him a monster and tries hopelessly to appeal to his conscience."
    "He asks her a few doctor-like questions, and then says he's going to prescribe some biometric tests."
    "Before he leaves, he offhandedly confirms that Maria and her parents were also captured, and that they've all heard what happened to her."
    "She begs him for a chance to speak to Maria or anyone else, but he doesn't even consider it."
    # Chapter 2.
    "The second chapter introduces Linda Watson, a doctor, chatting with her boyfriend Renier."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u114111 at std(p41)
    show natsuki u124111 at std(p42)
    show yuri u113111 at std(p43)
    show renier ru1113 at std(p44)
    with open_eyes
    if persistent.player_suggest_linda_natsuki_mom:
        menu:
            " "
            "Darn. Linda isn't Natsuki's mom.":
                show renier ru1213 at foc
                r "Why is that thought so funny to you?"
                r "I have to say I'm glad."
                r "Anyway..."
            "(continue)":
                pass
    show renier at foc
    r ru1213 "Wasn't she an accountant?"
    show renier at std
    mc "This has gotta be before the story in Yuri's file."
    mc "Looks like the boyfriend she mentioned was you after all."
    show natsuki at foc
    n xu4111 "I bet Markov wipes her memory after this story."
    n "Sounds like he can."
    scene black with close_eyes
    "We go back to the book."
    "After a round of laughter subsides, Renier's expression turns solemn."
    r "Linda..."
    r "I'm going to stop keeping secrets from you."
    l "Eh...?"
    r "When I said I was a factory worker, I was lying."
    r "I am a member of God's Family at an establishment studying a dangerous supernatural force named the Third Eye."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u115212 at std(p41)
    show natsuki u214114 at std(p42)
    show yuri u128116 at std(p43)
    show renier ru22a3 at foc(p44)
    with open_eyes
    r "No...!"
    r "I couldn't have been one of them!"
    show renier at std
    menu:
        " "
        "That's pretty damning, Renier.":
            $ persistent.player_judge_renier = 1
            show yuri u12i116
            show renier at foc
            r "I know!"
            r "But there must be more to the picture!"
            r "Look, Monika's got, what, ten murders now, and no one stays mad at her for long!"
            show renier at std
            menu:
                " "
                "All of Monika's murders were under severe influence.":
                    pass
            menu:
                " "
                "I don't think you were possessed into joining the cult and the entire time you were in it.":
                    pass
            show renier at foc
            r "But you can't judge me before you even know what happened!"
            show renier at std
        "(say nothing)":
            $ persistent.player_judge_renier = 0
            show yuri at foc zorder 1
            y "Renier, how--...?"
            show yuri at std
            show renier at foc zorder 1
            r "I...!"
            r "I must have been brainwashed somehow!"
            r "I'd never do those things!"
    show renier at std
    show yuri u124113
    show natsuki at foc zorder 1
    n "Maybe he didn't know what they did."
    n "Maybe he was just a pawn and they were lying to him."
    show natsuki at std
    show renier at foc
    r ru21a3 "Yeah..."
    r "It has to be..."
    show renier at std
    show natsuki at foc
    n u214113 "Talk about a pickup line, though..."
    show natsuki at std
    scene black with close_eyes
    "We go back to the book."
    "Linda almost falls out of her chair."
    "She's speechless for a moment, so Renier continues."
    r "I'm not supposed to tell anyone outside of the Family that it exists."
    r "But I won't lie to you any longer."
    "Linda is still unable to find words."
    r "I have faith that God introduced me to you because It wants you to join us."
    r "I can't induct you without the Prophet's permission..."
#    r "... and I can't ask the Prophet without revealing that I've broken the rules..."
    r "But God will find a way. I'm sure."
    l "-- Renier!"
    l "What are you talking about?!?"
    ln "He's never mentioned anything about God before."
    r "I have to go right now, but I'll talk to you about this more tomorrow."
    r "Don't tell anyone else I told you."
    "Renier leaves."
    "Linda can't get a hold of him for the rest of that day."
    "She does get an email from her boss that evening saying she's being laid off, with very little about what's going on."
    "That night, she has a dream where 'God' tells her the time has come, and she opens a third eye, which sees the world from above."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u114111 at std(p41)
    show natsuki u214111 at std(p42)
    show yuri u124111 at std(p43)
    show renier ru1213 at foc(p44)
    with open_eyes
    r "Who wants to bet God is Markov using his admin powers to mess with people's minds?"
    show renier at std
    show natsuki at foc
    n u114111 "Weird... Clare and Daniel and Abbey didn't seem to know about this in book one."
    n "It seems like it would've been worth mentioning that the cultists really do have visions that make them believe in their God."
    show natsuki at std
    show renier at foc
    r ru2113 "Clare said they were there for years?"
    r "How'd they have so little interaction with the cultists that they never even heard about this?"
    show renier at std
    show yuri at foc
    y u125111 "Probably much of it was in solitary confinement."
    show yuri at std
    show sayori at foc
    s u116193 "Oh no..."
    s u115153 "It sounds so terrible."
    s "I don't want to read this either."
    show sayori at std
    show yuri at foc
    y "He may have also wiped their memories sometimes."
    y "Like Monika did to us..."
    show yuri at std
    show natsuki u114114
    mc "Suddenly that seems like a mercy..."
    scene black with close_eyes
    "When Linda wakes up, she tries calling Renier again on her cellphone."
    r "Linda, I have wonderful news!"
    l "Renier, are you going to explain what happened yesterday?"
    r "The dream is God's signal!"
    l "Wait, you know about my dream?!?"
    r "God rewarded me..."
    r "God has allowed you to join us because I asked It to and took the appropriate action."
    r "I knew it!"
    r "God did want you in the Family."
    r "It was just waiting for me to act."
    r "How long ago was I supposed to do this?"
    l "Renier, what is this God?"
    r "I don't understand It much."
    r "But It's proven Its existence to us."
    r "You saw the vision, and so did I when I was chosen."
    r "Just a few minutes ago I received word from the Prophet that God had chosen a new Child."
    r "I never told him that I told you anything."
    r "God answered my prayer."
    l "Are you saying this God has chosen me to help study the Third Eye?"
    r "Yes."
    r "If you're ready, I can take you to speak to the Prophet."
    l "I..."
    l "... need to think about all this!"
    r "You can have time."
    l "I don't--..."
    l "But why would God even want or need a group of humans to study something for It?"
    r "I don't understand it fully."
    r "I don't think even the Prophet does."
    r "But we carry out God's will."
    l "..."
    l "Okay, I'm going to think about this..."
    r "Take your time."
    r "I'll see you later, and may God be with you."
    "Linda hangs up."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u114111 at std(p41)
    show yuri u124111 at std(p43)
    show natsuki u124111 at foc(p42)
    show renier ru1111 at std(p44)
    with open_eyes
    n "I'm curious to see how Prophet Markov sells himself as a leader."
    n "If I heard this story, I'd say, \"So what? Just because some supernatural being is giving me visions doesn't mean I should worship it or do what its Prophet says\"."
    show natsuki at std
    show yuri at foc zorder 1
    y u125111 "I suppose it's human nature to want to be subordinate to something powerful."
    y "It provides a feeling of assurance..."
    y "... removing some of the weight of making one's own choices."
    y "Because you believe that no matter what, God will guide you along the right path, and it's easier to externalize anything that goes wrong."
    show yuri at std
    scene black with close_eyes
    # Chapter 3.
    "In the next chapter, Linda decides she's going to trust Renier and speak to God's prophet."
    "She calls Renier and he ends up taking her to the facility."
    "Along the way, Linda asks him about how he found God."
    "His story is basically hers except without one of the others talking to him about it."
    "He has plenty of detail and doesn't hesitate to answer, so Linda is sure he's being honest."
    "She also asks him why God's Family and the Third Eye are secret."
    "He explains that the rationale is fear of public opposition on the grounds that what they do is dangerous."
    "He says it is, but that they must discover the truth of it for the ultimate good of everyone, and that he trusts God that it's the right path."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u114111 at std(p41)
    show yuri u124111 at std(p43)
    show natsuki u124111 at foc(p42)
    show renier ru1111 at std(p44)
    with open_eyes
    n "This can't work for long."
    n "If Linda's going to be helping them, they won't be able to stop her from finding out what they do."
    show natsuki at std
    show yuri at foc
    y u125114 "I wouldn't underestimate what you can make someone do or believe with peer pressure, authority, and the promise that it's for the greater good."
    show yuri at std
    show sayori u114112
    show natsuki u124114
    show renier at foc
    r ru11131 "..."
    scene black with close_eyes
    "They stop at a checking gate of some sort where a booth worker verifies Renier's identity and then lets them through."
    "They drive along a forested path and eventually stop at a camp with several large buildings buried in the forest."
    l "This..."
    l "Is larger than I expected..."
    r "God has provided for all of our needs."
    "They enter a hall where Renier leads her to an office labeled with Markov's name."
    "Linda enters Markov's office, and he dismisses Renier."
    k "Linda... Watson, is it?"
    l "How do you know my name?"
    k "God knows all things."
    k "I am a servant of God, and It tells me everything I need to know."
    l "..."
    k "You recall your vision and firing."
    k "God has asked you to join Its Family."
    k "But the choice is yours."
    k "I believe God will arrange for your job to be returned to you if you refuse."
    ln "It's so surreal..."
    ln "God really did do that, didn't It?"
    k "Now is the time for your questions."
    l "What is the Third Eye?"
    "She doesn't expect a real answer to this, but she asks anyway."
    k "It's a rare condition that involves medical complications, violent behavior, memory loss, and in some cases supernatural powers."
    "(I notice that Markov doesn't specify whether those things are associated as symptoms or causes.)"
    k "At this facility, we study patients who show signs of it."
    "(I notice Markov still hasn't said anything about the \"patients\" being held against their will and even tortured.)"
    "(I wonder when he's going to.)"
    l "That..."
    l "Does sound dangerous..."
    k "Indeed."
    k "The fear of our work is justified."
    k "But we must understand it if we are to cure it."
    k "I even believe that when we learn what drives this force, we will harness it for good."
    "Linda clears her throat."
    l "If God is all-knowing, why do we have to study for It?"
    l "Doesn't God already know it all?"
    k "I do not know."
    k "Perhaps even God's ability to work through the world is limited."
    k "It never seems to act in overt ways, and I'm the only one It even speaks to outside of dreams."
    k "Perhaps being told the truth would defeat the point of discovering it."
    k "It is not our place to question the will of the being that gives us life."
    k "It would be disrespectful to assume that just because we are guided by God, we have no need to do anything."
    k "How would you feel if your children decided they didn't need to study or learn any skills because you would take care of them?"
    l "..."
    l "I suppose that makes sense..."
    "Linda says that insincerely."
    k "Do you have a decision?"
    "Linda is internally hesitant, but saying no doesn't feel like an option in this situation."
    "So she agrees."
    "Markov takes Linda's hand and mutters something in a foreign language."
    k "You are now a Child of God's Family, Linda."
    k "Welcome."
    l "... Um..."
    l "What did you say?"
    k "Even I have not been allowed to know."
    k "The words were given to me by God years ago."
    k "I understand that I am not required or meant to understand them."
    # Chapter 4.
    "In the next chapter, Linda examines some subjects that have clearly had their memories wiped and been brainwashed."
    "They even themselves say that they're insane and dangerous."
    "Linda takes some notes on their physical symptoms and prescribes some treatment."
    "It's made clear that Markov wants Linda on the team to prevent him from killing his subjects by accident."
    "He claims the prison hall is a place of God that keeps the subjects' Third Eyes suppressed so they don't activate spontaneously..."
    "... and that the magic is harmed by Children of God being inside it..."
    "... hence why she and the other personnel can't visit the subjects without administrative approval."
    "Later in the chapter, when Linda starts to pick up on the fact that the \"patients\" are being subjected to torturous experiments..."
    "... she's told by Renier that most of the subjects were serial murderers before being taken for study."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show sayori u115113 at std(p41)
    show yuri u114111 at std(p43)
    show natsuki u114111 at std(p42)
    show renier ru1111 at std(p44)
    with open_eyes
    mc "The scary part of that is that if it were true..."
    mc "It'd be a pretty good rationale."
    menu:
        " "
        "(say nothing)":
            $ persistent.player_pacifist = 0
            show renier at foc
            r ru2113 "Yeah..."
            r ru2133 "I just hope I really believed what I'm telling her."
            show renier at std
        "You're wrong, [mc_name]. It's not remotely acceptable to torture a defenseless prisoner.":
            $ persistent.player_pacifist = 1
            mc "I mean..."
            mc "It's not like it's torture just for the sake of it."
            mc "Doesn't it make more sense to use people like that for science..."
            mc "... if this were legitimate science, that is, which I'm not saying it is..."
            mc "... than to just lock them up and leave them?"
            show renier at foc
            r ru2113 "It does."
            r "I have to agree it would make sense if what I'm telling Linda was true."
            show renier at std
            menu:
                " "
                "I guess so...":
                    show renier at foc
                    r ru2133 "I just hope I really believed it."
                    show renier at std
                "No. Nothing justifies such wanton cruelty.":
                    $ persistent.player_pacifist = 2
                    mc "Well, I'm not sure I agree, but fair enough."
    scene black with close_eyes
    "I notice it was the first time anyone called them 'subjects' instead of 'patients' around Linda."
    "For good measure, Renier tells her a story about one that kidnapped, raped, and then murdered several women, to make sure she doesn't start to feel any sympathy."
    "I notice what Renier's doing here."
    "Not only does he not give her a way to verify this, but the way he talks about it makes it sounds like {i}all{/i} the subjects are guilty of that."
    "He does also tell her that not everyone being held there is a murderer..."
    "... and that the ones who aren't have been afflicted with the Third Eye in ways that make them delirious and dangerous even if they don't mean to be."
    "He promises her they don't do anything cruel to those ones."
    "Then we find out why he says this even though he could've convinced her they were all guilty."
    "The last subject she examines that day is a two-year-old named Libitina."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show yuri u224118 at std(p43)
    show natsuki u113124 at std(p42)
    show renier ru1133 at std(p44)
    show sayori u128354 at foc(p41)
    with open_eyes
    s "A {i}two-year-old{/i}!"
    show sayori at std
    show natsuki at foc
    n "Holy fuck..."
    show natsuki at std
    show sayori at foc
    s u1183k4 "They can't...!"
    show sayori at std
    mc "... Sayori...?"
    show natsuki u114114
    show sayori at foc
    s u118354 "I know they're evil, but how can they do this?!?"
    s u128354 "It's worse than evil!"
    s "They're..."
    s u228354 "They can't be forgiven!!!"
    show sayori at std
    "I've never seen Sayori like this..."
    "I feel terrible for her."
    "She's not wrong, though."
    menu:
        " "
        "(say nothing)":
            $ persistent.player_advocate_mercy[0] = 0
            show sayori at foc
            s u113354 "How could anyone do that...?"
            s "I can't imagine being so evil..."
            s u1161k4 "..."
            s u115153 "I'm..."
            s "I'm ready to keep reading..."
        "Sayori, there's no such thing as an unforgivable sin.":
            $ persistent.player_advocate_mercy[0] = 1
            show sayori at foc
            s u113353 "I thought that too..."
            s "But this?"
            s u113153 "I don't know if I believe that anymore."
            s u115153 "..."
            s "I'm..."
            s "I'm ready to keep reading..."
        "Sayori's right. Mercy is out of the question for these monsters." if persistent.player_pacifist < 2:
            $ persistent.player_advocate_mercy[0] = -1
            show sayori at foc
            s u115351 "..."
            s u115151 "I'm..."
            s "I'm ready to keep reading..."
    show sayori at std
    call suggest_sayori_not_read
    scene black with close_eyes
    "Libitina acts strangely mature, which is noted as normal in her Subject Notes."
    "She also, like the others, doesn't seem to even see her captors as enemies." # It may be that Libitina does see them as enemies, but is threatened into not telling Linda.
    "Linda does some medical examination and manages to come away without hearing anything about what the poor child's probably been through already."
    "I figure Markov is probably wiping each subject's memories before Linda examines them, and maybe restoring them after."
    "Maybe he just wants Linda for her medical expertise and doesn't think he can corrupt her?"
    "..."
    # Chapter 5.
    "In the next chapter, Linda speaks to a lot of the other cultists."
    "They all come off as quite amicable, and tell inspirational stories about how God changed their lives and how they're determined to carry out Its will for the greater good."
    "Markov seems to be trying to get her to feel camaradarie with them."
    "And it seems to be working..."
    "The perspective changes to Elyssa."
    "Elyssa meets Libitina under supervision, tries to mercy kill her, and..."
    "... she's stopped by the cultists, but during the chaos Libitina apparently thinks this is one of the 'life threat elimination' tests."
    "She claws at one of the cultists' ankles..."
    # Maybe she should've kept a small piece of metal. A stray staple or nail or something.
    "... and her fingernail is apparently sharp enough to puncture."
    "For Libitina, just drawing the tiniest amount of blood seems to open her Third Eye enough to activate the 'distortion' mentioned in her monthly report."
    "She screams and everyone else becomes crippled with pain and weakness."
    "The cultists aren't able to stop her, or really do anything at all."
    "..."
    "I guess Yuri never displayed any powers like this because she never drew anyone else's blood."
    "It probably did happen with Monika, and that's why she was eventually able to break the rules and destroy the script."
    "After a few seconds, Libitina passes out."
    "Markov, who was present, claims he prayed to God to save them and It answered..."
    "But I think we all know what really happened."
    "Elyssa comes away from the event with even worse symptoms from Libitina's \"distortion\", including vomiting blood."
    "I hear Yuri start to choke."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show natsuki u114114 at std(p42)
    show renier ru1183 at std(p44)
    show sayori u223112 at std(p41)
    show yuri u224181 at foc(p43)
    with open_eyes
    y "Ahkh-"
    show sayori u227112
    show natsuki u113114
    y "Guh--"
    show yuri at std
    "Uh oh..."
    if persistent.mc_least_favorite != "Yuri":
        "I take Yuri's hand on the theory that it'll help calm her down."
        mc "Yuri, think about tea or something!"
    else:
        show natsuki at foc
        n "Yuri, think about tea or something!"
        show natsuki at std
    "Yuri coughs a bit."
    show yuri u224122
    "..."
    show natsuki u114114
    show renier ru1111
    show sayori u225112
    "After a minute, she recovers."
    show yuri at foc
    y u224177 "I definitely can't read anymore..."
    y "I can't handle it."
    y "..."
    y u224135 "And if just reading about the past makes me so sick..."
    y u224125 "What will it be like if I have to face them again...?"
    y u224177 "Hell..."
    show yuri at std
    if not persistent.sayori_stop_reading:
        show natsuki at foc
        n "I guess there's no reason we have to all read it."
        n "I'll quit too."
        show natsuki at std
        show sayori at foc
        s "Me too..."
        show sayori at std
    else:
        show natsuki at foc
        n "I'm done reading this too."
        n "There's no reason I should."
        show natsuki at std
    show sayori at thide
    show natsuki at thide
    show yuri at thide
    hide sayori
    hide natsuki
    hide yuri
    "..."
    show renier at foc
    r ru1213 "I guess it's just you and me, huh?"
    show renier at std
    mc "Yeah..."
    mc "(Crap...)"
    scene black with close_eyes
    "It's the first time Linda sees Elyssa."
    "But Markov makes sure to wipe Elyssa's memory first."
    "She doesn't even remember her name."
    "Linda ends up believing whatever Third Eye-related sickness she's contracted made her forget everything."
    "When Elyssa finally stops vomiting blood..."
    "... she doesn't want to leave the medical room."
    "Other cultists eventually drag her out and back to her cell."
    "They remind Linda that Elyssa murdered someone."
    # Chapter 6.
    "In the next chapter, we learn from Markov's introspection that no matter how many times a subject opens their Third Eye, it never seems to get any stronger."
    "He knows the other stuff he's been putting the subjects through doesn't directly open it, but his goal is to find ways to strengthen it passively."
    "He starts to wonder if something close was the answer."
    "And so he has his most promising subjects kill a few of the least promising ones..."
    "... including Libitina killing Maria..."
    "... and then orders the limbs of the dead ones to be dismembered and each one affixed to the ceiling of a promising subject's cell."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru1113 at std(p44)
    with open_eyes
    mc "Oh my god..."
    mc "That's so disgusting."
    mc "This is making {i}me{/i} nauseous."
    scene black with close_eyes
    "A couple days pass."
    "Linda is gradually finding out that Renier's depiction of the subjects wasn't as all-encompassing as he made it sound..."
    "... but she continually rejustifies the claim to herself as, \"He didn't mean a supermajority, I just misunderstood\"..."
    "... while in the cases she knows they're completely innocent, she starts to convince herself they're more dangerous than they appear..."
    "... and that what they do to them isn't as cruel as it seems."
    "There's a scene where one of the other cultists spitballs to her about what unlocking the secrets of the Third Eye could do, the advancement it could bring to society."
    "They're remarkably effective at keeping her from finding out the truth outright."
    "She's rarely let into one of the subject's cells, and never one of the ones that has a limb in it."
    "I come to realize there's not as much memory wiping going on here as I thought."
    "A lot of the subjects really seem to have lost all semblance of sanity from the experiments."
    "I wonder if some of them have internalized the lies about them being criminals as a post-justification!"
    "Things go on, and at one point, while Linda is taking notes on Elyssa's condition - whose name has been redacted to XXXXXX in all documents - Renier blurts out her name."
    "Linda asks him and he's forced to admit that he was talking about XXXXXX."
    "He says her name was made confidential some time ago for reasons only Markov knows..."
    "... but he remembers from before the change was made."
    l "So XXXXXX is Elyssa?"
    l "I remember reading about this in the news!"
    l "A girl named Elyssa was wanted by the police."
    "Renier makes an excuse to leave the room shortly after that, leaving Linda alone to think about the ramifications."
    ln "... So is this a government facility?"
    ln "When Renier talked about why they had to keep it secret, I got the impression it was rejected by the senate or something and was funded by some private organization."
    ln "I think I'm being lied to."
    "She stops herself from asking Markov about it though, because she doesn't want to reveal that Renier told her."
    "Later that day, before Linda can get ahold of him again, Renier is transferred out of the facility for some classified assignment."
    # Chapter 7.
    "Another day passes between chapters."
    "The second time Elyssa has an episode of blood-vomiting, she's brought to Linda again."
    "Linda asks her what preceded the episode..."
    "... and she says she heard screams from the cell next to hers, and then it started happening when she stopped hearing the screams."
    "Linda talks to her a bit about her uncertainty in dealing with the alien condition."
    "Elyssa tells her that she's seen a few other subjects have contracted the same symptoms..."
    "... and she knows the names of a couple."
    "During the conversation, Linda also accidentally mentions Elyssa's name."
    "Elyssa says it sounds familiar."
    "Linda ends up giving her an abridged version of how she knew it."
    "When Linda tells Elyssa she has to leave, Elyssa begs not to be dragged back to her cell again."
    "It's the first time Linda discusses one of the subject's alleged crimes with them."
    "Elyssa, of course, doesn't have her memories."
    "She cries, beginning to wonder if Linda is telling the truth."
    "Linda has a moment of conflict, imagining how it would feel... to be imprisoned and told you committed crimes you couldn't remember."
    ln "But Renier wouldn't lie to me."
    ln "The others wouldn't lie to me."
    ln "I know them."
    ln "They're people like me."
    ln "This Family is a force for good."
    ln "It's not practical for them to prove each subject's guilt to each examiner individually."
    ln "I have to trust them."
    ln "She {/i}is{i} guilty."
    ln "I should think about {/i}her{i} victim."
    ln "What life did they have ahead of them when this girl came and murdered them?"
    "Linda talks to her about how the experiments are for the greater good."
    l "You {i}owe{/i} it to be our subject!"
    l "It's your way of paying for what you did!"
    e "{i}Please kill me...{/i}"
    e "If I have to... if I have to vomit like that again..."
    e "Please just kill me!"
    ln "This seems wrong..."
    ln "If her crime is murder, can it really be fair to say that death is too kind a punishment?"
    l "..."
    "Finally, still feeling conflicted but afraid of getting in trouble, Linda drags Elyssa back to her cell."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru1283 at foc(p44)
    r "Damn..."
    r "This kind of situation can make good people do horrible things..."
    r "They've set it up so she doesn't want to believe that the cult is evil..."
    r "... so she convinces herself of whatever she has to to avoid that conclusion."
    r ru1113 "Maybe I was in the same situation as her..."
    scene black with close_eyes
    "Once Elyssa is gone, Linda requests to see the records on the other subjects she mentioned..."
    "... and a few hours later, Renier walks in to her office with the papers on them."
    "When she asks about his assignment, he says that it was to pick up a new subject God had told Markov about."
    "She also asks him her question about how the facility is related to the government."
    "He claims not to know anything about it himself."
    "It's the first time Linda becomes really suspicious of him."
    "He goes ahead and plays the relationship guilt card, asking her if she really thinks he would lie to her of all people."
    "When he goes, Linda gives him a pill to give to Elyssa and asks him to ensure she has water."
    "She tells him she's worried for her survival after the second episode of blood-vomiting."
    "Renier promises to do as she asks and says he'll be with Elyssa shortly, then leaves."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru1283 at std(p44)
    mc "This is where it happens, isn't it?"
    mc "The message Linda wrote..."
    show renier at foc
    r "Wait..."
    r "Was I..."
    r "{i}Mercy-killing her?{/i}"
    r "Like she wanted?"
    scene black with close_eyes
    "In the meantime, Linda starts to look through the data on the other subjects Elyssa said were afflicted."
    "A few minutes after Renier leaves the room, Linda starts hearing Elyssa scream."
    ln "Oh no, not again..."
    ln "I don't care what she's done."
    ln "I feel so terrible for her now."
    "She doesn't rush over for fear of being accused of acting on emotional attachment to a subject."
    ln "Renier will bring her over for an emergency if she can be moved, right?"
    "She continues to scan the data on the other subjects with the symptoms."
    ln "Irregular heartbeat. Heart palpitations. Arrhythmia."
    ln "I search and search, eyes scanning everything I can find on their symptoms."
    ln "What is this?"
    ln "Shortness of breath?"
    ln "Chest pain? Dizziness?"
    ln "No. This is all wrong."
    ln "Elyssa's symptoms are nowhere near this simple."
    ln "I've seen it twice now."
    ln "The screams of pain."
    ln "Sickeningly pale skin."
    ln "Vomiting blood."
    ln "There is no other explanation, except that Renier's information was a complete and utter lie."
    ln "This can't all be coincidence."
    ln "It's not possible."
    ln "I don't know how much of this Renier is behind. But I do know this:"
    ln "There is something horribly wrong with this family."
    ln "And I accepted the invitation to become a part of it."
    ln "I can hear Elyssa's screams through the walls now."
    ln "I listen helplessly."
    ln "Renier said that he would be with her shortly."
    ln "Is he in her room now?"
    ln "Why is she screaming even louder than before?"
    "The scene cuts to Renier a minute ago, entering Elyssa's cell."
    "Elyssa asks him again for a mercy kill."
    r "Subject XXXXXX..."
    r "You know I can't do that."
    r "God wants you alive."
    r "I'm sorry, but it's not my place to disobey God."
    r "I'm here to give you a pill that might help."
    "Renier has a knife on him." # It's probly standard practice.
    "Elyssa attacks him, hoping to make him kill her in self-defense."
    "As Renier tries to push her off, he ends up giving her arm a cut by accident."
    "He didn't know he had a Third Eye before this."
    "He reels back, shocked to notice how it feels."
    "But Elyssa keeps attacking him."
    "Struggling to resist the urge of the Eye, Renier impulsively stabs her."
    "And the urge becomes much stronger."
    "Elyssa screams and begs him to end it quickly."
    "He manages to get a hold of himself for just a second to grant that one wish..."
    "... and then the poem follows."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru22a3 at foc(p11)
    r "...!"
    show renier at std
    mc "But..."
    mc "So..."
    show renier at foc
    r ru2183 "It {i}was{/i} a mercy kill..."
    r "Sort of..."
    r "An unintentional one..."
    show renier at std
    mc "So we still don't know if you knew they were innocent..."
    scene black with close_eyes
    "The experience with the Third Eye convinced Renier that was the cult was doing was wrong."
    rn "The Third Eye is a force of evil."
    rn "Doctor Markov is wrong."
    rn "God is evil."
    rn "Nothing will come of this that could justify what we do to innocent people here."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru22a7 at foc(p44)
    r "NO!!!"
    r "Fuck, no!"
    show renier at std
    mc "..."
    "Well, holy fuck."
    "Renier was a true cultist."
    "No ignorance excuse."
    "A monster."
    show renier ru11632
    show sayori u114112 at std(p41)
    show natsuki u114114 at std(p42)
    show yuri u114118 at std(p43)
    "Everonye else looks over at us."
    mc "Renier knew the subjects were innocent."
    show sayori u227134
    show sayori u227114
    show natsuki u117122
    show yuri u228116
    "..."
    show renier at foc zorder 1
    r ru22a3 "It's true!"
    r "It's true..."
    show renier at std
    show natsuki at foc zorder 1
    n "So much for you being all self-righteous when Monika confessed to us!"
    n "What the actual fuck!"
    show natsuki at std
    show yuri at foc zorder 2
    y "How many people did you torture?!?"
    show yuri at std
    show renier at foc zorder 3
    r ru21a3 "A lot."
    r "But just consider one thing..."
    r "Am I really worse than Monika?"
    show renier at std
    "..."
    show renier at foc
    r "Just like her, I've already had my excruciating death..."
    r "And I'm on your side now...!"
    show renier at std
    "..."
    show natsuki u115112
    show yuri u22b114
    show sayori at foc zorder 2
    s u215113 "He's right..."
    s "We forgave Monika."
    show sayori at std
    show yuri at foc zorder 4
    y u125114 "I suppose this isn't any different from then."
    y "It sounds like they made it easy to fall into..."
    y "... by revealing the truth gradually, and pressuring the recruits to justify more and more of it."
    show yuri at std
    show renier at foc zorder 5
    r ru2133 "Yeah..."
    r "Thank you..."
    show renier at std
    show natsuki at foc zorder 6
    n u113112 "We'll count you on your team still, but don't you forget..."
    n u115112 "Don't you {i}ever{/i} forget what you did."
    show natsuki at std
    "Renier nods vigorously."
    mc "Alright..."
    mc "I guess let's continue the book..."
    scene black with close_eyes
    "Renier goes back to Linda's office to confess everything to her."
    l "Renier, what's going on!?!"
    l "The records you gave me are a lie!"
    r "I've told you a lot more lies."
    r "I..."
    r "I killed Elyssa."
    r "And it felt... good."
    "Renier tells her everything that's happened."
    "And he explains that Markov had him give her false subject records because if she had examined those subjects, Markov would've had to wipe their memories like he did Elyssa."
    r "How's it possible to do what I've done?"
    r "I have granted kids to hell."
    r "I wasn't wrong when I said this place was full of insane and dangerous people."
    r "I was just wrong about who they were."
    l "Renier--!"
    l "I trusted you!"
    l "I liked you!"
    l "How could you do these things?!?"
    r "I did them because the Doctor said..."
    r "Because {i}God{/i} said."
    r "And now all I can do is stop myself."
    r "I'm dangerous, with a Third Eye I can't control."
    r "I want your honest answer."
    r "Should I kill myself?"
    l "..."
    l "... We have to put a stop to this."
    l "Renier, I'm going to need your help."
    "And that's how Linda and Renier started working as double agents to sabotage the cult."
    # Chapter 8.
    "In the next chapter, Renier reports to Markov how he was forced to kill Elyssa, and Markov exonerates him."
    "It turns out that Renier's alcoholism started as a way to combat his Third Eye!"
    "It helped him resist the urge to cut."
    "The same day, Markov also cleared Libitina's Subject Notes..."
    "... and declared that introducing bias during testing with her as a result of 'personal attachment' would be punishable by death now."
    "Renier actually knew an even more disturbing secret..."
    "The censored last name of Libitina."
    "It was Markov."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru1283 at std(p11) zorder 1
    mc "!!"
    mc "Libitina... is his daughter?!?"
    show sayori u227231 at std(p41)
    show natsuki u113123 at std(p42)
    show yuri u228131 at std(p43)
    show renier at std(p44)
    "..."
    show renier at xif(p44)
    r "He must've known..."
    r "I wonder if she knew..."
    scene black with close_eyes
    "And soon after, Linda wrote the Monthly Examination Report on Libitina."
    "In the test notes she tried to convince Markov to cut Libitina some slack, knowing there was a risk Markov would execute her for it."
    "And..."
    "Markov does."
    "He calls her into his office the day after that."
    "He commands her to take a seat."
    "Linda does, quivering with fear."
    "Markov makes sure it's visible that he has a gun on him, and is sitting across."
    k "Linda, is something making you uncomfortable?"
    l "Um... no..."
    l "I'm just a bit cold..."
    k "Why have you disobeyed God?"
    "Linda jumps on hearing those words."
    "Markov chuckles."
    k "Who even needs lie detectors?"
    l "Markov, what are you talking about?"
    k "That's 'Doctor' to you."
    "Linda realizes she's gotten too comfortable calling him by his name from her and Renier talking about him."
    k "One might think, from your actions lately, that you were overcome by compassion and decided to undermine the integrity of my experiments."
    l "N-no Doctor, I would never!"
    k "Why do you even bother?"
    k "Did I even need to do this examination?"
    k "I think not."
    k "I'm just a little more cautious about falsely convicting people than I probably need to be."
    "Linda, half-given up, stops protesting but also doesn't admit yet."
    k "But don't worry, I'm not going to kill you."
    l "You're... you're not?"
    k "I'm not that foolish."
    k "I only said that because it most effectively scares people into compliance."
    k "I could wipe your memory, but I don't think that would work as a long-term solution."
    l "Aah!"
    ln "He can do it!"
    ln "I don't doubt him, and I bet he did it to Elyssa!"
    k "You'd still be too conscientous, and you'd just turn against me when you inevitably found out again."
    k "Tampering is always a bit risky anyway, so I try to only do it when I need to."
    k "I have a better idea."
    l "God no, God no..."
    k "Here's my better idea."
    k "You'll help me test out virtual reality."
    l "...V... Virtu..."
    k "The power holds a great deal of promise, but I want to test it on some people that don't have a Third Eye before I risk my most valued subjects in an experimental technology."
    "Linda looks at the door."
    "Markov would pick up his gun and shoot her before she could escape."
    "She can't reach him to try fighting before he could shoot."
    "There's no out."
    k "Are you excited?"
    l "You're insane!!!"
    k "One might say I'm the only sane person there is, because I'm the only one who can recognize this illusion."
    l "What...?"
    k "I promise to explain that to you someday, when this is all over."
    k "For the time being I'm too worried about what might happen if I tell anyone else the full truth."
    k "Well, enough talk. Time for your first VR test."
    k "These conversations are more fun than I often realize."
    k "It's really nice to have a break every now and then, and yet it's also a type of climax of excitement in some ways."
    l "..."
    k "Well, banal rambling like that helps me keep myself sane in here, I guess."
    k "Let's go."
    "The scene cuts to later that day."
    "When Renier hears about Linda being discovered as a traitor, he maintains his deception, and Markov calls him in to talk."
    "The scene actually makes me feel really bad for Renier."
    "He had to see the woman who basically saved his soul get captured and condemned to torture..."
    "And not a few minutes afterward has to outwardly denounce her as a traitor."
    "He pushes back a little, pointing out that Markov told him to induct Linda as the result of a vision."
    r "Doctor, you need to be careful about misinterpreting your visions!"
    r "Our experiments were harmed because of your mistake!"
    r "Every act of sabotage Linda took would've been avoided if you hadn't ordered me to recruit her!"
    k "Renier, you know that God plans everything."
    k "This could only have been God's plan."
    k "It has plans we cannot see."
    r "I agree..."
    r "God must have planned for you to make this mistake."
    r "But I'll carry out God's will, Doctor, I promise."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru2113 at foc(p11)
    with open_eyes
    r "Damn..."
    show renier at std
    mc "So you were the only one left..."
    mc "The only hope for us."
    "Suddenly, I feel like I'm rooting for Renier in this story."
    scene black with close_eyes
    # Chapter 9.
    "In the next chapter, after some successful trials, Markov decides virtual reality is stable."
    "He creates a persistent virtual sub-world like ours, and places Linda in it as the world admin, but with fake memories."
    "He also places Libitina in it, with fake memories, and writes the \"script\" of that world to tend toward Libitina finding Linda and killing her..."
    "... as it happened in the story."
    "And now we know why Linda didn't have any friends or other relationships."
    "She was driven to start looking into suicide because of that vague feeling that the world was fake, even though she didn't understand it, like Monika had."
    "Then when she met Libitina..."
    "... who didn't have a name prepared and pulled out \"Maria\" just because it was someone she had met in prison..."
    "... Linda felt something around her just like Monika did when I first showed up to the club."
    "After Libitina left, Linda's epiphany came, and she stopped contemplating suicide..."
    "... and started trying to find \"Maria\" again, the only other person in the world she thought was real."
    "But she couldn't because there was no one called that."
    "And then Libitina came back and killed her before she could get a word..."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru2113 at foc(p11)
    with open_eyes
    r "This doesn't add up."
    r "Libitina was supposedly 3 when this happened."
    r "The girl in that story was obviously older than that."
    r "A body switch wouldn't explain it. She thought about things 3 year olds don't know about."
    show renier at std
    mc "Yeah..."
    mc "I also don't get why killing Linda didn't seem to give Libitina any extreme Third Eye symptoms."
    mc "According to the report, she had one of the most sensitive Third Eyes ever."
    scene black with close_eyes
    # Chapter 10.
    "The rest of the chapter was dedicated to that."
    "Markov is panicked at seeing the results that the experiment ruined Libitina's Third Eye somehow."
    "He rushes to extract her and Linda..."
    "... but he has some technical issues."
    "Libitina comes out in the 19 year old body she was given for the experiment."
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show bg space_room
    show renier ru1113 at foc(p11)
    with open_eyes
    mc "Huh."
    mc "If that can happen, then maybe she was mentally older than that before, and got physically changed back to a kid somehow."
    show renier ru2113 at foc
    r "Would explain it."
    r "If I were him, she's probably less dangerous as a little kid."
    r "But that would've been before Markov came up with this virtual reality trick."
    r "So there must've been some other way it could happen."
    scene black with close_eyes
    "He's unable to remove Linda's consciousness at all."
    "He figures she's dead."
    "He tests Libitina outside of it and finds that it didn't affect her Third Eye; it just didn't work inside the virtual world."
    "Markov does find a bug in his code that he thinks caused it, and after he fixes it, there are no more problems like that..."
    "... so he starts doing as much as he can in virtual reality."
    "Renier continues to do everything he can to hamper Markov's progress."
    "He misplaces documents, carries lies between cultists, and gets two of Markov's most loyal flunkies killed by test subjects, without implicating himself."
    # I want him to take some notable action during this period.
    "The night after, Renier hears Linda's voice in a dream."
    "She tells him what happened inside her VR."
    l "When Libitina killed me, I was already starting to figure out the admin thing."
    l "I managed to get myself sort of stuck in the world as I died so Markov couldn't remove me properly."
    l "I waited until he figured I was dead and then escaped into..."
    l "I don't really know where."
    l "I don't understand what's going on."
    l "But it's like the real world is now the virtual world, and I can see its fabric like I'm the admin."
    r "So you're God now...?"
    l "... I don't know..."
    l "I think Markov has these same abilities, but he knows more about them."
    l "I can't do much over this world, though."
    l "I can see it, but I can't figure out how to change anything."
    l "All I can figure out how to do it besides see things is talk to you in a dream."
    "Renier does a lot more sabotage with Linda as his supernatural eyes."
    # I think I'm not handling this well. I want to explain their sabotage, and make it interesting.
    "Linda finds out about Character.reset, a method Markov uses on Libitina in dire situations to prevent her from dying."
    "One night, in Renier's dream, Linda reveals she's learned Markov's next big move from spying on him."
    "He plans to restore the character files of Clare, Abbey, Elyssa, Maria, and Daniel inside one of his virtual worlds, and ship it to the outside world under the guise of a dating sim."
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
    show natsuki u113123 at foc(p42)
    show yuri u226131 at std(p43)
    show renier ru2283 at std(p44)
    with open_eyes
    n "He can do that?!?"
    show natsuki at std
    show renier at foc
    r "Why wouldn't he just send himself in a game like this and ask for help?!?"
    r "Why the hell does he gotta do all {i}this{/i} to get out of his world?"
    show renier at std
    show sayori u224111
    show natsuki u114113
    show yuri u224131
    mc "Too risky, maybe?"
    mc "I guess if he put himself in a game like this, and [persistent.playername] didn't believe his story and turned the game off, he'd be screwed..."
    show yuri u224121
    show renier ruf13
    "..."
    show sayori at foc
    s u113121 "I guess I wouldn't take that risk either..."
    show sayori at std
    show natsuki at foc
    n u214111 "I feel like I'd have gotten impatient after..."
    n "How long has he been at this?"
    n "It must've been at least several months..."
    show natsuki at std
    show yuri at foc
    y u125111 "I wonder if his own Third Eye is affecting him."
    y u12b116 "Maybe he enjoys these experiments more than he cares to admit..."
    scene black with close_eyes
    "Linda says he wants to study the effects of the game being turned on and off from a physical endpoint, which he can't simulate in the same way from inside."
    l "Listen, we need to get in there."
    l "We can't stop all this from the inside."
    l "We need to get {i}outside{/i} help."
    l "If Markov's going to use his powers to touch the outside world, that's our boat."
    l "We're going to sneak ourselves in, with our memories intact, and get an outsider's help."
    r "I'm on it."
    r "Tell me what I need to do."
    "Renier and Linda put together a plan for Renier to sneak in, connect himself to the virtual world just before it launches..."
    "... and Linda, not having a body anymore, hopes she'll be able to follow him in just from being in his mind."
    "THE END."
    return


label suggest_sayori_not_read:
    menu:
        " "
        "(continue)":
            $ persistent.sayori_stop_reading = False
            return
        "Maybe you shouldn't.":
            $ persistent.sayori_stop_reading = True
            s "..."
            menu:
                "The others will tell you anything important they learn from the book.":
                    pass
            menu:
                "There's no need for you to torment yourself reading the details.":
                    pass
            show sayori u115151 at foc
            s "You're right..."
            s "Thanks, [persistent.playername]."
            show sayori at thide
            hide sayori
            "Sayori wipes her tears and moves a distance away from the book."
    return
