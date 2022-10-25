import pygame
from tropas import *
from campo import *
from card_holder import *
from mouse import *
from projeteis import *
from mana import *
from carta import Carta
from esqueleto import Esqueleto
pygame.init()

win = pygame.display.set_mode((768, 512))
pygame.display.set_caption("Tower of the Necrolord!")
bg_img = pygame.image.load('sprites/bg.png')
sprite_carta = (pygame.transform.scale((pygame.image.load('sprites/card-skeleton-001.png')), (64, 64)))
tabuleiro = Campo(12, 6, 50, 128)
entidades = Tropas(tabuleiro)
mouse = Mouse()
projeteis = Projeteis()
card_holder = Card_Holder(3)
manabar = Mana(400, 16)
run = True
while run:
    entidades.logica()
    manabar.logica()
    projeteis = entidades.atirar(projeteis)
    x, y = pygame.mouse.get_pos()
    mouse.logica(card_holder)
    win.blit(bg_img, (0, 0))
    card_holder.exibir(win)
    mouse.exibir(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = entidades.invocar_tropa(x, y, tabuleiro, mouse)
        if event.type == pygame.KEYDOWN:
            entidades.invocar_inimigos(x, y, tabuleiro)
    entidades.exibir(win)
    projeteis.exibir(win)
    manabar.exibir(win)



    pygame.time.delay(60)
    pygame.display.update()