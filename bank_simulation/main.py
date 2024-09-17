import threading
import time
import queue

class ContaBancaria:
    def __init__(self):
        self.saldo = 100.0
        self.lock = threading.Lock()
        self.fila_operacoes = queue.Queue()

    def rendimento_continuo(self):
        while True:
            time.sleep(10)
            self.fila_operacoes.put(('rendimento', 0))

    def processar_operacoes(self):
        while True:
            operacao, valor = self.fila_operacoes.get()
            with self.lock:
                if operacao == 'saque':
                    if valor <= self.saldo:
                        self.saldo -= valor
                        print(f"Saque de R${valor:.2f} realizado com sucesso.")
                    else:
                        print("Saldo insuficiente para saque.")
                elif operacao == 'deposito':
                    self.saldo += valor
                    print(f"Depósito de R${valor:.2f} realizado com sucesso.")
                elif operacao == 'rendimento':
                    self.saldo *= 1.01
                self.fila_operacoes.task_done()

    def saque(self, valor):
        self.fila_operacoes.put(('saque', valor))

    def deposito(self, valor):
        self.fila_operacoes.put(('deposito', valor))

    def visualizar_saldo(self):
        with self.lock:
            print(f"Saldo atual: R${self.saldo:.2f}")

def interacao_usuario(conta):
    while True:
        print("\nEscolha uma operação:")
        print("1. Saque")
        print("2. Depósito")
        print("3. Visualizar Saldo")
        print("4. Sair")
        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor do saque: "))
            conta.saque(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do depósito: "))
            conta.deposito(valor)
        elif opcao == '3':
            conta.visualizar_saldo()
        elif opcao == '4':
            conta.visualizar_saldo()
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    conta = ContaBancaria()

    thread_rendimento = threading.Thread(target=conta.rendimento_continuo)
    thread_usuario = threading.Thread(target=interacao_usuario, args=(conta,))
    thread_processamento = threading.Thread(target=conta.processar_operacoes)

    thread_rendimento.start()
    thread_usuario.start()
    thread_processamento.start()

    thread_usuario.join()
    thread_rendimento.join()
    thread_processamento.join()
