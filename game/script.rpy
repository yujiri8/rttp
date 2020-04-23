label start:
    $ persistent.autoload = None # empty this at the start of a new game just incase
    $ mc_name = persistent.mc_name

    if persistent.newgame == 1:
        jump game2
    elif persistent.newgame == 2:
        jump game3
    elif persistent.newgame == 3:
        jump game4
    elif persistent.newgame == 4:
        if persistent.pom_menu:
            jump escale_ddlc
        jump game5
    elif persistent.newgame == 5:
        jump game6

    label game1:
        call chapter1
        call chapter2

    label game2:
        call chapter3
    label after_pom_crash:
        $ mc_name = persistent.mc_name
        call chapter3_2
        call chapter4
        call chapter5
    label after_linda_crash:
        $ mc_name = persistent.mc_name
        call chapter6

    label game3:
        call chapter7
        call chapter8
        call chapter9
    label save_scum_experiment:
        $ mc_name = persistent.mc_name
        call chapter10

    label game4:
        call chapter11

    label game5:
        call chapter12
    label after_delete_script:
        $ mc_name = persistent.mc_name
        call chapter13
    label part2_skip_point:
        call chapter14
        call chapter15
        call chapter16
    label mc_in_void:
        $ mc_name = persistent.mc_name
        call chapter16_2
        call chapter17

    label escape_ddlc:
        $ mc_name = persistent.mc_name
        call chapter18
        call chapter19
        call chapter20
        call chapter21

    # this is also the part 3 skip point
    label after_markov_returns:
        $ mc_name = persistent.mc_name
        call chapter22

    label game6:
        call chapter23
        call chapter24
        call chapter25
        call chapter26
    label after_return_to_ddlc:
        $ mc_name = persistent.mc_name
        $ k_name = "Adam"
        call chapter26_2
        call chapter27
        call chapter28
        call chapter29
    label shutdown_to_save_pom:
        $ mc_name = persistent.mc_name
        $ k_name = "Adam"
        call chapter29_2
        call credits
    return
