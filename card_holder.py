import pygame.image

from carta import *
from spritesheet import *

class Card_Holder():

    def __init__(self):
        esqueleto_sprite = pygame.transform.scale(pygame.image.load('sprites/skeleton-turret-001.png'), (64, 64))
        carta_esqueleto = pygame.transform.scale(pygame.image.load('sprites/card-skeleton-001.png'), (64, 64))
        esq_carta_1 = Carta(carta_esqueleto, esqueleto_sprite, 1)
        esq_carta_2 = Carta(carta_esqueleto, esqueleto_sprite, 1)
        esq_carta_3 = Carta(carta_esqueleto, esqueleto_sprite, 1)
        self.cartas = []
        self.cartas.append(esq_carta_1)
        self.cartas.append(esq_carta_2)
        self.cartas.append(esq_carta_3)
        for i in range(len(self.cartas)):
            self.cartas[i].x = (10 + (i * 70))
            self.cartas[i].y = 7

    def exibir(self, win):
        for i in range(len(self.cartas)):
            win.blit(self.cartas[i].sprite, (self.cartas[i].x, self.cartas[i].y))

