#  Sets com strings

set1 = {'a', 'b','c'}
set2 = {'a', 'd','e'}
set3 = {'c', 'd','f'}

print(set1.union(set2)) # {'a', 'b', 'c', 'e', 'd'}
print(set1.intersection(set2)) # {'a'}
print(set1.difference(set3)) # mostra os elementos de set1 que não estão em set3  {'b', 'a'}
print(set1.symmetric_difference(set3)) # Esconde os repetidos - {'a', 'f', 'b', 'd'}
