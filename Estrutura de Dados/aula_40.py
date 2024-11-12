# Listas - Agregando Duas listas com o Zip

cores = ['amarelo', 'verde', 'azul', 'vermelho']

valores = [10,20,30,40]

duas_listas = zip(cores,valores) #Comando usado para unir duas listas, formando tuplas de mesmo indice.

print(list(duas_listas)) # comando usado para transformar o formato de sáida em tuplas 

#Saída: [('amarelo', 10), ('verde', 20), ('azul', 30), ('vermelho', 40)]