controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mario.vy == 0) {
        salto = 1
        mario.vy = -200
    }
})
function mov1 () {
    if (salto == 0) {
        if (controller.right.isPressed() && movd == 0) {
            animation.runImageAnimation(
            mario,
            [img`
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
                `,img`
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
                `],
            100,
            true
            )
            movd = 1
            movi = 0
        }
        if (controller.left.isPressed() && movi == 0) {
            animation.runImageAnimation(
            mario,
            assets.animation`mario iz`,
            100,
            true
            )
            movi = 1
            movd = 0
        }
        if (!(controller.left.isPressed()) && !(controller.right.isPressed()) && (movd == 1 || movi == 1)) {
            animation.stopAnimation(animation.AnimationTypes.All, mario)
            if (movd == 1) {
                mario.setImage(img`
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
                    `)
            }
            if (movi == 1) {
                mario.setImage(img`
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
                    `)
            }
            movd = 0
            movi = 0
        }
    } else {
        if (controller.left.isPressed()) {
            mario.setImage(assets.image`salto i`)
            movd = 0
            movi = 1
        } else {
            mario.setImage(assets.image`salto d`)
            movi = 0
            movd = 1
        }
    }
    if (mario.vy == 0) {
        salto = 0
    }
}
let movi = 0
let movd = 0
let mario: Sprite = null
let salto = 0
salto = 0
effects.clouds.startScreenEffect()
scene.setBackgroundColor(9)
tiles.setTilemap(tilemap`level1`)
mario = sprites.create(img`
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
    `, SpriteKind.Player)
scene.cameraFollowSprite(mario)
mario.ay = 500
controller.moveSprite(mario, 100, 0)
forever(function () {
    mov1()
})
