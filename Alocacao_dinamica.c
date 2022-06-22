#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

int i, tam, *vet;
tam = 20;

srand(time(NULL));

vet = malloc(tam * sizeof(int));

if (vet) {
    printf("Memoria alocada com sucesso!\n");

    for (i = 0; i < tam; i++)
        *(vet + i) = rand() % 100;
    
    for (i = 0; i < tam; i++)
        printf("%d ", *(vet + i));
    printf("\n");

    printf("Digite o novo tamanho do vetor: ");
    scanf("%d", &tam);

    vet = realloc(vet, tam);  // Utilização da função realloc(), realocação de novos números.

    printf("\nVetor realocado: \n");

    for (i = 0; i < tam; i++)
        printf("%d ", *(vet + i));
    printf("\n"); 

    free(vet); // liberação da memória, através da função free().  
}
else{
    printf("Erro na alocação de memoria!\n");
}

return 0;
}