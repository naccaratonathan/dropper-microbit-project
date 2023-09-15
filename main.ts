input.onButtonPressed(Button.A, function () {
    bucket.move(-1)
})
input.onButtonPressed(Button.B, function () {
    bucket.move(1)
})
let drop: game.LedSprite = null
let bucket: game.LedSprite = null
game.setScore(0)
bucket = game.createSprite(2, 4)
basic.forever(function () {
    drop = game.createSprite(randint(0, 4), -1)
    drop.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        drop.move(1)
        basic.pause(200)
        if (bucket.isTouching(drop)) {
            game.addScore(1)
            drop.delete()
        }
    }
    if (drop.isTouchingEdge()) {
        music.play(music.createSoundExpression(
        WaveShape.Square,
        1989,
        1,
        255,
        255,
        1291,
        SoundExpressionEffect.None,
        InterpolationCurve.Linear
        ), music.PlaybackMode.UntilDone)
        drop.delete()
        basic.clearScreen()
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        basic.showString("" + (game.score()))
    }
})
