# Desenvolva um código que utilize as seguintes características de um veículo:
# - Quantidade de rodas;
# - Peso bruto em quilogramas;
# - Quantidade de pessoas no veículo.

# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:

# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
# E: Veículos com quatro rodas ou mais e com mais de 6000 kg.



quantRodas = int(input('Qual a quant de rodas do veículo: ')) 
PesoBruto = float (input('Informe o Peso Bruto em quilogramas: '))
quatPessoas = float (input('Informe a quant de pessoas no veículo: '))

if quantRodas == 2 or quantRodas == 3:
    print('A melhor categoria para veículos com duas o três rodas é "A" ')
elif quantRodas == 4 and quatPessoas <= 8 and PesoBruto <= 3500:
    print('A melhor categoria para veículos com duas o três rodas é "B" ')
elif quantRodas >= 4 and PesoBruto >= 3500 and PesoBruto <= 6000:
    print('A melhor categoria para veículos com duas o três rodas é "C" ')
elif quantRodas >= 4 and quatPessoas > 8:
    print('A melhor categoria para veículos com duas o três rodas é "D" ')
else:
    if quantRodas >= 4 and PesoBruto > 6000:
        print('A melhor categoria para veículos com duas o três rodas é "E" ')
