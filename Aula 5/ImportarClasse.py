# 1. Abstração e Herança

# Criar uma classe ANIMAL abstrata que
# não faz nada, as tem nome, raça e idade. Essa classe tem um método
# de fazer ruido que deve ser implementado na class cachorro, gato. e
# vaca.

# from abc import ABC, abstractmethod

# class Animal(ABC):
    
    
#     @abstractmethod
#     def nome(self):
#         pass
    
#     def raca(self):
#         pass
    
#     def idade(self):
#         pass
    
#     def ruido(self):
#         pass
    

# class Cachorro(Animal):
#     def nome(self):
#         return f"Matheus"
    
#     def raca(self):
#         return "Pastor Alemão"

#     def idade(self):
#         return "10"
    
#     def ruido(self):
#         return "Auauau"
    
# class Gato(Animal):
#     def nome(self):
#         return f"Susana"
    
#     def raca(self):
#         return "Nuvem"

#     def idade(self):
#         return "7"
    
#     def ruido(self):
#         return "Miau"

# class Vaca(Animal):
#     def nome(self):
#         return f"Chloe"
    
#     def raca(self):
#         return "Holstein-Frísia"

#     def idade(self):
#         return "20"
    
#     def ruido(self):
#         return "Muu"
    
# cachorro = Cachorro()
# print(f"O {cachorro.nome} possui {cachorro.idade} e faz {cachorro.ruido}.")
    
    
from abc import ABC, abstractmethod

#Super Class
class Animal(ABC):
    def __init__(self, nome, raca, idade):
        self. nome = nome
        self.raca = raca
        self.idade = idade
    
    @abstractmethod
    def ruido(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade)
        
    def ruido(self):
        return "Auau"

class Gato(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade)
        
    def ruido(self):
        return "Miau"

class Vaca(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade)
        
    def ruido(self):
        return "Muuuu"
    
cachorro = Cachorro("Matheus", "Pastor Alemão", 10)
gato = Gato("Susana", "Nuvem", 7)
vaca = Vaca("Chloe", "Holstein-Frísia", 20)

lista = [cachorro, gato, vaca]
for i in lista:
    print(i.ruido())


# 2 Agregação e Composição
# Crie uma porta, uma chave e uma pessoa
# Pessoa deve pegar a chave, inserir na pporta, e rodar a chave.
# Pessoa deve informar se a porta está aberta ou fechada.

# Chave

class Chave:
    def __init__(self):
        self.pertence = False
        

# Porta

class Porta:
    def __init__(self):
        self.aberta = False

# Pessoa

class Pessoa:
    def __init__(self, nome, ):
        self.nome = nome
        self.porta = None
        self.chave = None
        
    def pegar_chave(self, chave: Chave):
        if self.chave == None:
            self.chave = chave
            print(f"{self.nome} pegou a chave.")
        else:
            print(f"{self.nome} já está com a chave.")
            
    def abrir_porta(self, porta: Porta):
        if self.chave != None and self.porta == None:
            self.porta = porta
            if not self.porta.aberta:
                self.porta.aberta = True
                print(f"{self.nome} inseriu a chave na porta e a abriu.")
        elif self.porta.aberta:
            print(f"A porta já está aberta.")
        else:
            print(f"{self.nome} não tem a chave.")
            
p1 = Pessoa("Zé da Manga")
chave = Chave()
porta = Porta()

p1.pegar_chave(chave)
p1.abrir_porta(porta)
p1.abrir_porta(porta)