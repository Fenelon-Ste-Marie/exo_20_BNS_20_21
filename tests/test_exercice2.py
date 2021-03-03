from exercices.exercice2 import *

def test_rendu_glouton():
    assert rendu_glouton(68,[],0) == [50, 10, 5, 2, 1]
    assert rendu_glouton(291,[],0) == [100, 100, 50, 20, 20, 1]
