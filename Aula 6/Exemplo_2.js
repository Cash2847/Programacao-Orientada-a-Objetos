class Imprimivel {
    imprimir() {
        throw new Error("O método imprimir() deve ser implementado.")
    }
}

class Relatorio extends Imprimivel {
    imprimir() {
        console.log("Gerando relatório...")
    }
}

const fila = [
    new Relatorio(),
    new Fatura(),
    new Relatorio()
];

fila.forEach(doc => doc.imprimir());
fila.forEach(doc => doc.imprimir());