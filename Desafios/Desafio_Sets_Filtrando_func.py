 # Desafio com 'Sets'


'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Listal = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia 
Lista3 = Funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

func_set = set(funcionarios)
t_dia_set = set(turno_dia)
t_noite_set = set(turno_noite)
tem_carro_set = set(tem_carro)


Lista1 = tem_carro_set.intersection(t_noite_set)
print("Lista 1: " + str(Lista1)) # Lista 1: {'Bruno'}

Lista2 = tem_carro_set.intersection(t_dia_set)
print("Lista 2: " + str(Lista2)) # Lista 2: {'Alice', 'Marcos', 'Melissa'}

Lista3 = func_set.difference(tem_carro_set)
print("Lista 3: " + str(Lista3)) # Lista 3: {'Pedro', 'Sophia', 'Ana'}


