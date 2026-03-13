class User:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
    def autenticar(self, usuario, senha):
        if senha == self.senha and usuario == self.usuario:
            print("Validação Realizada com Sucesso.")
        else:
            print("Usuário ou senha incorreto. Tente novamente.")


class Banco:
    def __init__(self, nome, numConta, saldo, agencia, CPF):
        self.nome = nome
        self.numConta = numConta
        self.saldo = saldo
        self.agencia = agencia
        self.CPF = CPF

    def depositar(self):
        quantidade_depositada = float(input("Quanto você deseja depositar? " ))
        saldo += quantidade_depositada
        print(f"Seu saldo atual é R${saldo}")

    
    def pix(self):
        
        

    def sacar(self):
        quantidade_retirada = float(input("Quanto você deseja sacar? " ))
        saldo -= quantidade_retirada
        if quantidade_retirada <= saldo:
            print(f"Seu saldo atual é R${saldo}")
        else:
            print("Você não possui essa quantidade em seu saldo.")



banco = Banco("Giovanni", 26783, 7500.87, "Nubank", 1135432323)
user = User("Giovanni", 2022)