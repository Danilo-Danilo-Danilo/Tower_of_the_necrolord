from esqueleto import *
from ponto_invoc import *
from campo import *

class Tropas:
    def __init__(self):
        self.matriz_tropas = []
        self.esq_ss = Spritesheet(pygame.image.load('sprites/ss.png').convert_alpha())


    def invocar_tropa(self, x, y, tabuleiro):
        ponto = tabuleiro.invocar_em(x,y)
        if ponto is not None:
            self.matriz_tropas.append(Esqueleto(ponto[0], ponto[1], 32, 32, self.esq_ss, 5, 1))


    def exibir(self, win):
        for i in range(len(self.matriz_tropas)):
            self.matriz_tropas[i].exibir(win)
