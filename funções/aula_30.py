# Funções vários argumentos (xargs)

def soma(*numeros):  # O uso do asterisco permite usar vários argumentos.
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(2, 3, 4, 7)  # passando vários argumentos

print(x)
