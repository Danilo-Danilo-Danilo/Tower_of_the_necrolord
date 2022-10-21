import pygame
from abc import ABC, abstractmethod

class Spritesheet:
    def __init__(self,img):
        self.imagem = img

    def recortar_imagem(self, linha, coluna, largura, altura, escala):
        img = pygame.Surface((largura, altura)).convert_alpha()
        img.blit(self.imagem, (0, 0), ((coluna * largura), (linha * altura), largura, altura))
        img = pygame.transform.scale(img, (largura * escala, altura * escala))
        img.set_colorkey((0, 0, 0))
        return img