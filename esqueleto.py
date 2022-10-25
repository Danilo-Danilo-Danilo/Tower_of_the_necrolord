from spritesheet import *
from entidade import *
from tropas import *
from projetil import *
import pygame

class Esqueleto(Entidade):
    id = 1
    vida = 360
    vel_ataque = 90
    dano = 100
    tijolo = pygame.transform.scale((pygame.image.load('sprites/sbrick.png')), (32, 32))
    atirar = False
    cooldown = 7
    def logica(self, matriz_inimigos, tabuleiro):
        if self.colodiu(matriz_inimigos, tabuleiro):
            self.atirar = True
            if self.frame >= len(self.animacoes[1]) - 1:
                self.frame = 0
            else:
                self.frame += 0.3
        else:
            self.atirar = False
            if self.frame >= len(self.animacoes[0]) -1:
                self.frame = 0
            else:
                self.frame += 0.3

    def exibir(self, win):
        if self.atirar == True:
            win.blit(self.animacoes[1][int(self.frame)], (self.x, self.y))
        else:
            win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

    def colodiu(self, matriz_inimigos, tabuleiro):
        for cav in matriz_inimigos:
            x0 = cav.x
            x1 = cav.x + (cav.largura * 2)
            y0 = cav.y
            y1 = cav.y + (cav.altura * 2)
            if x0 <= tabuleiro.x + (tabuleiro.largura -2) * 64:
                if y0 - 2 <= self.y <= y1 - 2:
                        print("tem cavaleiro")
                        return True
        return False
    def atirando(self, projeteis):
        if self.cooldown > 0:
            self.cooldown += 1
            if self.cooldown == 15:
                self.cooldown = 0
        elif self.cooldown == 0:
            if self.atirar is not None:
                if self.atirar:
                    projetil = Projetil(self.tijolo, self.x + 10, self.y + 16, 40)
                    projeteis.ad_projetil(projetil)
                    self.cooldown += 1
        return projeteis