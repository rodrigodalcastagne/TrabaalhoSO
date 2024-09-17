import time
import random
import threading

# Função para gerar um vetor com números aleatórios
def gerar_vetor(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

# Função para multiplicar uma parte dos vetores
def multiplicar_parte(vetor1, vetor2, resultado, inicio, fim):
    for i in range(inicio, fim):
        resultado[i] = vetor1[i] * vetor2[i]
        time.sleep(0.001)  # Simulando uma operação mais demorada

# Função principal para multiplicar vetores usando múltiplas threads
def multiplicar_vetores_multithread(vetor1, vetor2, num_threads):
    tamanho = len(vetor1)
    resultado = [0] * tamanho
    threads = []
    parte = tamanho // num_threads

    for i in range(num_threads):
        inicio = i * parte
        fim = (i + 1) * parte if i != num_threads - 1 else tamanho
        thread = threading.Thread(target=multiplicar_parte, args=(vetor1, vetor2, resultado, inicio, fim))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return resultado

# Medindo o tempo de execução
tamanho = 500
vetor1 = gerar_vetor(tamanho)
vetor2 = gerar_vetor(tamanho)

inicio = time.time()
resultado = multiplicar_vetores_multithread(vetor1, vetor2, num_threads=4)
fim = time.time()

print(f"Tempo de execução (múltiplas threads): {fim - inicio:.4f} segundos")
