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
proximo_tela = False
game_over_tela = False
ganhou_tela = False
win = pygame.display.set_mode((768, 512))
pygame.display.set_caption("Tower of the Necrolord!")
bg_img = pygame.image.load('sprites/bg.png')
menu = Menu(768, 512)
sprite_carta = (pygame.transform.scale((pygame.image.load('sprites/card-skeleton-001.png')), (64, 64)))
"""lvl_1 = [0,240,552,888,1008,1092,1248,1260,1548,1584,1740,1742,1752,1980,
             1982,2100,2112,2436,2484,2496,2498,2508,2510,2520,2522]"""
lvl_1 = [0, 20]
"""lvl_2 = [1,180,340,460,520,580,700,743,751,820,888,912,925,978,984,1008,1064,1092,1120,1245,1248,1260,
             1345,1444,1488,1548,1584,1688,1700,1740,1742,1752,1794,1821,1865,1922,1964,1980,1982,2012,2022,
             2100,2112,2212,2268,2348,2401,2436,2455,2484,2496,2498,2508,2510,2512,2516,2518,2520,2522,2524,2533,2540]"""""
lvl_2 = [1, 20]
lvl = lvl_1
tela = 0
while rodando:
    tabuleiro = Campo(12, 6, 50, 128)
    entidades = Tropas(tabuleiro)
    mouse = Mouse()
    projeteis = Projeteis()
    card_holder = Card_Holder(3)
    mx, my = pygame.mouse.get_pos()
    menu.logica(mx, my, como_tela, creditos_tela, proximo_tela, game_over_tela, ganhou_tela)
    pygame.mixer.music.load('music/Graze the Roof.mp3')
    menu.exibir(win, como_tela, creditos_tela, tela, proximo_tela, game_over_tela, ganhou_tela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in menu.todos_botoes:
                if i.ta_clicando:
                    if i.id == 1:
                        jogando = True
                        pygame.mixer.music.play(-1, 0, 0)
                        menu.logica(mx, my, como_tela, creditos_tela, proximo_tela, game_over_tela, ganhou_tela)
                        pygame.display.update()
                        i.ta_clicando = False
                    if i.id == 2:
                        creditos_tela = True
                        menu.logica(mx, my, como_tela, creditos_tela, proximo_tela, game_over_tela, ganhou_tela)
                        pygame.display.update()
                        i.ta_clicando = False
                    if i.id == 3:
                        como_tela = True
                        menu.logica(mx, my, como_tela, creditos_tela, proximo_tela, game_over_tela, ganhou_tela)
                        pygame.display.update()
                        i.ta_clicando = False
            for i in menu.botoes_voltar:
                if i.ta_clicando:
                    if i.id == 4:
                        if creditos_tela == True or como_tela == True:
                            creditos_tela = False
                            como_tela = False
                            menu.botoes_voltar.clear()
                            i.ta_clicando = False
                    if i.id == 5:
                        if tela < 2:
                            tela += 1
                        elif tela == 2:
                            tela = 0
                            i.ta_clicando = False
            if proximo_tela:
                for i in menu.botoes_proximo:
                    if i.ta_clicando:
                        if i.id == 6:
                            lvl = lvl_2
                            pygame.mixer.music.play(-1, 0, 0)
                            proximo_tela = False
                            jogando = True
                            como_tela = False
                            creditos_tela = False
                            game_over_tela = False
                            i.ta_clicando = False
                        if i.id == 7:
                            proximo_tela = False
                            jogando = False
                            como_tela = False
                            creditos_tela = False
                            game_over_tela = False
                            i.ta_clicando = False
            if game_over_tela:
                for i in menu.botoes_gameover:
                    if i.ta_clicando:
                        if i.id == 8:
                            pygame.mixer.music.play(-1, 0, 0)
                            proximo_tela = False
                            jogando = True
                            como_tela = False
                            creditos_tela = False
                            game_over_tela = False
                            i.ta_clicando = False
                        if i.id == 9:
                            proximo_tela = False
                            jogando = False
                            como_tela = False
                            creditos_tela = False
                            game_over_tela = False
                            i.ta_clicando = False
            if ganhou_tela:
                for i in menu.botoes_ganhou:
                    if i.ta_clicando:
                        if i.id == 10:
                            lvl = lvl_1
                            ganhou_tela = False
                            proximo_tela = False
                            jogando = False
                            como_tela = False
                            creditos_tela = False
                            game_over_tela = False
                            i.ta_clicando = False

    pygame.time.delay(60)
    pygame.display.update()

    while jogando:
        concluiu = entidades.spawn_inimigos(lvl)
        entidades.logica(mouse)
        projeteis = entidades.atirar(projeteis)
        x, y = pygame.mouse.get_pos()
        mouse.logica(card_holder)
        win.blit(bg_img, (0, 0))
        card_holder.exibir(win)
        card_holder.logica()
        mouse.exibir(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                lvl = lvl_1
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse, card_holder = entidades.invocar_tropa(x, y, tabuleiro, mouse, card_holder)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if lvl == lvl_1:
                        proximo_tela = True
                        jogando = False
                    elif lvl == lvl_2:
                        jogando = False
                        ganhou_tela = True



        entidades.exibir(win)
        projeteis.exibir(win)
        entidades.matriz_inimigos = projeteis.colisao(entidades.matriz_inimigos, entidades.matriz_tropas)
        for i in entidades.matriz_inimigos:
            entidades.matriz_tropas = i.atacar(entidades.matriz_tropas)
        pygame.time.delay(60)
        pygame.display.update()
        if entidades.perdeu:
            game_over_tela = True
            jogando = False
            creditos_tela = False
            como_tela = False
            proximo_tela = False

        if concluiu:
            if lvl[0] == 0:
                proximo_tela = True
                jogando = False
            if lvl[0] == 1:
                ganhou_tela = True
                jogando = False
            jogando = False