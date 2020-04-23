transform credits_scroll:
    xcenter 0.5
    yoffset 740
    linear 70 yoffset -4500

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5

image credits_text = ParameterizedText(style="credits_text")

label credits:
    play music determination
    scene black with dissolve_scene
    show credits_text credits at credits_scroll
    $ persistent.autoload = 'eternal_poem'
    pause 60
    stop music fadeout 10
    pause 10
label eternal_poem:
    call showpoem(poem = poem_monika_end, music = False)
    call showpoem(poem = poem_sayori_end(), music = False)
    if persistent.libitina_lived:
        call showpoem(poem = poem_yuri_libitina_end, music = False)
    else:
        call showpoem(poem = poem_yuri_end, music = False)
    call showpoem(poem = poem_natsuki_end(), music = False)
    if mc_dislike_player() < 2:
        call showpoem(poem = poem_mc_end(), music = False)
    else:
        call showpoem(poem = poem_mc_grumpy_end(), music = False)
    if persistent.libitina_lived:
        call showpoem(poem = poem_libitina_end(), music = False)
    if persistent.adam_lived:
        call showpoem(poem = poem_adam, music = False)
    $ renpy.quit()

define credits = """Return To The Portrait


By Yujiri (yujiri.xyz)


Contributors:


u/main_gi / main_gi#2358
Tremendous story help, description.mp3, and lots of proofreading and testing

231#1345
Helped plan part 3, found bugs

u/15LarueA / PluralRoses#0136
Linda, Libitina, Adam, and Albert sprites
Warehouse water pit room

u/SovietSpartan / SovietSpartan#5727
Renier sprites

TomTC (deviantart) / TommyGun#7531
Yuri forest, warehouse exterior, cult facility backgrounds

u/AgentGold
The Dynamic Pose Tool, which made my life 10x easier
Also:
  u/LunaticRabbit
  u/smearglexd
  u/TheRadioactive4
  Koya-Sato

Jan Hehr
Yuri and Natsuki's date tracks, the Third Eye theme, and Our Reality
(originally for Monika Before Story OST)

Dimas#4872
Glitch theme 'yesnt'

OliverCNorton#4433
Calm music 'yawa'

Kevin MacLeod
Lament music 'Past Sadness'

LeoDeCraprio#4239
Calm music 'Main Street Stroll'

Meddy-sin
(Amy sprites) used as Yuri's mom

Cyrke#8043, u/Cylent-Nite
Eric (Michael's brother) sprites

Speißer#7316
The portal

Obsoletovsky (DDNP)
Hospital hallway, hospital lobby, french_city.png

Nuxill#7870
Original MC's living room

u/yagamirai10
Background edits: MC's living room, school courtyard, street1.png

ari1192
Cult facility hallway

Childish-N
original work on MC sprites, both MC and Michael

u/GanstaKingOfSA
Editing casual MC outfit

Akame#8940
Natsuki's computer room

SpringingTraps#5243
Stab wound edited onto Adam

u/SamCapener
Comissioning Yuri's forest artwork and letting me use it for free :)

u/chronoshag
Comissioning the original Dadsuki sprites and letting me use them for free :)

Haikei Frame
Warehouse back

Uncle Mugen
Many backgrounds

Kimagure After
Many backgrounds

Pexels (pixabay)
Driving image

welcomia (Shutterstock)
City outskirts

All Sounds (youtube channel)
Car sound, distributing gun sounds

ShawnyBoy (Freesound)
Single gunshot sound

morganpurkis (Freesound)
Multiple gunshot sound

PictorialEnglish (youtube)
Phone ring sound

u/wingedterra147
Testing, bug reports and feedback on part 1

More details and URLs in credits.txt





Special thanks:

Dan Salvato, for creating the best story I've ever seen.
"""
