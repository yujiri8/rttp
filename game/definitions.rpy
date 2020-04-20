define config.developer = True
define _dismiss_pause = config.developer
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default currentpos = 0 # Position in the music track.

python early:
    import singleton, os
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    renpy.music.register_channel("sound2", mixer="sfx", loop=False, tight=True)
    renpy.music.register_channel("sound3", mixer="sfx", loop=False, tight=True)
    renpy.music.register_channel("soundloop", mixer="sfx", loop=True, tight=True)

    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    def check_character(name):
        try: renpy.file("../characters/" + name + ".chr")
        except: return False
        return True

    def delete_character(name):
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass

    def restore_character(name):
        open(config.basedir + "/characters/" + name + ".chr", "wb").write(renpy.file(name + ".chr").read())

    def delete_all_characters():
        for file in os.listdir(config.basedir + '/characters'):
            if file.endswith('.chr'):
                os.remove(config.basedir + '/characters/' + file)

    def restore_part1_characters():
        for char in 'monika', 'sayori', 'yuri', 'natsuki', 'renier', 'linda': restore_character(char)

    def pause(time=None):
        global _windows_hidden
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False

    def autosave():
        renpy.take_screenshot()
        renpy.save("1-1", "autosave")

    # Used in chapter 8.
    def question_remains():
        return any((
            not persistent.asked_monika_about_player_choices,
            not persistent.asked_monika_about_time,
            not persistent.asked_monika_about_mc_time,
            not persistent.asked_monika_about_dreams,
            not persistent.asked_linda_about_powers,
            not persistent.asked_linda_renier_relationship,
            not persistent.asked_linda_about_porn,
            not persistent.asked_about_perception,
            not persistent.asked_natsuki_forgive_renier,
            not persistent.asked_about_mc_poems,
            not persistent.asked_yuri_about_cutting,
        ))

    def mc_dislike_player():
        return persistent.player_insult_mc_for_questioning_base64 +\
            (2 - persistent.player_allow_free_will_test)

    def ch22_libitina_has_gun():
        return persistent.threaten_libitina_to_come and \
            not persistent.threaten_libitina_to_save_natsuki_albert and \
            not persistent.make_libitina_return_gun

    def write_error_file():
        import string
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        name = ''.join(random.choice(chars) for i in range(10))
        with open(basedir + '/error-' + name + '.txt', 'w') as f:
            f.write(glitchtext(5000))


    def night(image): # By Koya-Sato
        return im.MatrixColor(image, im.matrix.tint(0.4, 0.4, 0.6))

# For making sure the player can't skip through a crash or do anything else that would kill the effect.
# I would have made this a Python function, but apparently Renpy script variables like allow_skipping can only be set from script.
label prevent_escape:
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
label prevent_skip:
    $ allow_skipping = False
    $ config.skipping = False
    $ config.allow_skipping = False
    $ _skipping = False
    $ quick_menu = False
    $ _dismiss_pause = False
    return

define audio.t1 = "<loop 22.073>bgm/1.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t5monika = "<loop 4.444>bgm/5_monika.ogg"
define audio.t5sayori = "<loop 4.444>bgm/5_sayori.ogg"
define audio.t5yuri = "<loop 4.444>bgm/5_yuri.ogg"
define audio.t5natsuki = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.punch = "mod_assets/sfx/punch.ogg"
define audio.stab = "sfx/stab.ogg"

define audio.glitch_basic = "sfx/s_kill_glitch1.ogg"
define audio.glitch_squarewave = "sfx/gnid.ogg"
define audio.glitch_monikapound = "sfx/monikapound.ogg"
define audio.glitch_mscare = "sfx/mscare.ogg"
define audio.glitch_flatline = "sfx/interference.ogg"
define audio.glitch_horror = "sfx/glitch1.ogg"
define audio.glitch_medium = "sfx/glitch2.ogg"
define audio.glitch_small = "sfx/glitch3.ogg"
define audio.glitch_creepypurr = "sfx/eyes.ogg"

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_s_kill = "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg house2 = "bg/house.jpg"
image bg kitchen = "bg/kitchen.png"
image bg space_room = "images/cg/monika/monika_room.png"

# Stuff for space
image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2
image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3
image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1
image maskb:
    "images/cg/monika/maskb.png"
    xtile 3
image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)
image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")
transform room_mask:
    size (320,180)
    pos (30,200)
transform room_mask2:
    size (320,180)
    pos (935,200)

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki vomit = "natsuki/vomit.png"

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

image y_kill = "cg/y_kill/1a.png"
image n_kill = "natsuki/ghost3.png"

define audio.yesnt = "mod_assets/music/yesnt.ogg"
define audio.yawa = "mod_assets/music/yawa.ogg"
define audio.serenity = "mod_assets/music/serenity.ogg"
define audio.beautiful_interior = "mod_assets/music/beautiful_interior.ogg"
define audio.third_eye = "mod_assets/music/third_eye.ogg"
define audio.our_reality = "mod_assets/music/our_reality.ogg"
define audio.determination = "<loop 27.83>mod_assets/music/description.mp3"
define audio.spooky = "mod_assets/music/spoopy_song_1.wav"
define audio.stab_once = "mod_assets/sfx/stab_once.ogg"
define audio.car_speed = "<from 10.5 to 13.5>mod_assets/sfx/car.ogg"
define audio.gunshot1 = "mod_assets/sfx/gunshot1.mp3"
define audio.gunshot2 = "mod_assets/sfx/gunshot2.mp3"
define audio.phone = "<from 1.4 to 3.3>mod_assets/sfx/phone.ogg"

image natsuki_house = "mod_assets/bg/natsuki_house.png"
image living_room = "mod_assets/bg/mc_living_room.png"
image courtyard = "mod_assets/bg/courtyard.png"
image city = "mod_assets/bg/city.jpg"
image city_night = "mod_assets/bg/city_night.jpg"
image city2 = "mod_assets/bg/city2.png"
image city3 = "mod_assets/bg/french_city.png"
image city_outskirts = "mod_assets/bg/city_outskirts.jpg"
image lobby = "mod_assets/bg/lobby.png"
image hospital_hall = "mod_assets/bg/hospital_hall.png"
image hospital_hall2 = "mod_assets/bg/hospital_hall2.png"
image hospital_room = "mod_assets/bg/hospital_room_day.png"
image hospital_room_dawn = "mod_assets/bg/hospital_room_dawn.png"
image hospital_room_night = "mod_assets/bg/hospital_room_night.png"
image facility_hall = "mod_assets/bg/cult_hallway_darker.webp"
image facility_hall_r = im.Flip("mod_assets/bg/cult_hallway_darker.webp", horizontal = True)
image vr_room = "mod_assets/bg/hospital_room2.png"
image facility_rift = "mod_assets/bg/facility_rift.png"
image facility_ruin = "mod_assets/bg/facility_ruin.png"
image path = "mod_assets/bg/path.jpg"
image village = "mod_assets/bg/village.jpg"
image forest = "mod_assets/bg/forest.png"
image road1 = "mod_assets/bg/road1.png"
image road1_night = "mod_assets/bg/road1_night.jpg"
image road2 = "mod_assets/bg/road2.png"
image street1 = "mod_assets/bg/street1.png"
image street2 = "mod_assets/bg/street2.jpg"
image street3 = "mod_assets/bg/street3.png"
image street4 = "mod_assets/bg/street4.jpg"
image michael_house = "mod_assets/bg/michael_house.jpg"
image computer_room = "mod_assets/bg/computer_room.png"
image hospital_outside = "mod_assets/bg/hospital_outside.jpg"
image warehouse_outside_day = "mod_assets/bg/warehouse_outside_day.png"
image warehouse_outside_night = "mod_assets/bg/warehouse_outside_night.png"
image warehouse_inside = "mod_assets/bg/temple1.jpg"
image warehouse_inside_rev = im.Flip("mod_assets/bg/temple1.jpg", horizontal = True)
image warehouse_inside_back = "mod_assets/bg/steam_machinery.jpg"
image office = "mod_assets/bg/office.jpg"
image forest_path = "mod_assets/bg/forest_path.jpg"
image driving = "mod_assets/bg/driving.jpg"
image driving_night = night("mod_assets/bg/driving.jpg")
image portal = "mod_assets/bg/portal.jpg"
image portal_half = "mod_assets/bg/portal_half.png"
# FUCK Renpy for this. Pure black is replaced with grey, so I had to make a black image with a tiny splot of dark grey somewhere.
image dark_overlay = "mod_assets/bg/black.png"
image red_overlay = Solid("f00")
image darkred_overlay = Solid("400")


define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('mc_name', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define r = DynamicCharacter('r_name', image='renier', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define l = DynamicCharacter('l_name', image='linda', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define b = DynamicCharacter('b_name', image='libitina', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define k = DynamicCharacter('k_name', image='markov', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define al = DynamicCharacter('al_name', image='albert', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kn = DynamicCharacter('k_name', what_prefix='{i}', what_suffix='{/i}', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ms = DynamicCharacter('ms_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define e = Character('Elyssa', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define d = DynamicCharacter('d_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define c = DynamicCharacter('c_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('a_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ma = Character('Maria', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define en = Character('Elyssa', what_prefix='{i}', what_suffix='{/i}', ctc="ctc", ctc_position="fixed")
define dn = Character('Daniel', what_prefix='{i}', what_suffix='{/i}', ctc="ctc", ctc_position="fixed")
define o = DynamicCharacter('o_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define dad = DynamicCharacter("dad_name", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mom = DynamicCharacter("mom_name", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ln = Character('Linda', what_prefix='{i}', what_suffix='{/i}', ctc="ctc", ctc_position="fixed")
define rn = Character('Renier', what_prefix='{i}', what_suffix='{/i}', ctc="ctc", ctc_position="fixed")

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default r_name = "Renier"
default l_name = "Linda"
default b_name = "Libitina"
default k_name = "Markov"
default al_name = "Albert"
default o_name = "???"
default ms_name = "Monika & Sayori"
default a_name = "Abbey"
default c_name = "Clare"
default d_name = "Daniel"
default dad_name = "Elyssa's Dad"
default mom_name = "Elyssa's Mom"

default currentuser = "Player"
default persistent.playername = "Player"
default persistent.mc_name = "MC"
# This is honestly just a shortcut. Not sure if worth.
default mc_name = "MC"
default name_entry = "" # Garbage variable for the name input screen; should never be referenced
default persistent.player_subj_pronoun = "he"
default persistent.player_obj_pronoun = "him"
default persistent.player_pos_pronoun = "his"
default persistent.player_copula_pos_pronoun = "his"

define renier_unbase64 = """zlndix, tazm cre phjx alippm

pvz jgzlrw

crez rmk cupj swwe

ystk fbkkhd mywkmaltyo p tvyz pobhsrywrgh"""

define renier_decrypted = """renier, camt you here meeeee

ive failed

your our only hope

dont forget everything i taut yoooooooooo"""

# Story persistent vars
default persistent.newgame = 0 # The game number the player will start next, or 'glitch' or 'deny' if they can't.
default persistent.pom_menu = False # Whether to show the POM menu.
default persistent.menu_hide_monika = False # Set in chapter 13.
# Flags set throughout the plot just here so a default value is set if I skip ahead for testing.
default persistent.mc_awakened = False
default persistent.monika_request_shutdown = False
default persistent.mc_request_shutdown = False
default persistent.mc_survive_shutdown = False
default persistent.player_insult_mc_for_questioning_base64 = False # Chapter 5.
default persistent.sayori_reset_ynr = False # Chapter 6.
default persistent.linda_in_void = False # Chapter 6.
default persistent.player_allow_free_will_test = 0 # Chapter 8. 0 means the test wasn't performed; 1 means the player objected but was persuaded; 2 means the player didn't object.
default persistent.player_guilt_dokis = [0, 0] # Chapters 8 and 20.
default persistent.player_speculate_on_past = None # Chapter 8 - "refuse", "fake", or "real".
default persistent.player_support_renier_experiment = 0 # Chapter 9.
default persistent.experiment_over = False # Chapter 9.
default save_is_before_experiment = False # Chapter 9.
default persistent.player_support_escape_plan = 0 # Chapter 12. 0 means the player never agreed, 1 means the player initially objected but was persuaded, and 2 means the player didn't object.
default persistent.suggest_set_name = False # Chapter 13.
default persistent.player_early_theorize_elyssa_is_yuri = False # Chapter 14.
default persistent.player_reject_sayori_sacrifice = False # Chapter 14.
default persistent.player_guilt_trip_sayori = 0 # Chapter 14.
default persistent.player_pacifist = 0 # First in Chapter 15.
default persistent.player_advocate_mercy = [0, 0] # First in ch15, second in ch23.
default persistent.shutdown_in_pom = False # Chapter 20.
# chapter 8 questions
default persistent.asked_monika_about_player_choices = False
default persistent.asked_monika_about_time = False
default persistent.asked_monika_about_mc_time = False
default persistent.asked_monika_about_dreams = False
default persistent.asked_about_perception = False
default persistent.asked_linda_about_powers = False
default persistent.asked_linda_about_porn = False
default persistent.asked_linda_renier_relationship = False
default persistent.player_suggest_linda_natsuki_mom = 0 # can raise to 2 in ch14, if it was set before.
default persistent.asked_natsuki_forgive_renier = False
default persistent.asked_yuri_about_cutting = False
default persistent.asked_about_mc_poems = False
# Part 3
default persistent.ch22_monika_request_shutdown = False
default persistent.ch22_shutdown = False
default persistent.tried_reset_pom = False
default persistent.threaten_libitina_to_save_natsuki_albert = False
default persistent.threaten_libitina_to_come = False
default persistent.make_libitina_return_gun = None # for this one, None means she gave it back willingly
default persistent.suggest_albert_stay = False
default persistent.ch22_kill_guard = None # holds the name of the character if someone did
default persistent.contacted = set()
# ending
default persistent.adam_lived = None
default persistent.libitina_lived = None
