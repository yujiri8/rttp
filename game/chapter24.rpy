label chapter24:
    "Over the next couple hours, we all drive over to the facility site."
    scene forest_path with dissolve_scene_full
    "We stop before a hill, at the same place Renier's car is parked."
    play music determination
    show renier u1215 at foc(p11)
    r "Hi everyone..."
    r u1213 "The batallion of cultists is over the hill, about a hundred meters away."
    r "But don't anyone step over that ridge."
    r "If they see you, they might open fire." # I guess Renier anticipated their presence and got out of his car and peeked discreetly.
    r "So our plan is to use Libitina's Third Eye to wreak havoc on them?"
    show renier at std(p21)
    show libitina 1261222 at foc(p22)
    b "Yes..."
    b 1251222 "But..."
    b "Um..."
    b "I see a problem now."
    show libitina at std
    show renier at xif(p21)
    r "What...?"
    show renier at std
    show libitina at foc
    b 1261222 "Even if I used one of you as catalyst, I don't think it would work from this range."
    b "Once my Third Eye opens, I might be so overcome by bloodlust that I lose sight of my purpose..."
    show libitina at std
    m "Just like I did..."
    m "The Third Eye is too powerful a force."
    show libitina at foc
    b "Yeah."
    b "I might fail to wipe them out."
    show libitina at std
    show renier at foc
    r "And they'd open fire before they'd let us get close..."
    r "I dunno exactly what their orders are, but I doubt it's to take any risks."
    show renier at std
    m "Hold on."
    m "This would be much easier if she didn't have to get close or even use one of us to open her Third Eye."
    m "Let me see if world.create_object can solve this..."
    call updateconsole("world.create_object('gun')", "AttributeError: 'World' object\n has no attribute 'create_object'")
    m "Agh..."
    m "Looks like Adam broke world.create_object."
    m "Maybe he anticipated this."
    call hideconsole
    $ consolehistory = []
    show renier at std(p31)
    show libitina at std(p11)
    show mc c126311 at foc(p33)
    mc "Okay, this is probably a stupid idea..."
    mc "... but what about using a car to get closer?"
    mc "I mean..."
    mc c116111 "What if Libitina and whoever she's going to use as fuel use the car to get close to them, then they open Libitina's Third Eye..."
    mc "... and that way she can be within distortion range when she starts?"
    show mc at std
    show libitina at foc
    b "..."
    b 2261111 "I think that works as a plan."
    b "But the problem is still who's going to be my catalyst."
    b "I don't guess any of you consent."
    show libitina at std
    show mc at foc
    mc c116311 "Well of course not..."
    mc c116364 "That is a problem, I guess."
    show mc at std
    show libitina at foc
    b 1261112 "Someone has to."
    show libitina at std
    m "And the longer we wait, the more time we lose."
    show renier u1141 at foc
    "Renier clears his throat."
    r u1213 "Monika, it should be you."
    r "You're the only one here who's murdered others to open your Third Eye."
    r "If someone has to be fuel again--"
    show renier at std
    "I'm quick to respond."
    m "It can't be me."
    m "I'm our only admin..."
    m "If she messes me up, we could be lost."
    show renier u1143 at foc
    "Renier sighs."
    r uf13 "Good point. Okay."
    r uf23 "But it's sure as hell not gonna be me again."
    show renier at std
    show libitina at foc
    b 1261111 "You know..."
    b "At worst, you'll suffer for a few seconds between reset commands."
    show libitina at std
    show renier at std(p41)
    show libitina at std(p42)
    show mc at std(p44)
    show natsuki c223112 at foc(p43)
    n "Well you know what, some of us here know how much it hurts to be stabbed in the gut!"
    n "Don't act like you have the right to downplay that!"
    show natsuki at std
    show libitina at xif(p42)
    b 3271113 "Says the person who's never had the Third Eye sickness!"
    b "Do you know which one hurts more?"
    show libitina at std
    # Yuri's experience of being stabbed was only while her Third Eye was active.
    # TBH myabe Lib should mention there were experiences where she did go through that.
    show natsuki at foc
    n c113112 "Do you?"
    show natsuki at std
    "This is where I'd normally expect Sayori to jump in and try to cool things down..."
    show renier at std(p52)
    show libitina at std(p11)
    show natsuki at std(p54)
    show mc at std(p55)
    show sayori c115332 at std(p51)
    "But I see her starting to sweat."
    "She didn't get stabbed by me when [mc_name] and Natsuki and Renier all did, so she might feel like it's her turn to make the sacrifice..."
    show sayori at std(p61)
    show renier at std(p62)
    show libitina at std(p63)
    show natsuki at std(p64)
    show mc at std(p65)
    show linda 11b332b at foc(p66)
    l "It'll be me, I think."
    show renier u1133
    show libitina 2162114
    show natsuki c114114
    show sayori c115312
    show mc c114112
    l 11b112b "I was one of three who didn't get stabbed during Monika's frenzy."
    l "And I'm the only one of those three whose other death was painless."
    l "So if no one else will do it..."
    l "... I will."
    show linda at std
    show sayori c116293
    "I see Sayori look down."
    m "Okay. Thank you, Linda."
    m "I should make you POV before we do this."
    m "I don't know if automatic POV restoring uses the restore_character API or not, but just incase."
    "Libitina speaks up immediately after hearing that."
    show sayori c115212
    show libitina at xif(p63) zorder 1
    b "I want to be POV."
    show libitina at std
    show linda at foc
    l 124114 "Uh..."
    show linda at std
    show natsuki c116112 at xif(p64) zorder 2
    n "No way."
    n c113112 "You hear me, Libitina?"
    n c115112 "No{w=0.5} way."
    n c113112 "You already murdered Linda before..."
    if not persistent.threaten_libitina_to_come:
        n "... and refused to come along when you could've helped us break the world..."
    elif ch22_libitina_has_gun():
        n "... {i}and me{/i}..."
    n "... and she's volunteering to be your fuel."
    n c115112 "And you think {i}you{/i} deserve to be the one with death insurance?"
    show natsuki at std
    show linda
    show libitina at foc zorder 3
    b 2161111 "I didn't say I deserved it..."
    b "I just want it."
    show libitina at std
    show natsuki xc6112
    m "I'll give it to Linda if she wants it."
    m "Also, Linda's probably more likely to die here without it."
    show libitina at foc
    b 2261111 "Okay..."
    b "Then..."
    b "I'm ready if you are, Linda."
    show libitina at std
    show linda 115113
    show natsuki xc6114
    "Linda nods."
    show sayori at thide
    hide sayori
    show albert 22112 at leftinfoc(p61)
    al 22112 "I can't believe this is our plan."
    al "I'm so sorry, Linda."
    al 22152 "Good luck."
    show albert at xis(p61)
    scene black with dissolve_scene
    "Yuri bequeathes a knife to Libitina."
    "We retreat a safe distance."
    call switch_pov('linda')
label assault_facility:
    "..."
    "Libitina and I (Linda) board the vehicle."
    l "So I'm going to get us close..."
    l "... and provide you with live flesh to cut."
    l "Got it."
    "Lord, this is crazy."
    "How much is it going to hurt?"
    "It's going to be unlike anything I've ever felt, isn't it?"
    "I feel sick."
    b "I'm sorry."
    l "Don't bother."
    l "Just..."
    l "... make it count, okay?"
    l "Don't lose control and screw everything up."
    b "I won't."
    "..."
    "I drive over the hill."
    "It looks like there's some construction going on at the site, maybe the same buildings that later became his facility."
    "The guards are throughout it."
    "I see them talking and exchanging glances, but they don't open fire yet."
    play sound car_speed
    "I floor the gas."
    "We're getting in range as fast as possible."
    l "Libitina..."
    l "Get ready...!"
    "I duck so my head isn't a visible target."
    "We've got enough momentum that I don't have to do anything."
    play sound gunshot2
    pause 0.1
    play sound2 gunshot2
    pause 0.2
    play sound3 gunshot2
    "I hear the guards start to open fire on our vehicle."
    "None of the bullets strike me at first."
    "We must be in range now!"
    play sound stab_once
    "I hold out my arm, and Libitina stabs it."
    l "Go...!"
    "Is it...?"
    "I see Libitina's face react as if her Third Eye is opening."
    play sound stab_once
    "Just to make sure it's opening all the way, she gives me a second stab."
    "Finally, she starts doing that distortion thing..."
    show distort1
    show distort2
    with Dissolve(0.2)
    "This hurts like hell alright."
    "I feel like my head is being ripped apart."
    "I just have to deal with it for a minute...!"
    call updateconsole('linda.reset()', '0')
    call hideconsole
    $ consolehistory = []
    "Finally, Monika resets me..."
    "The cuts are gone."
    "But I still have to bear the torture Libitina is inflicting on me."
    "I could barely even feel the cuts anymore anyway."
    "Lord, I can't even tell what's happening!"
    "Is she doing it?"
    "Is she at least catching the guards in this field?"
    "It's not like I can see or hear anything, or feel anything... besides the feeling that my head is being ripped apart."
    stop music fadeout 3.0
    hide distort1
    hide distort2
    with Dissolve(0.4)
    "I feel like I lose my sense of time, and then..."
    scene facility_ruin with dissolve_scene_full
    "..."
    "I'm laying on the ground."
    "Things seem quiet."
    "I think Monika must've reset me."
    "Thank goodness, it's over..."
    "I sit up."
    "The car is a smoldering wreck, but I've been ejected out of it."
    "Maybe the last time Monika reset me, I couldn't be reset inside it, so the game spawned me out of it."
    "..."
    "The half-built buildings are a total wreckage."
    "I guess Libitina's Third Eye is this powerful, and I never saw her go uninterrupted before."
    "I see dismembered cultists everywhere..."
    "... and Libitina's lying in the dirt, seemingly unhurt, but unconscious."
    "Monika must've reset her too eventually."
    l "Hello...?"
    show renier ru2283 at foc(p11)
    r "Linda!"
    r "Are you okay?"
    show renier at std
    l "Yes..."
    show renier ru1114b
    show sayori at hopfoc(p31)
    s c222141 "Thank goodness you're both okay!"
    s c22x111 "We won!"
    show sayori at std
    l "Do I get a medal of honor or something?"
    show renier at foc
    r ru1115 "I didn't get one when I did this..."
    show renier at std
    "I laugh."
    l "We all deserve one by now."
    show monika c217113 at foc(p33)
    m "Hold on!"
    m c127113 "Where's the rift?!?"
    show sayori c224111
    show renier u1113
    show monika at std
    "I look at the camp again."
    "Now that she mentions it, there's no rift!"
    "The entire area is intact."
    show renier at foc zorder 1
    r u2283 "Wait..."
    r "It's not here?!?"
    show sayori c227212 at std(p41)
    show renier at std(p42)
    show monika at std(p43)
    show mc c118113 at foc(p44)
    mc "You're telling me this was for nothing?"
    show mc at std
    show renier at xif(p42)
    r u2283 "But why were they guarding this place if there's no rift?!?"
    show renier at std
    "..."
    l "So we gained nothing here, and we still need to find Adam before he manages to disconnect the viewport?"
    show monika at foc zorder 1
    m c114244 "Yes..."
    show monika at std
    l "What the hell!"
    "I thought I was giving us a chance again!"
    show sayori at std(p51)
    show renier at std(p52)
    show monika c114211 at std(p11)
    show mc at std(p54)
    show albert 21111 at foc(p55)
    al "Hold on!"
    al "These guards would probably have had a way to contact him."
    al "Maybe we can call him and at least scrape a possible clue."
    show albert at std
    "Renier picks up one of their phones."
    show mc c114211
    show sayori c225212
    show renier at foc zorder 2
    r u1113 "He's there..."
    r "They've got him as a contact."
    r u1111 "Let me try."
    show renier at std(p63)
    show sayori at std(p62)
    show monika at std(p64)
    show mc at std(p65)
    show albert at std(p66)
    show yuri c226211 at foc(p61)
    y "Wait!"
    y c225113 "We should think about what we're going to tell him."
    y "He obviously won't cooperate if he knows it's us."
    y "Is it possible we could pose as his troops, and say we captured... us?"
    y "If all the location or spying APIs are broken, he couldn't check, right?"
    y "So he might come over."
    show yuri at std
    show renier at foc
    r u1113 "Ooh..."
    r "Good thought."
    show renier at std
    show sayori at thide
    hide sayori
    show yuri at std(p62)
    show natsuki c124111 at foc(p61)
    n "Remember, he wanted to leave [persistent.playername] hope."
    n "So if he thought we'd all been captured, he'd probably panic and contrive some way to set us free."
    show natsuki at std
    show yuri at foc zorder 1
    y c124142 "Oh..."
    y "I forgot."
    y c125111 "Surely there's a way to contrive a reason his troops could give him to come personally over here?"
    show yuri at std
    show mc at foc zorder 1
    mc c124111 "Should be easy enough."
    mc "Tell him a weird-looking portal opened."
    show mc at std
    show renier at foc
    r u1115 "Heh... that's clever."
    show renier at foc
    r u2113 "But he'll still see who's reporting and know if their voice is wrong."
    r "He knows all these people personally."
    r "He hand-picked them, after all."
    r "Over the phone, it might be passable with a sound-alike, but not for me..."
    r u1113 "He'll know my voice."
    show renier at std
    l "I probably shouldn't do it either."
    show albert at foc zorder 2
    al 22111 "I'll do it. He doesn't know me."
    show albert at std
    show renier at foc
    r "Alright..."
    "Renier points to a different fallen cultist."
    r uf13 "That one's voice sounds the most like yours, I think."
    show renier at std
    "Albert gets the guard's phone from Renier and attempts to call Adam."
    show natsuki c114114
    show yuri c124118
    show monika c114112
    play sound phone
    "..."
    pause 2.0
    "I hear a sound from the phone."
    "Albert signals with his hand that he established contact."
    "He puts Adam on speaker mode."
    show albert at foc
    al 11111 "Doctor, there's something you need to see."
    al "Some kind of portal opened around here..."
    al "It looks like..."
    al "... I don't know how to describe it!"
    al "It must be a sign from God."
    show albert at std
    "..."
    k "Albert, is it?"
    show natsuki c113214
    show yuri c228235
    show monika c117312
    show mc c118215
    show renier u1183
    show albert 11142 at hop
    al "...!"
    k "I don't know who you are, but this was a pretty good try, I'll admit."
    "What...?"
    "How did he know?"
    "Not just that it wasn't the follower he knew, but he knew Albert's name?"
    show monika at foc zorder 2
    m "{i}I don't understand...{/i}"
    show monika at std
    k "I can't spy on any of you directly, but I can still see the viewport's perspective."
    k "And I can also read the history from it, so I know how you tried to fool me."
    show monika at foc
    m c117214 "No...!"
    m c114244 "I could've known, but somehow I didn't think of that..."
    show monika at std
    k "It was a good try though."
    k "By the way, I did station the cultists here because of the rift."
    k "I didn't know if it would still be here or not, and I sent them here just incase."
    # As for why he didn't send them away after, maybe he was going to meet up with them for protection? But he doesn't reveal that cause he doesn't want to give them clues about where he is?
    # Or maybe he didn't tell them what their purpose was in going there, and didn't want to hint at it.
    k "I'm impressed at how easily you killed them all."
    k "They deserved it, of course."
    k "And I hope they suffered in it as much as they made you suffer."
    k "With luck, once I finish getting [persistent.playername] out of this picture I'll be able to get them back if I still need them."
    show monika at foc
    m c118213 "Adam, come to your senses!"
    m "Ursula broke out using combined Third Eye and admin status!"
    m "I have those requirements too!"
    m "Do you know of any reason I can't open the portal like she did?"
    m c117115 "Because if I can, there's no need for you to be doing all this evil shit!"
    show monika c117113 at std
    k "Yes!"
    k "You think I didn't think of that?"
    k "I know yours doesn't work, or else I'd have encouraged you to try it."
    k "Your Third Eye isn't strong enough."
    k "I know because when you do it with a strong enough Third Eye but no admin status, it backfires and you lose your physical age."
    k "That's what happened to Libitina."
    k "I tried it on other test subjects."
    show mc at foc zorder 2
    mc c114135 "..."
    mc "Now that he says it... I might remember that..."
    mc "He didn't explain it to me, but I think I do remember being taken outside the facility to some place and opening my Third Eye."
    show mc at std
    k "Yeah..."
    k "No one but Libitina got that backfire effect."
    k "That must be because it takes a strong enough Third Eye, and yours isn't that high up."
    k "I tried it on some people whose Third Eye was stronger than yours."
    show monika at foc zorder 3
    m c124113 "So you're telling us if Libitina was an admin, she could open the portal?"
    show monika at std
    show mc c114115
    show natsuki c114114
    show yuri c224135
    k "..."
    k "No..."
    k "No....."
    k "{i}No...{/i}"
    k "Oh my god..."
    "He hangs up."
    show mc c114111
    show natsuki c114111
    show yuri c223113
    show albert 11111
    show renier at foc zorder 3
    r uf13 "I don't even know what to make of that."
    r "What did he realize?"
    show renier at std
    l "I'm not quite sure either..."
    l "... but I think it's pretty clear the ultimate way to get out of here is by making Libitina an admin."
    l "Of course, we'd have to understand a little more about it to make sure we know how to get everyone out, instead of just her..."
    l "But we've got to look into it."
    show monika at foc zorder 4
    m c124111 "Do you think we could make Libitina admin by putting her in DDLC..."
    m "... making her Club President, and then having her use her Third Eye to break out like I did?"
    show monika at std
    l "I think that would work."
    "I realize that by discussing this plan, we've disclosed it to Adam."
    "If he happens to read the viewport history, he'll break admin.jail and our plan will be foiled!"
    l "Monika quick!"
    l "Before he breaks admin.jail!"
    show natsuki c114114
    show yuri c223118
    show mc c114115
    show albert 12142
    show renier uf33
    show monika at foc
    m c124112 "Huh...?"
    show monika at std
    l "Quick!"
    l "The viewport history's giving away our plan!"
    show monika at foc
    m c117212 "Oh crap!"
    show monika c217212
    call updateconsole("ddlc = admin.get_world(\n  'doki_doki_literature_club')")
    call updateconsole("ch = admin.jail(ddlc, libitina)")
    call updateconsole("sig = pgp_sign(ch, markov_key")
    call updateconsole("admin.complete_action(sig)", "Libitina moved to jail\n doki_doki_literature_club")
    $ delete_character('libitina')
    call hideconsole
    $ consolehistory = []
    show monika c114212 at std
    "I see Libitina's body disappear."
    l "Now break admin.unjail!"
    show monika at foc
    m "But how does that stop him from breaking admin.jail?"
    show monika at std
    l "He won't!"
    l "If admin.unjail doesn't exist, then our plan should be the only way to get her back."
    l "I don't think he'll break admin.jail then."
    l "He valued her so much as a test subject that he wouldn't even risk deleting her when there was no evidence he wouldn't be able to restore her."
    l "Do it now!"
    show monika at foc
    m "Okay!"
    show monika c214212
    call updateconsole("admin.unjail(ursula)", "ERROR: escaped character.\nDisabling admin.unjail.")
    m "Done..."
    show monika at std
    call hideconsole
    $ consolehistory = []
    l "Phew..."
    show natsuki c114111
    show yuri c223111
    show renier uf12
    show mc c114111
    show albert 12111
    show monika c114111
    l "Our plan ought to be safe now."
    "..."
    show yuri at foc zorder 3
    y c125117 "It still feels wrong to do this to Libitina without her permission."
    y "But I suppose we had no choice."
    show yuri at std
    l "Yeah..."
    if ch22_libitina_has_gun():
        show natsuki at foc zorder 4
        n xc4111 "Well, she can't really object after she shot me to break the world without waiting for permission."
        show natsuki at std zorder 2
        show yuri c124112 at foc
        y "That's true..."
        show yuri at std
    show monika at foc
    m c124112 "So now..."
    m "We have to talk about..."
    m "Who."
    show natsuki c114114
    show yuri c114118
    show mc c114115
    show renier uf33
    show albert 12112
    m "Probably, one of us will have to go in with her and let her kill us to open her Third Eye."
    show monika at std
    show mc zorder 0
    show albert at foc
    al "Good Lord, didn't we just do this?"
    show albert at std
    l "It wasn't the first time, and this probably won't be the last."
    show albert at foc
    al "I remember the story of how you escaped, but..."
    al "..."
    al "Does that feel almost normal to you now?"
    show albert at std
    l "..."
    l "Yeah. It does."
    show albert at foc
    al "That's horrible."
    show albert at std
    show yuri at foc
    y c114112 "To be honest..."
    y "Being stabbed to death pales in comparison to what most of us went through as Adam's prisoners."
    y "I tried to make them kill me, and counted myself incredibly lucky when I finally succeeded."
    y "Even if it was agony for a minute... I immeasurably preferred it to the prolonged torture of that place."
    show yuri at std
    show albert at foc
    al 11152 "..."
    al 11162 "I can't imagine..."
    show albert at std
    "Well, welcome to the club..."
    "That's pretty much what things have been like."
    l "Um... Monika, I'm really sorry, but it clearly has to be you this time."
    l "Assuming the plan works and Libitina gets out, she probably won't be taking whoever she used with her."
    l "She'll be out of her mind, and will certainly have killed you."
    l "So you'll need admin powers to have any chance of getting out."
    show monika at foc
    m c114212 "..."
    m "You're right..."
    m "Jeez."
    m c113214 "Guess I still haven't been through enough, huh?"
    show monika at std
    show albert at thide
    hide albert
    show sayori c125212 at rightinfoc(p66)
    s "..."
    s c123212 "Monika, we're all really sorry about this."
    s "It's not fair."
    s "This reality's been cruel to everyone."
    s "But someday, we will be free."
    s "And it'll be thanks to what you did here."
    s "And Natsuki will bake cupcakes for you!"
    show sayori at xis(p66)
    show natsuki at foc zorder 5
    n c212114 "Ahaha..."
    n c214114 "I mean I totally will, if we all survive this."
    n "I'll make them the best you've ever tasted, okay?"
    show natsuki at std
    show monika at foc
    m c114214 "I guess that would be nice..."
    m "But even with admin powers, it's not obvious I'll be able to get out."
    m "What if it's the end for me?"
    show monika at std
    call screen dialog("Monika, did you break the memory-wiping API?", ok_action=Return())
    show monika at foc
    m c117113 "You bet I did!"
    m c127115 "What, you wanted to mind-wipe us?"
    m "And also forgot that doesn't work on alert characters?"
    show monika at std
    l "Huh?"
    call screen dialog("You cruel bastard.", ok_action=Return())
    call screen dialog("I can't hide from it anymore.", ok_action=Return())
    show monika at foc
    m c114211 "...?"
    show monika at std
    call screen dialog("You reminded me.", ok_action=Return())
    call screen dialog("And now I can't forget again.", ok_action=Return())
    show monika at foc
    m "What did I remind you of?"
    show monika at std
    show sayori at foc
    s "Monika, who're you talking to?"
    show sayori at std
    show monika at foc
    m "..."
    m "I got some OK-dialogs from Adam."
    m "He called me a cruel bastard for breaking the memory wiping API..."
    m "I reminded him of something, and he wanted to forget again, but now he can't."
    show monika at std
    call screen dialog("Oh fuck, I'll just tell you what happened.", ok_action=Return())
    call screen dialog("I'll use the viewport menus so everyone can hear me.", ok_action=Return())
    menu:
        " "
        "I thought of making Libitina an admin not long after the beginning of this. - Adam":
            pass
    menu:
        " "
        "But I didn't want to do it because I thought she would use those powers to exact revenge on me while she was at it. - Adam":
            pass
    menu:
        " "
        "... So I took my own memory of the idea. - Adam":
            pass
    show sayori c124111
    show mc c124112
    show yuri c114111
    show natsuki c113113
    menu:
        " "
        "And I wrote a script to stop myself from thinking of it again. - Adam":
            pass
    menu:
        " "
        "All the years I spent searching for another way out... - Adam":
            pass
    menu:
        " "
        "I wasn't doing this to save us all. - Adam":
            pass
    menu:
        " "
        "I knew how to do that years ago. - Adam":
            pass
    menu:
        " "
        "I did all of this to save myself. - Adam":
            pass
    menu:
        " "
        "I can't believe how evil I really am...! - Adam":
            pass
    menu:
        " "
        "I must be so much more evil than my cult followers. - Adam":
            pass
    show renier at foc zorder 5
    r u2226b "Of all the times to fucking notice that!"
    r "You're responsible for every last drop of blood spilled!"
    r "You can never pay it back!"
    r "The best thing you can do is kill yourself right now!"
    show renier at std
    menu:
        " "
        "I probably would if I could. - Adam":
            pass
    show monika at foc zorder 6
    if persistent.player_advocate_mercy[1]:
        m c117113 "How about you be the one to sacrifice yourself?!?"
        m "If you really give one shit about the people you've hurt, you'll let Libitina use you as fuel so I don't have to!"
        show monika at std
        menu:
            " "
            "What... - Adam":
                pass
    else:
        m c114115 "Oh don't worry, we're not gonna make it that easy for you..."
        m c118115 "We're gonna put you through everything you did to us!"
        show monika at std
        "Monika's voice rises to a scream."
        menu:
            " "
            "Dammit... I know how little it means now, but I swear I'm sorry. - Adam":
                pass
        menu:
            " "
            "But that doesn't mean I can just give up when I know you're going to torture me... - Adam":
                pass
        show sayori at foc
        s c128114 "If you felt anything for the people you've hurt, you'd volunteer to be Libitina's fuel so Monika doesn't have to!"
        show sayori at std
        menu:
            " "
            "What...? - Adam":
                pass
    menu:
        " "
        "Oh no. - Adam":
            pass
    menu:
        " "
        "You put her in {i}DDLC{/i}? - Adam":
            pass
    show monika at foc
    m c127113 "We're gonna give her admin status out here the same way I got it!"
    show monika at std
    menu:
        " "
        "DDLC has got to be broken by now! - Adam":
            pass
    show monika at foc
    m c114113 "She got in alright..."
    show monika at std
    menu:
        " "
        "That's the worst part of this news! What if we can't get her out?!? - Adam":
            pass
    show sayori c125112
    show renier u2213
    show natsuki c114111
    menu:
        " "
        "Wait, you broke admin.unjail too? - Adam":
            pass
    l "Well did you think we were stupid?"
    l "We weren't just gonna let you foil our plan!"
    l "Now the only hope to save her is our plan."
    menu:
        " "
        "I see. Well played. - Adam":
            pass
    menu:
        " "
        "I pray it isn't too broken for your plan to work. - Adam":
            pass
    l "There's no reason it should be any more broken than it was when we left it, right?"
    menu:
        " "
        "That was pretty broken. - Adam":
            pass
    menu:
        " "
        "Broken enough that it was the only VR that didn't get removed when you started a new game... - Adam":
            pass
    menu:
        " "
        "Because apparently it couldn't be. - Adam":
            pass
    l "But we were able to get out of it!"
    show sayori at foc
    s c123112 "Actually, she might've gotten stuck like you and [mc_name] were for a while!"
    s "And then that might also happen to whoever goes in to do the plan..."
    show sayori at std
    l "Yeah, it's possible."
    l "But Character.reset was the solution to that before, and now we know about it."
    menu:
        " "
        "Okay. I'm going to put myself in DDLC. - Adam":
            pass
    menu:
        " "
        "I have to save Libitina. - Adam":
            pass
    menu:
        " "
        "Whatever the costs. - Adam":
            pass
    menu:
        " "
        "I'll have to fall asleep to be inserted. - Adam":
            pass
    menu:
        " "
        "I'll start a throttled loop to keep trying to put me in every few seconds until it works. - Adam":
            pass
    show monika at foc
    m c114211 "..."
    show monika at std
    show natsuki at foc zorder 5
    n c124111 "He's buying time."
    n "He's just saying that so we won't go in to try to get her."
    n "Meanwhile, he keeps hacking away at the viewport."
    show natsuki at std
    show monika at foc
    m c114212 "..."
    show monika at std
    show natsuki at foc
    n "Or maybe he is gonna go in, and then just bring him and her both out without making her admin."
    show natsuki at std
    show monika at foc
    m c117114 "Ugh, you're right..."
    m c114214 "I still have to do this."
    # Should this be given to the player?
    menu:
        " "
        "(say nothing)":
            pass
        "Hold on, did you notice he implied that he thought of making Libitina an admin before he discovered VR?":
            menu:
                " "
                "There must be a way to do it without that.":
                    pass
            m "That wouldn't help though."
            m "We already put her in."
            m "Which means we can't access her data from out here."
            m "I still have to go in to get her."
            m "Besides, there's no way he didn't break it after that conversation, and since we can't tell the difference between a broken API and one that never existed, it's not even any use trying to guess it."
    m "I could try to fall asleep before him and put myself in first, like we were going to do."
    show monika at std
    show mc at thide
    hide mc
    show albert 11511 at foc(p65) zorder 6
    al "Do it!"
    al "Stop giving him a head start!"
    show albert 12111 at std
    show renier at foc zorder 6
    r u2113 "Wait, there's a faster way."
    r "For our plan to work, Monika needs to get into DDLC before Adam does."
    r "We've already seen that reset knocks you out when your Third Eye is open."
    r "So let's have Monika schedule a reset command on herself and then open her Third Eye."
    show renier at std
    show monika at foc zorder 7
    m c114212 "Ooh..."
    m "You're right. That's faster."
    m "It's really dangerous, but we have to make sure I get in there before him."
    show monika at std zorder 6
    l "Let me just say..."
    l "I'm not being your fuel."
    l "There are two other people here who haven't done it yet."
    show sayori c115332
    show yuri c224225
    show albert at foc zorder 7
    al 11111 "Three, actually..."
    al 12111 "But I've just got a better idea."
    show yuri c223111
    show sayori c114111
    al "A much safer one."
    al "Use blunt trauma to knock her out."
    al "I feel bad suggesting something so violent, but it has to be better than using her Third Eye."
    show albert at std
    show renier at foc zorder 7
    r "Mm... you're right."
    show renier at std
    show monika at foc zorder 8
    m c124112 "If I'm understanding you, you're going to bludgeon me into unconsciousness?"
    m "I guess you're right. It's a way better plan than using my Third Eye."
    show monika at std
    show renier at foc zorder 9
    r u1113 "Albert, I take it you know how to do this?"
    r "Somehow I don't think she's going to fall unconscious if I just whack her in the head."
    show renier at std
    show albert at foc zorder 9
    al "Indeed, there's some science to it."
    al "The knockout that experienced boxers or martial artists can deliver is caused by rattling the brain inside the skull."
    al "The brain floats in--"
    show albert at std
    show renier at foc
    r u2113 "Okay okay, we don't need all the science."
    r "Just tell me how to do it."
    show renier at std
    show albert at foc
    al "It's more about the lack of anticipation than the amount of force."
    al "To knock someone out cold, you need to hit them in the head by surprise."
    al "If they see it coming, their body reacts."
    show albert at std
    show renier at foc
    r "Alright..."
    "Renier steps through some of the wreckage and picks up a broken metal pipe from what might've been part of a plumbing system or something."
    show renier at std
    show monika at foc zorder 10
    m c113113 "Let me schedule my insertion."
    m "I'll add on a Character.reset so I don't get a bruise..."
    call updateconsole("import time")
    call updateconsole("def insert_monika():\n time.sleep(60)\n monika.reset()\n challenge = admin.jail(ddlc, monika)\n signature = pgp_sign(challenge, markov_key)\n admin.complete_action(signature)")
    call updateconsole("insert_monika()")
    call hideconsole
    $ consolehistory = []
    m c114212 "Okay..."
    m "It'll try to insert me in one minute."
    show monika c113143
    "Monika closes her eyes."
    m "I'm waiting."
    show monika at std
    show renier at foc zorder 11
    r u1231 "Here we go..."
    show renier at std
    m c114243 "I really hope this works on the first try."
    play sound punch
    play sound2 fall
    show monika at thide
    hide monika
    show albert 12112
    show sayori c115112
    show natsuki c124114
    show yuri c224118
    "Renier swings, and Monika falls over without a cry."
    "I think it worked."
    show albert at foc
    al "Phew..."
    al "Well done..."
    show albert at std
    "A few seconds later, Monika's reset command executes and her nascent bruise disappears."
    $ delete_character('monika')
    "A few seconds later, her body disappears."
    l "Well there we go..."
    l "Now we wait."
    return
