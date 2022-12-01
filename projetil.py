

class Projetil():
    def __init__(self, sprite, x, y, vel, dano, lado):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.vel = vel
        self.dano = dano
        self.lado = lado
    def movimento(self):
        self.x += self.vel

    def exibirp(self, win):
        win.blit(self.sprite, (self.x, self.y))

