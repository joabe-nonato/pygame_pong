import pygame as pg
import numpy as np
from audio.gerar_audio import gerar_tom

class Efeito:
    def __init__(self):
        self.hit = pg.sndarray.make_sound(
            gerar_tom(900, 0.05)
        )
        self.wall = pg.sndarray.make_sound(
            gerar_tom(450, 0.05)
        )
        self.score = pg.sndarray.make_sound(
            np.concatenate([
                gerar_tom(523, 0.12),
                gerar_tom(784, 0.18)
            ])
        )
        
        self.menu = pg.sndarray.make_sound(np.concatenate([
            gerar_tom(1200, 0.01),
            gerar_tom(800, 0.01)
        ]))
        
        self.vitoria = pg.sndarray.make_sound(np.concatenate([
                gerar_tom(523, 0.15),  # C5
                gerar_tom(659, 0.15),  # E5
                gerar_tom(784, 0.15),  # G5
                gerar_tom(1046, 0.30), # C6
            ]))
        
        self.enter = pg.sndarray.make_sound(np.concatenate([
                gerar_tom(600, 0.04),
                gerar_tom(900, 0.06)
            ]))
        
        self.inicio = pg.sndarray.make_sound(np.concatenate([
            gerar_tom(392, 0.10),  # G4
            gerar_tom(523, 0.10),  # C5
            gerar_tom(784, 0.20),  # G5
        ]))
