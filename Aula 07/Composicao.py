class Historico:
    def __init__(self):
        self.movimentos = []
    
    def adicionar_movimentos(self, descricao):
        print(f"O valor definido e inserido é: {descricao}")
        self.movimentos.append(descricao)
        
class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.historico = Historico()
        
    def depositar(self, valor):
        print('Valor depositado.')
        self.historico.adicionar_movimentos(valor)
        print(f"O valor é: {self.historico.movimentos}")
        
c1 = Conta(123456, 'Zé da Manga')
c1.depositar(250)