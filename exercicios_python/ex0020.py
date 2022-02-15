#exercicio 020
#criar um algoritimo que lê o nome e mostra:
#   todas as letras maiusculas e minusculas
# total de letras
#quantas letras tem o primeiro nome

frase = str(input('Eu vou virar prgramador ainda esse ano! diga seu nome: '))
print('analisando seu nome')
print('seu nome em maiuculo é: {}'.format(frase.upper()))
print('seu nome todo em minusculo é: {} '.format(frase.lower()))
print('seu nome tem ao todo tem: {} letras.'.format(len(frase) - frase.count(' ')))
separa = frase.split()
print('seu primeiro nome tem. {} e eles tem {} letras'.format(separa[0], len(separa[0])))