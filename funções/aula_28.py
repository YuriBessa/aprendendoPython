# Funções com argumentos Default e Non-Default 
# Parametro --> Argumento
# Default = Aquele que você define o valor no parâmetro. Deve ser colocada depois dos valores default.
# Non-Default = Aquele que você não define o valor no parâmetro.



def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 4)
boas_vindas('Linda', 2)
