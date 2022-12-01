

class Lugar():
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.tem_unidade = False

    def colidiu(self, x, y):
        if self.x < x < self.x + self.largura:
            if self.y < y < self.y + self.altura:
                return True
        return False