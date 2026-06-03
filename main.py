import pygame as pg
import sys
from system.settings import WIDTH, HEIGHT, FPS, PONTO_MAXIMO, BRANCO
from entities.base_ball import Ball
from entities.base_CPU import CPU
from entities.base_player import Player
from entities.base_score import Pontuacao
from system.helpers import escrever
from audio.efeitos import Efeito
from audio.musicas import Musica

#CRIAR OBJETOS
pg.init()
pg.mixer.init(
    frequency=44100,
    size=-16,
    channels=2
)
pg.display.set_caption('PONG')

lista_textos = []
lista_textos.append(f"Ganha quem fizer {PONTO_MAXIMO} pontos primeiro")
lista_textos.append("devolva a bola para pontuar")
lista_textos.append("[Esc] para sair")
lista_textos.append("[Setas] para mover")
lista_textos.append("[Enter] para começar")

efeitos = Efeito()

class Game:
    def __init__(self):        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.executar = False
        self.efeitos = Efeito()
        self.musicas = Musica()
        self.resetar()
    
    def resetar(self):
        self.ball = Ball()
        self.CPU = CPU()
        self.player = Player()
        self.pontuacao = Pontuacao()
        self.vitoria = False
        # self.sons["enter"].play()
        
    def encerrar(self):
        pg.quit()
        sys.exit()
        

# FUNÇÕES
    # varificar eventos (entradas)
    def events(self):
        lista_eventos = pg.event.get()
        for event in lista_eventos:
            if event.type == pg.QUIT:
                self.encerrar()                            
            self.player.events(event)
            
            if self.executar == False:
                if event.type == pg.KEYDOWN:  
                    if event.key == pg.K_RETURN:
                        self.resetar()
                        self.executar = True
                        self.musicas.tema.play(-1)
                    if event.key == pg.K_ESCAPE:
                        self.encerrar()
            
            if self.pontuacao.vitoria:                
                if event.type == pg.KEYDOWN:  
                    if event.key == pg.K_RETURN or event.key == pg.K_ESCAPE:
                        self.resetar()

    # atualizar valores do game
    def update(self):        
        if self.pontuacao.vitoria == False:
            
            self.player.update()
            
            if self.executar:            
                self.CPU.update() 
                self.pontuacao.update()
                self.ball.update()     
                
                
                if (self.ball.objeto.colliderect(self.player.objeto)
                    or self.ball.objeto.colliderect(self.CPU.objeto)):
                    self.ball.speed_x *= -1
                    self.ball.dificuldade += 0.1
                    self.efeitos.hit.play()
                                
                self.CPU.ball_centery = self.ball.objeto.centery
                
                
                self.pontuacao.ball_left = self.ball.objeto.left
                self.pontuacao.ball_right = self.ball.objeto.right
                
                
                self.ball.reset = self.pontuacao.ponto
                
                if self.pontuacao.ponto:
                   self.efeitos.score.play() 
                   
                if self.pontuacao.vitoria:
                    self.efeitos.vitoria.play()
        
        pg.display.update()
        self.clock.tick(FPS)


    def draw(self):
        self.screen.fill('purple')
        pg.draw.aaline(self.screen, (255,255,255), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

        if self.pontuacao.vitoria:
            self.ball.cor = BRANCO
            self.player.cor = BRANCO
            self.CPU.cor = BRANCO

        self.ball.draw(self.screen)
        self.CPU.draw(self.screen)
        self.player.draw(self.screen)
        self.pontuacao.draw(self.screen)
        
        if self.executar == False:            
            
            
            posy = (HEIGHT / 2) - 35
            for texto in lista_textos[::-1]:                        
                escrever(self.screen, texto, 30, 0 , posy)                
                posy -= 35
                        
    def run(self):     
        self.efeitos.menu.play()   
        # GAME LOOP
        while True:
            
            self.events()
            
            self.update()
            
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()

