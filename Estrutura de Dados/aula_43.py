from array import array

# Array != Lista
# Também chamada de Matriz
# Deve ser utilizada quando uma lista é muito grande.
# Tem melhor performance

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras) # array('u', 'abcd')
print(numeros_i) # array('i', [10, 20, 30, 40])
print(numeros_f) # array('f', [1.2000000476837158, 2.200000047683716, 3.200000047683716])



