// class Usuario {
//     constructor(nome, email) {
//         this.nome = nome;
//         this.email - email;
//     }
// }

// ================================================================================
// Exercício 1 - Classe Produto (atribútos e método)
// ================================================================================

class Produto {
    constructor(nome, preco, estoque) {
        this.nome = nome;
        this.preco = preco;
        this.estoque = estoque;
    }

    exibirInfo() {
        console.log(`${this.nome}: R$${this.preco} | ${this.estoque}.`)
    }
}

// Instanciando e chamando
const p = new Produto("Café", 18.90, 50);
p.exibirInfo();

// ================================================================================
// Exercício 2 - Interação entre objetos (Pedido recebe Produto)
// ================================================================================

class Pedido {
    constructor() {
        this.itens = [];
    }

    adicionarProduto(produto) {
        this.itens.push(produto.nome);
        consol.log(`Adicionado: ${produto.nome}`);
    }
}

// Criando os dois objetos
const cafe = new Produto("Café", 18.90, 50);
const pedido = new Pedido();

//Interação: pedido recebe café