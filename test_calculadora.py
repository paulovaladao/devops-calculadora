import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora.soma(10, 5), 15)

    def test_subtracao(self):
        self.assertEqual(calculadora.subtracao(10, 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(calculadora.multiplicacao(10, 5), 50)

    def test_divisao(self):
        self.assertEqual(calculadora.divisao(10, 5), 2)

    def test_divisao_por_zero(self):
        # Valida o tratamento da excecao matematica para divisao por zero
        resultado = calculadora.divisao(10, 0)
        self.assertEqual(resultado, "Erro: Divisão por zero")

if __name__ == '__main__':
    unittest.main()