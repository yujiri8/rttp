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
