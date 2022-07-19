import unittest
from .escada import escada2

class TestEscadaNos(unittest.TestCase):

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
