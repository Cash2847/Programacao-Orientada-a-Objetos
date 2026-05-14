// =============================================================
// Heranca, excecoes e projeto orientado a objetos em JavaScript
// Exemplo: Quitanda do Ze da Manga
// =============================================================

class EstoqueInsuficienteError extends Error {
  constructor(message) {
    super(message);
    this.name = "EstoqueInsuficienteError";
  }
}

class PrecoInvalidoError extends Error {
  constructor(message) {
    super(message);
    this.name = "PrecoInvalidoError";
  }
}

class Produto {
  constructor(nome, preco, estoque) {
    if (preco <= 0) {
      throw new PrecoInvalidoError(`Preco invalido para ${nome}: ${preco}`);
    }

    if (estoque < 0) {
      throw new Error("Estoque nao pode ser negativo.");
    }

    this.nome = nome;
    this.preco = preco;
    this.estoque = estoque;
  }

  vender(quantidade) {
    if (quantidade <= 0) {
      throw new Error("Quantidade vendida precisa ser maior que zero.");
    }

    if (quantidade > this.estoque) {
      throw new EstoqueInsuficienteError(
        `So tem ${this.estoque} unidade(s) de ${this.nome}. Ze da Couve tentou passar do limite.`
      );
    }

    this.estoque -= quantidade;
    return quantidade * this.preco;
  }

  repor(quantidade) {
    if (quantidade <= 0) {
      throw new Error("Reposicao precisa ser maior que zero.");
    }

    this.estoque += quantidade;
  }

  descricao() {
    return `${this.nome} | R$ ${this.preco.toFixed(2)} | estoque: ${this.estoque}`;
  }
}

class Fruta extends Produto {
  constructor(nome, preco, estoque, maturacao) {
    super(nome, preco, estoque);
    this.maturacao = maturacao;
  }

  descricao() {
    return `${super.descricao()} | maturacao: ${this.maturacao}`;
  }
}

class Verdura extends Produto {
  constructor(nome, preco, estoque, unidade) {
    super(nome, preco, estoque);
    this.unidade = unidade;
  }

  descricao() {
    return `${super.descricao()} | vendida por: ${this.unidade}`;
  }
}

class ProdutoPromocional extends Produto {
  constructor(nome, preco, estoque, desconto) {
    super(nome, preco, estoque);

    if (desconto <= 0 || desconto >= 1) {
      throw new Error("Desconto precisa ficar entre 0 e 1.");
    }

    this.desconto = desconto;
  }

  vender(quantidade) {
    const totalNormal = super.vender(quantidade);
    return totalNormal * (1 - this.desconto);
  }

  descricao() {
    return `${super.descricao()} | desconto: ${this.desconto * 100}%`;
  }
}

// -------------------------------------------------------------
// Analise orientada a objetos
// Cliente, Pedido e Item Pedido representam outras partes do problema.
// Cada classe fica com uma responsabilidade pequena e mais facil de mexer.
// -------------------------------------------------------------

class Cliente {
  constructor(nome, apelido) {
    this.nome = nome;
    this.apelido = apelido;
  }

  toString() {
    return `${this.nome} (${this.apelido})`;
  }
}

class ItemPedido {
  constructor(produto, quantidade) {
    this.produto = produto;
    this.quantidade = quantidade;
  }

  subtotal() {
    return this.produto.preco * this.quantidade;
  }
}

class Pedido {
  constructor(cliente) {
    this.cliente = cliente;
    this.itens = [];
  }

  adicionarItem(produto, quantidade) {
    this.itens.push(new ItemPedido(produto, quantidade));
  }

  totalPrevisto() {
    return this.itens.reduce((total, item) => total + item.subtotal(), 0);
  }

  fechar() {
    let total = 0;

    for (const item of this.itens) {
      total += item.produto.vender(item.quantidade);
    }

    return total;
  }
}

// -------------------------------------------------------------
// Testes simples
// -------------------------------------------------------------

const manga = new Fruta("Manga do Ze da Manga", 4.5, 8, "quase no ponto");
const couve = new Verdura("Couve do Ze da Couve", 3.0, 5, "maco");
const abacaxi = new ProdutoPromocional("Abacaxi da Dona Jurema", 7.0, 3, 0.15);

const produtos = [manga, couve, abacaxi];

console.log("=== Produtos cadastrados ===");
for (const produto of produtos) {
  console.log(produto.descricao());
}

console.log("\n=== Venda com tratamento de excecao ===");
try {
  const total = manga.vender(2);
  console.log(`Venda feita. Total: R$ ${total.toFixed(2)}`);
  console.log(manga.descricao());
} catch (erro) {
  if (erro instanceof EstoqueInsuficienteError) {
    console.log("Problema de estoque:", erro.message);
  } else {
    console.log("Erro de venda:", erro.message);
  }
} finally {
  console.log("Conferencia da venda finalizada.");
}

console.log("\n=== Tentativa de venda exagerada ===");
try {
  const total = couve.vender(20);
  console.log(`Venda feita. Total: R$ ${total.toFixed(2)}`);
} catch (erro) {
  if (erro instanceof EstoqueInsuficienteError) {
    console.log("Deu ruim no estoque:", erro.message);
  } else {
    console.log("Entrada invalida:", erro.message);
  }
}

console.log("\n=== Pedido completo ===");
const cliente = new Cliente("Jose Marinaldo", "Ze da Manga");
const pedido = new Pedido(cliente);

pedido.adicionarItem(manga, 2);
pedido.adicionarItem(abacaxi, 1);

console.log("Cliente:", pedido.cliente.toString());
console.log(`Total previsto sem regra promocional: R$ ${pedido.totalPrevisto().toFixed(2)}`);

try {
  const totalFinal = pedido.fechar();
  console.log(`Total final considerando as regras das classes: R$ ${totalFinal.toFixed(2)}`);
} catch (erro) {
  console.log("Pedido nao fechado:", erro.message);
}

console.log("\n=== Cadastro com preco invalido ===");
try {
  const produtoEsquisito = new Produto("Banana invisivel do Seu Ninguem", -2.0, 10);
  console.log(produtoEsquisito.descricao());
} catch (erro) {
  if (erro instanceof PrecoInvalidoError) {
    console.log("Cadastro recusado:", erro.message);
  } else {
    console.log("Erro inesperado:", erro.message);
  }
}
