class BancoDeDadosLocal {
conectar() { return 'Conectado ao DB interno.'; }
}
class AplicacaoWeb {
    constructor() {
    this.db = new BancoDeDadosLocal();
    iniciar();
    console.log(this.db.conectar());
    }
}

// Execução do Sistema
const app = new AplicacaoWeb();
// A responsabilidade de instanciar o DB é exclusiva da Aplicação.