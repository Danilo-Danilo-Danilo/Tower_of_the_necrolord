from ponto_invoc import *

class Campo:
    def __init__(self, largura, altura, x, y):
        self.x = x
        self.y = y
        self.blocos = []
        self.largura = largura
        self.altura = altura
        for i in range(largura):
            linha = []
            for j in range(altura):
                linha.append(Lugar((i * 64) + x, (j * 64) + y, 64, 64))
            self.blocos.append(linha)

    def invocar_em(self, x, y):
        for i in range(self.largura):
            for j in range(self.altura):
                if self.blocos[i][j].colidiu(x, y):
                    if self.blocos[i][j].tem_unidade == False:
                        ponto = [self.blocos[i][j].x + 4, self.blocos[i][j].y - 26]
                        self.blocos[i][j].tem_unidade = True
                        return ponto
        return None
