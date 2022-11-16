from botoes import *
from spritesheet import *

class Menu:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.fundo_ss = Spritesheet(pygame.image.load('sprites/ss_menu.png').convert_alpha())
        self.botao = Spritesheet(pygame.image.load('sprites/botao64x32.png').convert_alpha())
        self.botaot = Spritesheet(pygame.image.load('sprites/botaot64x32.png').convert_alpha())
        self.botaoti = Spritesheet(pygame.image.load('sprites/botaoti64x32.png').convert_alpha())
        self.animacoes = []
        self.botoes_voltar = []
        self.botoes_gameover = []
        self.botoes_proximo = []
        self.botoes_ganhou = []
        self.frame = 0
        self.tela = 0
        self.creditos = pygame.image.load('sprites/creditos_msm.png').convert_alpha()
        self.como = []
        self.como.append(pygame.transform.scale(pygame.image.load('sprites/regras.png'), (768, 512)))
        self.como.append(pygame.transform.scale(pygame.image.load('sprites/regras_2.png'), (768, 512)))
        self.como.append(pygame.transform.scale(pygame.image.load('sprites/regras_3.png'), (768, 512)))
        self.font = pygame.font.Font('font/alagard.ttf', 32)
        self.white = (255, 255, 255)
        self.text = self.font.render("Nivel Concluido", True, self.white)
        self.text2 = self.font.render("PERDEU!!!", True, self.white)
        self.text3 = self.font.render("Parabens ai Ganhou hein!!!", True, self.white)
        for i in range(1):
            sprites_vetor = []
            for j in range(29):
                sprites_vetor.append(self.fundo_ss.recortar_imagem(i, j, self.largura, self.altura, 1))
            self.animacoes.append(sprites_vetor)
        self.todos_botoes = []
        for i in range(3):
            if i == 0:
                self.todos_botoes.append(Butao(320, 201 + (i * 80), 64, 32, self.botao, 2, 1, 1, 1, 2, "Jogar"))
                self.todos_botoes[i].larguratxt = 32
                self.todos_botoes[i].alturatxt = 16
            elif i == 1:
                self.todos_botoes.append(Butao(320, 201 + (i * 80), 64, 32, self.botao, 2, 1, 1, 1, 2, "Creditos"))
                self.todos_botoes[i].larguratxt = 10
                self.todos_botoes[i].alturatxt = 16
            elif i == 2:
                self.todos_botoes.append(Butao(320, 201 + (i * 80), 64, 32, self.botao, 2, 1, 1, 1, 2, "Tutorial"))
                self.todos_botoes[i].larguratxt = 10
                self.todos_botoes[i].alturatxt = 16
            self.todos_botoes[i].id = 1+i



    def logica(self, mx, my, como_tela, creditos_tela, proximo_tela, game_over_tela, ganhou_tela):
        if creditos_tela or como_tela or proximo_tela or game_over_tela or ganhou_tela:
            if creditos_tela:
                self.botoes_voltar.append(Butao(2, 460, 64, 32, self.botaoti, 2, 1, 1, 1, 1, ""))
                self.botoes_voltar[0].id = 4
            elif como_tela:
                self.botoes_voltar.append(Butao(2, 460, 64, 32, self.botaoti, 2, 1, 1, 1, 1, ''))
                self.botoes_voltar[0].id = 4
                self.botoes_voltar.append(Butao(702, 460, 64, 32, self.botaot, 2, 1, 1, 1, 1, ''))
                self.botoes_voltar[1].id = 5
            elif proximo_tela:
                if self.botoes_proximo == []:
                    self.botoes_proximo.append(Butao(320, 301, 64, 32, self.botao, 2, 1, 1, 1, 2, "Nivel 2"))
                    self.botoes_proximo[0].larguratxt = 20
                    self.botoes_proximo[0].alturatxt = 16
                    self.botoes_proximo[0].id = 6
                    self.botoes_proximo.append(Butao(320, 381, 64, 32, self.botao, 2, 1, 1, 1, 2, "Menu"))
                    self.botoes_proximo[1].larguratxt = 28
                    self.botoes_proximo[1].alturatxt = 16
                    self.botoes_proximo[1].id = 7
            elif game_over_tela:
                if self.botoes_gameover == []:
                    self.botoes_gameover.append(Butao(320, 301, 64, 32, self.botao, 2, 1, 1, 1, 2, "Novamente"))
                    self.botoes_gameover[0].larguratxt = 10
                    self.botoes_gameover[0].alturatxt = 16
                    self.botoes_gameover[0].id = 8
                    self.botoes_gameover.append(Butao(320, 381, 64, 32, self.botao, 2, 1, 1, 1, 2, "Menu"))
                    self.botoes_gameover[1].larguratxt = 28
                    self.botoes_gameover[1].alturatxt = 16
                    self.botoes_gameover[1].id = 9
            elif ganhou_tela:
                if self.botoes_ganhou == []:
                    self.botoes_ganhou.append(Butao(320, 301, 64, 32, self.botao, 2, 1, 1, 1, 2, "Menu"))
                    self.botoes_ganhou[0].larguratxt = 28
                    self.botoes_ganhou[0].alturatxt = 16
                    self.botoes_ganhou[0].id = 10
            else:
                self.botoes_ganhou.clear()
                self.botoes_voltar.clear()
                self.botoes_gameover.clear()

        if self.frame >= len(self.animacoes[0]) - 1:
            self.frame = 0
        else:
            self.frame += 0.3
        if creditos_tela or como_tela:
            for i in self.botoes_voltar:
                i.logica(mx, my)
        elif proximo_tela:
            for i in self.botoes_proximo:
                i.logica(mx, my)
        elif game_over_tela:
            for i in self.botoes_gameover:
                i.logica(mx, my)
        elif ganhou_tela:
            for i in self.botoes_ganhou:
                i.logica(mx, my)
        else:
            for i in self.todos_botoes:
                i.logica(mx, my)
    def exibir(self, win, como_tela, creditos_tela, tela, proximo_tela, game_over_tela, ganhou_tela):
        if creditos_tela == True:
            win.blit(self.creditos, (0, 0))
            for i in self.botoes_voltar:
                i.exibir(win)
        elif como_tela == True:
            win.blit(self.como[tela], (0, 0))
            for i in self.botoes_voltar:
                i.exibir(win)
        elif proximo_tela:
            win.blit(pygame.image.load('sprites/quadrado-preto.png'), (0, 0))
            win.blit(self.text,(282, 201))
            for i in self.botoes_proximo:
                i.exibir(win)
        elif game_over_tela:
            win.blit(pygame.image.load('sprites/quadrado-preto.png'), (0, 0))
            win.blit(self.text2, (282, 201))
            for i in self.botoes_gameover:
                i.exibir(win)
        elif ganhou_tela:
            win.blit(pygame.image.load('sprites/quadrado-preto.png'), (0, 0))
            win.blit(self.text3, (282, 201))
            for i in self.botoes_ganhou:
                i.exibir(win)
        else:
            win.blit(self.animacoes[0][int(self.frame)], (0, 0))
            for i in self.todos_botoes:
                i.exibir(win)