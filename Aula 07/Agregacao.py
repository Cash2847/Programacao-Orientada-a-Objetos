class Cliente_in_NULL:
    def __init__(self):
        self.nome = None # Defini que é um dado nulo

class Cliente:
    def __init__(self, nome):
        self.nome = nome # O sistema é obrigado a definir Cliente
        
class Banco:
    def __init__(self, nome):
        self.nome = nome # Nome do banco.
        self.lista = [] #Aqui entra os clientes.
     
     # Método de agregação   
    def adicionar_cliente(self, cliente):
        self.lista.append(cliente)
        
    def apresentar_cliente(self):
        # Apresentar o nome do banco
        print(f"O Banco: {self.nome}")
        # nome dos meus clientes
        for i in self.lista:
            print(i.nome)
        
# cliente_nulo = Cliente_in_NULL()
cliente = Cliente('Zé da Manga')

banco1 = Banco("Zé da Manga Bank")

print(cliente.nome)