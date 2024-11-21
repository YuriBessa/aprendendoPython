'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. 
O usuário deverá fornecer as seguintes informações rendimento, altura e largura. 
O programa deve mostrar na tela a mensagem você necessita de X latas de tinta. 

'''

rendimento = float(input('Qual o rendimento da lata? '))
largura = float(input('Qual a altura da parede? '))
altura = float(input('Qual a largura da parede? '))

def calcula_tinta(rend, larg, alt):
    area_parede = larg * alt
    total_latas = area_parede/rend
    print(f'Você precisa de {total_latas} latas de tinta')

calcula_tinta(rendimento, largura, altura)




