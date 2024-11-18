#  Entendendo List Comprehension com números

#modo comum:

# valores = []

# for x in range(6):
#     valores.append(x*10)

# print(valores) # [0, 10, 20, 30, 40, 50]

# Utilizando List Comprehension

valores = [x * 5 for x in range(6)]

print(valores) # [0, 5, 10, 15, 20, 25]