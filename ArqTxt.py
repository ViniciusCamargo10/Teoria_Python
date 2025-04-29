# Exemplo 1 - Criar e escrever em um novo arquivo
conteudo = open("ArqTxt.txt", "w")  # "w" cria um arquivo novo ou sobrescreve
conteudo.write("Linha 1: Olá, mundo!\n")
conteudo.write("Linha 2: Aprendendo a trabalhar com arquivos.\n")
conteudo.close()

# Exemplo 2 - Ler o conteúdo do arquivo
arquivo = open("ArqTxt.txt", "r")  # "r" abre para leitura
texto = arquivo.read()
print("Conteúdo do arquivo:\n")
print(texto)
arquivo.close()

print("\n--------------------------------\n")

# Exemplo 3 - Adicionar conteúdo (sem apagar o que já existe)
arquivo = open("ArqTxt.txt", "a")  # "a" = append (adicionar ao final)
arquivo.write("Linha 3: Este texto foi adicionado depois!\n")
arquivo.write("Linha 4: E mais uma linha!\n")
arquivo.close()

# Exemplo 4 - Ler novamente o conteúdo atualizado
arquivo = open("ArqTxt.txt", "r")
print("Conteúdo atualizado do arquivo:\n")
print(arquivo.read())
arquivo.close()

print("\n--------------------------------\n")

# Exemplo 5 - Ler linha por linha
arquivo = open("ArqTxt.txt", "r")
linhas = arquivo.readlines()  # Retorna uma lista de linhas
for linha in linhas:
    print(f"Linha lida: {linha.strip()}")  # strip() remove \n do final
arquivo.close()

print("\n--------------------------------\n")

# Exemplo 6 - Usando with open() (não precisa chamar close())
with open("ArqTxt.txt", "r") as arquivo:
    print("Usando 'with' para abrir o arquivo:")
    for linha in arquivo:
        print(f">> {linha.strip()}")
