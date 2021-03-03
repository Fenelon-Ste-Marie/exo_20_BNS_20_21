from exercices.exercice1 import *

def test_recherche():
    assert recherche('e', "sciences") == 2
    assert recherche('i',"mississippi") == 4
    assert recherche('a',"mississippi") == 0
