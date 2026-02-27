# # 1a Classe Rica
# class Pessoa:
#     # Método Construtor
#     def __init__(self, nome, idade, altura):
#         # Atributos
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura

#     # Apresentar
#     def apresentar(self):
#         return f"""
# Olá. Eu sou {self.nome}, tenho {self.altura} de altura e {self.idade} anos de idade.
#         """
    
# zedamanga = Pessoa("Zé da Manga", 20, 1.75)

# print(zedamanga.apresentar())

# Construir um termometro que avalia se a pessoa está com febre, 
# ou se a temperatura dela esta muito baixa,
# ou se a pessoa está com a temperatura normal

# isso deve ser feito em Classe Rica

class Temperatura:
    def __init__(self, nome, temperatura):
        self.nome = nome
        self.temperatura = temperatura

    def verifica_temperatura(self):
        if self.temperatura > 37.5:
            return f"A temperatura corporal de {self.nome} é de {self.temperatura}°, indicando febre."
        elif self.temperatura > 34 and self.temperatura <= 37.5:
            return f"A temperatura corporal de {self.nome} é de {self.temperatura}°, indicando um estado saudável."
        else:
            return f"A temperatura corporal de {self.nome} é de {self.temperatura}°, indicando possível hipotermia."
        
Lorenzo = Temperatura("Lorenzo", 35)
print(Lorenzo.verifica_temperatura())