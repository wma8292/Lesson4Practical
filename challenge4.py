from microbit import *
import music

while True:
    if pin_logo.is_touched():
        display.show(Image.HAPPY)
        music.play(music.CHASE)
    else:
        display.clear()
        music.stop()
