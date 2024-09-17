import time
import random

# Função para gerar um vetor com números aleatórios
def gerar_vetor(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

# Função para multiplicar dois vetores
def multiplicar_vetores(vetor1, vetor2):
    resultado = []
    for i in range(len(vetor1)):
        resultado.append(vetor1[i] * vetor2[i])
        time.sleep(0.001)  # Simulando uma operação mais demorada
    return resultado

# Medindo o tempo de execução
tamanho = 500
vetor1 = gerar_vetor(tamanho)
vetor2 = gerar_vetor(tamanho)

inicio = time.time()
resultado = multiplicar_vetores(vetor1, vetor2)
fim = time.time()

print(f"Tempo de execução (thread principal): {fim - inicio:.4f} segundos")
