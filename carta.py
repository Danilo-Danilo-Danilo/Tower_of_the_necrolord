
class Carta():
    def __init__(self, sprite, sprite_un, id, recarga, taxa_de_recarga):
        self.id = id
        self.sprite_un = sprite_un
        self.x = None
        self.y = None
        self.sprite = sprite
        self.largura = 64
        self.altura = 64
        self.contador = 64
        self.recarga = recarga
        self.taxa_de_recarga = taxa_de_recarga
    def colidiu(self, x, y):
        if self.x < x < self.x + self.largura:
            if self.y < y < self.y + self.altura:
                return True
        return False
