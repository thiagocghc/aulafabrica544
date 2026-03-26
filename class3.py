class Professor:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []  # Composição
        self.professores = []    # Agregação

    def adicionar_departamento(self, nome_dep):
        self.departamentos.append(Departamento(nome_dep))

    def adicionar_professor(self, prof):
        self.professores.append(prof)
