# Definindo uma classe chamada Carro
class Carro:
    # Método especial __init__ para inicializar as propriedades do carro
    def __init__(self, cor, modelo, ano):
        self.cor = cor        # Atributo cor
        self.modelo = modelo  # Atributo modelo
        self.ano = ano        # Atributo ano

    # Método para buzinar
    def buzinar(self):
        print("Biiih!")

    # Método para exibir detalhes do carro
    def mostrar_detalhes(self):
        print(f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}")

    # Método para acelerar
    def acelerar(self):
        print(f"O {self.modelo} está acelerando!")

    # Método para frear
    def frear(self):
        print(f"O {self.modelo} está freando!")

# Criando um objeto da classe Carro
meuCarro = Carro("Roxo", "Mustang", 2025)

# Acessando atributos
print(f"A cor do meu carro é: {meuCarro.cor}")

# Chamando métodos do objeto
meuCarro.buzinar()
meuCarro.mostrar_detalhes()
meuCarro.acelerar()
meuCarro.frear()

print("\n---------------------------------\n")

# Criando outro objeto
segundoCarro = Carro("Preto", "Camaro", 2024)
segundoCarro.mostrar_detalhes()
segundoCarro.buzinar()
