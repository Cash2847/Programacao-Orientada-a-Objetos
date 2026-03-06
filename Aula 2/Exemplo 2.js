class Termometro {
    constructor(temperatura) {
        this.temperatura = temperatura
    }

    verificar_estado() {
        if (this.temperatura < 35) {
            return "Hipotermia.";
        } else if (this.temperatura >= 37.5) {
            return "Doente (Febre).";
        } else{
            return "Temperatura normal."
        }
    }
}

class Pessoa {

    constructor(nome, idade, altura, temperatura) {
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;
        this.temperatura = temperatura;
    }

    usar_termometro(Termometro) {
        return `${this.nome} está medindo a temperatura... Temperatura: ${this.temperatura} ºC. Estado: ${this.chamaTermometro()}.`;
    }
    
    

    chamaTermometro = (temperatura) => {
        temperatura = new Termometro(this.temperatura);
        return temperatura.verificar_estado();
    }
}

const pessoa = new Pessoa("João", 40, 1.90, 50);
const hh = pessoa.usar_termometro();
console.log(hh)