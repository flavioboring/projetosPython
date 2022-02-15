'''Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Digite um número inteiro: '))
print('''escolha uma das bases para a conversão:
[1] converter para Binário
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print("{} Convertido para BINÁRIO é igual a {}.". format(num, bin(num) [2:]))
elif opção == 2:
    print("{} Convertido para OCTAL é igual a {}.".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} Convertido para OCTAL é igual a {}.".format(num, hex(num)[2:]))
else:
    print('Opção Invalida, tente novamente')
