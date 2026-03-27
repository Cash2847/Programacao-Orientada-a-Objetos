from abc import ABC, abstractmethod

class GatewayPagamento(ABC):
    
    @abstractmethod
    def processar(self, valor):
        pass
    

class Pagamento(GatewayPagamento):
    
    def processar(self, valor):
        print(f"Procedimento")