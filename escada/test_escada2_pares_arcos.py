import unittest
from .escada2 import escada2

class TestEscada(unittest.TestCase):

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

  def test_caso5(self):
    N = 3
    M = 2
    matriz = [[1,2,3],
              [0,2,3],
              [0,0,3]]
    self.assertEqual(escada2(N,M,matriz), 'S', "Erro")

  def test_caso6(self):
    N = 3
    M = 2
    matriz = [[1,2,3],
              [0,2,3],
              [0,2,3]]
    self.assertEqual(escada2(N,M,matriz), 'N', "Erro")

  def test_caso7(self):
    N = 4
    M = 6
    matriz = [[1, 2, 9, 9 ,9 ,9],
            [0, 0, 3, 9 ,9, 9],
            [0, 1, 0, 0, 5, 9],
            [0, 0, 0, 0, 0, 6]]
    self.assertEqual(escada2(N,M,matriz), 'N', "Erro")