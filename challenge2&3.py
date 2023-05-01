from microbit import *

while True:
    sleep(250)
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("And What!?")
    if button_a.is_pressed() or button_b.is_pressed():
        display.scroll('Or What!?')

