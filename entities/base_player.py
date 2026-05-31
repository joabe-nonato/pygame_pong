from system.settings import WIDTH, HEIGHT, CINZA2, BRANCO
import pygame as pg

class Player:
    def __init__(self):
        self.objeto = pg.Rect(0,0,20,100)
        self.objeto.centery = HEIGHT / 2
        self.objeto.midright = (WIDTH, HEIGHT / 2)
        # self.speed_x = 6
        self.speed_y = 0
        self.cor = CINZA2
        
    def events(self, event):
            if event == None:
                return

            self.speed_y = 0
                
            if event.type == pg.KEYDOWN:                        
                if event.key == pg.K_UP:
                    self.speed_y = -6
                if event.key == pg.K_DOWN:
                    self.speed_y = 6                
            

    def update(self):     
        self.cor = CINZA2
        if self.speed_y < 0:
            if self.objeto.top >= 0:
                self.objeto.y += self.speed_y
                
        if self.speed_y > 0:
            if self.objeto.bottom <= HEIGHT:
                self.objeto.y += self.speed_y                    

    def draw(self, screen):
        pg.draw.rect(screen, self.cor, self.objeto)