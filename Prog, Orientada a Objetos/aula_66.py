#  Adicionando mais funções a classe

# criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc

    def nome_completo(self):
        return self.nome + " " + self.sobrenome


# Criar o objeto passando parâmetros
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Yuri', 'Bessa', '01/01/2001')

print(usuario1.nome_completo()) # Elena Cabral
print(Funcionarios.nome_completo(usuario3)) # Yuri Bessa