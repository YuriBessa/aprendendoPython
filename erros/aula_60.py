# Trabalhando com o Try e Except com o input

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')


print('O try except continua, mesmo após o erro')