import pygame

pygame.init()

win = pygame.display.set_mode((768, 512))

pygame.display.set_caption("NECROLORDE!")


class Unidade:

    def __init__(self, hp, ataque, sprite):
        self.hp = hp
        self.ataque = ataque
        self.sprite = sprite
        self.select = False


class Carta:
    def __init__(self, pos, sprite, unidade, custo):
        self.x, self.y = pos
        self.sprite = sprite
        self.unidade = unidade
        self.custo = custo
        self.size = None
        self.surface = None
        self.rect = None
        self.criar_surface()

    def show(self):
        win.blit(self.sprite, (self.x, self.y))

    def criar_surface(self):
        """Pega o tamanho do sprite da carta"""
        self.size = self.sprite.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.blit(self.sprite, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def spawn_uni(self, event):
        """"Quando clicar na carta faz unidade seguir mouse até clicar com botão
            esquerdo ou coloca-la no mapa"""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.unidade.select = True
        if self.unidade.select:
            win.blit(self.unidade.sprite, (x, y))
            if pygame.mouse.get_pressed() == (0, 0, 1):
                self.unidade.select = False


run = True
bg_img = pygame.image.load('background.png')
card_esq = pygame.image.load('carta_esqueleto.png')
un_esq = pygame.image.load('un_esqueleto.png')
bg = pygame.transform.scale(bg_img, (789, 512))
carta_1 = [40, 15]
tam_carta = (52, 64)
c_esq = pygame.transform.scale(card_esq, tam_carta)
uni_esq = pygame.transform.scale(un_esq, tam_carta)

esqueleto = Unidade(100, 100, uni_esq)
carta_esqueleto = Carta((7, 7), c_esq, esqueleto, 100)
while run:

    win.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    carta_esqueleto.show()
    carta_esqueleto.spawn_uni(event)

    pygame.time.delay(15)

    pygame.display.update()
