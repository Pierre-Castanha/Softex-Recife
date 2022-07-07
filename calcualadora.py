
def calculadora(num1,num2,operador):
    
    if operador == '0':
        return 0
    elif operador == '1':
        return num1 + num2
    elif operador == '2':
        return num1-num2
    elif operador == '3':
        return num1*num2
    elif operador == '4':
        return num1/num2
    
while True:
        num1 = int(input('Informe o Primeiro Valor: '))
        num2 = int(input('Informe o Segundo  Valor: '))
        print('================== OPERADORES ==========================')
        print('1. Para Soma; 2 Subtração; 3. Multiplicação e 4. Divisão')
        print('========================================================')
        operador = str(input('Informe o Operador desejado: '))

        print('Resultado:',calculadora(num1,num2,operador))