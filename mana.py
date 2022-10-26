import pygame
from entidade import *

class Mana():
    def __init__(self, x, y):
        self.mana_total = 256
        self.mana_ps = 10
        self.mana_tamanho = 24
        self.sprite_back = pygame.transform.scale(pygame.image.load('sprites/mana-back.png'), (self.mana_total + 8, 18))
        self.sprite_fro = pygame.transform.scale(pygame.image.load('sprites/mana-glass.png'), (self.mana_total + 8, 24))
        self.sprite = pygame.image.load('sprites/mana.png')
        self.barra = pygame.transform.scale(self.sprite, (self.mana_tamanho, 24))
        self.x = x
        self.y = y
        self.font = pygame.font.Font('font/alagard.ttf', 16)
        self.white = (255, 255, 255)
    def logica(self):
        self.barra = pygame.transform.scale(self.sprite, (self.mana_tamanho, 24))
        if self.mana_tamanho < self.mana_total:
            self.mana_tamanho += self.mana_ps
        if self.mana_tamanho > self.mana_total:
            self.mana_tamanho = self.mana_total
        mana_atual = str(self.mana_tamanho)
        mana_de = "/"
        mana_tt = str(self.mana_total)
        mana_texto = (mana_atual + mana_de + mana_tt)
        self.text = self.font.render(mana_texto, True, self.white)


    def exibir(self, win):
        win.blit(self.sprite_back, (self.x - 4, self.y + 3))
        win.blit(self.barra, (self.x, self.y))
        win.blit(self.sprite_fro, (self.x - 4, self.y))
        x, y = pygame.mouse.get_pos()
        if (self.x <= x <= self.x + self.mana_total) and (self.y <= y <= self.y + 24):
            win.blit(self.text,(self.x + 104, self.y + 6))


