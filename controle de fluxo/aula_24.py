# Criando condições com While

# Publicar um produto com comissão de 10% se o produto for acima de R$ 20,00.

valor = int(input('Digite o valor do seu produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R${valor}')
    break