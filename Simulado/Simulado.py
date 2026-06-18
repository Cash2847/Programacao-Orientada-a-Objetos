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

    def adicionar_habilidade(self, habilidade):
        if not isinstance(habilidade, Habilidade):
            raise ErroTipoInvalido("Por favor, insira algo que se encaixe na categoria de Habiidades.")
        self.habilidades.append(habilidade)
    
    def listar_habilidades(self):
        return self.habilidades
    
    def __str__(self):
        return f"Nome: {self.nome} | Nível: {self.nivel}."


    def atacar(self):
        raise NotImplementedError

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca: int):
        super().__init__(nome, nivel,)
        self.forca = forca

    def atacar(self):
        return f"O Guerreiro {self.nome} atacou usando usando {self.forca} de sua força."

class Mago(Personagem):
    def __init__(self, nome, nivel, mana: int):
        super().__init__(nome, nivel)
        self.mana = mana
    
    def atacar(self):
        return f"O Mago {self.nome} atacou usando {self.mana} de sua mana."

class Guilda:
    def __init__(self, nome: str):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, personagem):
        if not isinstance(personagem, Personagem):
            raise ErroTipoInvalido("Por favor, insira algo que se encaixe na categoria de Personagem.")
        self.membros.append(personagem)
        print(f"{personagem} foi inserido na Guilda.")
    
    def remover_membro(self, personagem):
        if personagem not in self.membros:
            raise MembroNaoEncontradoErro("Esse personagem não está na Guilda.")
        self.membros.remove(personagem)
        print(f"{personagem} foi removido da Guilda.")

    def listar_membros(self):
        return self.membros

guerreiro_1 = Guerreiro("Arthur", 100, 250)
guerreiro_2 = Guerreiro("Leonidas", 85, 500)
mago = Mago("Frieren", 70, 1200)

print(guerreiro_1)
print(guerreiro_2)
print(mago)

mago.adicionar_habilidade(Habilidade("Chaos", 53, "Mágico"))
mago.adicionar_habilidade(Habilidade("Zoltrak", 40, "Mágico"))
guerreiro_1.adicionar_habilidade(Habilidade("Excalibur", 100, "Físico"))
guerreiro_2.adicionar_habilidade(Habilidade("Phalanx Lambda", 80, "Físico"))
guerreiro_2.adicionar_habilidade(Habilidade("Phalanx Nemesis", 54, "Físico"))

for personagem in [guerreiro_1, guerreiro_2, mago]:
    print(personagem.atacar())

for h in guerreiro_2.listar_habilidades():
    print(h)

guilda = Guilda("Einherjar")

print("\n====Adicionando Membros===")

guilda.adicionar_membro(guerreiro_1)
guilda.adicionar_membro(guerreiro_2)
guilda.adicionar_membro(mago)

print(f"Guilda: {guilda.nome}")
print("Membros:")
for m in guilda.listar_membros():
    print(" -", m)

print("\n====Removendo Membro====")

guilda.remover_membro(guerreiro_1)
print("Membros:")
for m in guilda.listar_membros():
    print(" -", m)

print("==== Testando Exceções ====")

try:
    guerreiro_1.adicionar_habilidade("hwjdjewhb")
except ErroTipoInvalido as error:
    print(f"Tipo invaldo: {error}")
    
try:
    guilda.remover_membro(guerreiro_1)  # Já foi removido
except MembroNaoEncontradoErro as error:
    print(error)

try:
    guilda.adicionar_membro(42)
except ErroTipoInvalido as error:
    print(f"Tipo Invalido capturado: {error}")

try:
    personagem_base = Personagem("Teste", 1)
    personagem_base.atacar()
except NotImplementedError as error:
    print(f"Opção não pode ser implementada.")
