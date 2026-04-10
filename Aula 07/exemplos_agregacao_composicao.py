class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


class Sistema:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def autenticar(self, nome, senha):
        for usuario in self.usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                return f"Usuario {nome} autenticado com sucesso."
        return "Falha na autenticacao."


class Token:
    def __init__(self, valor="ABC123"):
        self.valor = valor


class Autenticacao:
    def __init__(self):
        # Composição: o token nasce dentro da autenticacao
        self.token = Token()

    def exibir_token(self):
        return f"Token gerado: {self.token.valor}"


class Motorista:
    def __init__(self, nome):
        self.nome = nome


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motorista = None
        # Composição: o carro cria seu proprio motor
        self.motor = Motor(potencia_motor)

    def definir_motorista(self, motorista):
        # Agregação: o motorista ja existe e eh associado ao carro
        self.motorista = motorista

    def mostrar_dados(self):
        nome_motorista = self.motorista.nome if self.motorista else "Sem motorista"
        return (
            f"Carro: {self.modelo} | "
            f"Motor: {self.motor.potencia} cv | "
            f"Motorista: {nome_motorista}"
        )


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Historico:
    def __init__(self):
        self.movimentos = []

    def adicionar_movimento(self, descricao):
        self.movimentos.append(descricao)


class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        # Composição: o historico faz parte da conta
        self.historico = Historico()

    def depositar(self, valor):
        self.historico.adicionar_movimento(f"Deposito de R$ {valor}")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def adicionar_cliente(self, cliente):
        # Agregação: o cliente pode existir fora do banco
        self.clientes.append(cliente)


if __name__ == "__main__":
    print("=== AUTENTICACAO ===")
    usuario = Usuario("Ana", "1234")
    sistema = Sistema()
    sistema.adicionar_usuario(usuario)
    print(sistema.autenticar("Ana", "1234"))

    auth = Autenticacao()
    print(auth.exibir_token())

    print("\n=== CARRO ===")
    motorista = Motorista("Carlos")
    carro = Carro("Fusca", 85)
    carro.definir_motorista(motorista)
    print(carro.mostrar_dados())

    print("\n=== BANCO ===")
    cliente = Cliente("Marina")
    banco = Banco("Banco POO")
    banco.adicionar_cliente(cliente)

    conta = Conta("0001", cliente.nome)
    conta.depositar(500)

    print(f"Banco: {banco.nome}")
    print(f"Cliente agregado: {banco.clientes[0].nome}")
    print(f"Conta: {conta.numero} | Titular: {conta.titular}")
    print("Historico da conta:", conta.historico.movimentos)
