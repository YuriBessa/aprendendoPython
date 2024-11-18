# Função Filter
    #Servem para aplicar uma função a um iterable, filtrando todos os itens

valores = [10,12,34,44,57]

# def remover20(x) :
#     return x > 20

# print(list(filter(remover20, valores))) # [34, 44, 57]

# Utilizando função lambda.

print(list(filter(lambda x : x > 20, valores))) # [34, 44, 57]