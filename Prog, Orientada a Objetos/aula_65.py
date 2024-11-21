# Utilizando Construtores

# criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc


# Criar o objeto passando parâmetros
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')

# print
print(usuario1.nome)  # Elena
print(usuario1.data_nasc)  # 12/01/2009
print(usuario2.nome)  # Carol
print(usuario2.sobrenome)  # Silva
