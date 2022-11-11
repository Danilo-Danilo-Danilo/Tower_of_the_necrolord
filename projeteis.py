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

    def colisao(self, matriz_inimigos, matriz_tropas):
        for projetil in self.projeteis:
            for inimigo in matriz_inimigos:
                if inimigo.lado != projetil.lado:
                    if (inimigo.x <= projetil.x <= inimigo.x + 64) and (inimigo.y <= projetil.y <= inimigo.y + 32):
                        if projetil in self.projeteis:
                            self.projeteis.remove(projetil)
                            inimigo.vida -= projetil.dano
                            if inimigo.vida <= 0:
                                matriz_inimigos.remove(inimigo)

            for tropa in matriz_tropas:
                if tropa.lado != projetil.lado:
                    if (tropa.x <= projetil.x <= tropa.x + 64) and (tropa.y <= projetil.y <= tropa.y + 32):
                        if projetil in self.projeteis:
                            tropa.vida -= projetil.dano
                            self.projeteis.remove(projetil)

        return matriz_inimigos

