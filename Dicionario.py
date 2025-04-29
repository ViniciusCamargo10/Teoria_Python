# Criando um dicionário
meu_dicionario = {
    "nome": "Vinicius",
    "idade": 19,
    "linguagem": "Python"
}

# Outra forma de criar um dicionário usando a função dict()
d = dict(nome="Vini", idade=19, linguagem="Java")

print("Dicionário criado com dict():")
print(d)
print("\n")

# Acessando valores
print("Nome no meu_dicionario:", meu_dicionario["nome"])  # Vinicius

# Adicionando um novo par chave-valor
meu_dicionario["cidade"] = "São Paulo"

# Atualizando o valor de uma chave existente
meu_dicionario["idade"] = 26

# Removendo um par chave-valor
del meu_dicionario["linguagem"]

# Obtendo todas as chaves
print("\nChaves do dicionário:")
print(meu_dicionario.keys())

# Obtendo todos os valores
print("\nValores do dicionário:")
print(meu_dicionario.values())

# Obtendo todos os itens (chave-valor)
print("\nItens (chave-valor) do dicionário:")
print(meu_dicionario.items())

# Verificando se uma chave existe no dicionário
print("\nA chave 'nome' existe no dicionário?")
print("nome" in meu_dicionario)  # True

# Forma segura de obter um valor (retorna None se a chave não existir)
print("\nTentando acessar a chave 'profissao':")
print(meu_dicionario.get("profissao"))  # None (não existe)
