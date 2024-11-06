#Aprendendo a usar string formatada

nome = 'Marcos'
sobrenome ='Silva'
profissao = 'Programador'

#Concatenar esse texto é bem trabalhoso
texto1 = 'O ' + nome + ' ' + sobrenome + ' é um excelente [' + profissao + ']'


#Para facilitar, surge a string formatada com o uso do f' na frante da string.
texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'

print(texto1)
print(texto2)