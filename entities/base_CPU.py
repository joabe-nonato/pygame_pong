from system.settings import HEIGHT, PRETO
import pygame as pg

class CPU:
    def __init__(self):
        self.objeto = pg.Rect(0,0,20,100)
        self.objeto.centery = HEIGHT / 2
        self.speed_y = 0
        self.ball_centery = 0     
        self.cor = PRETO 
        
    def update(self):
        self.cor = PRETO 
                        
        self.objeto.y += self.speed_y
        
        if self.ball_centery <= self.objeto.centery:
            self.speed_y = -6
        elif self.ball_centery >= self.objeto.centery:
            self.speed_y = 6
        else:
            self.speed_y = 0
        
        if self.objeto.top <= 0 and self.speed_y < 0:        
            self.speed_y = 0
        if self.objeto.bottom >= HEIGHT  and self.speed_y > 0:
            self.speed_y = 0
            
            

    def draw(self, screen):
        pg.draw.rect(screen, self.cor, self.objeto)
