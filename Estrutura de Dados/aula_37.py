# Listas - Extraindo variáveis de Listas (Unpacking)

#Associar cada item da lista a uma variável:

produtos = ['arroz', 'feijão', 'laranja', 'banana']

produto1 = produtos[0]
produto2 = produtos[1]
produto3 = produtos[2]
produto4 = produtos[3]

print (f'{produto1} + {produto2} + {produto3} + {produto4}')

# Fazendo de forma mais simples: 

item1, item2, item3, item4 = produtos 

print (f'{item1} // {item2} // {item3} //{item4}')

#Outras possibilidades (Uso do *)
# Neste exemplo, quero armazenar somente os 3 primeiros itens

produtos2 = ['maçã', 'uva', 'manga', 'laranja', 5, 6, 7, 8]

prod1, prod2, prod3, *outros = produtos2 

print (f'{prod1} // {prod2} // {prod3}')    # maçã // uva // manga
print(outros)                               # ['laranja', 5, 6, 7, 8]

# É possivel colocar para o *outros para o meio também.

produtos3 = ['uva', 'manga', 'laranja', 5, 6, 7, 8]

prod4, prod5, prod6, *outros2, prod7 = produtos3

print (f'{prod4} // {prod5} // {prod6}')    # uva // manga // laranja
print(outros2) # [5, 6, 7]
print(prod7) # 8
