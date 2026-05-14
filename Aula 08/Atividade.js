class SaldoInsuficienteError extends Error {
  constructor(message) {
    super(message);
    this.name = "SaldoInsuficienteError";
  }  
}

class contaBase {
    constructor(){
    this.saldo = 0
}
}

class contaCorrente extends contaBase {
    constructor() {
        super();
    }

    sacar(valor) {
        if (valor > this.saldo) {
            throw new SaldoInsuficienteError(
                `O valor sacado (R$ ${valor}) é maior do que o saldo disponível (R$ ${self.saldo}). Logo, o saque é inválido.`
            );
        };

        this.saldo -= valor;
        return `Saque completo. Saldo atual: ${self.saldo}.`
    };
};

const conta = new contaCorrente();
conta.saldo = 10;

console.log(`O saldo atual da conta é ${conta.saldo}`);

try {
    conta.sacar(20);
} catch(erro) {
    if (erro instanceof SaldoInsuficienteError) {
        console.log("Saldo incapaz de ser realizado: ", erro.message)
    };
    console.log(`Saque completo. Saldo atual: ${conta.saldo}.`);
    
} finally {
  console.log("Operação completa");
}