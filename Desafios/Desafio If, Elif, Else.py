# Desafio If, Elif, Else - Ponto do Steak


''' 
Criar um programa que dependendo da temperatura em Celsius do stake, ele retorna ao ponto de cozimento. Em português usuário deverá fornecer a temperatura.

Antes de 48° - Cozinhar por mais alguns minutos
Acima de 71° - Bem passada

Temperaturas - Cozimento
120°F ou 48°C - Rare (selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (bem passada) 
'''

temp = int(input('Qual a temperatura da carne? '))

if (temp > 70):
    print('Bem passada')
elif (temp > 64):
    print('Ao ponto para o bem')
elif (temp > 59):
    print('Ao ponto')
elif (temp > 53):
    print('Ao ponto para o ma')
elif (temp > 47):
    print('Selada')
else :
    print('Cozinhar por mais alguns minutos')