
def calculadora(num1,num2,operador):
    
    if operador == '0':
        return 
    elif operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1-num2
    elif operador == '*':
        return num1*num2
    elif operador == '/':
        return num1/num2
    
while True:
        num1 = int(input('Informe o Primeiro Valor: '))
        num2 = int(input('Informe o Segundo  Valor: '))
        print('================== OPERADORES ==========================')
        print('"+". Para Soma; "-" Subtração; "*" Multiplicação e "/" Divisão')
        print('========================================================')
        operador = str(input('Informe o Operador desejado: '))

        print('Resultado:',calculadora(num1,num2,operador))