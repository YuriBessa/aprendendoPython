# Iterações com for em If e Else

for enviar in range(3):
    valor_compra = input('Digite o valor da compra: ')
    if valor_compra != "12.50":
        print(f'o valor de R${valor_compra} está errado tente novamente')
    else:
        print(f'o valor de R${valor_compra} está correto')
        break
