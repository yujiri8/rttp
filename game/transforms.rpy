define p11 = 640
define p21 = 400
define p22 = 880
define p31 = 240
define p33 = 1040
define p41 = 200
define p42 = 493
define p43 = 786
define p44 = 1080
define p51 = 180
define p52 = 410
define p54 = 870
define p55 = 1100
define p61 = 160
define p62 = 352
define p63 = 544
define p64 = 736
define p65 = 928
define p66 = 1120

# Basic transform used for appearing or moving, unfocused or unfocusing.
transform std(x=None, z=0.80):
    subpixel True
    on show:
        yanchor 1.0 ypos 1.03
        zoom z*0.95 alpha 0.0
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00 yoffset 0 yanchor 1.0 ypos 1.03
        easein .25 xcenter x zoom z*1.00

# Pop in instantly with no easein.
transform inst(x=None, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

# Changing x position without changing anything else.
transform x(x, z=0.80):
    alpha 1.00
    easein .25 xcenter x

# Focus - the character zooms in slightly.
transform foc(x=None, z=0.80, a=0.0):
    subpixel True
    on show:
        yanchor 1.0 ypos 1.03
        zoom z*0.95 alpha a
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
    on replace:
        alpha 1.00 yoffset 0
        easein .25 xcenter x zoom z*1.05

# Pop in focused instantly with no easein.
transform foci(x=None, z=0.80):
    xcenter x yoffset 0 zoom z*1.05 alpha 1.00 yanchor 1.0 ypos 1.03

# Move instantly and focus - used for overcoming Renpy's transform issues.
transform xif(x=640, z=0.80):
    alpha 1.00 yoffset 0 xcenter x
    easein .25 zoom z*1.05

# Move instantly and unfocus - used for overcoming Renpy's transform issues.
transform xis(x=640, z=0.80):
    alpha 1.00 yoffset 0 xcenter x
    easein .25 zoom z*1.00

transform sink:
    easein .5 ypos 1.06

transform unsink:
    easein .15 ypos 1.03

# A longer unsink, used when sinking represented kneeling.
transform unkneel:
    easein .5 ypos 1.03

# Unfocus only.
transform uf(z=0.80):
    easein .25 zoom z*1.00

# Appear/unfocus instantly and hop.
transform hop(x=None, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

# Appear/focus instantly and hop.
transform hopfoc(x=None, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

transform dip(z=0.80):
    yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

transform leftinfoc(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .25 xcenter x

transform rightin(x=640, z=0.80):
    # You can't mix int and float arguments to the same parameter in the same transform, so I use the absolute screen size, 1280, and add 300.
    xcenter 1580 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

transform rightinfoc(x=640, z=0.80):
    xcenter 1580 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .25 xcenter x

transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300
transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 1580

transform face(z=0.80, y=500, x=None):
    subpixel True
    xcenter x
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform unface(z=0.80, x=None):
    subpixel True
    parallel:
        easein .25 xcenter x zoom z*1.00
    parallel:
        easein .15 yoffset 0 ypos 1.03

transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

define dissolve = Dissolve(0.25)
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)

define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

image vignette:
    truecenter
    "images/bg/vignette.png"

transform flashback_horror(z=1.1):
    truecenter
    zoom z
    parallel:
        easeout_bounce 0.2 xpos 0.55
        easeout_bounce 0.2 xpos 0.45
        repeat
    parallel:
        easeout_bounce 0.33 ypos 0.55
        easeout_bounce 0.33 ypos 0.45
        repeat

transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat
