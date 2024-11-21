# Criando Objetos dentro de uma Classe

#criar a classe
class Funcionarios: 
    pass

#Criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()
#criar parâmetros do usuário 1
usuario1.nome = 'Elena'
usuario1.sobrenome = "Cabral"
usuario1.data_nasc = '12/01/2009'

#criar parâmetros do usuário 2
usuario2.nome = 'Carol'
usuario2.sobrenome = "Silva"
usuario2.data_nasc = '15/10/2005'

#print
print(usuario1.nome) # Elena
print(usuario1.data_nasc) # 12/01/2009
print(usuario2.nome) # Carol     
print(usuario2.sobrenome) # Silva     