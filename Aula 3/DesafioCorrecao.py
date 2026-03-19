class User:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    
    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha


# ___ Teste rápido _________________________________________________________    
u = User("Ana", "senha123")

print(u.autenticar("Ana", "senha123")) # True
print(u.autenticar("Ana", "se")) # False


class Banco:
    contas_cadastradas = []
    def __init__(self, nome, agencia, numero_conta, saldo, cpf, user):
        self.nome = nome
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.cpf = cpf
        self.user = user
        self.ativa = True
        
        Banco.contas_cadastradas.append(self)
        
    def exibir_saldo(self):
        print(f"R$ {self.saldo:.2f}")
    
    def verificar_conta_ativa(self):
        if not self.ativa:
            print("Conta encerrada, Operação não permitida.")
            return False
        return True
    
    def autenticacao(self, usuario, senha):
        if not self.verificar_conta_ativa():
            return False
        if not self.user.autenticar(usuario, senha):
            print("Usuário ou senha incorretos!")
            return False
        return True
    
print("Classe Banco definida com sucesso!")

def depositar(self, valor, usuario, senha):
    if not self.autenticacao(usuario, senha):
        return
    
    if valor <= 0:
        print("O valor de depósito deve ser positivo.")
        return
    
    self.saldo += valor
    print(f"Depósito de R$ {valor:.2f} realizado! Saldo: {self.exibir_saldo()}")
    
Banco.depositar = depositar

user_ana = User("Ana", "senha123")
conta_ana = Banco("Ana Silva", "0001", "10001", 400.00, "111.111.111-11", )

def sacar(self, valor, usuario, senha):
    if not self.autenticacao(usuario, senha):
        return
    if valor <= 0:
        print("O valor do saque deve ser positivo.")
        return
    
    limite_total