from datetime import datetime

# Calculando a idade do funcionário

# criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc

    def nome_completo(self):
        return self.nome + " " + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano_nasc
        return idade

# Criar o objeto passando parâmetros
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005)
usuario3 = Funcionarios('Yuri', 'Bessa', 2001)

print(usuario1.idade_funcionario()) # 15
print(Funcionarios.idade_funcionario(usuario2)) # 19