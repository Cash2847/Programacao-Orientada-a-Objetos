class Coisa:
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status

class Teste:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.coisa = []

    def __str__(self):
        return f"Esse é o Teste do {self.nome}, {self.idade} anos."

    def adicionar_coisa(self, nome, idade):
        varcoisa = Coisa(nome, idade)
        self.coisa = self.coisa.append(varcoisa)

    def mostra_coisa(self):
        for c in self.coisa:
            print(c)

teste = Teste("Zé da Manga", 29)
teste.adicionar_coisa("Teste", "Correto")
print(teste.nome)
teste.mostra_coisa()