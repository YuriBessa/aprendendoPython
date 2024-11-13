# Tuples
    # Armazena mais de uma informações em variáveis
    # Manter a sequência dos dados em uma variável 
    # Não podem ser alterados (Inmutable)

cores_list = ['amarelo','verde','azul', 'vermelho']
cores_tuple = ('amarelo','verde','azul', 'vermelho')
 
print(cores_list) # ['amarelo', 'verde', 'azul', 'vermelho']

print(cores_tuple) # ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list)) # <class 'list'>
print(type(cores_tuple)) # <class 'tuple'>

tuple_duplicada = cores_tuple * 2

print(tuple_duplicada) # ('amarelo', 'verde', 'azul', 'vermelho', 'amarelo', 'verde', 'azul', 'vermelho')

# Tupla X Lista

# Tupla =  Deve ser utilizada se você quiser ter uma lista imutável - Tupla gasta menos memória e é mais rápida
# Lista = Se quiser uma lista com possibilidade de modificação.
