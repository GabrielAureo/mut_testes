import unittest
from .baralho import baralho2

class TestBaralhoISP(unittest.TestCase):
    # Ordem da Saída: C E U P
    
    def test_caso1(self):
        # ['T1', 'DUb', 'DPb', 'DEb', 'DCb', 'CUb', 'CPb', 'CEb', 'CCb']
        entrada = '01U'
        self.assertEqual(baralho2(entrada), [13,13,12,13], "Erro")

    def test_caso2(self):
        # ['T2', 'DUa', 'DPa', 'DEa', 'DCa', 'CUa', 'CPa', 'CEa', 'CCb']
        entrada = '01U01U02U03U04U05U06U07U08U09U10U11U12U13U'+\
                  '01C01C02C'+\
                  '01P01P02P03P04P05P06P07P08P09P10P11P12P13P'+\
                  '01E01E02E03E04E05E06E07E08E09E10E11E12E13E'
        self.assertEqual(baralho2(entrada), ['erro','erro','erro','erro'], "Erro")
    
    def teste_caso3(self):
        # ['T2', 'DUb', 'DPb', 'DEb', 'DCb', 'CUb', 'CPb', 'CEb', 'CCa']
        entrada = '01U'+\
                  '01C02C03C04C05C06C07C08C09C10C11C12C13C'+\
                  '01P'+\
                  '01E'
        self.assertEqual(baralho2(entrada), [0, 12, 12, 12], "Erro")

    def teste_caso4(self):
        # ['T3', 'DUa', 'DPa', 'DEa', 'DCa', 'CUa', 'CPa', 'CEa', 'CCb']
        entrada = '01U01U02U03U04U05U06U07U08U09U10U11U12U13U'+\
                  '01C01C02C03C04C05C06C07C08C09C10C'+\
                  '01P01P02P03P04P05P06P07P08P09P10P11P12P13P'+\
                  '01E01E02E03E04E05E06E07E08E09E10E11E12E13E'
        self.assertEqual(baralho2(entrada), ['erro','erro','erro','erro'], "Erro")
    
    def teste_caso5(self):
        # ['T3', 'DUb', 'DPb', 'DEb', 'DCb', 'CCa', 'CUa', 'CPa', 'CEa']
        entrada = '01U02U03U04U05U06U07U08U09U10U11U12U13U'+\
                  '01C02C03C04C05C06C07C08C09C10C11C12C13C'+\
                  '01P02P03P04P05P06P07P08P09P10P11P12P13P'+\
                  '01E02E03E04E05E06E07E08E09E10E11E12E13E'
        self.assertEqual(baralho2(entrada), [0,0,0,0], "Erro")

    def teste_caso6(self):
        # ['T3', 'CUb', 'CPb', 'CEb', 'DUa', 'DPb', 'DEb', 'DCb', 'CCa']
        entrada = '01U01U02U02U03U04U05U06U07U08U09U10U11U12U'+\
                  '01C02C03C04C05C06C07C08C09C10C11C12C13C'+\
                  '01P02P03P04P05P06P07P08P09P10P11P12P'+\
                  '01E02E03E04E05E06E07E08E09E10E11E12E'
        self.assertEqual(baralho2(entrada), [0,1,'erro',1], "Erro")
    
    def teste_caso7(self):
        # ['DUb', 'DPa', 'DEa', 'DCa', 'CUb', 'CPb', 'CEb', 'CCa']
        entrada = '01U02U03U04U05U06U07U08U09U10U11U'+\
                  '01C01C02C03C04C05C06C07C08C09C10C11C12C13C'+\
                  '01P01P02P03P04P05P06P07P08P09P10P11P12P'+\
                  '01E01E02E03E04E05E06E07E08E09E10E11E12E'
        self.assertEqual(baralho2(entrada), ['erro','erro',2,'erro'], "Erro")
    
    def teste_caso8(self):
        # ['DPa', 'DEb', 'DCb', 'CUa', 'CPb', 'CEb']
        entrada = '01U02U03U04U05U06U07U08U09U10U11U12U13U'+\
                  '01C02C03C04C05C06C07C08C09C10C11C12C'+\
                  '01P02P03P04P05P06P07P08P09P10P11P12P12P'+\
                  '01E02E03E04E05E06E07E08E09E10E11E12E'
        self.assertEqual(baralho2(entrada), [1,1,0,'erro'], "Erro")

    def teste_caso9(self):
        # ['DPb', 'DEa', 'DCa', 'CUb', 'CPa', 'CEa']
        entrada = '01U02U03U04U05U06U07U08U09U10U11U12U'+\
                  '01C02C03C04C05C06C07C08C09C10C11C12C12C'+\
                  '01P02P03P04P05P06P07P08P09P10P11P12P13P'+\
                  '01E02E03E04E05E06E07E08E09E10E11E12E13E13E'
        self.assertEqual(baralho2(entrada), ['erro','erro',1,0], "Erro")

    def teste_caso10(self):
        # ['DEa', 'DCb', 'CPa', 'CEb']
        entrada = '01U02U03U04U05U06U07U08U09U10U11U12U13U'+\
                  '01C02C03C04C05C06C07C08C09C10C11C12C13C'+\
                  '01P02P03P04P05P06P07P08P09P10P11P12P13P'+\
                  '01E02E03E04E05E06E07E08E09E10E11E12E12E'
        self.assertEqual(baralho2(entrada), [0,'erro',0,0], "Erro")
    
    def teste_caso11(self):
        # ['DEb', 'DCa', 'CPb', 'CEa']
        entrada = '01U02U03U04U05U06U07U08U09U10U11U12U13U'+\
                  '01C02C03C04C05C06C07C08C09C10C11C12C12C'+\
                  '01P02P03P04P05P06P07P08P09P10P11P12P'+\
                  '01E02E03E04E05E06E07E08E09E10E11E12E13E'
        self.assertEqual(baralho2(entrada), ['erro',0,0,1], "Erro")