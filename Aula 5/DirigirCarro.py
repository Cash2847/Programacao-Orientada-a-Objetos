# Considerando o exercício realizado em sala de aula, crie uma classe chamada carro.

# Carro deve ter --> velocidade, marcha, marca e ano.

# Seus métodos devem ser acelerar, passar de marcha, reduzir marcha 
# e frear, junto com ligar e desligar.

# Mas só quem pode fazer isso é quem tem a chave 
# do carro ou seja temos que ter uma classe Pessoa e Chave para 
# que essa pessoa realize todos os passos.



class Chave:
    def __init__(self, marca):
        self.marca = marca


class Pessoa:
    def __init__(self, nome, chave):
        self.nome = nome
        self.chave = chave

class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        self.velocidade = 0
        self.marcha = 0
        self.ligado = False

    def entrar_carro(self, pessoa, chave):
        if pessoa.chave and chave.marca == self.marca:
            print(f"{pessoa.nome} entrou no carro.")
            return True
        else:
            print("A chave utilizada não é a chave correta.")
            return False
    
    def ligar_carro(self, pessoa, chave):
        if self.entrar_carro(pessoa, chave):
            self.ligado = True
            print("O carro está ligado.")

        
    def desligar_carro(self, pessoa, chave):
        if self.entrar_carro(pessoa, chave):
            self.ligado = False
            self.velocidade = 0
            print("O carro foi desligado.")

    
    def acelerar(self, pessoa, chave, aceleracao):
        if self.entrar_carro(pessoa, chave) and self.ligado:
            self.velocidade += aceleracao
            print(f"Carro acelerou, e agora está á {self.velocidade} KM/H.")

    def frear(self, pessoa, chave, desaceleracao):
        if self.entrar_carro(pessoa, chave):
            self.velocidade = max(0, self.velocidade - desaceleracao)
            print(f"Após frear, a velocidade atual do carro é de {self.velocidade}.")


    def passar_marcha(self, pessoa, chave):
        if self.entrar_carro(pessoa, chave):
            self.marcha += 1
            print(f"A marcha atual é {self.marcha}.")

    def reduzir_marcha(self, pessoa, chave):
        if self.entrar_carro(pessoa, chave):
            self.marcha = max(0, self.marcha - 1)
            print(f"Após reduzir a marcha, a marcha atual é {self.marcha}.")


chave_do_carro = Chave("Volkswagen")
pessoa = Pessoa("Zé da Manga", chave_do_carro)
carro = Carro("Volkswagen", 2024)

carro.ligar_carro(pessoa, chave_do_carro)
carro.acelerar(pessoa, chave_do_carro, 100)
carro.frear(pessoa, chave_do_carro, 70)

