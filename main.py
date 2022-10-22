import pygame
from spritesheet import *
from tropas import *
from campo import *
pygame.init()

win = pygame.display.set_mode((768, 512))
pygame.display.set_caption("Tower of the Necrolord!")
bg_img = pygame.image.load('sprites/bg.png')
entidades = Tropas()
tabuleiro = Campo(704, 384, 50, 128)

run = True
while run:
    entidades.logica()
    x, y = pygame.mouse.get_pos()
    win.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            entidades.invocar_tropa(x, y, tabuleiro)
        if event.type == pygame.KEYDOWN:
            entidades.invocar_inimigo(x, y, tabuleiro)
    entidades.exibir(win)



    pygame.time.delay(60)
    pygame.display.update()