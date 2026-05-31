import pygame as pg
import random
from system.settings import WIDTH, HEIGHT, AMARELO

class Ball():
    def __init__(self):
        self.objeto = pg.Rect(0,0,30,30)
        self.objeto.center = (WIDTH / 2, HEIGHT / 2)
        self.dificuldade = 1
        self.speed_x = 6
        self.speed_y = 6
        self.reset = False
        self.cor = AMARELO
        
    def update(self):
        self.cor = AMARELO
        
        if self.reset:
            self.dificuldade = 0
            self.objeto.x = (WIDTH / 2)
            self.objeto.y = random.randint(10, 100)
            
        
        self.objeto.x += (self.speed_x + self.dificuldade)
        self.objeto.y += (self.speed_y + self.dificuldade)
        
        if self.objeto.bottom >= HEIGHT or self.objeto.top <= 0:
            self.speed_y *= -1
        
        
    def draw(self, screen):
        pg.draw.ellipse(screen, self.cor, self.objeto)