# Tuplas não podem ser alteradas (imutáveis)
tupla = (1, 2, 3)

# Imprimir o último elemento da tupla
print("Último elemento da tupla:", tupla[-1])

# Criar uma nova tupla para concatenar com a original
novaTupla = (4, 5, 6)

# Concatenando tuplas para criar uma nova tupla
tupla += novaTupla  # Isso não modifica a tupla original, mas cria uma nova

# Imprimir a tupla atualizada
print("Tupla atualizada:", tupla)

# Imprimir a soma das duas tuplas (nova concatenação)
print("Concatenação novamente:", tupla + novaTupla)

# Iterar sobre os elementos da novaTupla
for i in novaTupla:
    print(i)
    