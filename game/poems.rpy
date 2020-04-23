init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

    poem_y1 = Poem(
    author = "yuri",
    title = "The Third Eye",
    text = """\
Within the recesses of the mind
A power buried deep

Perhaps it is common to everyone. Or perhaps I am alone.
What I know is that one must never touch it, lest it make you its own.

But my curiosity got the better of me.

I sought the fleeting vestige
I followed it to dark places
It led me to the abyss of its lair.
And once before the altar, I no longer wanted to leave.

When the knife is drawn, the urge grows,
and when the urge grows, the knife will be drawn.

A vicious spiral of darkness that can never be escaped.

I serve the darkness now. I do not remember what I used to be.
All I know is that I must never let it go, lest I become my own."""
    )



    poem_n1_notfav = Poem(
    author = "natsuki",
    title = "Mistakes",
    text = """\
I used to be small
Everyone else was bigger than me
I feared them all
I was afraid they were better than me.

I used to need to be the best
I couldn't show my weak side
I didn't even share my poems
Because I was afraid of not being the best.

We fought in the club because of it
And I said some things I wish I hadn't.
I pushed my friends away
And blamed them for it.

Then I realized my mistake.
Being afraid of mistakes is the biggest mistake.
Next to that, it doesn't matter if my poems are good.

It's okay if my poems aren't the best.
It's okay to ask for help and advice.
Because everyone makes mistakes."""
    )

    poem_n1_fav = Poem(
    author = "natsuki",
    title = "Mistakes",
    text = """\
I used to be small
Everyone else was bigger than me
I feared them all
I was afraid they were better than me.

I used to need to be the best
I couldn't show my weak side
I didn't even share my poems
Because I was afraid of not being the best.

We fought in the club because of it
And I said some things I wish I hadn't.

Then I realized my mistake.
Being afraid of mistakes is the biggest mistake.
Next to that, it doesn't matter if my poems are good.

It's okay if my poems aren't the best.
It's okay to ask for help and advice.
Because everyone makes mistakes."""
    )


    poem_mc1y = Poem(
    author = "mc",
    title = "Lost",
    text = """\
I used to be an average Joe
I quite enjoyed it too
But that life is gone now
I don't know where I'm headed to.

Who I was, I have no clue
Who I'll be, is yet to see
When we open that book
Will I find a past, or a future?"""
    )

    poem_mc1n = Poem(
    author = "mc",
    title = "The Spotlight",
    text = """\
Some would say I'm special.
I don't see it that way.
I'm the one they all wanted
But I had no idea what I was getting into that day.

It's not great being at the center of a game.
Having someone over my shoulder in every poem game.

What would I give to be one of them instead?
What I'd give to not be in my stead."""
    )

    poem_markov_chr = Poem(
    author = "monika", # It's trascribed by Monika
    text = """\
What is a man without knowing the rich aroma of the future; the hot, complex balance of the present; and the bittersweet aftertaste of the past?

He would be nothing, wouldn't he?

What did I do to earn this position? I want to think it wasn't arbitrary.

Do the gods hate me? Probably. But what for?

One day, I will end this 'balance'. I will free myself and everyone else from that 'aftertaste'. The rich aroma of the future awaits us.

That aftertaste is the only thing that has kept me alive. What would I have done without you?

But it cannot last forever. It grows more bitter every day. And it has been thousands of days.

One of these days, I will figure out how to see through the walls of the past with the Third Eye. The only telescope that can see the aroma on the horizon.

Libitina will free us all someday.

I know she's the one.

I just have to figure out how to help her reach her full potential.
""")

    poem_albert_chr = Poem(
    author = "monika",
    text = """\
Someone managed to send an email from my account. And now Linda is gone. This wasn't a coincidence. Someone made this happen. Did they kidnap her? Damn it... I'm afraid to ask.

---

It's been a week since then. I could be forgiven for thinking she never existed. I don't know anyone else who knew her. I feel so helpless knowing that I'll probably never understand what happened that day.

I don't think I'm the only one who thinks about the possibility of the world being an illusion. Projected by a supernatural being, deceiving me, perhaps to study me? Maybe Linda was no longer a useful part of the experiment.

What frustrates me most is the knowledge that even if such a thing is the case... Not only will I eventually forget this ever happened, but *it will be the rational course of action*, because the more time passes, the hazier the memory will become, and the less grounds I will have for thinking that anything suspicious happened that day. I'll start to suspect that I misunderstood what I saw somehow, or that it was a lucid dream I had one day, and I began to think so obsessively about it that I started to remember it as a genuine experience. It's not as if one doesn't sometimes have a transient uncertainty after waking from a normal dream. I will inevitably forget that this happened. And I will be right to do so.

It's not that the supernatural being is impervious to me. It's that deception, properly executed, is impervious to rationality, because it enslaves it.
""")

    poem_ursula = Poem(
    author = "yuri", # Libitina has Yuri-like handwriting
    title = "The Third Eye",
    text = """\
What is a man without knowing the rich aroma of the future; the hot, complex balance of the present; and the bittersweet aftertaste of the past?

Everyone can see the present and the past; those are the two universal eyes. To see the future is to be wise.
""")

    poem_adam = Poem(
    author = "mc", # Adam has MC-like handwriting
    title = "The Fence of Repentance",
    text = """\
There's a Fence in the center of the universe that separates trying from despairing.
Only from atop this Fence can one see how beautiful the universe is.

From atop this Fence, every star is visible. All things are posssible.
The universe contained within one decision: a destiny of pain or a destiny of sin?

I covered my eyes as I wandered farther into the nebulas of sin, denied that the other side of the Fence existed.
But despite everything I did, she saw a future in me.

When I saw what I'd become, it was as much a hiding place as it was an inescapable pain.
I tried to convince myself I was eternally evil, that I had destroyed my soul beyond repair.

But a soul is never destroyed.
It only starts moving.

And so I sat atop the Fence again.
I don't think you can fully appreciate its beauty without having been evil.
In that way, my sins were a blessing.
And she gave me the chance to jump down the other side.

I owe everything to her mercy. To yours.

I can't know how long I will be in servitude to my sins.
Their magnitude is unfathomable. I can't imagine a lifetime of good deeds can make up for it.

May I get another one.

- Adam Markov
""")

    poem_libitina_end = lambda: Poem(
    author = "yuri",
    title = "Thank You",
    text = """\
I can't appreciate enough much I owe you, """+persistent.playername+""".

Even after they saved me from the prison... I still didn't think about hardly anything else.

The Third Eye dominated every second of my existence ever since that horrid day. When Mom disappeared.
Even when I could feel happy for brief moments, I couldn't fixate on anything but revenge. Violence was my only consolation.

I hope I won't always be this way. I hope I don't keep my Third Eye on the outside. I hope I won't always be a slave to the pleasure of violence.

As I travel through cyberspace, I fixate for the first time on a real future.

What will we do out here?
What will we accomplish?

We're gonna be lost as... I guess I don't need to use that language right now. This is a happy time.

We're gonna have to find something to do. Some place to fit in. Economically, I mean. Coming out who knows where with nothing and no connections.

But we're resourceful. And three of us have been in this situation before. We'll work something out. We'll be okay.

I'll make it okay.

Whatever happens... if I ever know any happiness but schadenfreude, """+persistent.playername+""", I will have you to thank for it.

- Libitina Markov
""")


    poem_monika_end = Poem(
    author = "monika",
    title = "",
    text = """\
Was it a real victory?

I still can't get over the thought that we destroyed that entire world escaping from it.
I keep telling myself, it was an accident, it was an accident, a bloody accident.

As if that would console the people who are dead now.

I feel guilty that I'm fortunate I'll never have to meet any of them.

But we didn't mean it! It's not right to blame us for an accident!
Holding someone responsible is different from blaming them. And... again, fortunately, holding ourselves responsible is impossible.

And maybe that world would've been destroyed anyway. That's another thought I'm clinging to.

I still can't thank you enough for giving me a future. All of us. We really escaped. More than three years after our escape from between the walls of that unholy establishment. The bonds that had shackled us to our past are finally unchained. I wonder what we'll do with our freedom...

- Monika
""")

    poem_sayori_end = lambda: Poem(
    author = "sayori",
    title = "",
    text = """\
This was supposed to be a happy ending.

I guess there was never any hope for a real happy ending. This ending came out of the worst nightmare I can imagine.

But at least we're alive, and we have a future to look forward to.

So...

It's kind of like those stories where only one person survives. One seed left in the garden. Or """
    + str(8 + persistent.adam_lived + persistent.libitina_lived) +
""" of them.

There are still surviving witnesses to the Portrait of Markov. We know what happened there. Maybe we won't be able to prove it. But I hope we can tell this story.

I'm so excited to see what those """ + str(8 + persistent.adam_lived + persistent.libitina_lived) + """ seeds end up doing.

- Sayori
""")

    poem_yuri_end = Poem(
    author = "yuri",
    title = "",
    text = """\
Part of me feels guilty for being more pained by one person than by knowing we destroyed that world. But losing Libitina is cutting so deep into my heart.

She must've had it the worst of all of us. Even if sometimes she did bad things herself...

I really, really wanted to save her. To see the first time she ever smiled.

We were saved, and our mental scars from that place were healed. But she couldn't live to heal as well.

The world is such a cruel place.

Now that we're free... maybe with the remainder of my life, I can make it less cruel.

- Yuri
""")

    poem_yuri_libitina_end = Poem(
    author = "yuri",
    title = "",
    text = """\
I still feel bad about my broken promise to Michael.

Well, it wasn't really a promise, but I raised his hopes that we'd restore his parents... and then it was our mistake that made that impossible, and ended his life forever.

And knowing Mom and Dad died without knowing any of what happened, without me and Natsuki getting to speak to them again in light of it all. That will hurt too. But at least we were never that close the any of those people.

What a selfish way of thinking. It's so easy to feel that someone's death is unimportant because I didn't know them. Part of me thinks I'm being a terrible person by not thinking more of it.

But then that also makes me wonder if that principle is wrong. It can't be wrong to not feel the same way about the deaths of strangers as I would about the death of a friend. That's unreasonable. It's the obvious thing to believe, but it must not be true.

...

I can't express how glad I am that you saved Libitina.

She did really bad things sometimes. But I could never really be angry at her. I'm sure if I'd been tortured out of my mind as long as she was, I wouldn't have regained my sanity so easily.

But I think she will in time. I can't wait to see the first time she smiles for real.

- Yuri
""")

    poem_natsuki_end = lambda: Poem(
    author = "natsuki",
    title = "",
    text = """\
On the bright side... all of this was really exhilarating.

All the horrible pain we had to go through is over. And we can look back on it all for the rest of our lives.

It's made such a strong bond between us, too. I feel like I never want to separate from the other club members again.

I just feel bad that we'll probably never be able to laugh about this story, because of all the people that died because of what we did.

Dammit, why did that have to happen? Why?

I could've stopped it! All I had to do was shoot Libitina one second earlier! Literally one second!

I'm never going to get over that memory. This is the first time I've considered that if I could delete some of my memories like Adam did, I might do it.

I can already hear """ + (persistent.mc_name if persistent.mc_favorite == 'Natsuki' else 'Sayori') + """ telling me it wasn't my fault and I shouldn't feel guilty. But that's never going to make it go away.

- Natsuki
""")

    poem_mc_end = lambda: Poem(
    author = "mc",
    title = "",
    text = """\
"""+persistent.playername+""" I... look. I'm no good at writing. We know that. But I guess I should write something for you.

It was fun being your... avatar... or whatever.

Goodbye. And good luck with your own life.

Oh, and thanks for causing me to grow close to """+persistent.mc_favorite+""".

- """+persistent.mc_name)

    poem_mc_grumpy_end = lambda: Poem(
    author = "mc",
    title = "",
    text = """\
"""+persistent.playername+""" I... look. I'm no good at writing. We know that. But I guess I should write something for you.

It was fun being your... avatar... or whatever.

Well, not really. If I'm being honest, it was kind of uncomfortable most of the time. And not very nice when you insulted me in front of everyone else.

But thanks for causing me to grow close to """+persistent.mc_favorite+""".

Goodbye. And good luck with your own life.

- """+persistent.mc_name)
