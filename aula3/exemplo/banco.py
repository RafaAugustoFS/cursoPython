class ContaBancaria:
    
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if valor<=self.saldo:
            self.saldo -= valor
            print(f'SAQUE EXECUTADO!')
            return True
        else:
            print(f'SALDO INSUFICIENTE, SALDO ATUAL {self.saldo}')
            return False
    
    def get_saldo(self):
        print(f'saldo: {self.saldo}')
        return self.saldo
    
c1 = ContaBancaria(1000)

c1.depositar(1000)
c1.sacar(500)
c1.get_saldo()