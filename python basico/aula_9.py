#Metodos para String
mensagem = "Eu adoro comida caseira"

print (mensagem.lower()) # Transforma o conteúdo de mensagem em minúsculo. //eu adoro comida caseira
print (mensagem.upper()) # Transforma o conteúdo de mensagem em maiúsculas. //EU ADORO COMIDA CASEIRA
print (mensagem.capitalize()) # Transforma transforma a primeira em maiúscula. //Eu adoro comida caseira
print (mensagem.find('o')) # Retorna o indice da primeira vez que letra solicitada aparece dentro da função (Case Sensitive). // 5
print (mensagem.find('adoro')) # Retorna a posição onde inicia a palavra solicitada dentro da função (Case Sensitive). // 3
# Obs. Se retornar -1 a palavra solicitada não existe.
print (mensagem.replace('caseira', 'feita em casa')) # Usado para substituir um caractere ou uma palavra inteira. //Eu adoro comida feita em casa
print (mensagem.strip()) # Retira todos os espaços anteriores à primeira palavra da string
