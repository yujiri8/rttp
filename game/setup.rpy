label setup:
        call screen name_input(message="Then now is the time to name MC.")
        $ mc_name = persistent.mc_name = _return
        "Now you need to answer a few questions about your playthrough of the original DDLC."
        "(It will be assumed that [mc_name] took his favorite girl's side in the argument on Day 2, and that he confessed love to Sayori if and only if she was his favorite.)"
        menu:
                "Who is [mc_name]'s favorite girl?"
                "Sayori":
                        $ persistent.mc_favorite = 'Sayori'
                "Yuri":
                        $ persistent.mc_favorite = 'Yuri'
                "Natsuki":
                        $ persistent.mc_favorite = 'Natsuki'
        menu:
                "Who is [mc_name]'s least favorite girl?"
                "Sayori" if persistent.mc_favorite != "Sayori":
                        $ persistent.mc_least_favorite = 'Sayori'
                "Yuri" if persistent.mc_favorite != "Yuri":
                        $ persistent.mc_least_favorite = 'Yuri'
                "Natsuki" if persistent.mc_favorite != "Natsuki":
                        $ persistent.mc_least_favorite = 'Natsuki'
        return
