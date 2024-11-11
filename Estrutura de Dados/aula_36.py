# Listas - Concantenando Listas 

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

final = numeros * 2  # duplica a lista seguindo a ordem: [2, 3, 4, 5, 2, 3, 4, 5]

final2 = numeros + letras  # Concatena as listas: [2, 3, 4, 5, 'a', 'b', 'c', 'd'] 
numeros.extend(letras) # Função que concatena uma lista em outra, dando o mesmo resultado acima. [2, 3, 4, 5, 'a', 'b', 'c', 'd']

print(final)
print(final2)
print(numeros) 

# Lista dentro de lista

itens = [['item1', 'item2'] , ['item3', 'item4']]

print(itens[0]) # ['item1', 'item2']
print(itens[1]) # ['item3', 'item4']
print(itens[1][0]) # // item3
print(itens[0][0]) # // item1
print(itens[1][1]) # // item4




