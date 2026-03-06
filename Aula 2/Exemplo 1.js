class UsuarioJS {
    // Palavra-chave 'constructor' para inicialização
    constructor(nome, email) {
        this.nome = nome;
        this.email = email;
    }
    exibirPerfil() {
        console.log(`Usuário: ${this.nome}; Contato: ${this.email}.`);
    }
}

// Instanciação utilizando a palavra-chave 'new'
const user1 = new UsuarioJS('João Mendes', 'joao@email.com');
user1.exibirPerfil();