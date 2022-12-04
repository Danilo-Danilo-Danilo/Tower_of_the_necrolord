import random
from altar import Altar
from esqueleto import Esqueleto
from cavaleiro import Cavaleiro
from campo import Campo
from mago import Mago
from spritesheet import Spritesheet
from esqueleto_escudo import Esqueleto_Tank
import pygame


class Tropas:
    def __init__(self, tabuleiro):
        self.perdeu = False
        self.atraso_invoc = 0
        self.entidades = {
            'inimigos':[],
            'aliados':[]
        }
        self.tabuleiro = tabuleiro
        self.cava_ss = Spritesheet(pygame.image.load('sprites/ss_cavaleiro.png'))
        self.esq_ss = Spritesheet(pygame.image.load('sprites/ss_todo.png'))
        self.altar_ss = Spritesheet(pygame.image.load('sprites/altar_sprite.png'))
        self.tank_ss = Spritesheet(pygame.image.load('sprites/skeleto_tank.png'))
        self.mago_ss = Spritesheet(pygame.image.load('sprites/mage-001.png'))
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

    def logica(self, mouse, projeteis):
        self.perdeu = self.perdemo(self.entidades['inimigos'])
        self.morreu(self.entidades["aliados"], self.tabuleiro)
        self.logicaIni(self.entidades['inimigos'], projeteis, self.entidades['aliados'])
        self.logicaAli(self.entidades['aliados'], projeteis, self.tabuleiro, self.entidades['inimigos'], mouse)

    """separei a logica dos inimigos e aliados da logica tropas"""
    def logicaAli(self, aliados, projeteis, tabuleiro, inimigos, mouse):
        for i in aliados:
            match i.id:
                case 2:
                    i.logica(mouse)
                case 1:
                    i.logica(inimigos, tabuleiro, projeteis)
                case 3:
                    i.logica(inimigos, tabuleiro)
    def logicaIni(self, inimigos, projeteis, aliados):
        for i in inimigos:
            match i.id:
                case 2:
                    i.logica(aliados, projeteis)
                case 1:
                    i.logica(aliados)

    """separei a função perdemo do logica"""
    def perdemo(self, inimigos):
        if inimigos == None or len(inimigos) == 0:
            return False
        for i in inimigos:
            if i.x + 64 <= 0:
                return True
            else:
                return False

    """Função q verifica se morreu"""
    def morreu(self, aliados, tabuleiro):
        if len(aliados) == 0:
            return False
        else:
            for i in aliados:
                if i.vida <= 0:
                    aliados.remove(i)
                    tabuleiro.blocos[i.linha][i.coluna].tem_unidade = False
                    return True
                else:
                    return False