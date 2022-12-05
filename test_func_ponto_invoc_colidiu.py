from ponto_invoc import *
import pytest

def run_lugar():
    lugar = Lugar(0,0,32,32)
    return lugar

#test_01_s_s_t
def test_func_must_return_true_01():
    bloco = run_lugar()
    assert bloco.colidiu(1, 1) == True
#test_02_s_n_f
def test_func_must_return_false_02():
    bloco = run_lugar()
    assert bloco.colidiu(1, -1) == False
#test_03_n_s_f
def test_func_must_return_false_03():
    bloco = run_lugar()
    assert bloco.colidiu(-1, 1) == False
#test_03_n_n_f
def test_func_must_return_false_04():
    bloco = run_lugar()
    assert bloco.colidiu(-1, -1) == False

