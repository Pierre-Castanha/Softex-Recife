public class Financiamento {

    public Double valorTotal;
    public Double entrada;
    public Integer parcelas;


    public Financiamento(Double valorTotal, Double entrada, Integer parcelas) {
        if( entrada < valorTotal * 0.2) {
            throw new RuntimeException("A entrada deverá ser maior ou igual 20% do valor do financiamento!");
        }
        else if(parcelas < 6) {
            throw new RuntimeException("A quantidade de parcelas deve ser maior ou igual a 6!");
        }
        this.valorTotal = valorTotal;
        this.entrada = entrada;
        this.parcelas = parcelas;
    }

    public double prestacao(){
        return (valorTotal-entrada)/parcelas;
    }
    }
