from botoes import *
from spritesheet import *

class Menu:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.fundo_ss = Spritesheet(pygame.image.load('sprites/fundo_menu.png').convert_alpha())
        self.botao = Spritesheet(pygame.image.load('sprites/bt-jogar.png').convert_alpha())
        self.animacoes = []
        self.frame = 0
        self.creditos = pygame.image.load('sprites/CREDITOS.png').convert_alpha()
        for i in range(1):
            sprites_vetor = []
            for j in range(15):
                sprites_vetor.append(self.fundo_ss.recortar_imagem(i, j, self.largura, self.altura, 1))
            self.animacoes.append(sprites_vetor)
        self.todos_botoes = []
        for i in range(3):
            self.todos_botoes.append(Butao(320, 201+(i*80), 32, 32, self.botao, 1, 1, 1, 1))
            self.todos_botoes[i].id = 1+i


    def logica(self, mx,my):
        if self.frame >= len(self.animacoes[0]) - 1:
            self.frame = 0
        else:
            self.frame += 0.3
        for i in self.todos_botoes:
            i.logica(mx, my)


    def exibir(self, win, ):
        win.blit(self.animacoes[0][int(self.frame)], (0, 0))
        for i in self.todos_botoes:
            i.exibir(win)
