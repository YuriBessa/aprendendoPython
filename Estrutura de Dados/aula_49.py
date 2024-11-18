# Looping em dicionários

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for x in aluno:
    print(x) 
    
#O for acima Somente imprime as keys: 
# nome
# idade
# nota_final
# aprovação

for x in aluno.values():
    print(x) 

#O for acima Somente imprime os values: 
# Ana
# 16
# A
# True


for x in aluno.items():
    print(x)
# Este for imprime as Keys e values, em formato de tuple    
# ('nome', 'Ana')
# ('idade', 16)
# ('nota_final', 'A')
# ('aprovação', True)


for x, y in aluno.items():
    print(x, y) 
#Dessa forma é possível imprimir Key e Value
# nome Ana
# idade 16
# nota_final A
# aprovação True