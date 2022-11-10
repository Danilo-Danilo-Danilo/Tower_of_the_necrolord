import random
from altar import *
from esqueleto import *
from ponto_invoc import *
from cavaleiro import *
from campo import *
from mago import *


class Tropas:
    def __init__(self, tabuleiro):
        self.atraso_invoc = 0
        self.matriz_tropas = []
        self.matriz_inimigos = []
        self.tabuleiro = tabuleiro
        self.cava_ss = Spritesheet(pygame.image.load('sprites/ss_cavaleiro.png').convert_alpha())
        self.esq_ss = Spritesheet(pygame.image.load('sprites/ss_todo.png').convert_alpha())
        self.altar_ss = Spritesheet(pygame.image.load('sprites/altar_sprite.png').convert_alpha())
        self.tank_ss = Spritesheet(pygame.image.load('sprites/skeleto_tank.png').convert_alpha())
        self.mago_ss = Spritesheet(pygame.image.load('sprites/mage-001.png').convert_alpha())
        self.wave = 1
    def invocar_tropa(self, x, y, tabuleiro, mouse, card_hold):
        p = tabuleiro.invocar_em(x, y)
        if pygame.mouse.get_pressed()[0]:
            if mouse.id is not None:
                if p is not None:
                    match mouse.id:
                        case 1:
                            if mouse.mana.mana_tamanho >= 60:
                                self.matriz_tropas.append(Esqueleto(p[0], p[1], 32, 32,self.esq_ss, 5, 2, p[2], p[3]))
                                mouse.id = None
                                mouse.unidade = None
                                mouse.mana.mana_tamanho -= 60
                                tabuleiro.blocos[p[2]][p[3]].tem_unidade = True
                                card_hold.cartas[0].contador = card_hold.cartas[0].recarga
                        case 2:
                            if mouse.mana.mana_tamanho >= 40:
                                mouse.id = None
                                mouse.unidade = None
                                self.matriz_tropas.append(Altar(p[0], p[1], 32, 32, self.altar_ss, 5, 2, p[2], p[3]))
                                tabuleiro.blocos[p[2]][p[3]].tem_unidade = True
                                mouse.mana.mana_tamanho -= 40
                                card_hold.cartas[1].contador = card_hold.cartas[1].recarga
                        case 3:
                            if mouse.mana.mana_tamanho >= 60:
                                mouse.id = None
                                mouse.unidade = None
                                self.matriz_tropas.append(Altar(p[0], p[1], 32, 32, self.tank_ss, 1, 1, p[2], p[3]))
                                tabuleiro.blocos[p[2]][p[3]].tem_unidade = True
                                mouse.mana.mana_tamanho -= 60
                                card_hold.cartas[2].contador = card_hold.cartas[2].recarga
        return mouse, card_hold


    def invocar_inimigos(self, x, y, tabuleiro):
        p = tabuleiro.invocar_em(x, y)
        if p is not None:
            self.matriz_inimigos.append(Mago(p[0], p[1], 32, 32, self.mago_ss, 1, 1, p[2], p[3]))

    def spawn_inimigos(self, tempo, level):
        if tempo == (90 * self.wave):
            for i in range(level[self.wave]):
                random.seed()
                a = random.randint(0, 5)
                y = (a * 64) + 118
                self.matriz_inimigos.append(Cavaleiro(780, y, 32, 32, self.cava_ss, 4, 1, a + 1, 14 ))
                self.wave += 1
    def exibir(self, win):
        for i in self.matriz_tropas:
            i.exibir(win)
        for i in self.matriz_inimigos:
            i.exibir(win)

    def logica(self, mouse):
        for i in self.matriz_inimigos:
            if i.x + 64 <= 0:
                print("Tu perdeu chefia")
        for i in self.matriz_tropas:
            if i.id == 2:
                i.logica(mouse)
            else:
                i.logica(self.matriz_inimigos, self.tabuleiro)
            if i.vida <= 0:
                self.matriz_tropas.remove(i)
                self.tabuleiro.blocos[i.linha][i.coluna].tem_unidade = False
        for i in self.matriz_inimigos:
            i.logica(self.matriz_tropas)

    def atirar(self, projeteis):
        for i in self.matriz_tropas:
            if i.id == 1:
                projeteis = i.atirando(projeteis)
        for i in self.matriz_inimigos:
            if i.id == 2:
                projeteis = i.atirando(projeteis)
        return projeteis



