class Aluno:
    def __init__(self, nome,ra):
        self.nome = nome
        self.ra = ra

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # Lista de alunos que frequentam a universidade

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)


a1 = Aluno("João","1234")
a2 = Aluno("Maria","4321")

faculdade = Universidade("Faculdade Insted")
faculdade.adicionar_aluno(a1)
faculdade.adicionar_aluno(a2)

print(f"Alunos da {faculdade.nome}:")
for aluno in faculdade.alunos:
    print(f"Nome: {aluno.nome} - RA: {aluno.ra}")
