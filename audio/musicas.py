import pygame as pg

from audio.partituras import TEMA
from audio.gerar_audio import gerar_musica


class Musica:

    def __init__(self):

        self.tema = pg.sndarray.make_sound(
            gerar_musica(TEMA)
        )