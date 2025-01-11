class ContaBancaria:
    def _init_(self, deposito, saque) -> None:
        self.deposito = deposito
        self.saque = saque
    
    def depositar(self):
        self.deposito = None
        self.saque = None

    def sacar(self):