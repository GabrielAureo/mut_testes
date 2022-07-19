import unittest
from .escada import escada2

class TestEscadaParesArcos(unittest.TestCase):

  def test_caso1(self):
    N = 3
    M = 3
    matriz = [[0, 1, 1], 
                [0, 1, 1],
                [0, 0, 1]]

    self.assertEqual(escada2(N,M,matriz), 'N', "Erro")

  def test_caso2(self):
    N = 2
    M = 2
    matriz = [[0, 1], 
                [1, 1]]

    self.assertEqual(escada2(N,M,matriz), 'N', "Erro")

  def test_caso3(self):
    N = 1
    M = 1
    matriz = [[0]]

    self.assertEqual(escada2(N,M,matriz), 'S', "Erro")

  def test_caso4(self):
    N = 2
    M = 1
    matriz = [[0],
            [1]]

    self.assertEqual(escada2(N,M,matriz), 'N', "Erro")