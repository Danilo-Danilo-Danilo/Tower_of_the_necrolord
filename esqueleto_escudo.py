from entidade import *

class Esqueleto_Tank(Entidade):
    id = 3
    vida = 3000
    lado = 0

    def logica(self, mouse):
        if self.frame > len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.5


    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

