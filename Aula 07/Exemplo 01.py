class Produto:
    def _init_ (self, nome):
        self.nome = nome
    
class Carrinho:
    def _init_(self):
        self.itens = []
    
    def adicionar_produto(self, produto): self.itens.append(produto)
    
    
# Execução do Sistema
celular = Produto('Smartphone')
meu_carrinho = Carrinho()
meu_carrinho.adicionar_produto(celular)