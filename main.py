import pygame.mouse
from esqueleto import *
from mouse import *
from projeteis import *
from menu import *
pygame.init()

rodando = True
jogando = False
creditos_tela = False
como_tela = False

while rodando:
    win = pygame.display.set_mode((768, 512))
    pygame.display.set_caption("Tower of the Necrolord!")
    bg_img = pygame.image.load('sprites/bg.png')
    creditos = pygame.image.load('sprites/creditos_msm.png').convert_alpha()
    como = pygame.image.load('sprites/como_jogar.png')
    menu = Menu(768, 512)
    sprite_carta = (pygame.transform.scale((pygame.image.load('sprites/card-skeleton-001.png')), (64, 64)))
    tabuleiro = Campo(12, 6, 50, 128)
    entidades = Tropas(tabuleiro)
    mouse = Mouse()
    projeteis = Projeteis()
    card_holder = Card_Holder(3)
    tempo = 1
    level_1 = [1, 1, 1, 2, 2, 2, 3, 4, 6, 8]
    mx, my = pygame.mouse.get_pos()
    menu.logica(mx, my)
    menu.exibir(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in menu.todos_botoes:
                if i.ta_clicando:
                    if i.id == 1:
                        jogando = True
                    if i.id == 2:
                        creditos_tela = True
                    if i.id == 3:
                        como_tela = True
    pygame.time.delay(60)
    pygame.display.update()

    while creditos_tela:
        win.blit(creditos, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                creditos_tela = False

    while como_tela:
        win.blit(como, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                como_tela = False

    while jogando:
        entidades.spawn_inimigos(tempo, level_1)
        entidades.logica(mouse)
        projeteis = entidades.atirar(projeteis)
        x, y = pygame.mouse.get_pos()
        mouse.logica(card_holder)
        win.blit(bg_img, (0, 0))
        card_holder.exibir(win)
        mouse.exibir(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = entidades.invocar_tropa(x, y, tabuleiro, mouse)
            if event.type == pygame.KEYDOWN:
                entidades.invocar_inimigos(x, y, tabuleiro)
        entidades.exibir(win)
        projeteis.exibir(win)
        entidades.matriz_inimigos = projeteis.colisao(entidades.matriz_inimigos)
        for i in entidades.matriz_inimigos:
            entidades.matriz_tropas = i.atacar(entidades.matriz_tropas)

        tempo += 1
        pygame.time.delay(60)
        pygame.display.update()
