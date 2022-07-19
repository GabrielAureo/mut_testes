import unittest
from .baralho2 import baralho2

class TestBaralhoNos(unittest.TestCase):
    def test_case_nos_1(self):
        self.assertEqual(baralho2('01C01E01E'), [12, 'erro', 13, 13]) 

class TestBaralhoArcos(unittest.TestCase):
    def test_case_arcos_1(self):
        self.assertEqual(baralho2('01C01E01E'), [12, 'erro', 13, 13]) 

class TestBaralhoParesArcos(unittest.TestCase):
    def test_case_pares_arcos_1(self):
        self.assertEqual(baralho2('01C01E01E'), [12, 'erro', 13, 13]) 
    