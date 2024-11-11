# Listas - Funções para listas

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']

cidades.append('Santa Catarina') # ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania', 'Santa Catarina']
cidades.remove('Salvador') # ['Rio de Janeiro', 'São Paulo', 'Goiania', 'Santa Catarina']
cidades.insert(1, 'Fortaleza') # ['Rio de Janeiro', 'Fortaleza', 'São Paulo', 'Goiania', 'Santa Catarina']
cidades.pop(0) # ['Fortaleza', 'São Paulo', 'Goiania', 'Santa Catarina']
cidades.sort() # ['Fortaleza', 'Goiania', 'Santa Catarina', 'São Paulo']

print(cidades)