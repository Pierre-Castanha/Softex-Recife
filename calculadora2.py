from ast import Str


def calculadora(num1,num2,operador):
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1-num2
    elif operador == 3:
        return num1*num2
    elif operador == 4:
        return num1/num2
    

while True:

        num1 = int(input('Informe o Primeiro Valor: '))
        num2 = int(input('Informe o Segundo  Valor: '))
        
        print('=============[]========= OPERADORES ===================[]=========')
        print(' 1. Para Soma; 2 Subtração; 3. Multiplicação; 4. Divisão e 5. Sair')
        print('=====[]====================================[]=====================')

        operador = int(input('Informe o Operador desejado: '))

        calculadora(num1, num2, operador)

        if operador == 0:
            print(' SAIR!!!')
            exit()
        elif operador =='' or operador < 0 or operador >= 5:
            print('Essa Opção não existe! Escolha entre 1 a 4')
        else:
           print('O resultado: ', calculadora(num1, num2, operador))