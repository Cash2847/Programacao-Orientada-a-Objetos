
# Superclass/Classe Mãe
class Veiculo:
    def __init__(self):
        self.velocidade = float(0)

# Subclass/Classe Filha
class Carro(Veiculo): # A Herança é colocada entre parênteses.
    def __init__(self, marca, ano, velocidade, placa):
        super().__init__(velocidade)
        self.marca = marca
        self.ano = ano
        self.placa = placa

class SerVivo:
    def __init__(self):
        self.idade = 0.0

class Pessoa(SerVivo):
    def __init__(self):
        super().__init__()
        self.nome = "Zé da Manga"

ze = Pessoa()
ze.idade = 10
print(ze.nome,"de idade", ze.idade)