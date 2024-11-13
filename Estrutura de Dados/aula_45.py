# Funções com Set

#É possivel transformar uma lista em set utilizando o comando abaixo.
list1 = set([1,2,3,4,5,6])

print(list1) # {1, 2, 3, 4, 5, 6}
print(type(list1)) # <class 'set'>

# OBS: Cuidado ao usar {} para definir um set vazio, pois o Python interpreta como dicionário vazia.

s1 = {1,2,3,4,5,6}

# Comando para adicionar um dado ao set
s1.add(7) # {1, 2, 3, 4, 5, 6, 7}

# Comando para adicionar vários dados ao set (necessário passar os dados dentro do colchete)
s1.update([6,7,8,9,10,'palavra']) #  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'palavra'}

# Comando para remover um dado do set (Caso esse dado não exista e Python dá erro)
s1.remove('palavra') # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Comando para remover um dado do set (Mesmo que dado não exista o Python não dá erro).

s1.discard(4) # {1, 2, 3, 5, 6, 7, 8, 9, 10}
s1.discard(80) # {1, 2, 3, 5, 6, 7, 8, 9, 10}



print(s1)