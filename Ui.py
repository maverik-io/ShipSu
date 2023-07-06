import pygame as pg
from pygame.math import Vector2


class Ui():
    def __init__(self):
        self.pos = Vector2(500,750)
        self.uisurf = pg.surface.Surface((400,200))
    
    
    def update(self,screen,selection,clock,font):
        self.uisurf.fill('#000010')
        pg.draw.polygon(self.uisurf,'white',[
            Vector2(200,100) + Vector2(-200,50),
            Vector2(200,100) + Vector2(-100,-50),
            Vector2(200,100) + Vector2(100,-50),
            Vector2(200,100) + Vector2(200,50)
        ])
        pg.draw.polygon(self.uisurf,'#222222',[
            Vector2(200,100) + Vector2(-200,50),
            Vector2(200,100) + Vector2(-100,-50),
            Vector2(200,100) + Vector2(100,-50),
            Vector2(200,100) + Vector2(200,50)
        ],2)


        label = font.render(f'ETA : {selection.desvec.magnitude()/(clock.get_fps()+0.01):.1f} sec(s)',1,'black')
        rect  = label.get_rect(topleft = Vector2(100,80))
        self.uisurf.blit(label,rect)

        label = font.render(f'<--{selection.name.upper()}-->',1,'black')
        rect  = label.get_rect(center = Vector2(200,70))
        self.uisurf.blit(label,rect)


        return self.uisurf
