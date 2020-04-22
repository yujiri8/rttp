label update_to_part3:
    python:
        # part 1 -> part 2
        if persistent.player_claim_all_time is not None:
            persistent.player_guilt_dokis[0] = persistent.player_claim_all_time
            del persistent.player_claim_all_time
        # -> part 3
        if persistent.post_escape_plan:
            persistent.menu_hide_monika = True # ch13
            persistent.newgame = 'glitch'
            if persisent.escape_ddlc:
                persistent.newgame = 'deny'
                persistent.pom_menu = True
    return
