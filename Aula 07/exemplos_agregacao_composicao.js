class Usuario {
  constructor(nome, senha) {
    this.nome = nome;
    this.senha = senha;
  }
}

class Sistema {
  constructor() {
    this.usuarios = [];
  }

  adicionarUsuario(usuario) {
    this.usuarios.push(usuario);
  }

  autenticar(nome, senha) {
    const usuario = this.usuarios.find(
      (item) => item.nome === nome && item.senha === senha
    );

    return usuario
      ? `Usuario ${nome} autenticado com sucesso.`
      : "Falha na autenticacao.";
  }
}

class Token {
  constructor(valor = "XYZ789") {
    this.valor = valor;
  }
}

class Autenticacao {
  constructor() {
    // Composição: o token é criado dentro da autenticacao
    this.token = new Token();
  }

  exibirToken() {
    return `Token gerado: ${this.token.valor}`;
  }
}

class Motorista {
  constructor(nome) {
    this.nome = nome;
  }
}

class Motor {
  constructor(potencia) {
    this.potencia = potencia;
  }
}

class Carro {
  constructor(modelo, potenciaMotor) {
    this.modelo = modelo;
    this.motorista = null;
    // Composição: o carro cria seu proprio motor
    this.motor = new Motor(potenciaMotor);
  }

  definirMotorista(motorista) {
    // Agregação: o motorista ja existia antes da associacao
    this.motorista = motorista;
  }

  mostrarDados() {
    const nomeMotorista = this.motorista ? this.motorista.nome : "Sem motorista";
    return `Carro: ${this.modelo} | Motor: ${this.motor.potencia} cv | Motorista: ${nomeMotorista}`;
  }
}

class Cliente {
  constructor(nome) {
    this.nome = nome;
  }
}

class Historico {
  constructor() {
    this.movimentos = [];
  }

  adicionarMovimento(descricao) {
    this.movimentos.push(descricao);
  }
}

class Conta {
  constructor(numero, titular) {
    this.numero = numero;
    this.titular = titular;
    // Composição: o historico pertence a conta
    this.historico = new Historico();
  }

  depositar(valor) {
    this.historico.adicionarMovimento(`Deposito de R$ ${valor}`);
  }
}

class Banco {
  constructor(nome) {
    this.nome = nome;
    this.clientes = [];
  }

  adicionarCliente(cliente) {
    // Agregação: o cliente existe independentemente do banco
    this.clientes.push(cliente);
  }
}

console.log("=== AUTENTICACAO ===");
const usuario = new Usuario("Ana", "1234");
const sistema = new Sistema();
sistema.adicionarUsuario(usuario);
console.log(sistema.autenticar("Ana", "1234"));

const auth = new Autenticacao();
console.log(auth.exibirToken());

console.log("\n=== CARRO ===");
const motorista = new Motorista("Carlos");
const carro = new Carro("Fusca", 85);
carro.definirMotorista(motorista);
console.log(carro.mostrarDados());

console.log("\n=== BANCO ===");
const cliente = new Cliente("Marina");
const banco = new Banco("Banco POO");
banco.adicionarCliente(cliente);

const conta = new Conta("0001", cliente.nome);
conta.depositar(500);

console.log(`Banco: ${banco.nome}`);
console.log(`Cliente agregado: ${banco.clientes[0].nome}`);
console.log(`Conta: ${conta.numero} | Titular: ${conta.titular}`);
console.log("Historico da conta:", conta.historico.movimentos);
