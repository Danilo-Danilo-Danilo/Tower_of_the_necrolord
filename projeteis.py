from projetil import *
import pygame

class Projeteis:
    def __init__(self):
        self.projeteis =[]

    def ad_projetil(self, projetil):
        self.projeteis.append(projetil)

    def exibir(self, win):
        for projetil in self.projeteis:
            projetil.exibirp(win)
            if projetil.x > 768:
                 self.projeteis.remove(projetil)
            projetil.movimento()
