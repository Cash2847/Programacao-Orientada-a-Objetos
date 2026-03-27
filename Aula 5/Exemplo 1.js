class GatewayPagamento {
    constructor() {
        if (this.constructor === GatewayPagamento) {
            throw new Error("Classe abstrata não pode ser instanciada.");
        }
    }

    processar(valor) {
        throw new Error("Método abstrato 'processar()' deve ser implementado")
    }
}

class PagamentoPix extends GatewayPagamento {
    processar(valor) {
        console.log(``)
    }
}