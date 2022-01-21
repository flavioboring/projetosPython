#exercicio 8
#5º exercicio da lista do curso
#crie um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1
print('O sucessor de {} é {} e o antecessor de {} é {} '.format(numero, sucessor, numero, antecessor))
#ou pode ser feito dessa forma
print('O sucessor de {} é {} e o antecessor de {} é {} '.format(numero, (numero+1), numero, (numero-1)))
