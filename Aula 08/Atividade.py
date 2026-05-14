class SaldoInsuficienteError(Exception):
    """Erro utilizado quando o valor sacado é maior do que o que está amarzenado no saldo."""
    pass
    

class Conta_Base:
    def __init__(self):
        self.saldo = float(0)

class Conta_Corrente(Conta_Base):
    def __init__(self):
        super().__init__()

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"O valor sacado (R$ {valor:.2f}) é maior do que o saldo disponível (R$ {self.saldo:.2f}). Logo, o saque é inválido.")
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque completo. Saldo atual: {self.saldo:.2f}.")

conta = Conta_Corrente()
conta.saldo = 100

print(f"O saldo atual da conta é {conta.saldo:.2f}.")

try:
    conta.sacar(20)
except SaldoInsuficienteError as erro:
    print("Saldo incapaz de ser realizado: ", erro)
finally:
    print("Operação completa.")