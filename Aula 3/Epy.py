class Validar:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def validarUser(self, user, senha):
        if senha == self.senha and user == self.nome:
            return "Validção Realizada com Sucesso."
        else:
            return "Usuário ou senha incorreto. Tente novamente."
        
u = Validar("Zé", "ze123")

print(u.validarUser("Zé", "ze14r3"))