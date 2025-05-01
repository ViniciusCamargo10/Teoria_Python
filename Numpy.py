import numpy as np

print("===== 1. Atributos de Arrays =====")
# Criando um array 2D
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr.shape)          # Formato (linhas, colunas)
print("Dimensões:", arr.ndim)       # Número de dimensões
print("Tamanho total:", arr.size)   # Quantidade de elementos
print("Tipo de dado:", arr.dtype)   # Tipo dos dados (int, float, etc.)

print("\n===== 2. Tipos de Dados =====")
# Definindo tipos de dados específicos
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.1, 2.2, 3.3], dtype=np.float64)
print("Tipo de arr_int:", arr_int.dtype)
print("Tipo de arr_float:", arr_float.dtype)

print("\n===== 3. Preenchendo Arrays =====")
# Criando arrays com valores fixos
zeros = np.zeros((2, 3))  # Array com zeros
ones = np.ones((2, 3))    # Array com uns
full = np.full((2, 3), 7) # Array preenchido com o valor 7
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Full:\n", full)

print("\n===== 4. NaN e Inf =====")
# Criando arrays com NaN (Not a Number) e Inf (Infinito)
arr_nan = np.array([1, np.nan, 3])
arr_inf = np.array([1, np.inf, 3])
print("Com NaN:", arr_nan)
print("Com Inf:", arr_inf)
# Soma ignorando valores NaN
print("Soma ignorando NaN:", np.nansum(arr_nan))

print("\n===== 5. Operações Matemáticas =====")
# Operações entre arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Soma:", a + b)
print("Produto:", a * b)
print("Seno:", np.sin(a))
print("Logaritmo:", np.log(a))

print("\n===== 6. Métodos de Arrays =====")
# Métodos úteis para análise
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Máximo:", arr2d.max())               # Maior valor
print("Soma por linha:", arr2d.sum(axis=1)) # Soma por linha
print("Transposta:\n", arr2d.T)             # Transposição do array

print("\n===== 7. Métodos de Estruturação =====")
# Redimensionando e achatando arrays
reshaped = np.arange(9).reshape((3, 3))
print("Reshape:\n", reshaped)          # Novo formato
print("Flatten:", reshaped.flatten())  # Array em 1 dimensão

print("\n===== 8. Concatenando, Empilhando, Dividindo =====")
# Juntando e separando arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
concat = np.concatenate([x, y], axis=0)  # Junta verticalmente
stack = np.stack([x, x], axis=1)         # Empilha horizontalmente
split = np.split(x, 2)                   # Divide o array em 2
print("Concatenado:\n", concat)
print("Empilhado:\n", stack)
print("Dividido:", split)

print("\n===== 9. Funções Agregadas =====")
# Estatísticas básicas
data = np.array([1, 2, 3, 4])
print("Média:", np.mean(data))
print("Desvio padrão:", np.std(data))
print("Mínimo:", np.min(data))

print("\n===== 10. NumPy Random =====")
# Geração de números aleatórios
np.random.seed(0)  # Semente para reprodutibilidade
rand_arr = np.random.rand(2, 3)                  # Floats aleatórios
rand_ints = np.random.randint(0, 10, (2, 2))     # Inteiros aleatórios
print("Aleatórios float:\n", rand_arr)
print("Aleatórios inteiros:\n", rand_ints)

print("\n===== 11. Exportando e Importando =====")
# Salvando e carregando arrays
np.save("meu_array.npy", data)          # Salva o array em arquivo .npy
carregado = np.load("meu_array.npy")    # Carrega de volta
print("Array carregado:", carregado)