class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def exibirdados(self):
        print(f'nome do aluno: {self.nome}')
        print(f'curso do aluno: {self.curso}')

    def atulizarcurso(self, novocurso):
        self.curso = novocurso

nomealuno = input('insira o nome do aluno: ')
cursoaluno = input('insira o curso do aluno: ')

aluno = Aluno(nomealuno, cursoaluno)

print('\n dados do aluno ')
aluno.exibirdados()
