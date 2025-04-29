# Definições de Tipos

"""
- String: Uma sequência de caracteres. Exemplo: "Olá"
- int: Um número inteiro, sem casas decimais. Exemplo: 25
- float: Um número de ponto flutuante, com casas decimais. Exemplo: 3.14
- bool: Um valor Booleano, pode ser True (Verdadeiro) ou False (Falso). Exemplo: True
- list: Uma coleção ordenada de itens, mutável (pode ser alterada). Exemplo: [1, 2, 3]
"""

# Exemplos de cada tipo

# String
minha_string = "Olá"
print("String:", minha_string)

# Inteiro
meu_inteiro = 25
print("Inteiro:", meu_inteiro)

# Float
meu_float = 3.14
print("Float:", meu_float)

# Booleano
meu_booleano = True
print("Booleano:", meu_booleano)

# Lista
minha_lista = [1, 2, 3]
print("Lista:", minha_lista)

print("\n")

# Usando split() para transformar uma string em lista
nome = "Vinicius Souza Camargo"
nome = nome.split(" ")  # Divide a string onde houver espaço
print("Nome dividido em lista:", nome)
