from pygame import *
from random import randint
from time import time as timer
font.init()
#экран
back = (200, 255, 255)
win_width = 700
win_height = 500
display.set_caption("PingPong")
window = display.set_mode(
    (win_width, win_height)
)
window.fill(back)
#цикл
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()