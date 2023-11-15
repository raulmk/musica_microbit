input.onButtonPressed(Button.A, function () {
    music.play(music.stringPlayable("G F G A - F E D ", input.acceleration(Dimension.X)), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    music.play(music.stringPlayable("C C C C C C C C5 ", input.acceleration(Dimension.X)), music.PlaybackMode.UntilDone)
})
