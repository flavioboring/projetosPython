#exercicio 021
#Faça um programa que leia um número de 0a 9999 e mostre na tela cada um dos digitos separados
numero = int(input('Informe um número: '))
u = numero // 1% 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o seu número: {} '.format(numero))
print('Unidade: {}'. format(u))
print('dezenaa: {}'. format(d))
print('centena: {}'. format(c))
print('Milhar: {}'. format(m))