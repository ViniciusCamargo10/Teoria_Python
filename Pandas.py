# Importações
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Series com pandas
valores = [10, 20, 30, 40, 50]
serie_exemplo = pd.Series(valores, index=['a', 'b', 'c', 'd', 'e'])

print("Valor no índice 'a':", serie_exemplo.loc['a'])
print("\nSérie completa:\n", serie_exemplo)

# Criação e manipulação de DataFrame
dados_funcionarios = pd.DataFrame({
    "nome": ["Fulano", "Ciclano", "Beltrano"],
    "idade": [28, 35, 32],
    "cargo": ["Desenvolvedor", "Analista", "Engenheiro"]
})

print("\nDataFrame original:\n", dados_funcionarios)

# Definir índice
dados_indexado = dados_funcionarios.set_index("nome")
print("\nCom índice definido:\n", dados_indexado)

# Resetar índice
dados_resetado = dados_indexado.reset_index()
print("\nApós reset do índice:\n", dados_resetado)

# Soma de DataFrames
df_soma1 = pd.DataFrame({'valores': [1, 2, 3]})
df_soma2 = pd.DataFrame({'valores': [10, 20, 30]})

print("\nSoma dos DataFrames (por índice):\n", df_soma1 + df_soma2)

# Salvando e lendo CSV (comentado)
# dados_funcionarios.to_csv('funcionarios.csv')
# df_lido = pd.read_csv('funcionarios.csv', index_col=0)
# print(df_lido)

# Visualização: California Housing
dados_housing = fetch_california_housing(as_frame=True).frame

# Histograma da idade das casas
dados_housing['HouseAge'].hist(bins=30, edgecolor='black')
plt.title('Distribuição da Idade das Casas')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Histogramas de todas as colunas
dados_housing.plot(figsize=(12, 8))
plt.tight_layout()
plt.show()

# Adicionando linhas ao DataFrame
turma = pd.DataFrame({
    "nome": ["João", "Maria", "Pedro"],
    "idade": [10, 12, 11],
    "status": ["Aluno", "Aluno", "Aluno"]
})

print("\nAntes de adicionar:\n", turma)

# Adicionando linha
turma.loc[len(turma)] = ['Ana', 13, 'Aluno']

print("\nApós adicionar:\n", turma)

# Função com apply
def transforma_idade(idade):
    if idade % 3 == 0:
        return idade ** 2
    else:
        return idade / 2

resultado_transformacao = turma['idade'].apply(transforma_idade)
print("\nTransformação da idade com função personalizada:\n", resultado_transformacao)

# Agrupando com groupby
empregados = pd.DataFrame({
    'nome': ['Carlos', 'Fernanda', 'Lucas', 'Bruna'],
    'idade': [25, 30, 40, 35],
    'cargo': ['Dev', None, None, 'Dev']
})

empregados_filtrados = empregados.dropna(subset=['cargo'])

media_por_cargo = empregados_filtrados.groupby('cargo').agg({'idade': 'mean'})
print("\nMédia de idade por cargo:\n", media_por_cargo)

# Ordenando
print("\nOrdenado por idade crescente:\n", media_por_cargo.sort_values('idade'))
print("\nOrdenado por idade decrescente:\n", media_por_cargo.sort_values('idade', ascending=False))

# Concatenando DataFrames
estoque_1 = pd.DataFrame({
    'produto': ['A', 'B', 'C'],
    'quantidade': [10, 20, 30]
})

estoque_2 = pd.DataFrame({
    'produto': ['D', 'E', 'F'],
    'quantidade': [40, 50, 60]
})

estoque_total = pd.concat([estoque_1, estoque_2], ignore_index=True)
print("\nEstoque total após concatenação:\n", estoque_total)

# Join com índice
precos = pd.DataFrame({
    'preco': [100, 200, 300]
}, index=['A', 'B', 'C'])

categorias = pd.DataFrame({
    'categoria': ['X', 'Y', 'Z']
}, index=['B', 'C', 'D'])

juncao = precos.join(categorias, how='outer')
print("\nJoin dos DataFrames com how='outer':\n", juncao)

# Mais Funcionalidades Avançadas em Pandas

# Tratamento de Dados Faltantes
df_com_faltas = pd.DataFrame({
    'nome': ['Carlos', 'Ana', 'João'],
    'idade': [25, None, 30],
    'cargo': [None, 'Estagiária', 'Desenvolvedor']
})

print("\nDataFrame com dados faltantes:\n", df_com_faltas)

# Preencher valores ausentes com a média (por exemplo) ou outro valor
df_com_faltas['idade'] = df_com_faltas['idade'].fillna(df_com_faltas['idade'].mean())
df_com_faltas['cargo'] = df_com_faltas['cargo'].fillna('Desconhecido')

print("\nDataFrame após preencher dados faltantes:\n", df_com_faltas)

# Trabalhando com DataFrames Temporais
dados_temporais = pd.DataFrame({
    'data': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'valor': [100, 200, 150]
})

# Convertendo para datetime
dados_temporais['data'] = pd.to_datetime(dados_temporais['data'])

print("\nDataFrame com dados temporais:\n", dados_temporais)

# Selecionando dados de uma data específica
dados_janeiro = dados_temporais[dados_temporais['data'] >= '2025-01-02']
print("\nDados de janeiro:\n", dados_janeiro)

# Merge (mesclando DataFrames)
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'nome': ['Carlos', 'Fernanda', 'Lucas']
})

df2 = pd.DataFrame({
    'id': [2, 3, 4],
    'cargo': ['Desenvolvedor', 'Analista', 'Gerente']
})

# Fazendo merge
df_merge = pd.merge(df1, df2, on='id', how='inner')
print("\nMerge dos DataFrames:\n", df_merge)

# Manipulações Avançadas com Strings
df_strings = pd.DataFrame({
    'nome': ['Carlos', 'Fernanda', 'Lucas'],
    'cargo': ['Desenvolvedor', 'Analista', 'Engenheiro']
})

# Filtrando nomes que começam com 'C'
filtro_nomes = df_strings[df_strings['nome'].str.startswith('C')]
print("\nFiltrando nomes que começam com 'C':\n", filtro_nomes)

# Substituindo 'Engenheiro' por 'Desenvolvedor'
df_strings['cargo'] = df_strings['cargo'].replace('Engenheiro', 'Desenvolvedor')
print("\nApós substituir 'Engenheiro' por 'Desenvolvedor':\n", df_strings)

# Melting e Pivot
df_pivot = pd.DataFrame({
    'Produto': ['A', 'B', 'C'],
    'Jan': [100, 200, 300],
    'Fev': [110, 210, 310]
})

# Melting (transformando para formato longo)
df_melted = pd.melt(df_pivot, id_vars=['Produto'], var_name='Mês', value_name='Valor')
print("\nDataFrame em formato longo (melted):\n", df_melted)

# Pivoting (transformando para formato largo novamente)
df_pivot_back = df_melted.pivot(index='Produto', columns='Mês', values='Valor')
print("\nDataFrame em formato largo (pivoted):\n", df_pivot_back)

