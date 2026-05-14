class Veiculo {
    constructor() {}
}

class Carro extends Veiculo { // Uso explícito da palavra-chave para Herança.
    constructor() {
        super();
    }
}


try {
    processarDados();
} catch (error) {
    if (instanceof TypeError) {
        logErro(error);
    }
} finally {
    fecharConexao();
}