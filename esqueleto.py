from spritesheet import *
from entidade import *
import pygame

class Esqueleto(Entidade):
    vida = 360
    vel_ataque = 90
    dano = 100
    def logica(self):
        if self.frame > len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.3

    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))