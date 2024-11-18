# Adicionando o Else e Finally
    # Else = permite realizar mais ações caso o try dê certo
    # Finally = permite realizar mais ações mesmo que o try não dê certo

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(f'O valor digitado foi: {valor}')
except ValueError:
    print('Só é permitido digitar valor em número inteiro')
else:
    resultado = valor * 2
    print(f'O dobro do valor é: {resultado}')
finally: 
    print('Execução encerrada')

print('Fim do programa')
