from entidade import *

class Altar(Entidade):
    id = 2
    tempo_recarga = 300
    vida = 300
    energia = 30

    def logica(self, matriz_tropas):
        if self.energia == 120:
            self.energia = 30
        else:
            self.energia += 1
        if self.frame > len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.5


    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))
