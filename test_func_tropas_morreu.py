import pytest
from tropas import *

def run_tropas():
    pygame.init()
    pygame.display.set_mode((768, 512))
    tropas = Tropas(Campo(12, 6, 50, 128))
    tropas.entidades['aliados'].append(Esqueleto(0, 0, 32, 32, tropas.esq_ss, 5, 2, 0, 0, 2, ""))
    return tropas

def add_allies(tropas, qnt):
    for i in range(qnt + 1):
        tropas.entidades['aliados'].append(Esqueleto(0, 0, 32, 32, tropas.esq_ss, 5, 2, 0, 0, 2, ""))

def reset_all_allies_health(aliados):
    for i in aliados:
        i.vida = 0
#teste com varios aliados na lista e com sua vida > 0
def test_func_must_return_false_01():
    tropas = run_tropas()
    add_allies(tropas, 10)
    assert tropas.morreu(tropas.entidades['aliados'], tropas.tabuleiro) == False
#teste com apenas um aliado na lista e com sua vida > 0
def test_func_must_return_false_02():
    tropas = run_tropas()
    assert tropas.morreu(tropas.entidades['aliados'], tropas.tabuleiro) == False
#teste com vários inimigos e todos com vida <= 0
def test_func_must_return_true_03():
    tropas = run_tropas()
    add_allies(tropas, 10)
    reset_all_allies_health(tropas.entidades['aliados'])
    assert tropas.morreu(tropas.entidades['aliados'], tropas.tabuleiro) == True
#teste com um inimigo com vida <= 0
def test_func_must_return_true_04():
    tropas = run_tropas()
    reset_all_allies_health(tropas.entidades['aliados'])
    assert tropas.morreu(tropas.entidades['aliados'], tropas.tabuleiro) == True



