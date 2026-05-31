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


# def recuperar_sons():
#     return {
#     "hit": pg.mixer.Sound("hit.wav"),
#     "wall": pg.mixer.Sound("wall.wav"),
#     "score": pg.mixer.Sound("score.wav"),
#     "victory": pg.mixer.Sound("victory.wav"),
#     "menu": pg.mixer.Sound("menu.wav"),
#     "enter": pg.mixer.Sound("enter.wav"),
#     "start": pg.mixer.Sound("start.wav"),
# }

def musica_tema():
    pg.mixer.music.load("tema.wav")
    pg.mixer.music.play(-1)
    