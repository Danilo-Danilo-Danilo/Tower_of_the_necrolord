import random

from altar import *
from esqueleto import *
from ponto_invoc import *
from cavaleiro import *
from campo import *


class Tropas:
    def __init__(self, tabuleiro):
        self.atraso_invoc = 0
        self.matriz_tropas = []
        self.esq_ss = Spritesheet(pygame.image.load('sprites/ss_todo.png').convert_alpha())
        self.matriz_inimigos = []
        self.cava_ss = Spritesheet(pygame.image.load('sprites/ss_cavaleiro.png').convert_alpha())
        self.tabuleiro = tabuleiro
        self.altar_ss = Spritesheet(pygame.image.load('sprites/altar_sprite.png').convert_alpha())
        self.wave = 1
    def invocar_tropa(self, x, y, tabuleiro, mouse):
        ponto = tabuleiro.invocar_em(x, y)
        if pygame.mouse.get_pressed()[0]:
            if mouse.id is not None:
                if ponto is not None:
                    match mouse.id:
                        case 1:
                            if mouse.mana.mana_tamanho >= 60:
                                esqueleto = Esqueleto(ponto[0], ponto[1], 32, 32, self.esq_ss, 5, 2)
                                self.matriz_tropas.append(esqueleto)
                                mouse.id = None
                                mouse.unidade = None
                                mouse.mana.mana_tamanho -= 60
                                tabuleiro.blocos[ponto[2]][ponto[3]].tem_unidade = True
                        case 2:
                            if mouse.mana.mana_tamanho >= 40:
                                mouse.id = None
                                mouse.unidade = None
                                self.matriz_tropas.append(Altar(ponto[0], ponto[1], 32, 32, self.altar_ss, 5, 2))
                                tabuleiro.blocos[ponto[2]][ponto[3]].tem_unidade = True
                                mouse.mana.mana_tamanho -= 40
        return mouse


    def invocar_inimigos(self, x, y, tabuleiro):
        ponto = tabuleiro.invocar_em(x, y)
        if ponto is not None:
            self.matriz_inimigos.append(Cavaleiro(ponto[0], ponto[1], 32, 32, self.cava_ss, 4, 1))
            print(ponto[0])
            print(ponto[1])

    def spawn_inimigos(self, tempo, level):
        if tempo == (90 * self.wave):
            for i in range(level[self.wave]):
                random.seed()
                y = ((random.randint(0, 5) * 64) + 118)
                self.matriz_inimigos.append(Cavaleiro(780, y, 32, 32, self.cava_ss, 4, 1))
                self.wave += 1
    def exibir(self, win):
        for i in self.matriz_tropas:
            i.exibir(win)
        for i in self.matriz_inimigos:
            i.exibir(win)

    def logica(self):
        for i in self.matriz_tropas:
            if i.id == 2:
                i.logica(self.matriz_tropas)
            else:
                i.logica(self.matriz_inimigos, self.tabuleiro)
        for i in self.matriz_inimigos:
            i.logica(self.matriz_tropas)

    def atirar(self, projeteis):
        for i in self.matriz_tropas:
            if i.id == 1:
                projeteis = i.atirando(projeteis)
        return projeteis
