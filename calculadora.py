def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

import time

if __name__ == "__main__":
    print("======================================")
    print("🚀 Calculadora DevOps rodando no Docker!")
    print("O container ficará ativo por 60 segundos...")
    print("======================================")
    time.sleep(60)