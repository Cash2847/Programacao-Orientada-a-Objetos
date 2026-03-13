class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def exibir_info(self):
        print(f"{self.nome}: R${self.preco} | {self.estoque} un.")



class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto:Produto):
        self.itens.append(produto.nome)
        print(f"Adcionado: {produto.nome}.")

cafe = Produto("Café", 18.9, 50)
pedido = Pedido()

cafe.exibir_info()
pedido.adicionar_produto(cafe)