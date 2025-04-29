# Recebendo a nota do aluno em matemática
notaAluno = float(input("Qual foi sua nota em matemática? "))

# Verificando a nota e fornecendo feedback baseado no desempenho
if notaAluno < 6:
    print("Você foi reprovado. Tente novamente!")
elif 6 <= notaAluno <= 8:
    print("Você foi aprovado, mas ainda pode melhorar.")
else:
    print("Você foi aprovado com ótimos resultados. Parabéns!")

# Manipulando uma lista de números
listaNumeros = [10, 15, 20]

print(listaNumeros)

# Removendo o número 10 da lista
listaNumeros.remove(10)

print(listaNumeros)
