# List Comprehension
    # Mais simples de se escrever 
    # Utilizado quando se precisa criar uma nova lista a patir de uma já existente
    # [expressao for item in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# modo mais utilizado

# frutas2 = []

# for fruta in frutas1:
#     if 'a' in fruta:
#         frutas2.append(fruta) 
# print(frutas2) # ['abacate', 'banana', 'morango', 'abacaxi']

# Utilizando list comprehension

frutas2 = [fruta for fruta in frutas1 if 'a' in fruta]

print(frutas2) # ['abacate', 'banana', 'morango', 'abacaxi']