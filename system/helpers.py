import pygame as pg

def escrever(screen, texto, tamanho = 10, posX = 0, posY = 0):
    fonte = pg.font.Font(None, tamanho)
    surf_texto = fonte.render(texto, True, (255,255,255))
    txt = surf_texto.get_rect()
    retangulo = screen.get_rect()
    
    if posX == 0:
      posX = retangulo.centerx - txt.centerx
    
    if posY == 0:
        posY = (retangulo.centery - txt.centery)
    
    screen.blit(surf_texto,( posX,  posY ))
    
