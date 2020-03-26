init python:
    for i in renier_images():
        renpy.image('renier ' + i, def_renier_pose(i))

python early:
    def def_renier_pose(pose):
        basepath = "mod_assets/renier/"
        inputs = ((960, 960),)
        if pose[0] != 'r':
            # Pad 1 to make the length consistent.
            pose = ' ' + pose
        # So far, just ignore the u.
        # Arms folded.
        if pose[2] == 'f':
            inputs += ((0, 0), basepath+"1_folded/u_def.png")
            # This time we pad if it is found, because having the f makes the tag shorter.
            # We pad between 0 and 1 instead of at the beginning for compatibility with reversal.
            pose = pose[0] + ' ' + pose[1:]
        else:
            # Put the right half image first because his left body image with the bottle has to be able to overlap it.
            inputs += ((0, 0), basepath+"1_uniform/2_body_right/" + pose[3] + ".png")
            inputs += ((0, 0), basepath+"1_uniform/1_body_left/" + pose[2] + ".png")
        # Face.
        inputs += ((0, 0), basepath+"2_face/1_main/" + pose[4] + ".png")
        inputs += ((0, 0), basepath+"2_face/2_mouth/" + pose[5] + ".png")
        if len(pose) >= 7 and pose[6] != "b":
            inputs += ((0, 0), basepath+"2_face/3_eyes/" + pose[6] + ".png")
        if pose[-1] == 'b':
            inputs += ((0, 0), basepath+"2_face/4_cheeks/1.png")

        if pose[0] != 'r':
            return im.Composite(*inputs)
        else:
            return im.Flip(im.Composite(*inputs), horizontal=True)

    def renier_images():
        for prefix in 'u11', 'u12', 'u13', 'u21', 'u22', 'u23', 'ub1', 'ub2', 'ub3', 'uf':
            for main in '123456789a':
                for mouth in '1234567':
                    for eye in '', '1', '2', '3':
                        for cheek in '', 'b':
                            for reverse in 'r', '':
                                yield reverse + prefix + main + mouth + eye + cheek
