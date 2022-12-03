from projetil import Projetil
import pygame
from entidade import Entidade

class Esqueleto(Entidade):
    id = 1
    vida = 240
    vel_ataque = 15
    dano_projetil = 40
    vel_projetil = 30
    tijolo = pygame.transform.scale((pygame.image.load('sprites/sosso.png')), (32, 32))
    atirar = False
    cd = 7
    lado = 0
    def logica(self, matriz_inimigos, tabuleiro, projeteis):
        if self.frame >= len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.3
        if self.atirar:
            self.atirando(projeteis)
        self.colodiu(matriz_inimigos, tabuleiro)

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
                if cav.y + (cav.altura * 2) - 8 >= self.y >= cav.y:
                    if cav.x > self.x:
                        self.atirar = True
                        return True
        self.atirar = False
        return False
    def tempo_Recarga(self):
        if self.cd == 0:
            self.cd += 1
            return True
        elif self.cd == self.vel_ataque:
            self.cd = 0
            return False
        else:
            self.cd += 1
    def atirando(self, projeteis):
        if self.tempo_Recarga():
            projetil = Projetil(self.tijolo, self.x + 10, self.y + 16, self.vel_projetil, self.dano_projetil, self.lado)
            projeteis.ad_projetil(projetil)