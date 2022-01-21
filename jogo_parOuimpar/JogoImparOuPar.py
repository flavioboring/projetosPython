import random

nome = input('Digite um nome: ')
computador = random.randint(0, 10)

while True:
    utilizador = input('Quer par ou impar? ')
    if utilizador == 'par' or utilizador == 'impar':
        break

if utilizador == 'par':
    par = utilizador
    impar = computador
elif utilizador == 'impar':
    impar = utilizador
    par = computador

numero = input('Digite um número de 0 a 10: ')
print('\n Computador escolheu: ', computador)
print(nome, 'escolheu: ', numero)
total = int(numero) + computador
print('A soma é: ', total)
computador = '0'
if total % 2 == 0:
    print('O resultado é par')
    computador = 'par'
else:
    print('O resultado é impar')
    computador = 'impar'
if utilizador == 'par' and computador == 'par':
          print('O Vencedor é: ', nome)
elif utilizador == 'impar' and computador == 'impar':
        print('O vencedor é: ', nome)
else:
    print('O vencedor é o computador!')

