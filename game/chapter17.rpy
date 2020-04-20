label chapter17:
    show linda at foc
    l 114111 "Thank you all."
    show linda at std
    show yuri at foc zorder 4
    y u125114 "Just incase we keep these when we leave this world..."
    "Yuri goes to her schoolbag and gets the two knives she had with her."
    y "One of us with a Third Eye should be holding each of these."
    show yuri at std
    "She gives the second to Renier."
    show renier at foc zorder 5
    r ru2113 "Good idea..."
    show renier at std
label chapter17_escape:
    show linda at foc zorder 6
    call updateconsole("import admin")
    call updateconsole("challenge = admin.expose_destination_file()")
    call updateconsole("signature = pgp_sign(challenge, markov_key)")
    call updateconsole("admin.complete_action(signature)", "Virtual Reality Viewport destination\nfile exposed.")
    python:
        with open(config.basedir + '/DESTINATION.txt', 'w') as f:
            f.write("/jails/doki_doki_literature_club")
    l "The file should be exposed now."
    l "[persistent.playername]..."
    l "I need you to wait until we leave..."
    l "... and then turn off the game, change the text in the file to just \"/\", and reboot the game."
    l "Are you ready?"
    show linda at std
    menu:
        " "
        "Yes.":
            pass
    show linda at foc
    l "Okay..."
    l 114112 "Here we go."
    call hideconsole
    $ consolehistory = []
    call updateconsole("def extract(char):\n" +\
        "  challenge = admin.extract_character(char)\n" +\
        "  signature = pgp_sign(challenge, markov_key)\n" +\
        "  admin.complete_action(signature)\n" +\
        "\n" +\
        "for char in (sayori, natsuki, yuri,\n" +\
        "    renier, "+mc_name.lower()+", linda):\n" +\
        "  extract(char)")
    hide sayori
    call updateconsole('', "Sayori extracted")
    hide natsuki
    call updateconsole('', "Natsuki extracted")
    hide yuri
    call updateconsole('', "Yuri extracted")
    hide renier
    call updateconsole('', "Renier extracted")
    scene black
    $ persistent.escape_ddlc = True
    $ persistent.autoload = 'chapter17_portal'
    while True:
        "{cps=200}Fatal error: player character missing.{/cps}"

label chapter17_portal:
    scene black
    python:
        correct = False
        try:
            with open(config.basedir + '/DESTINATION.txt') as f:
                correct = f.read().strip() == '/'
        except: pass
    if correct:
        jump escape_ddlc
    else:
        'Invalid destination.'
        $ renpy.quit()
