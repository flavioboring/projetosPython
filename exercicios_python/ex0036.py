# exercicio 36
'''Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print( '\033[1;92m' '=' *20)
lado1 = int(input( 'Digite o primeiro: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Pode formar um triangulo.')
else:
    print('Não pode formar um triângulo')
    print('=' * 30)