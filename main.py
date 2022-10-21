import pygame

pygame.init()

win = pygame.display.set_mode((768, 512))

pygame.display.set_caption("Tower of the Necrolord!")

class Projetil:

    def __init__(self, pos, sprite):
        self.x = pos[0]
        self.y = pos[1]
        self.sprite = sprite
    def draw_projetil(self):
        win.blit(ata_esq, (self.x, self.y))

    def mover(self):
        self.x += 1

    def fora_da_tela(self):
        if self.x > 768:
            return True
        elif self.x <= 768:
            return False

class Inimigo:
    def __init__(self, hp, ataque, sprite):
        self.hp = hp
        self.ataque = ataque
        self.sprite = sprite
        self.x = None
        self.y = None
        self.linha = None

    def spawn(self, linha):
        self.x = 780
        self.y = 112 + (64 * linha)
        self.linha = linha
        return linha

    def mover(self):
        if self.x is not None:
            self.x -= 1
            win.blit(self.sprite, (self.x, self.y))


class Unidade:

    def __init__(self, hp, ataque, sprite, sprite_ataque):
        self.hp = hp
        self.ataque = ataque
        self.sprite = sprite
        self.select = False
        self.sprite_ataque = sprite_ataque
        self.cooldown_cont = 0

    def cooldown(self):
        if self.cooldown_cont >= 10:
            self.cooldown_cont = 0
        elif self.cooldown_cont > 0:
            self.cooldown_cont += 1
class Lugar:
    def __init__(self, pos, linha):
        self.x, self.y = pos
        self.linha = linha
        self.unidade = None
        self.rect = None
        self.surface = None
        self.criar_surface()

    def criar_surface(self):
        """Pega o tamanho do sprite da carta"""
        self.size = (64, 64)
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def colocar_unidade(self, event, unit, inimigos, projeteis):
        """"Coloca unidade selecionada em um espaço"""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if unit is not None:
                        self.unidade = unit

                        unit = None
        bala = self.mostrar_unidade(inimigos)
        if bala is not None:
            projeteis.append(bala)
        for bala in projeteis:
            bala.draw_projetil()
            bala.mover()
        return unit

    def mostrar_unidade(self, inimigos):
        """Mostra a unidade no espaço"""

        if self.unidade is not None:
            self.unidade.cooldown()
            win.blit(self.unidade.sprite, (self.x + 8, self.y - 16))
            for i in range(len(inimigos)):
                if (inimigos[i].linha == self.linha) and (self.unidade.cooldown_cont == 0) :
                    bala = Projetil((self.x, self.y), self.unidade.sprite_ataque)
                    self.unidade.cooldown_cont = 1
                    return bala
        else:
            return None







class Tabuleiro:
    """"Cria tabuleiro que é uma matriz de lugares"""

    def __init__(self, pos_ini):
        self.pos_ini = pos_ini
        self.lugar = []
        for i in range(11):
            lugar_linha = []
            for j in range(6):
                if i == 0 and j == 0:
                    lugar_linha.append(Lugar(pos_ini, j))
                else:
                    pos_atual = (pos_ini[0] + (i * 64)), (pos_ini[1] + (j * 64))
                    lugar_linha.append(Lugar(pos_atual, j))
            self.lugar.append(lugar_linha)


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
        """"Mostra carta"""
        win.blit(self.sprite, (self.x, self.y))

    def criar_surface(self):
        """Pega o tamanho do sprite da  e faz uma superficie"""
        self.size = self.sprite.get_size()
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def spawn_uni(self, event, um):
        """"Quando clicar na carta faz unidade seguir mouse até clicar com botão
            esquerdo ou coloca-la no mapa"""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.unidade.select = True
                    um = self.unidade
        if self.unidade.select:
            if um is None:
                self.unidade.select = False
            win.blit(self.unidade.sprite, (x - 32, y - 32))
            if pygame.mouse.get_pressed()[2]:
                self.unidade.select = False
                um = None
        return um


run = True
bg_img = pygame.image.load('background.png')
card_esq = pygame.image.load('sprites\card-skeleton-001.png')
un_esq = pygame.image.load('sprites\skeleton-turret-001.png')
in_mago = pygame.image.load('sprites\mage-001.png')
ataque_esq = pygame.image.load('sprites\sbrick.png')
ata_esq = pygame.transform.scale(ataque_esq, (32, 32))
bg = (pygame.transform.scale(bg_img, (768, 512)))
carta_1 = [40, 15]
tam_carta = (64, 64)
c_esq = pygame.transform.scale(card_esq, tam_carta)
uni_esq = pygame.transform.scale(un_esq, tam_carta)
mago = pygame.transform.scale(in_mago, tam_carta)
unidade_mouse = None
esqueleto = Unidade(100, 100, uni_esq, ata_esq)
carta_esqueleto = Carta((7, 7), c_esq, esqueleto, 100)
maguin = Inimigo(40, 60, mago)
tabuleiro = Tabuleiro((22, 128))
inimigos = []
projeteis = []
while run:

    win.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                maguin.spawn(0)
            if event.key == pygame.K_2:
                maguin.spawn(1)
            if event.key == pygame.K_3:
                maguin.spawn(2)
            if event.key == pygame.K_4:
                maguin.spawn(3)
            if event.key == pygame.K_5:
                maguin.spawn(4)
            if event.key == pygame.K_6:
                maguin.spawn(5)
        inimigos.append(maguin)
        if event.type == pygame.QUIT:
            run = False

    carta_esqueleto.show()
    unidade_mouse = carta_esqueleto.spawn_uni(event, unidade_mouse)
    for i in range(11):
        for j in range(6):
            unidade_mouse = tabuleiro.lugar[i][j].colocar_unidade(event, unidade_mouse, inimigos, projeteis)

    maguin.mover()

    pygame.time.delay(15)

    pygame.display.update()
