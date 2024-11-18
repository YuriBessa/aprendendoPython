# Função Lambda dentro de outra função

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

