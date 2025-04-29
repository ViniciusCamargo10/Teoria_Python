# Lista de nomes
listaNomes = ["Vinicius", "Gustavo", "Giovanna"]

# Imprime a lista e o seu tamanho
print(listaNomes)  # Imprime os nomes
print(len(listaNomes))  # Quantos elementos há na lista
print(listaNomes[2])  # Corrigido: imprime o terceiro nome
print("\n")

# Diversas listas com tipos de dados diferentes
lista1 = ["A", "B", "C"]
lista2 = [1, 2, 3, 4]
lista3 = [True, False]
lista4 = ["Robson", 1, "True"]

# Imprime a lista4
print(lista4)

print("\n")

# Acessando posições específicas em lista2
print("Elemento na posição 3:", lista2[3])  # Posição 3 em lista2
print("Último elemento da lista2:", lista2[-1])  # Último elemento

# Fatiamento da lista (posição 1 até 3 - excluso)
print("Elementos entre as posições 1 e 3:", lista2[1:3])

# Primeiros três elementos
print("Três primeiros elementos da lista2:", lista2[:3])

# Pulando de dois em dois
print("Elementos de dois em dois:", lista2[::2])

# Lista ao contrário
print("Lista2 em ordem reversa:", lista2[::-1])

print("\n")

# Encontrando valores mínimo e máximo
listaMaxMin = [23, 50, 53, 34, 20]
print("Valor mínimo:", min(listaMaxMin))
print("Valor máximo:", max(listaMaxMin))

print("\n")

# Criando uma lista com números de 0 até 10
listaAteDez = [i for i in range(101) if i <= 10]
print("Lista de números até 10:", listaAteDez)

print("\n")

# Criando uma lista com números pares de 0 a 100
listaPares = list(range(0, 102, 2))
print("Números pares de 0 a 100:", listaPares)

print("\n")

# Copiando uma lista
listaOriginal = ["Uno", "Gol", "Compass"]
listaCopia = listaOriginal.copy()
print("Lista copiada:", listaCopia)

print("\n\n")

# Juntando duas listas
listaNumeros = [1, 3, 2]
listaLetras = ["A", "C", "B"]
listasUnidas = listaLetras + listaNumeros
print("Listas unidas:", listasUnidas)

# Adicionando um elemento no final da lista
listaNumeros.append(4)
print("ListaNumeros após append:", listaNumeros)

# Inserindo um elemento em uma posição específica
listaNumeros.insert(2, 7)
print("ListaNumeros após insert:", listaNumeros)

# Ordenando a lista de letras em ordem crescente
listaLetras.sort()
print("ListaLetras ordenada (A a Z):", listaLetras)

# Ordenando a lista de números em ordem decrescente
listaNumeros.sort(reverse=True)
print("ListaNumeros ordenada (Z a A):", listaNumeros)
