# Exemplo de tratamento de exceções usando try, except, else e finally

try:
    idade = int(input("Digite sua idade: "))  # Tenta converter a entrada para inteiro
except Exception as erro:
    # Captura qualquer erro que acontecer e mostra
    print(f"Ocorreu um erro: {erro}")
else:
    # Se não houver erro, executa este bloco
    print("Entrada de idade realizada com sucesso!")
finally:
    # Este bloco é executado sempre, independentemente de erro ou não
    print("Obrigado por usar o programa.\n")

# Se a conversão der certo, mostra a idade
# Se der erro, essa parte abaixo pode causar erro porque 'idade' pode não existir
# Então é melhor garantir que 'idade' existe usando uma proteção:

try:
    print(f"Sua idade é {idade}")
except NameError:
    print("Não foi possível mostrar a idade porque ocorreu um erro anteriormente.")
    