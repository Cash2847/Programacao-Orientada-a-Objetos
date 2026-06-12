class ErroRPG(Exception):
    """Base para todas as exceções desse simulado."""
    pass

class ErroTipoInvalido(ErroRPG):
    """Lançada para quando um personagem/Habilidade inserido(a) é inválida."""
    pass

class MembroNaoEncontradoErro(ErroRPG):
    """Lançada quando o membro procurado não é encontrado."""
    pass

class Habilidade:
    def __init__(self, nome: str, nivel: int, tipo: str):
        self.nome = nome
        self.nivel = nivel
        self.tipo = tipo

    def __str__(self):
        return f"Habilidade: {self.nome} | Nível: {self.nivel} | Tipo: {self.tipo}."

class Personagem:
    """
    Classe que agrupa Guerreiros e Magos.
    """

    def __init__(self, nome: str, nivel: int):
        self.nome = nome
        self.nivel = nivel
        self.habilidades = []

    def adicionar_habilidade(self, hab):
        self.habilidade = Habilidade()
        self.habilidades.append(habilidade)
    
    def listar_habilidades(self):
        return self.habilidades
    
    def __str__(self):
        return f"Nome: {self.nome} | Nível: {self.nivel}."
    
p1 = Personagem("Zé da Manga", 21)
p1.adicionar_habilidade("Sky Eater")
p1.listar_habilidades

