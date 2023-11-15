def on_button_pressed_a():
    music.play(music.string_playable("G F G A - F E D ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.change_tempo_by(120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play(music.string_playable("C C C C C C C C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.change_tempo_by(120)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    music.change_tempo_by(input.acceleration(Dimension.X))
basic.forever(on_forever)
