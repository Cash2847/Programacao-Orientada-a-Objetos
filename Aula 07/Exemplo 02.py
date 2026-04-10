class BancoDeDadosLocal:
    def conectar(self):
        return 'Conectado ao DB interno.'

class AplicacaoWeb:
    def _init_ (self):
        self.db = BancoDeDadosLocal()

    def iniciar(self):
        print(self.db.conectar())

# Execução do Sistema
app = AplicacaoWeb()
# 0 app cria seu próprio banco de dados internamente.
# Deletar 'app' deleta o banco junto.