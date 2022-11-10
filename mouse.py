from esqueleto import *
from campo import *
from card_holder import *
from carta import *
from mana import *
import pygame

class Mouse():
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.unidade = None
        self.id = None
        self.mana = Mana(400, 16)

    def pegar_carta(self, card_hold):
        for carta in card_hold.cartas:
            if carta.x < self.x < carta.x + carta.largura:
                if carta.y < self.y < carta.y + carta.altura:
                    if pygame.mouse.get_pressed()[0]:
                        if self.unidade is None:
                            if carta.contador == 0:
                                self.unidade = carta.sprite_un
                                self.id = carta.id

    def soltar_carta(self):
        if self.unidade is not None:
                if pygame.mouse.get_pressed()[2]:
                    self.unidade = None
                    self.id = None

    def logica(self, card_hold):
        self.x, self.y = pygame.mouse.get_pos()
        self.pegar_carta(card_hold)
        self.soltar_carta()
        self.mana.logica()
        return card_hold

    def exibir(self, win):
        if self.unidade is not None:
            win.blit(self.unidade, (self.x - 32, self.y - 32))
        self.mana.exibir(win)




