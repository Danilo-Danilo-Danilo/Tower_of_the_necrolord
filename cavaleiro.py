from spritesheet import *
from entidade import *
from tropas import *
import pygame

class Cavaleiro(Entidade):
    vida = 540
    velocidade = 2
    dano = 100
    vel_ataque = 90

    def logica(self, matriz_tropas):
        if self.frame > len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.5
        if not self.colodiu(matriz_tropas):
            self.x -= self.velocidade

    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

    def colodiu(self, matriz_tropas):
        for esq in matriz_tropas:
            x0 = esq.x
            x1 = esq.x + (esq.largura * 2)
            y0 = esq.y
            y1 = esq.y + (esq.altura * 2)
            if x0 <= self.x + 5 <= x1:
                if y0 - 2 <= self.y <= y1 - 2:
                    return True
        return False