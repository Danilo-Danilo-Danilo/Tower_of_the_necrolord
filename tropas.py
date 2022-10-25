from esqueleto import *
from ponto_invoc import *
from cavaleiro import *
from campo import *


class Tropas:
    def __init__(self, tabuleiro):
        self.matriz_tropas = []
        self.esq_ss = Spritesheet(pygame.image.load('sprites/ss_todo.png').convert_alpha())
        self.matriz_inimigos = []
        self.cava_ss = Spritesheet(pygame.image.load('sprites/ss_cavaleiro.png').convert_alpha())
        self.tabuleiro = tabuleiro

    def invocar_tropa(self, x, y, tabuleiro, mouse):
        ponto = tabuleiro.invocar_em(x, y)
        if pygame.mouse.get_pressed()[0]:
            if mouse.id is not None:
                if ponto is not None:
                    match mouse.id:
                        case 1:
                            self.matriz_tropas.append(Esqueleto(ponto[0], ponto[1], 32, 32, self.esq_ss, 5, 2))
                            mouse.id = None
                            mouse.unidade = None
        return mouse

    def invocar_inimigo(self, x, y, tabuleiro):
        ponto = tabuleiro.invocar_em(x, y)
        if ponto is not None:
            self.matriz_inimigos.append(Cavaleiro(ponto[0], ponto[1], 32, 32, self.cava_ss, 4, 1))

    def exibir(self, win):
        for i in self.matriz_tropas:
            i.exibir(win)
        for i in self.matriz_inimigos:
            i.exibir(win)

    def logica(self):
        for i in self.matriz_tropas:
            i.logica(self.matriz_inimigos, self.tabuleiro)
        for i in self.matriz_inimigos:
            i.logica(self.matriz_tropas)
