import unittest
from .escada import escada2

class TestEscadaLogico(unittest.TestCase):

  def test_caso1(self):
    N = 2
    M = 2
    matriz = [[0, 0], 
              [0, 1]]

    self.assertEqual(escada2(N,M,matriz), 'N', "Erro")

  def test_caso2(self):
    N = 2
    M = 2
    matriz = [[1, 1], 
              [0, 1]]

    self.assertEqual(escada2(N,M,matriz), 'S', "Erro")
