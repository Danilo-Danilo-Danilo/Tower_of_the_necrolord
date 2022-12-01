from spritesheet import Spritesheet
from entidade import Entidade
import pygame

class Cavaleiro(Entidade):
    id = 1
    vida = 400
    velocidade = 2
    dano = 60
    vel_ataque = 15
    cd = 0
    lado = 1
    def logica(self, matriz_tropas):
        if self.frame > len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.5
        if not self.colodiu(matriz_tropas):
            self.x -= self.velocidade

    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

    def colodiu(self, matriz_tropas):
        for esq in matriz_tropas:
            x0 = esq.x
            x1 = esq.x + (esq.largura * 2)
            if self.x <= esq.x + (esq.largura * 2) - 4:
                if self.tempo_Recarga():
                    print("atacou")
                    esq.vida -= self.dano
                return True
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