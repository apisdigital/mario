def on_a_pressed():
    if mario.vy == 0:
        mario.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def mov1():
    global movd, movi
    if mario.vy == 0:
        if controller.right.is_pressed() and movd == 0:
            animation.run_image_animation(mario,
                [img("""
                        . . . . . . 2 2 2 2 2 . . . . . 
                                        . . . . . 2 2 2 2 2 2 2 2 2 . . 
                                        . . . . . e e e d d e d . . . . 
                                        . . . . e d e d d d e d d d . . 
                                        . . . . e d e e d d d e d d d . 
                                        . . . . e e d d d d e e e e . . 
                                        . . . . . . d d d d d d . . . . 
                                        . . . . 2 2 8 8 2 2 8 . . . . . 
                                        . . . 2 2 2 2 8 8 8 8 8 . . . . 
                                        . . . 2 2 2 2 8 8 8 8 8 . . . . 
                                        . . . . 8 2 2 1 8 8 5 8 . . . . 
                                        . . . . 8 8 1 1 1 8 8 8 . . . . 
                                        . . . . 8 8 8 1 8 8 8 8 . . . . 
                                        . . . . . 8 8 8 8 8 8 . . . . . 
                                        . . . . . . 8 e e e . . . . . . 
                                        . . . . . . . e e e e e . . . .
                    """),
                    img("""
                        . . . . . . 2 2 2 2 2 . . 1 1 1 
                                        . . . . . 2 2 2 2 2 2 2 2 2 1 1 
                                        . . . . . e e e d d e d . 2 2 2 
                                        . . . . e d e d d d e d d d 2 2 
                                        . . . . e d e e d d d e d d d 2 
                                        . . . . e e d d d d e e e e 2 . 
                                        . . . . . . d d d d d d d 2 . . 
                                        . . 2 2 2 2 2 8 2 2 2 8 2 . . . 
                                        . 2 2 2 2 2 2 2 8 2 2 2 8 . . . 
                                        1 1 2 2 2 2 2 2 8 8 8 8 8 . . . 
                                        1 1 1 . . 8 2 8 8 8 5 8 5 . . e 
                                        . 1 . . . 8 8 8 8 8 8 8 8 . . e 
                                        . . . e . 8 8 8 8 8 8 8 8 8 e e 
                                        . . e e e 8 8 8 8 8 8 8 8 8 e e 
                                        . e e e 8 8 8 8 8 8 8 . . . . . 
                                        . e . . 8 8 8 8 . . . . . . . .
                    """)],
                100,
                True)
            movd = 1
            movi = 0
        if controller.left.is_pressed() and movi == 0:
            animation.run_image_animation(mario, assets.animation("""
                mario iz
            """), 100, True)
            movi = 1
            movd = 0
        if not (controller.left.is_pressed()) and not (controller.right.is_pressed()) and (movd == 1 or movi == 1):
            animation.stop_animation(animation.AnimationTypes.ALL, mario)
            if movd == 1:
                mario.set_image(img("""
                    . . . . . 2 2 2 2 2 . . . . . . 
                                        . . . . 2 2 2 2 2 2 2 2 2 . . . 
                                        . . . . e e e d d e d . . . . . 
                                        . . . e d e d d d e d d d . . . 
                                        . . . e d e e d d d e d d d . . 
                                        . . . e e d d d d e e e e . . . 
                                        . . . . . d d d d d d d . . . . 
                                        . . . . 2 2 8 2 2 2 2 . . . . . 
                                        . . . 2 2 2 8 2 2 8 2 2 2 . . . 
                                        . . 2 2 2 2 8 8 8 8 2 2 2 2 . . 
                                        . . 1 1 2 8 5 8 8 5 8 2 1 1 . . 
                                        . . 1 1 1 8 8 8 8 8 8 1 1 1 . . 
                                        . . 1 1 8 8 8 8 8 8 8 8 1 1 . . 
                                        . . . . 8 8 8 . . 8 8 8 . . . . 
                                        . . . e e e . . . . e e e . . . 
                                        . . e e e e . . . . e e e e . .
                """))
            else:
                mario.set_image(img("""
                    . . . . . . 2 2 2 2 2 . . . . . 
                                        . . . 2 2 2 2 2 2 2 2 2 . . . . 
                                        . . . . . d e d d e e e . . . . 
                                        . . . d d d e d d d e d e . . . 
                                        . . d d d e d d d e e d e . . . 
                                        . . . e e e e d d d d e e . . . 
                                        . . . . d d d d d d d . . . . . 
                                        . . . . . 2 2 2 2 8 2 2 . . . . 
                                        . . . 2 2 2 8 2 2 8 2 2 2 . . . 
                                        . . 2 2 2 2 8 8 8 8 2 2 2 2 . . 
                                        . . 1 1 2 8 5 8 8 5 8 2 1 1 . . 
                                        . . 1 1 1 8 8 8 8 8 8 1 1 1 . . 
                                        . . 1 1 8 8 8 8 8 8 8 8 1 1 . . 
                                        . . . . 8 8 8 . . 8 8 8 . . . . 
                                        . . . e e e . . . . e e e . . . 
                                        . . e e e e . . . . e e e e . .
                """))
            movd = 0
            movi = 0
    elif controller.left.is_pressed():
        mario.set_image(assets.image("""
            salto i
        """))
        movi = 1
        movd = 0
    else:
        mario.set_image(assets.image("""
            salto d
        """))
        movd = 1
        movi = 0
movi = 0
movd = 0
mario: Sprite = None
effects.clouds.start_screen_effect()
scene.set_background_color(9)
tiles.set_tilemap(tilemap("""
    level1
"""))
mario = sprites.create(img("""
        . . . . . 2 2 2 2 2 . . . . . . 
            . . . . 2 2 2 2 2 2 2 2 2 . . . 
            . . . . e e e d d 1 d . . . . . 
            . . . e d e d d d f d d d . . . 
            . . . e d e e d d d e d d d . . 
            . . . e e d d d d e e e e . . . 
            . . . . . d d d d d d d . . . . 
            . . . . 2 2 8 2 2 2 2 . . . . . 
            . . . 2 2 2 8 2 2 8 2 2 2 . . . 
            . . 2 2 2 2 8 8 8 8 2 2 2 2 . . 
            . . 1 1 2 8 5 8 8 5 8 2 1 1 . . 
            . . 1 1 1 8 8 8 8 8 8 1 1 1 . . 
            . . 1 1 8 8 8 8 8 8 8 8 1 1 . . 
            . . . . 8 8 8 . . 8 8 8 . . . . 
            . . . e e e . . . . e e e . . . 
            . . e e e e . . . . e e e e . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(mario)
mario.ay = 500
controller.move_sprite(mario, 100, 0)

def on_forever():
    global movd, movi
    if controller.right.is_pressed() and movd == 0:
        animation.run_image_animation(mario,
            [img("""
                    . . . . . . 2 2 2 2 2 . . . . . 
                                . . . . . 2 2 2 2 2 2 2 2 2 . . 
                                . . . . . e e e d d e d . . . . 
                                . . . . e d e d d d e d d d . . 
                                . . . . e d e e d d d e d d d . 
                                . . . . e e d d d d e e e e . . 
                                . . . . . . d d d d d d . . . . 
                                . . . . 2 2 8 8 2 2 8 . . . . . 
                                . . . 2 2 2 2 8 8 8 8 8 . . . . 
                                . . . 2 2 2 2 8 8 8 8 8 . . . . 
                                . . . . 8 2 2 1 8 8 5 8 . . . . 
                                . . . . 8 8 1 1 1 8 8 8 . . . . 
                                . . . . 8 8 8 1 8 8 8 8 . . . . 
                                . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . . . . 8 e e e . . . . . . 
                                . . . . . . . e e e e e . . . .
                """),
                img("""
                    . . . . . . 2 2 2 2 2 . . 1 1 1 
                                . . . . . 2 2 2 2 2 2 2 2 2 1 1 
                                . . . . . e e e d d e d . 2 2 2 
                                . . . . e d e d d d e d d d 2 2 
                                . . . . e d e e d d d e d d d 2 
                                . . . . e e d d d d e e e e 2 . 
                                . . . . . . d d d d d d d 2 . . 
                                . . 2 2 2 2 2 8 2 2 2 8 2 . . . 
                                . 2 2 2 2 2 2 2 8 2 2 2 8 . . . 
                                1 1 2 2 2 2 2 2 8 8 8 8 8 . . . 
                                1 1 1 . . 8 2 8 8 8 5 8 5 . . e 
                                . 1 . . . 8 8 8 8 8 8 8 8 . . e 
                                . . . e . 8 8 8 8 8 8 8 8 8 e e 
                                . . e e e 8 8 8 8 8 8 8 8 8 e e 
                                . e e e 8 8 8 8 8 8 8 . . . . . 
                                . e . . 8 8 8 8 . . . . . . . .
                """)],
            100,
            True)
        movd = 1
    if controller.left.is_pressed() and movi == 0:
        animation.run_image_animation(mario, assets.animation("""
            mario iz
        """), 100, True)
        movi = 1
    if not (controller.right.is_pressed()) and not (controller.left.is_pressed()) or controller.right.is_pressed() and controller.left.is_pressed():
        animation.stop_animation(animation.AnimationTypes.ALL, mario)
        if movi == 1:
            mario.set_image(img("""
                . . . . . . 2 2 2 2 2 . . . . . 
                                . . . 2 2 2 2 2 2 2 2 2 . . . . 
                                . . . . . d e d d e e e . . . . 
                                . . . d d d e d d d e d e . . . 
                                . . d d d e d d d e e d e . . . 
                                . . . e e e e d d d d e e . . . 
                                . . . . d d d d d d d . . . . . 
                                . . . . . 2 2 2 2 8 2 2 . . . . 
                                . . . 2 2 2 8 2 2 8 2 2 2 . . . 
                                . . 2 2 2 2 8 8 8 8 2 2 2 2 . . 
                                . . 1 1 2 8 5 8 8 5 8 2 1 1 . . 
                                . . 1 1 1 8 8 8 8 8 8 1 1 1 . . 
                                . . 1 1 8 8 8 8 8 8 8 8 1 1 . . 
                                . . . . 8 8 8 . . 8 8 8 . . . . 
                                . . . e e e . . . . e e e . . . 
                                . . e e e e . . . . e e e e . .
            """))
        if movd == 1:
            mario.set_image(img("""
                . . . . . 2 2 2 2 2 . . . . . . 
                                . . . . 2 2 2 2 2 2 2 2 2 . . . 
                                . . . . e e e d d e d . . . . . 
                                . . . e d e d d d e d d d . . . 
                                . . . e d e e d d d e d d d . . 
                                . . . e e d d d d e e e e . . . 
                                . . . . . d d d d d d d . . . . 
                                . . . . 2 2 8 2 2 2 2 . . . . . 
                                . . . 2 2 2 8 2 2 8 2 2 2 . . . 
                                . . 2 2 2 2 8 8 8 8 2 2 2 2 . . 
                                . . 1 1 2 8 5 8 8 5 8 2 1 1 . . 
                                . . 1 1 1 8 8 8 8 8 8 1 1 1 . . 
                                . . 1 1 8 8 8 8 8 8 8 8 1 1 . . 
                                . . . . 8 8 8 . . 8 8 8 . . . . 
                                . . . e e e . . . . e e e . . . 
                                . . e e e e . . . . e e e e . .
            """))
        movd = 0
        movi = 0
forever(on_forever)
