import pygame
from spritesheet import *
from tropas import *
pygame.init()

win = pygame.display.set_mode((768, 512))
pygame.display.set_caption("Tower of the Necrolord!")
bg_img = pygame.image.load('sprites/bg.png')
aliados = Tropas()
tabuleiro = Campo(704, 384, 50, 128)


run = True
while run:
    x, y = pygame.mouse.get_pos()
    win.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            aliados.invocar_tropa(x, y, tabuleiro)
    aliados.exibir(win)



    pygame.time.delay(60)
    pygame.display.update()