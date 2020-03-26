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
    "We end up spending the night at Albert's hospital."
    "We really owe this guy."
    scene black with dissolve_scene
    return
