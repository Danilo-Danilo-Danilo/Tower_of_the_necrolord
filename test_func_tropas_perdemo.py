import pytest
from tropas import *

def run_tropas():
    pygame.init()
    pygame.display.set_mode((768, 512))
    test_lvl = [0, 1]
    tropas = Tropas(Campo(12, 6, 50, 128))
    tropas.tempo = 1
    tropas.spawn_inimigos(test_lvl)
    return tropas
def add_enemies(tropas, qnt):
    for i in range(qnt + 1):
        tropas.spawn_inimigos([0,1])
#teste com 10 inimigos dentro e todos com x inicial = 780
def test_func_must_return_false_01():
    tropas = run_tropas()
    add_enemies(tropas, 10)
    assert tropas.perdemo(tropas.entidades['inimigos']) == False
#teste com um inimigo dentro do dicionario de entidades e com o x inicial = 780
def test_func_must_return_false_02():
    tropas = run_tropas()
    assert tropas.perdemo(tropas.entidades['inimigos']) == False
#teste com 10 inimigos e todos com seu x + 64 <= 0
def test_func_must_return_True_03():
    tropas = run_tropas()
    add_enemies(tropas, 10)
    tropas.entidades['inimigos'][0].x = -64
    assert tropas.perdemo(tropas.entidades['inimigos']) == True
#testo com um inimigo dentro do dicionario e com seu x + 64 <= 0
def test_func_must_return_True_04():
    tropas = run_tropas()
    tropas.entidades['inimigos'][0].x = -64
    assert tropas.perdemo(tropas.entidades['inimigos']) == True