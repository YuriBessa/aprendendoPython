#  Atualizando itens no dicionário

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# Atualizar o nome (há duas formas) 
aluno['nome'] = 'Jose'

print(aluno) # {'nome': 'Jose', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# Com o update é possivel atualizar mais de uma chave, inclusive é possível adicionar valores.
aluno.update({'nome': 'Yuri', 'nota_final': 'A'})
aluno.update({'endereço': 'Rua A'}) 

print(aluno) # {'nome': 'Yuri', 'idade': 16, 'nota_final': 'A', 'aprovação': True, 'endereço': 'Rua A'}

# há uma forma de buscar dados que não retorna erro se o dado não for encontrado.
print(aluno.get('endereço')) # Rua A
print(aluno.get('genero')) # retorna None pois a chave genero não existe.

# Remover Keys

del aluno['idade']
print(aluno) # {'nome': 'Yuri', 'nota_final': 'A', 'aprovação': True, 'endereço': 'Rua A'}

