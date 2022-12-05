

class Lugar():
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.tem_unidade = False

    def colidiu(self, x, y):
        if x == None or y == None:
            return None
        else:
            if self.colidiux(x):
                if self.colidiuy(y):
                    return True
            return False
    def colidiux(self, x):
        if x == None:
            return None
        else:
            if self.x < x < self.x + self.largura:
                return True
            else:
                return False
    def colidiuy(self, y):
        if y == None:
            return None
        else:
            if self.y < y < self.y + self.altura:
                return True
            else:
                return False