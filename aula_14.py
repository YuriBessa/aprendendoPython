# Operadores lógicos 

# and - retorna true quando todas as condições são verdadeiras 
# or - retorna true quando pelo menos uma das condições er verdadeira
# not ou ! - nega uma condição

renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo: # Imprimirá "Financiamento aprovado" pois as duas condições são verdadeiras 
    print('Financiamento aprovado')
else:
    print('Financiamento negado')


nome_limpo = False

if renda_acima_5mil and nome_limpo: # Imprimirá "Financiamento negado" uma das duas condições é falsa 
    print('Financiamento aprovado')
else:
    print('Financiamento negado')

if renda_acima_5mil or nome_limpo: # Imprimirá "Financiamento aprovado" pois uma duas condições é verdadeira.
    print('Financiamento aprovado')
else:
    print('Financiamento negado')
