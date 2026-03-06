class Usuario:
   # Método Construtor: Inicializa os atributos (Estado)
    def __init__(self, nome, email):
      self.nome = nome
      self.email = email
    
    # Método de Classe (Comportamento)

    def exibir_perfil(self):
       print(f"Usuário: {self.nome}; Contato: {self.email}.")

# Instanciando dois objetos distintos na memórias
usuario1 = Usuario("Ana Silva", "ana@email.com")
usuario2 = Usuario("Carlos Moura", "carlos@email.com")

# Invocando comportamentos

usuario1.exibir_perfil()
usuario2.exibir_perfil()