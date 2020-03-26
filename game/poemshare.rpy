label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=inst(p11), paper=None):
    if poem == None:
        return
    play sound page_turn
    if music:
        $ currentpos = get_pos()
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
        elif poem.author == "mc": # MC's poems play his favorite girl's music.
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + persistent.mc_favorite.lower() + ".ogg"
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide
    $ renpy.game.preferences.afm_enable = False
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    with Dissolve(1)
    $ config.skipping = False
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem with Dissolve(.5)
    window auto
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return

image paper = "images/bg/poem.jpg"
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "images/bg/poem-glitch1.png"
image paper_glitch2:
    "images/bg/poem-glitch2.png"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat

transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            if currentpoem.yuri_2:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.yuri_3:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
            else:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
        elif currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        elif currentpoem.author == "natsuki":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
        elif currentpoem.author == "monika":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
        elif currentpoem.author == "mc":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "mc_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

style poem_vbox:
    xalign 0.5

style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280

style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    ysize 700

style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style yuri_text_2:
    font "gui/font/y2.ttf"
    size 40
    color "#000"
    outlines []

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []

style mc_text:
    font "mod_assets/Inkfree.ttf"
    size 26
    color "#000"
    outlines []
