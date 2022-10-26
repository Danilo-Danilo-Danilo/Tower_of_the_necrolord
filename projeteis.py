from projetil import *
import pygame


class Projeteis:
    def __init__(self):
        self.projeteis = []

    def ad_projetil(self, projetil):
        self.projeteis.append(projetil)

    def exibir(self, win):
        for projetil in self.projeteis:
            projetil.exibirp(win)
            if projetil.x > 768:
                self.projeteis.remove(projetil)
            projetil.movimento()

    def colisao(self, matriz_inimigos):
        for projetil in self.projeteis:
            for inimigo in matriz_inimigos:
                if (projetil.x > inimigo.x) and (inimigo.y <= projetil.y <= inimigo.y + inimigo.altura):
                    if projetil in self.projeteis:
                        self.projeteis.remove(projetil)
                        inimigo.vida -= projetil.dano
                    if inimigo.vida <= 0:
                        matriz_inimigos.remove(inimigo)
        return matriz_inimigos
