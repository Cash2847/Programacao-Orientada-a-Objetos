class Carro {
    constructor(marca) {
        this.marca = marca;
    }

    acelerar() {
        console.log(`O ${this.marca} acelerou!`)
    }
}

const meuCarro = new Carro("Toyota");
meuCarro.acelerar();