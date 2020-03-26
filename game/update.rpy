label update_to_part2:
    python:
        if persistent.player_claim_all_time is not None:
            persistent.player_guilt_dokis[0] = persistent.player_claim_all_time
            del persistent.player_claim_all_time
    return
