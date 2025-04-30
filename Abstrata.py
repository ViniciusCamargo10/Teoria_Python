from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def registrar_ponto(self):
        pass

    @abstractmethod
    def receber_salario(self):
        pass

class Estagiario(Funcionario):
    def registrar_ponto(self):
        print("Estagiario registrou o ponto")
    
    def receber_salario(self):
        print("Estagiario recebeu salario")

class Gerente(Funcionario):
    def registrar_ponto(self):
        print("Gerente registrouuuuu o ponto")
    
    def receber_salario(self):
        print("Gerente recebeu salario")

estag = Estagiario()
gerente = Gerente()

estag.receber_salario()
estag.registrar_ponto()

gerente.receber_salario()
gerente.registrar_ponto()