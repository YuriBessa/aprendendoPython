#  Função Map em uma lista
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, por item (list, tuple, diction..)

lista1 = [1,2,3,4]

def multi(x):
    return x*2

lista2 = map(multi, lista1)

print(list(lista2)) # [2, 4, 6, 8]