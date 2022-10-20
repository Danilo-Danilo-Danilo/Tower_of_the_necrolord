import pygame
import numpy as np

pygame.init()

win = pygame.display.set_mode((768, 512))

pygame.display.set_caption("NECROLORDE!")


class Unidade:

    def __init__(self, hp, ataque, sprite):
        self.hp = hp
        self.ataque = ataque
        self.sprite = sprite
        self.select = False


class Lugar:
    def __init__(self, pos):
        self.x, self.y = pos
        self.unidade = None
        self.rect = None
        self.surface = None
        self.criar_surface()

    def criar_surface(self):
        """Pega o tamanho do sprite da carta"""
        self.size = (64, 64)
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def colocar_unidade(self, event, unit):
        """"Coloca unidade selecionada em um espaço"""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if unit is not None:
                        self.unidade = unit

                        unit = None
        self.mostrar_unidade()
        return unit

    def mostrar_unidade(self):
        """Mostra a unidade no espaço"""
        if self.unidade is not None:
            win.blit(self.unidade.sprite, (self.x + 8, self.y - 16))


class Tabuleiro:
    """"Cria tabuleiro que é uma matriz de lugares"""

    def __init__(self, pos_ini):
        self.pos_ini = pos_ini
        self.lugar = []
        for i in range(11):
            lugar_linha = []
            for j in range(6):
                if i == 0 and j == 0:
                    lugar_linha.append(Lugar(pos_ini))
                else:
                    pos_atual = (pos_ini[0] + (i * 64)), (pos_ini[1] + (j * 64))
                    lugar_linha.append(Lugar(pos_atual))
            self.lugar.append(lugar_linha)


class Carta:
    def __init__(self, pos, sprite, unidade, custo):
        self.x, self.y = pos
        self.sprite = sprite
        self.unidade = unidade
        self.custo = custo
        self.size = None
        self.surface = None
        self.rect = None
        self.criar_surface()

    def show(self):
        """"Mostra carta"""
        win.blit(self.sprite, (self.x, self.y))

    def criar_surface(self):
        """Pega o tamanho do sprite da  e faz uma superficie"""
        self.size = self.sprite.get_size()
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def spawn_uni(self, event, um):
        """"Quando clicar na carta faz unidade seguir mouse até clicar com botão
            esquerdo ou coloca-la no mapa"""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.unidade.select = True
                    um = self.unidade
        if self.unidade.select:
            if um is None:
                self.unidade.select = False
            win.blit(self.unidade.sprite, (x - 32, y - 32))
            if pygame.mouse.get_pressed()[2]:
                self.unidade.select = False
                um = None
        return um


run = True
bg_img = pygame.image.load('background.png')
card_esq = pygame.image.load('sprites\card-skeleton-001.png')
un_esq = pygame.image.load('sprites\skeleton-turret-001.png')
bg = (pygame.transform.scale(bg_img, (768, 512)))
carta_1 = [40, 15]
tam_carta = (64, 64)
c_esq = pygame.transform.scale(card_esq, tam_carta)
uni_esq = pygame.transform.scale(un_esq, tam_carta)
unidade_mouse = None
esqueleto = Unidade(100, 100, uni_esq)
carta_esqueleto = Carta((7, 7), c_esq, esqueleto, 100)
lugar1 = Lugar((22, 128))
tabuleiro = Tabuleiro((22, 128))

while run:

    win.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    carta_esqueleto.show()
    unidade_mouse = carta_esqueleto.spawn_uni(event, unidade_mouse)
    for i in range(11):
        for j in range(6):
            unidade_mouse = tabuleiro.lugar[i][j].colocar_unidade(event, unidade_mouse)

    pygame.time.delay(15)

    pygame.display.update()
