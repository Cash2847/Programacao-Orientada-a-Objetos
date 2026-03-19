class Carro:
    def __init__(self, marca):
        self.marca = marca
        
    def acelerar(self):
        print(f"O {self.marca} acelerou!")
        
meu_carro = Carro("Toyota")
meu_carro.acelerar()