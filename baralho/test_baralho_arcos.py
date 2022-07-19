import unittest
from .baralho import baralho2

class TestBaralhoArcos(unittest.TestCase):
    def test_case_arcos_1(self):
        self.assertEqual(baralho2('01C01E01E'), [12, 'erro', 13, 13]) 
