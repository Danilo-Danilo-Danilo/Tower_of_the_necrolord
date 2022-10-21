import pygame
from spritesheet import *
from esqueleto import *
pygame.init()

win = pygame.display.set_mode((768, 512))
pygame.display.set_caption("Tower of the Necrolord!")
bg_img = pygame.image.load('sprites/bg.png')
esq_ss = Spritesheet(pygame.image.load('sprites/ss.png').convert_alpha())
esq = Esqueleto(100, 100, 32, 32, esq_ss, 5, 1)

run = True
while run:
    win.blit(bg_img, (0, 0))
    esq.logica()
    esq.exibir(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.time.delay(60)
    pygame.display.update()