# Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:

# - Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
# - Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
# - Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.

# No sistema, todos os valores devem estar armazenados em variáveis.


nome = (input('Informe o nome do Aluno: ')) 
nota1 = float (input('Informe a 1ª. Nota do Aluno: '))
nota2 = float (input('Informe a 2ª. Nota do Aluno: '))
faltas = int (input('Informe a quantidade de faltas do Aluno: '))

media = (nota1 + nota2)/2


if media >= 7 and  faltas < 3:
    print('O aluno: {}, foi Aprovado! Sua média foi: {} e teve faltas inferior a 3'.format(nome, media))
else:
    if media < 7 and faltas < 3:
        print('O aluno: {}, foi Reprovado! por não atingir a média necessária (7.0), sua média foi: {}'.format(nome, media))
    else:
        print('O aluno: {}, foi Reprovado! por ultrapassar a quantidade de faltas máxima (3.0), sua faltas foram: {}'.format(nome, faltas))

