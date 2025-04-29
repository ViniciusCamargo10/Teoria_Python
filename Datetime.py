# Importando o módulo datetime
import datetime

# Obtendo a data e hora atual
agora = datetime.datetime.now()

# Exibindo a data e hora atual
print(f"Data e hora atual: {agora}")

# Pegando apenas a data
data_atual = agora.date()
print(f"Data atual: {data_atual}")

# Pegando apenas a hora
hora_atual = agora.time()
print(f"Hora atual: {hora_atual}")

# Pegando partes específicas
print(f"Ano: {agora.year}")
print(f"Mês: {agora.month}")
print(f"Dia: {agora.day}")
print(f"Hora: {agora.hour}")
print(f"Minuto: {agora.minute}")
print(f"Segundo: {agora.second}")

# Formatando a data/hora
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data formatada: {data_formatada}")

# Criando uma data específica
data_especifica = datetime.datetime(2025, 4, 28, 14, 30, 0)
print(f"Data criada manualmente: {data_especifica}")
