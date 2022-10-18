import pygame

pygame.init()

win = pygame.display.set_mode((1000, 500))

pygame.display.set_caption("NECROLORDE!")

x = 500
y = 485
raio = 15
run = True
click1 = False
bg_img = pygame.image.load('background.png')
card_esq = pygame.image.load('carta_esqueleto.png')
un_esq = pygame.image.load('un_esqueleto.png')
bg = pygame.transform.scale(bg_img, (1000, 500))
carta_1 = (40, 15)
cartaf_1 = (92, 79)
c_esq = pygame.transform.scale(card_esq, (52, 64))
uni_esq = pygame.transform.scale(un_esq, (52, 64))
while run:

    win.blit(bg, (0, 0))
    win.blit(c_esq, carta_1)
    pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), raio)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    userInput = pygame.key.get_pressed()

    #Movimento
    if pygame.mouse.get_pressed() == (1, 0, 0) and carta_1 < pygame.mouse.get_pos() < cartaf_1:
        click1 = True

    if click1:
        carta_1 = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (0, 0, 1):
            click1 = False


    pygame.time.delay(15)

    pygame.display.update()
