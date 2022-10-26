import pygame

class Projetil():
    def __init__(self, sprite, x, y, vel):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.vel = vel

    def movimento(self):
        self.x += self.vel

    def exibirp(self, win):
        win.blit(self.sprite, (self.x, self.y))

