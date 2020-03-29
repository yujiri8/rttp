# Adam should still be terrified of being killed afterward.
label chapter27:
    scene road1_night with dissolve_scene_full
    "We park a ways out of the city, as Adam directed."
    "I get out of the vehicle."
    mc "Adam!"
    mc "We're here like you said!"
    mc "Wanna come ambush us?!?"
    "..."
    "Another car pulls up behind ours."
    "He's here."
    "He comes out."
    show markov uf423 at foc(p11)
    k "Hello."
    show markov at std
    "Just seeing him makes my blood boil."
    ""


    show markov at foc
    k "It's time for me to go save Monika."
    call updateconsole("def insert_adam():\n  sleep(60)\n  admin.jail(ddlc, adam)\n\ninsert_adam()")
    k "I'm ready."
    k "Swing the pipe or whatever."
    show markov at std
    r "I don't have the pipe anymore."
    # Maybe Adam brought a pipe?
    return
