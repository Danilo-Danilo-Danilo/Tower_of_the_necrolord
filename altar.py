from entidade import *

class Altar(Entidade):

    id = 2
    tempo_recarga = 0
    vida = 300
    energia = 30
    tempo_de_animacao_da_gota = 0

    def logica(self, mouse):
        if self.tempo_recarga == 60:
            self.tempo_recarga = 0
            mouse.mana.mana_tamanho += 20

        elif self.tempo_recarga < 60:
            self.tempo_recarga += 1
        if self.frame > len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.5


    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

