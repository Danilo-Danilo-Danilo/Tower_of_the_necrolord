import pygame
from carta import *
from spritesheet import *

class Card_Holder():

    def __init__(self, qnt):
        esqueleto_sprite = pygame.transform.scale(pygame.image.load('sprites/skeleton-turret-001.png'), (64, 64))
        carta_esqueleto = pygame.transform.scale(pygame.image.load('sprites/card-skeleton-001.png'), (64, 64))
        altar_sprite = pygame.transform.scale(pygame.image.load('sprites/altar_sprite1.png'), (64, 64))
        carta_altar = pygame.transform.scale(pygame.image.load('sprites/card_altar-export.png'), (64, 64))
        tank_sprite = pygame.transform.scale(pygame.image.load('sprites/skeleto_tank.png'), (64, 64))
        carta_tank = pygame.transform.scale(pygame.image.load('sprites/card-tank.png'), (64, 64))
        self.carta_carregando = pygame.transform.scale(pygame.image.load('sprites/carregando.png'), (64, 64))
        self.cartas = []
        self.cartas.append(Carta(carta_esqueleto, esqueleto_sprite, 1, 64))
        self.cartas.append(Carta(carta_altar, altar_sprite, 2, 64))
        self.cartas.append(Carta(carta_tank, tank_sprite, 3, 64))

        for i in range(len(self.cartas)):
            self.cartas[i].x = (10 + (i * 70))
            self.cartas[i].y = 7

    def exibir(self, win):
        for i in range(len(self.cartas)):
            win.blit(self.cartas[i].sprite, (self.cartas[i].x, self.cartas[i].y))
            if self.cartas[i].contador > 0:
                self.carta_carregando = pygame.transform.scale(self.carta_carregando, (64, self.cartas[i].contador))
                win.blit(self.carta_carregando, (self.cartas[i].x, self.cartas[i].y + (self.cartas[i].altura - self.cartas[i].contador)))

    def logica(self):
        for i in range(len(self.cartas)):
            if self.cartas[i].contador > 0:
                self.cartas[i].contador -= 1
