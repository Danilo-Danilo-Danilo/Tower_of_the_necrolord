import random
from altar import *
from esqueleto import *
from ponto_invoc import *
from cavaleiro import *
from campo import *
from mago import *
from esqueleto_escudo import *


class Tropas:
    def __init__(self, tabuleiro):
        self.perdeu = False
        self.atraso_invoc = 0
        self.entidades = {
            'inimigos':[],
            'aliados':[]
        }
        self.tabuleiro = tabuleiro
        self.cava_ss = Spritesheet(pygame.image.load('sprites/ss_cavaleiro.png').convert_alpha())
        self.esq_ss = Spritesheet(pygame.image.load('sprites/ss_todo.png').convert_alpha())
        self.altar_ss = Spritesheet(pygame.image.load('sprites/altar_sprite.png').convert_alpha())
        self.tank_ss = Spritesheet(pygame.image.load('sprites/skeleto_tank.png').convert_alpha())
        self.mago_ss = Spritesheet(pygame.image.load('sprites/mage-001.png').convert_alpha())
        self.wave = 1
        self.tempo = 0
    def invocar_tropa(self, x, y, tabuleiro, mouse, card_hold):
        p = tabuleiro.invocar_em(x, y)
        if pygame.mouse.get_pressed()[0]:
            if mouse.id is not None:
                if p is not None:
                    match mouse.id:
                        case 1:
                            if mouse.mana.mana_tamanho >= 60:
                                self.entidades['aliados'].append(Esqueleto(p[0], p[1], 32, 32,self.esq_ss, 5, 2, p[2], p[3], 2, ""))
                                mouse.id = None
                                mouse.unidade = None
                                mouse.mana.mana_tamanho -= 60
                                tabuleiro.blocos[p[2]][p[3]].tem_unidade = True
                                card_hold.cartas[0].contador = card_hold.cartas[0].recarga
                        case 2:
                            if mouse.mana.mana_tamanho >= 40:
                                mouse.id = None
                                mouse.unidade = None
                                self.entidades['aliados'].append(Altar(p[0], p[1], 32, 32, self.altar_ss, 5, 2, p[2], p[3], 2, ""))
                                tabuleiro.blocos[p[2]][p[3]].tem_unidade = True
                                mouse.mana.mana_tamanho -= 40
                                card_hold.cartas[1].contador = card_hold.cartas[1].recarga
                        case 3:
                            if mouse.mana.mana_tamanho >= 60:
                                mouse.id = None
                                mouse.unidade = None
                                self.entidades['aliados'].append(Esqueleto_Tank(p[0], p[1], 32, 32, self.tank_ss, 1, 1, p[2], p[3], 2, ""))
                                tabuleiro.blocos[p[2]][p[3]].tem_unidade = True
                                mouse.mana.mana_tamanho -= 60
                                card_hold.cartas[2].contador = card_hold.cartas[2].recarga
        return mouse, card_hold


    def invocar_inimigos(self, x, y, tabuleiro):
        p = tabuleiro.invocar_em(x, y)
        if p is not None:
            self.entidades['inimigos'].append(Mago(p[0], p[1], 32, 32, self.mago_ss, 1, 1, p[2], p[3], 2, ""))

    def spawn_inimigos(self, level):
        concluiu = False
        if self.wave < len(level):
            if level[self.wave] == self.tempo:
                random.seed()
                a = random.randint(0, 5)
                y = (a * 64) + 118
                id_in = random.randint(0, level[0])
                match id_in:
                    case 0:
                        self.entidades['inimigos'].append(Cavaleiro(780, y, 32, 32, self.cava_ss, 4, 1, a + 1, 14, 2, ""))
                        self.wave += 1
                    case 1:
                        self.entidades['inimigos'].append(Mago(780, y, 32, 32, self.mago_ss, 1, 1, a + 1, 14, 2, ""))
                        self.wave += 1
        if self.wave == len(level) and len(self.entidades['inimigos']) == 0:
            concluiu = True

        self.tempo += 1

        return concluiu
    def exibir(self, win):
        for i in self.entidades['aliados']:
            i.exibir(win)
        for i in self.entidades['inimigos']:
            i.exibir(win)

    def logica(self, mouse):
        for i in self.entidades['inimigos']:
            if i.x + 64 <= 0:
                self.perdeu = True
        for i in self.entidades['aliados']:
            if i.id == 2:
                i.logica(mouse)
            else:
                i.logica(self.entidades['inimigos'], self.tabuleiro)
            if i.vida <= 0:
                self.entidades['aliados'].remove(i)
                self.tabuleiro.blocos[i.linha][i.coluna].tem_unidade = False
        for i in self.entidades['inimigos']:
            i.logica(self.entidades['aliados'])

    def atirar(self, projeteis):
        for i in self.entidades['aliados']:
            if i.id == 1:
                projeteis = i.atirando(projeteis)
        for i in self.entidades['inimigos']:
            if i.id == 2:
                projeteis = i.atirando(projeteis)
        return projeteis



