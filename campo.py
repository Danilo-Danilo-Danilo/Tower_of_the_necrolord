from ponto_invoc import *

class Campo:
    def __init__(self, largura, altura, x, y):
        self.x = x
        self.y = y
        self.blocos = []
        self.largura = largura
        self.altura = altura
        for i in range(largura):
            for j in range(altura):
                self.blocos[i].append(Lugar((i * 64) + x), (j * 64) + y, 64, 64)

    def invocar_em(self, x, y):
        for i in range(self.largura):
            for j in range(self.altura):
                if self.blocos[i][j].colidiu(x, y):
                    ponto = [i, j]
                    return ponto
        return None