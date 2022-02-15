#exercicio 26
#Procurar uma string dentro de outra
frase = str(input('Escreva seu nome completo:')).strip()
print('Seu nome é Santos?'.format('SANTOS' in frase.lower()))
