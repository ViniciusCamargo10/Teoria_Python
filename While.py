# Exemplo de laço While (enquanto)

# Inicializa a variável número
numero = 1

# O laço while continuará executando enquanto a condição for verdadeira
while numero < 11:
    # Imprime o valor atual da variável número
    print(numero)
    
    # Incrementa o valor da variável em 1 a cada iteração
    numero += 1  # Equivalente a: numero = numero + 1

print("\n")

# Exemplo de adivinhação com laço while
comida_favorita = "lasanha"

comida = input("Digite a comida favorita até acertar ou 'sair': ").lower()

while comida_favorita != comida:
    if comida == 'sair':
        print("Saindo do programa.")
        break
        
    print("Você digitou:", comida)
    comida = input("Digite a comida favorita até acertar ou 'sair': ").lower()
        
    if comida == comida_favorita:
        print("Você acertou! É:", comida_favorita)
        