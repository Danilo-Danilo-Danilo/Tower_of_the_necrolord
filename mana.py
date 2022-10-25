import pygame
from entidade import *

class Mana():
    def __init__(self, x, y):
        self.mana_inicial = 300
        self.mana_ps = 30
        self.mana_tamanho = 32
        self.sprite = pygame.image.load('sprites/mana.png')
        self.barra = pygame.transform.scale(self.sprite, (self.mana_tamanho, 32))
        self.x = x
        self.y = y

    def logica(self):
        self.barra = pygame.transform.scale(self.sprite, (self.mana_tamanho, 32))
        if self.mana_tamanho < self.mana_inicial:
            self.mana_tamanho += self.mana_ps


    def exibir(self, win):
        win.blit(self.barra, (self.x, self.y))



