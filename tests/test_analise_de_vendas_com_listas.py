import unittest

from desafios_de_codigo.src.analise_de_vendas_com_listas import (
    analise_vendas,
    obter_entrada_vendas,
)


class TestAnaliseVendas(unittest.TestCase):

    def test_analise_vendas_caso_1(self):
        vendas = [120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190]
        resultado_esperado = "2120, 176.67"
        self.assertEqual(analise_vendas(vendas), resultado_esperado)

    def test_analise_vendas_caso_2(self):
        vendas = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
        resultado_esperado = "780, 65.00"
        self.assertEqual(analise_vendas(vendas), resultado_esperado)

    def test_analise_vendas_caso_3(self):
        vendas = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        resultado_esperado = "390, 32.50"
        self.assertEqual(analise_vendas(vendas), resultado_esperado)


class TestObterEntradaVendas(unittest.TestCase):

    def test_obter_entrada_vendas_caso_1(self):
        entrada = "120,150,170,130,200,250,180,220,210,160,140,190"
        resultado_esperado = [
            120,
            150,
            170,
            130,
            200,
            250,
            180,
            220,
            210,
            160,
            140,
            190,
        ]
        self.assertEqual(obter_entrada_vendas(entrada), resultado_esperado)

    def test_obter_entrada_vendas_caso_2(self):
        entrada = "10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120"
        resultado_esperado = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
        self.assertEqual(obter_entrada_vendas(entrada), resultado_esperado)

    def test_obter_entrada_vendas_caso_3(self):
        entrada = "5,10,15,20,25,30,35,40,45,50,55,60"
        resultado_esperado = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        self.assertEqual(obter_entrada_vendas(entrada), resultado_esperado)


if __name__ == "__main__":
    unittest.main()
