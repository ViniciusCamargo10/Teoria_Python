class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def ver_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

conta = ContaBancaria(1000)

conta.depositar(100)

conta.ver_saldo()