
def calculo_idade(nome, ano):

    if (nome != ''):
        if ((ano >= 1922) and (ano <= 2021)):
            res = 2022 - ano
        else:
            raise Exception('Ano de Nascimento deve ser entre 1922 a 2021.') 
    else:
            raise Exception('Nome deverá ser preeenchido!')
   
    return res


prog = True

while (prog):
    try:
        print('====================================')
        print(' Programa de Cálculo de idade atual')
        print('====================================')

        print('Informe o seu nome:')
        nome = str(input())
        print('Informe o ano de Nascimento: ')
        ano = int(input())
        
        idade = calculo_idade(nome, ano)

        print('Caro(a) ' + str(nome) + ', você atualmente tem: ' + str(idade))

        prog = False

    except:
        print('dados inválidos!!')
        clear()



