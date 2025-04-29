# Criando um conjunto
meu_conjunto = {1, 2, 3, 4, 5}

# Adicionando um elemento
meu_conjunto.add(6)

# Removendo um elemento
meu_conjunto.remove(2)

# Verificando se um elemento está no conjunto
print(3 in meu_conjunto)  # True (Verdadeiro)

# Conjunto com valores duplicados (serão automaticamente removidos)
conjunto_com_duplicados = {1, 2, 3, 3, 4, 5, 5}
print(conjunto_com_duplicados)  # {1, 2, 3, 4, 5}

# Tamanho do conjunto
print(len(meu_conjunto))  # 5

# Operações com conjuntos (união, interseção e diferença)

# Criando dois conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# União: junta os elementos dos dois conjuntos, sem repetir
uniao = conjunto1 | conjunto2
print(f"União: {uniao}")  # {1, 2, 3, 4, 5}

# Interseção: elementos comuns entre os conjuntos
intersecao = conjunto1 & conjunto2
print(f"Interseção: {intersecao}")  # {3}

# Diferença: elementos que estão em conjunto1 mas não em conjunto2
diferenca = conjunto1 - conjunto2
print(f"Diferença: {diferenca}")  # {1, 2}
