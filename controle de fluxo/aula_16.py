# Iterações com for em números

# imprimir de 1 a 5

for numero in range(5):
    print(numero)  # 0,1,2,3,4 (roda 5 vezes começando do 0)

for numero in range(1, 6):
    print(numero)  # 1,2,3,4,5 (roda começando do 1 e não conta o 6, terminando em 5)

# Parametros da função range(inicio, fim, incremento)
for numero in range(1, 10, 2):  # 1,3,5,7,9 (conta de 2 em 2)
    print(numero)
