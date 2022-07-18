
def votacao(candidato):  # fução para votação com a variavel candidato como argumento
    global candidato_X, candidato_Y, candidato_Z, branco, nulos
 
    if candidato.isalpha():  # checa se candidato contem apenas letras
        if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()

    elif candidato.isnumeric():  # checa se candidato e um caracter numérico

        if candidato == '889' or candidato == '847' or candidato == '515' or candidato =='0':
            if candidato == '889':
                candidato_X += 1
            elif candidato == '847':
                 candidato_Y += 1
            elif candidato == '515':
                 candidato_Z += 1
            elif candidato == '0':
	             branco += 1
        elif candidato != '889' or candidato != '847' or candidato != '515' or candidato !='0':
                 nulos += 1
                 candidato = str(input('Digite um numero válido : '))



def print_resultados():  # printa resultados e encerra programa
    global candidato_X, candidato_Y, candidato_Z, branco, nulos

    tot_validos = int(candidato_X) + int(candidato_Y) + int(candidato_Z) + int(branco)

    a = candidato_X
    b = candidato_Y
    c = candidato_Z
    
    if a > b and a > c:
        eleito_a = "Candidato X"
    elif b > a and b > c:
        eleito_a = "Candidato Y"
    else:
        eleito_a = "Candidato Z"

    print('==================================')
    print('  B O L E T I M   D E   U R N A')
    print('==================================')

    print('QUANTIDADE DE   VOTOS....: ' + str(tot_validos))

    print('CANDIDATO X   - TOTAL DE : ' + str(candidato_X))
    print('CANDIDATO Y   - TOTAL DE : ' + str(candidato_Y))
    print('CANDIDATO Z   - TOTAL DE : ' + str(candidato_Z))
    print('VOTOS BRANCOS – TOTAL DE : ' + str(branco))
    print('VOTOS NULOS   – TOTAL DE : ' + str(nulos))

    print('===================================')
    print(' CANDIDATO ELEITO É: ' + str(eleito_a))
    print('===================================')

    exit()  # encerra prog


if __name__ == '__main__':  # funcao main 
    candidato_X = 0
    candidato_Y = 0
    candidato_Z = 0
    branco = 0
    nulos = 0

    while True:  # laço ocorre indefinidamente até que ocorra o 'Fim'
        
        print('====================================')
        print('     Programa Votação Eleitoral     ')
        print('====================================')
        print('====================================')
        print('       C A N D I D A T O S          ')
        print('====================================')
        print('====================================')
        print(' CAND X Nº 889   -   CAND Y Nº 847  ')
        print(' CAND Z Nº 515   -   BRANCO Nº   0  ')
        print('====================================')

        candidato = str(input('ELEIÇÃO \n Digite o número do seu candidato: '))
        votacao(candidato)