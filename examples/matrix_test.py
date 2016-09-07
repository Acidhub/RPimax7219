#!/usr/bin/env python3

import RPimax7219.led as led
from time import sleep
from RPimax7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange

mx = led.matrix(cascaded=1)

mx.show_message("MAX7219 LED Matrix Demo", font=proportional(CP437_FONT))


sleep(1)
mx.show_message("Brightness")

sleep(1)
mx.letter(0, ord('A'))
sleep(1)
for _ in range(5):
    for intensity in range(16):
        mx.brightness(intensity)
        sleep(0.1)

mx.brightness(7)

sleep(1)
mx.show_message("Orientation")

sleep(1)
mx.letter(0, ord('A'))
sleep(1)
for _ in range(5):
    for angle in [0, 90, 180, 270]:
        mx.orientation(angle)
        sleep(0.2)

for row in range(8):
    mx.scroll_down()
    sleep(0.2)

mx.orientation(0)
sleep(1)

mx.show_message("Inverse")
sleep(1)
mx.letter(0, ord('A'))
sleep(1)
for _ in range(10):
    mx.invert(1)
    sleep(0.25)
    mx.invert(0)
    sleep(0.25)

sleep(1)
mx.show_message("Alternative font!", font=SINCLAIR_FONT)

sleep(1)
mx.show_message("Proportional font - characters are squeezed together!", font=proportional(SINCLAIR_FONT))

# http://www.squaregear.net/fonts/tiny.shtml
sleep(1)
mx.show_message(
"Tiny is, I believe, the smallest possible font \
(in pixel size). It stands at a lofty four pixels \
tall (five if you count descenders), yet it still \
contains all the printable ASCII characters.",
font=proportional(TINY_FONT))

sleep(1)
mx.show_message("CP437 Characters")

sleep(1)
for x in range(256):
#    mx.letter(1, 32 + (x % 64))
    mx.letter(0, x)
    sleep(0.1)

sleep(1)
mx.show_message("Scrolling and pixel setting...")

while True:
    for x in range(300):
        mx.pixel(4, 4, 1, redraw=False)
        direction = randrange(8)
        if direction == 7 or direction == 0 or direction == 1:
            mx.scroll_up(redraw=False)
        if direction == 1 or direction == 2 or direction == 3:
            mx.scroll_right(redraw=False)
        if direction == 3 or direction == 4 or direction == 5:
            mx.scroll_down(redraw=False)
        if direction == 5 or direction == 6 or direction == 7:
            mx.scroll_left(redraw=False)

        mx.flush()
        sleep(0.01)
