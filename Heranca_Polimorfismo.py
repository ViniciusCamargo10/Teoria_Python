class Veiculo:
    
    def __init__(self, cor, modelo, ano, tipo):
        self.cor = cor       
        self.modelo = modelo 
        self.ano = ano      
        self.tipo = tipo

    def buzinar(self):
        print("buzinandooooh\n")
    
    def detalhes(self):
        print(f"Detalhes do Veiculo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}\n")

class Moto(Veiculo):
    def __init__(self, cor, modelo, ano):
        super().__init__(cor, modelo, ano, tipo="Moto")

moto = Moto("vermelha","Moto XJ",2025)

moto.detalhes()
moto.buzinar()

class Caminhao(Veiculo):
    def __init__(self, cor, modelo, ano):
        super().__init__(cor, modelo, ano, tipo="Caminhao")

    def buzinar(self):
        print("BAMMM, BAMMM, BAMMM")

caminhao = Caminhao("dourado", "Caminhao da Honda",2024)

caminhao.detalhes()
caminhao.buzinar()        
