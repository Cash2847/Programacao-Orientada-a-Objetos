# =============================================================
# GABARITO – P1 Laboratório de POO 2026.1
# Professor: Diego Ramos Inácio
# =============================================================

# -------------------------------------------------------
# QUESTÃO 1 – Criação das Classes (1 ponto)
# -------------------------------------------------------

class Ficha:
    def __init__(self):
        self.exercicios = []
        self.data_criacao = "2026-04-16"

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

    # -------------------------------------------------------
    # QUESTÃO 2 – listar exercicios (parte dos 2 pontos)
    # -------------------------------------------------------
    def listar_exercicios(self):
        return self.exercicios

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.ficha = Ficha()  # composição: Ficha criada junto com o Aluno

    # -------------------------------------------------------
    # QUESTÃO 2 – Método __str__ (parte dos 2 pontos)
    # -------------------------------------------------------
    def __str__(self):
        return f"Aluno: {self.nome} | Matrícula: {self.matricula}"


class Academia:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  #agregação: alunos existem de forma independente

    # -------------------------------------------------------
    # QUESTÃO 2 – Métodos matricular_aluno e listar_alunos
    # -------------------------------------------------------
    def matricular_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return self.alunos

    # -------------------------------------------------------
    # QUESTÃO 3 – Processamento com Listas (1,5 ponto)
    # -------------------------------------------------------
    def buscar_aluno(self, matricula):
        for a in self.alunos:
            if a.matricula == matricula:
                return a
        return None

    def buscar_por_nome(self, trecho):
        return [a for a in self.alunos if trecho.lower() in a.nome.lower()]

    def exercicios_do_aluno(self, matricula):
        aluno = self.buscar_aluno(matricula)
        if aluno:
            return aluno.ficha.listar_exercicios()
        return []


# -------------------------------------------------------
# QUESTÃO 4 – Demonstração dos Relacionamentos (2,5 pontos)
# -------------------------------------------------------

# 1. Criar três Alunos (Ficha criada automaticamente – composição)
a1 = Aluno("Ana Lima", "20260001")
a2 = Aluno("Bruno Dias", "20260002")
a3 = Aluno("Carla Mota", "20260003")

# 2. Adicionar pelo menos dois exercícios na Ficha de cada Aluno
a1.ficha.adicionar_exercicio("Supino")
a1.ficha.adicionar_exercicio("Agachamento")

a2.ficha.adicionar_exercicio("Corrida")
a2.ficha.adicionar_exercicio("Ciclismo")

a3.ficha.adicionar_exercicio("Natação")
a3.ficha.adicionar_exercicio("Pilates")

# 3. Criar uma Academia e matricular os três Alunos
academia = Academia("FitLife")
academia.matricular_aluno(a1)
academia.matricular_aluno(a2)
academia.matricular_aluno(a3)

# 4. Percorrer a lista e exibir nome + exercícios de cada Aluno
print("=== Alunos da Academia ===")
for aluno in academia.listar_alunos():
    print(aluno)
    for exercicio in aluno.ficha.listar_exercicios():
        print(" -", exercicio)

# 5. Remover um Aluno e demonstrar que ainda existe (agregação)
print("\n=== Removendo a1 da Academia ===")
academia.alunos.remove(a1)
print(f"a1 ainda existe fora da academia: {a1}")
print(f"Alunos restantes na academia: {len(academia.listar_alunos())}")
