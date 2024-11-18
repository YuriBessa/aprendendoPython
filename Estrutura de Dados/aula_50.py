#  Visualizando Itens, Keys e Values


#Pode ser organizado desta forma também:
aluno = {
    'nome': 'Ana',
    'idade': 16, 
    'nota_final': 'A', 
    'aprovação': True, 
    'materias':['Fisica','Matemática','Ingles']
}


print(aluno.get('materias')) # ['Fisica', 'Matemática', 'Ingles']
print(len(aluno)) # Saber o número de keys // 5

print(aluno.keys()) # dict_keys(['nome', 'idade', 'nota_final', 'aprovação', 'materias'])
print(aluno.items()) # dict_items([('nome', 'Ana'), ('idade', 16), ('nota_final', 'A'), ('aprovação', True), ('materias', ['Fisica', 'Matemática', 'Ingles'])])
print(aluno.values()) # dict_values(['Ana', 16, 'A', True, ['Fisica', 'Matemática', 'Ingles']])