# Função Lambda
    # É uma função pequena
    # Pode ter vários argumentos mas somente uma expressão
    # Muito utilizada dentro de outras funções
    # Código mais clean

# função comum:
def somar(x):
    return x + 10

print(somar(2))

# função lambda

somar10 = lambda x: x + 10

print(somar10(5)) # 15

somar10com2args = lambda x,y : x + y + 10
print(somar10com2args(5,7)) # 22