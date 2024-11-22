# Calculadora de IMC
'''
Qual a sua altura em cm:
Qual é o seu peso em kg:

MENOR QUE 18,5      MAGREZA
ENTRE 18,5 E 24,9   NORMAL
ENTRE 18,5 E 24,9   SOBREPESO
ENTRE 30,0 E 39,9   OBESIDADE
MAIOR QUE 40,0      OBESIDADE GRAVE
'''

altura = float(input('Qual a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

altura_M = altura/100

IMC =  peso/(altura_M**2)

if IMC < 18.5:
    print(f'IMC {IMC} - MAGREZA')
elif  18.5>= IMC <= 24.9:
    print(f'IMC {IMC} - NORMAL')
elif  25>= IMC <= 29.9:
    print(f'IMC {IMC} - SOBREPESO')
elif  30>= IMC <=39.9:
    print(f'IMC {IMC} - OBESIDADE')
else:
    print(f'IMC {IMC} - OBESIDADE GRAVE')
