import sys
import math

import pygame as pg
from pygame.math import Vector2

from scripts.ships import *
from scripts.Ui import *

pg.init()
screen = pg.display.set_mode((1000, 800))

font = pg.font.Font('OpenSans.ttf',20)





clock = pg.time.Clock()
quitted = False
ship1 = Ship(450, 450,'Ship1',"#00ff00")
ship2 = Ship(250, 250,'Ship2',"#00f0f0")

ship1.target = 'Ship2'
ship2.target = 'Ship1'
ui = Ui()
keypressed = False

ship1.destination =Vector2(300, 600)
mouse = (300, 300)
selection = ship1
while not quitted:
    clock.tick(60)
    quitted = pg.event.get(pg.QUIT)

    screen.fill('#000010')

    

    if not keypressed and pg.mouse.get_pressed()[0]:
        mouse = pg.mouse.get_pos()
        selection.destque.append(Vector2(mouse[0], mouse[1]))
        ship2.destque.append(Vector2(1000-mouse[0],800-mouse[1]))
        #print(selection.destque)
        keypressed = True
    elif not pg.mouse.get_pressed()[0]:
        keypressed = False

    ship1.update(screen)
    ship2.update(screen)
    update_bullets(screen)
    #dotline((0,0),(100,100))
    ui.update(screen,selection,clock,font)
    pg.draw.circle(screen,'green',(100,100),1)
    pg.display.flip()
    
pg.quit()
sys.exit()
