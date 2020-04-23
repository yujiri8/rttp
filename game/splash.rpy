init python:
    import datetime
    menu_trans_time = 1
    splash_message_default = "This game is not suitable for children\nor those who are easily disturbed."

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image pom_menu = "mod_assets/bg/eye.png"

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "mod_assets/gui/ddmc_logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

#image tos = "bg/warning.png"
#image tos2 = "bg/warning2.png"

image tos = Fixed(
    "white",
    "menu_art_y_ghost",
    "menu_art_n_ghost",
    "menu_art_s_ghost",
    "menu_art_m_ghost",
)


label splashscreen:

    # A script that converts saves from part 1 or part 2 to be part 3-compatible.
    call update_to_part3

    # Special things for the mod, since it deals with the game being turned off.
    $ persistent.awaiting_shutdown = False
    # This one has to be handled here, because it doesn't work the same way as other shutdowns and autoloads.
    if persistent.can_save_libitina:
        call save_libitina

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass
        else:
            try:
                user = os.environ.get("USER")
                if user: currentuser = user
            except:
                pass


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "This is a Doki Doki Literature Club fan game that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed."
        "You can download Doki Doki Literature Club at: {a=https://ddlc.moe}https://ddlc.moe{/a}"
        menu:
            "Do NOT proceed unless you have finished Doki Doki Literature Club."
            "I have finished Doki Doki Literature Club.":
                pass
        "Excellent."
        "This mod also assumes that you are aware of the many secrets found in the game files of the base game, as the story builds on them."
        "If not, they can be found at the fandom wiki articles on: {a=https://doki-doki-literature-club.fandom.com/wiki/Easter_Eggs}the general list of easter eggs{/a}, {a=https://doki-doki-literature-club.fandom.com/wiki/Natsuki/Poems}Natsuki's poems{/a}, and {a=https://doki-doki-literature-club.fandom.com/wiki/Yuri/Poems}Yuri's poems{/a}."
        menu:
            "Have you seen them?"
            "Yes.":
                pass
        call setup
        $ persistent.first_run = True
        jump start

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload

    $ config.allow_skipping = False

    show white
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    if persistent.pom_menu:
        stop music
        $ config.main_menu_music = None
    return

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ style.say_dialogue = style.normal
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
