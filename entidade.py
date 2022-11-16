from abc import ABC, abstractmethod
from spritesheet import *
import pygame

class Entidade(ABC):
    def __init__(self, x, y, largura, altura, sprites, max_frames, max_linhas, linha, coluna, escala, textobt):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.frame = 0
        self.linha = linha
        self.coluna = coluna
        self.animacoes = []
        self.escala = escala
        self.font = pygame.font.Font('font/alagard.ttf', 28)
        self.white = (255, 255, 255)
        self.textobt = textobt
        self.text = self.font.render(self.textobt, True, self.white)
        for i in range(max_linhas):
            sprites_vetor = []
            for j in range(max_frames):
                sprites_vetor.append(sprites.recortar_imagem(i, j, largura, altura, self.escala))
            self.animacoes.append(sprites_vetor)

    @abstractmethod
    def logica(self):
        pass

    @abstractmethod
    def exibir(self, win):
        pass

