from botoes import *
from spritesheet import *

class Menu:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.fundo_ss = Spritesheet(pygame.image.load('sprites/fundo_menu.png').convert_alpha())
        self.botao = Spritesheet(pygame.image.load('sprites/botao64x32.png').convert_alpha())
        self.animacoes = []
        self.frame = 0
        self.creditos = pygame.image.load('sprites/creditos_msm.png').convert_alpha()
        self.como = pygame.image.load('sprites/como_jogar.png').convert_alpha()
        for i in range(1):
            sprites_vetor = []
            for j in range(15):
                sprites_vetor.append(self.fundo_ss.recortar_imagem(i, j, self.largura, self.altura, 1))
            self.animacoes.append(sprites_vetor)
        self.todos_botoes = []
        for i in range(3):
            self.todos_botoes.append(Butao(320, 201+(i*80), 64, 32, self.botao, 2, 1, 1, 1))
            self.todos_botoes[i].id = 1+i


    def logica(self, mx, my, como_tela, creditos_tela):
        if creditos_tela == True:
            self.todos_botoes.append(Butao(10, 420, 64, 32, self.botao, 2, 1, 1, 1))
            self.todos_botoes[3].id = 4
        if como_tela == True:
            self.todos_botoes.append(Butao(10, 420, 64, 32, self.botao, 2, 1, 1, 1))
            self.todos_botoes[3].id = 5




        if self.frame >= len(self.animacoes[0]) - 1:
            self.frame = 0
        else:
            self.frame += 0.3
        for i in self.todos_botoes:
            i.logica(mx, my)


    def exibir(self, win, como_tela, creditos_tela):
        if creditos_tela == True:
            win.blit(self.creditos, (0, 0))
            for i in self.todos_botoes:
                if i.id == 4:
                    i.exibir(win)
        elif como_tela == True:
            win.blit(self.como, (0, 0))
            for i in self.todos_botoes:
                if i.id == 5:
                    i.exibir(win)
        else:
            win.blit(self.animacoes[0][int(self.frame)], (0, 0))
            for i in self.todos_botoes:
                i.exibir(win)
