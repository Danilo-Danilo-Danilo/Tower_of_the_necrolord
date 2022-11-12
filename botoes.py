from entidade import *
from pygame import *

class Butao(Entidade):
    id = 0
    ta_clicando = False

    def logica(self, mx, my):
        if self.clicou(mx, my):
            self.frame = 1
        else:
            self.frame = 0

    def clicou(self, x, y):
        if self.x  < x < self.x + self.largura*2:
            if self.y < y < self.y + self.altura*2:
                self.ta_clicando = True
                return True
        self.ta_clicando = False
        return False

    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))