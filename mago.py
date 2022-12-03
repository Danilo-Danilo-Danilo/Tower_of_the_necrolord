from spritesheet import Spritesheet
from entidade import Entidade
from projetil import Projetil
import pygame


class Mago(Entidade):
    id = 2
    vida = 160
    velocidade = 2
    dano_projetil = 60
    vel_projetil = -30
    cooldown = 0
    andarei = True
    tijolo = pygame.transform.scale((pygame.image.load('sprites/fogo.png')), (32, 32))
    atirar = False
    parar = False
    cd = 0
    lado = 1

    def logica(self, matriz_tropas, projeteis):
        if self.frame > len(self.animacoes[0]) - 1:
            self.frame = 0
        else:
            self.frame += 0.5
        if not self.colidiu(matriz_tropas):
            if self.atirar and 10 < self.cooldown < 15:
                self.x = self.x
            else:
                self.x -= self.velocidade
        if self.tempo():
            self.atirando(projeteis)

    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

    def colidiu(self, matriz_tropas):
        en_counter = 0
        if len(matriz_tropas) == 0:
            self.atirar = False
        for esq in matriz_tropas:
            x0 = esq.x
            x1 = esq.x + (esq.largura * 2)
            y0 = esq.y
            y1 = esq.y + (esq.altura * 2)
            if y0 - 2 <= self.y <= y1 - 2:
                en_counter += 1
            if en_counter > 0:
                self.atirar = True
            else:
                self.atirar = False
            if x0 <= self.x + 5 <= x1:
                if y0 - 2 <= self.y <= y1 - 2:
                    return True
        return False
    def tempo(self):
        if self.cooldown == 15:
            self.cooldown = 0
            return True
        elif self.cooldown < 15:
            self.cooldown += 1
        elif self.cooldown == 0:
            self.cooldown += 1
    def atirando(self, projeteis):
        if self.atirar:
            projetil = Projetil(self.tijolo, self.x + 10, self.y + 16, self.vel_projetil, self.dano_projetil, self.lado)
            projeteis.ad_projetil(projetil)