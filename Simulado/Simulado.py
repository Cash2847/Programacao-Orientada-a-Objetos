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

    def __init__(self, nome: str, nivel: int, habilidades):
        self.nome = nome
        self.nivel = nivel
        self.habilidades = []

    def adicionar_habilidade(self, habilidade):
        self.habilidades.append(habilidade(Habilidade))
    
    def listar_habilidades(self):
        return self.habilidades
    
    def __str__(self):
        return f"Nome: {self.nome} | Nível: {self.nivel}."


    def atacar():
        return NotImplementedError

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, habilidades, forca: int):
        super().__init__(nome, nivel, habilidades)
        self.forca = forca

    def atacar(self):
        return f"O Guerreiro {self.nome} atacou usando a habilidade {self.habilidades} usando sua força."

class Mago(Personagem):
    def __init__(self, nome, nivel, habilidades, mana: int):
        super().__init__(nome, nivel, habilidades)
        self.mana = mana
    
    def atacar(self):
        return f"O Mago {self.nome} atacou usando a habilidade {self.habilidades} usando sua mana."
        
