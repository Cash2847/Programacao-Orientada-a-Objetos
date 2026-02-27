# # Procedural
# variavel = int(input("Digite um valor: "))

# # Estruturada
# if variavel >= 25:
#     print(f"O valor é {variavel}, e por isso é maior ou igual que 25.")
# else:
#     print(f"O valor é {variavel}, e por isso é menor que 25")

# # Sub-Classe
# # Estruturada
# def tomada_decisão():
#     if variavel >= 25:
#         print(f"O valor é {variavel}, e por isso é maior ou igual que 25.")
#     else:
#         print(f"O valor é {variavel}, e por isso é menor que 25.")

# tomada_decisão()

# class TomadaDecisao:
#     def tomada_decisão():
#         if variavel >= 25:
#             print(f"O valor é {variavel}, e por isso é maior ou igual que 25.")
#         else:
#             print(f"O valor é {variavel}, e por isso é menor que 25.")

#     def tomada_decisão_inversa():
#         variavel = int(input("digite um valor: "))
#         if variavel <= 25:
#             print(f"O valor é {variavel}, e por isso é<= 25.")
#         else:
#             print(f"O valor é {variavel}, e por isso é > 25.")



# TomadaDecisao.tomada_decisão()

# 1a Classe Rica

class Termometro:
    def __init__(self, temperatura:float):
        self.temperatura = temperatura

    def verifica_temperatura(self):
        if self.temperatura > 37.5:
            return f"A temperatura corporal é de {self.temperatura}°, indicando febre."
        elif self.temperatura > 34 and self.temperatura <= 37.5:
            return f"A temperatura corporal é de {self.temperatura}°, indicando um estado saudável."
        else:
            return f"A temperatura corporal é de {self.temperatura}°, indicando possível hipotermia."
        
class Pessoa:
    # Método Construtor
    def __init__(self, nome, idade, altura, temperatura):
        # Atributos
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.temperatura = temperatura

    # Apresentar
    def apresentar(self):
        return f"""
Olá. Eu sou {self.nome}, tenho {self.altura} de altura e {self.idade} anos de idade.
        """
    def verifica_temperatura(self):
        temperatura = Termometro(self.temperatura)
        return temperatura.verifica_temperatura()
    
zedamanga = Pessoa("Zé da Manga", 20, 1.75, 34)

print(zedamanga.apresentar())
print(zedamanga.verifica_temperatura())
