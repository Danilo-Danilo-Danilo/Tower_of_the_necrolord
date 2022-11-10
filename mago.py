from spritesheet import *
from entidade import *
from tropas import *
import pygame


class Mago(Entidade):
    id = 2
    vida = 200
    velocidade = 2
    dano = 100
    vel_ataque = 60
    cooldown = 1
    tijolo = pygame.transform.scale((pygame.image.load('sprites/fogo.png')), (32, 32))
    atirar = False
    lado = 1

    def logica(self, matriz_tropas):
        if self.frame > len(self.animacoes[0]) - 1:
            self.frame = 0
        else:
            self.frame += 0.5
        if self.atirar and (self.cooldown > 30):
            self.x = self.x
        elif not self.colodiu(matriz_tropas):
            self.x -= self.velocidade

    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

    def colodiu(self, matriz_tropas):
        if len(matriz_tropas) == 0:
            self.atirar = False
        for esq in matriz_tropas:
            x0 = esq.x
            x1 = esq.x + (esq.largura * 2)
            y0 = esq.y
            y1 = esq.y + (esq.altura * 2)
            if y0 - 2 <= self.y <= y1 - 2:
                self.atirar = True
            else:
                self.atirar = False
            if x0 <= self.x + 5 <= x1:
                if y0 - 2 <= self.y <= y1 - 2:
                    return True
        return False

    def atacar(self, matriz_tropas):
        if self.cooldown > 0:
            self.cooldown += 1
            if self.cooldown == 45:
                self.cooldown = 0
        return matriz_tropas

    def atirando(self, projeteis):
        if self.cooldown == 0:
            if self.atirar:
                projetil = Projetil(self.tijolo, self.x + 10, self.y + 16, -30, 40, 1)
                projeteis.ad_projetil(projetil)
                self.cooldown += 1
        return projeteis
