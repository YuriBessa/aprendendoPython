# Funções vários argumentos (xargs)
# com parâmetros identificando esses argumentos (Retorna um dicionário)

# Esse duplo asterisco permite que coloque, multiplos parâmetros e nomeados.
def agencia(**carro):
    return carro


print(agencia(modelo="Gol", cor="Branca", motor="1.0"))
print(agencia(modelo="Ka", cor="Azul"))
print(agencia(modelo="Gol", cor="Branca", motor="1.0", placa=123123))
