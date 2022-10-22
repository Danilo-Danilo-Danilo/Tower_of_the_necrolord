from esqueleto import *
from ponto_invoc import *
from cavaleiro import *

class Tropas:
    def __init__(self):
        self.matriz_tropas = []
        self.esq_ss = Spritesheet(pygame.image.load('sprites/ss.png').convert_alpha())
        self.matriz_inimigos = []
        self.cava_ss = Spritesheet(pygame.image.load('sprites/ss_cavaleiro.png').convert_alpha())
    def invocar_tropa(self, x, y, tabuleiro):
        ponto = tabuleiro.invocar_em(x,y)
        if ponto is not None:
            self.matriz_tropas.append(Esqueleto(ponto[0], ponto[1], 32, 32, self.esq_ss, 5, 1))
    def invocar_inimigo(self, x, y, tabuleiro):
        ponto = tabuleiro.invocar_em(x,y)
        if ponto is not None:
            self.matriz_inimigos.append(Cavaleiro(ponto[0], ponto[1], 32, 32, self.cava_ss, 3, 1))

    def exibir(self, win):
        for i in self.matriz_tropas:
            i.exibir(win)
        for i in self.matriz_inimigos:
            i.exibir(win)

    def logica(self):
        for i in self.matriz_tropas:
            i.logica()
        for i in self.matriz_inimigos:
            i.logica(self.matriz_tropas)
