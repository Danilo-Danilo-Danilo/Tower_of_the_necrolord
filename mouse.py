from esqueleto import *
from campo import *
from card_holder import *
from carta import *
import pygame

class Mouse():
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.unidade = None

    def pegar_carta(self, card_hold):
        for carta in card_hold.cartas:
            if carta.x < self.x < carta.x + carta.largura:
                if carta.y < self.y < carta.y + carta.altura:
                    if pygame.mouse.get_pressed()[0]:
                        if self.unidade is None:
                            self.unidade = carta.sprite_un
                            print("Esqueleto")

    def soltar_carta(self):
        if self.unidade is not None:
                if pygame.mouse.get_pressed()[2]:
                    self.unidade = None

    def logica(self):
        self.x, self.y = pygame.mouse.get_pos()

    def exibir(self, win):
        if self.unidade is not None:
            win.blit(self.unidade, (self.x, self.y))


