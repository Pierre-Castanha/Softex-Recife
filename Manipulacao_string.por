programa
{
	inclua biblioteca Texto-->tx
	
	cadeia nome, endereco, pai, mae, cx_alta, cx_baixa
	inteiro contador
	
	funcao inicio()
	{
		nome= "Pierre Leon Castanha de Lima"
		endereco= "Rua João Pessoa, 549"
		mae= "Maria Aparecida"
		pai= "José Walter"
		cx_alta= tx.caixa_alta(nome)
		cx_baixa = tx.caixa_baixa(nome)
		contador = tx.numero_caracteres(nome)
		
		escreva("Meu nome é: ", nome, ", meu pai é: ", pai, ", minha mãe chama-se: ", mae, "\n")
		escreva ("nome em caixa alta: ", cx_alta, "\n")
		escreva ("nome em caixa baixa: ", cx_baixa, "\n")
		escreva ("Meu nome tem: ", contador, ", caracteres")

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 600; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */