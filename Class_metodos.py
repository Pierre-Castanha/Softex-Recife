from email.errors import InvalidDateDefect
from mailbox import NotEmptyError


class Aluno:
    def __init__(self, nome, idade, nota_1, nota_2, media):
        self.nome = nome 
        self.idade = idade
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media = media
    
    def Media (self):
        self.media = (self.nota_1 + self.nota_2) / 2
        if self.media >= 6:
            print('Aluno Aprovado!')
        else:
            print('Aluno Reprovado!')
    
    def ExibirInformacao(self):
        print(self.nome + ' ', self.idade, self.media)
    
Aluno_A = Aluno('Pierre Castanha', '52 anos', 7.0, 8.0, 0.0)
Aluno_A.Media()
Aluno_A.ExibirInformacao()

