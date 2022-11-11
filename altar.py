from entidade import *

class Altar(Entidade):

    id = 2
    tempo_recarga = 0
    vida = 240
    energia = 30
    tempo_de_animacao_da_gota = 0
    lado = 0
    def logica(self, mouse):
        if self.tempo_recarga == 80:
            self.tempo_recarga = 0
            mouse.mana.mana_tamanho += 5

        elif self.tempo_recarga < 80:
            self.tempo_recarga += 1
        if self.frame > len(self.animacoes[0]) -1:
            self.frame = 0
        else:
            self.frame += 0.5


    def exibir(self, win):
        win.blit(self.animacoes[0][int(self.frame)], (self.x, self.y))

