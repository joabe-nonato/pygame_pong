import pygame as pg
from system.settings import WIDTH, PONTO_MAXIMO, BRANCO
from system.helpers import escrever

class Pontuacao:
    def __init__(self):
        self.ball_left = 0
        self.ball_rigth = 0
        self.cpu_ponto = 0
        self.player_ponto = 0        
        self.font = pg.font.Font(None, 50)
        self.ponto = False
        self.vitoria = False
                
    def update(self):
        self.ponto = False
        if self.ball_left <= 0: 
            self.player_ponto += 1
            self.ponto = True
        elif self.ball_left >= WIDTH:
            self.cpu_ponto += 1
            self.ponto = True
        
        if self.cpu_ponto >= PONTO_MAXIMO or self.player_ponto >= PONTO_MAXIMO:
            self.vitoria = True
            
    def draw(self, screen):        
        escrever(screen, f"CPU: {self.cpu_ponto}", 70, 20 , 20)
        escrever(screen, f"Player: {self.player_ponto}", 70, ((WIDTH / 4) * 2) + 20 , 20)
                                
        if self.vitoria:
            
            vencedor = "CPU"
            if self.player_ponto >= PONTO_MAXIMO:
                vencedor = "PLAYER"            
                
            escrever(screen, vencedor, 100, 0, 0)
                