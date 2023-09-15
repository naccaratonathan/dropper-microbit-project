def on_button_pressed_a():
    bucket.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bucket.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

drop: game.LedSprite = None
bucket: game.LedSprite = None
game.set_score(0)
bucket = game.create_sprite(2, 4)

def on_forever():
    global drop
    drop = game.create_sprite(randint(0, 4), -1)
    drop.turn(Direction.RIGHT, 90)
    for index in range(4):
        drop.move(1)
        basic.pause(225)
        if bucket.is_touching(drop):
            game.add_score(1)
            drop.delete()
    if drop.is_touching_edge():
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                1989,
                1,
                255,
                255,
                1291,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        drop.delete()
        basic.clear_screen()
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        basic.show_string("" + str((game.score())))
basic.forever(on_forever)
