# sempre no código eu vou ter uma funçao de soma de dois numeros.

def soma(a, b):
    resultado = a + b * 2 # variavel locar
    return resultado

print(soma(25, 30))

print("\n")

resultado = 0 # variavel global

def subtraçao(a,b):
    global resultado # chama a variavel global 
    resultado = a - b
    
subtraçao(20,10)
print(resultado)   

    