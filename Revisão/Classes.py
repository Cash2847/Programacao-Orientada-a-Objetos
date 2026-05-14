class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vender(self, vendas):
        self.vendas = vendas

    def bater_meta(self, meta):
        if self.vendas >= meta:
            print(f"A meta foi atingida por {self.nome}.")
        else:
            print(f"A meta não foi atingida por {self.nome}.")