import time
import hashlib

class Conta:
    def __init__(self, titular, senha):
        self.titular = titular
        self.senha = senha  # Já esperamos receber a senha em hash aqui
        self.saldo = 0.0
        self.extrato = []
        self.cartao_credito = None

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R${valor:.2f}")
        print("\nProcessando o depósito.")
        for _ in range(10):
            print("#", end='', flush=True)
            time.sleep(0.3)  # pausa de 0.3 segundos
        print("\nDepósito efetuado com sucesso!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return
        self.saldo -= valor
        self.extrato.append(f"Saque de R${valor:.2f}")

    def ver_extrato(self):
        return self.extrato

    def emprestimo(self, valor):
        self.saldo += valor
        self.extrato.append(f"Empréstimo de R${valor:.2f}")

    def solicitar_cartao_credito(self):
        self.cartao_credito = {"limite": 5000.0}  # Exemplo de limite inicial
        print("Solicitação de cartão de crédito feita!")

    def comprar_cartao_credito(self, valor):
        if self.cartao_credito and self.cartao_credito['limite'] >= valor:
            self.cartao_credito['limite'] -= valor
            self.extrato.append(f"Compra no cartão de crédito: R${valor:.2f}")
            print("Compra efetuada com sucesso!")
        else:
            print("Limite insuficiente no cartão de crédito ou cartão não solicitado.")

    def pagar_cartao_credito(self, valor):
        if self.saldo >= valor:
            if self.cartao_credito:
                self.cartao_credito['limite'] += valor
                self.saldo -= valor
                self.extrato.append(f"Pagamento no cartão de crédito: R${valor:.2f}")
                print("Pagamento efetuado com sucesso!")
            else:
                print("Você não possui um cartão de crédito.")
        else:
            print("Saldo insuficiente.")

def hash_senha(senha):
    """Retorna a senha em hash."""
    return hashlib.sha256(senha.encode()).hexdigest()

def input_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um valor válido!")

def input_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido!")

def checar_senha(conta_logada):
    tentativa = input("Digite sua senha para continuar: ")
    if hash_senha(tentativa) == conta_logada.senha:
        return True
    else:
        print("Senha incorreta!")
        return False

def imprimir_extrato_animacao():
    print("Iniciando impressão do extrato...")
    for i in range(4):
        print("###>", end='', flush=True)
        time.sleep(0.5)
    print("\nErro: Impressora não conectada.")

def main():
    contas = []
    conta_logada = None

    while True:
        print("\n--- Menu Principal ---")
        print("1. Criar conta")
        print("2. Acessar conta")
        print("3. Sair")

        opcao = input_int("Escolha uma opção: ")

        if opcao == 1:
            nome = input("Digite o nome do titular: ")
            senha = input("Digite a senha da conta: ")
            senha_hash = hash_senha(senha)
            conta_nova = Conta(nome, senha_hash)
            contas.append(conta_nova)
            print("Conta criada com sucesso!")

        elif opcao == 2:
            nome = input("Digite o nome do titular: ")

            conta_logada = None
            for conta in contas:
                if conta.titular == nome:
                    conta_logada = conta
                    break

            if not conta_logada:
                print("Conta não encontrada!")
                continue

            if not checar_senha(conta_logada):
                continue

            while True:
                print("\n--- Menu da Conta ---")
                print("1. Sacar")
                print("2. Depositar")
                print("3. Ver Extrato")
                print("4. Empréstimo")
                print("5. Solicitar Cartão de Crédito")
                print("6. Comprar no cartão de crédito")
                print("7. Pagar cartão de crédito")
                print("0. Sair")

                opcao_conta = input_int("Escolha uma opção: ")

                # Opções de conta agora utilizam input_float e verificam valores negativos

                if opcao_conta == 3:
                    print("\n--- Opções de Extrato ---")
                    print("1. Extrato em tela")
                    print("2. Extrato impresso")

                    opcao_extrato = int(input("Escolha uma opção: "))

                    if opcao_extrato == 1:
                        for item in conta_logada.ver_extrato():
                            print(item)
                    elif opcao_extrato == 2:
                        imprimir_extrato_animacao()
                        
                elif opcao_conta == 1:
                    valor = input_float("Digite o valor a ser sacado: ")
                    if valor < 0:
                        print("Valor inválido!")
                        continue
                    conta_logada.sacar(valor)

                elif opcao_conta == 2:
                    valor = input_float("Digite o valor a ser depositado: ")
                    if valor < 0:
                        print("Valor inválido!")
                        continue
                    conta_logada.depositar(valor)

                elif opcao_conta == 4:
                    valor = input_float("Digite o valor do empréstimo: ")
                    if valor < 0:
                        print("Valor inválido!")
                        continue
                    conta_logada.emprestimo(valor)

                elif opcao_conta == 5:
                    conta_logada.solicitar_cartao_credito()

                elif opcao_conta == 6:
                    valor = input_float("Digite o valor da compra no cartão de crédito: ")
                    if valor < 0:
                        print("Valor inválido!")
                        continue
                    conta_logada.comprar_cartao_credito(valor)

                elif opcao_conta == 7:
                    valor = input_float("Digite o valor a ser pago no cartão de crédito: ")
                    if valor < 0:
                        print("Valor inválido!")
                        continue
                    conta_logada.pagar_cartao_credito(valor)

                elif opcao_conta == 0:
                    break

        elif opcao == 3:
            break

if __name__ == "__main__":
    main()
