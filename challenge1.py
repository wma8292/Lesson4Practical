from microbit import *

while True:
    if button_a.is_pressed():
        display.clear()
        display.set_pixel(0,0,9)
        display.set_pixel(0,1,9)
        display.set_pixel(0,2,9)
        display.set_pixel(0,3,9)
        display.set_pixel(0,4,9)

    if button_b.is_pressed():
        display.clear()
        display.set_pixel(4,0,9)
        display.set_pixel(4,1,9)
        display.set_pixel(4,2,9)
        display.set_pixel(4,3,9)
        display.set_pixel(4,4,9)

