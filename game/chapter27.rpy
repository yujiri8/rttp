# Adam should still be terrified of being killed afterward.
label chapter27:
    scene road1_night with dissolve_scene_full
    "We drive back to the Markovs' hometown."
    # Maybe Adam doesn't make it before bleeding out so they pull over along the way to insert and extract.

    call updateconsole("def insert_adam():\n  sleep(60)\n  admin.jail(ddlc, adam)\n\ninsert_adam()")
    return
