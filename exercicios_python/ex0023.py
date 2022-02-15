#exercicio 22
#faaça um algoritimo que sortea um de seus quatro a alunos para apagar o quadro

import random
nome1 = str(input('1º ALuno. '))
nome2 = str(input('2º Aluno. '))
nome3 = str(input('3º Aluno. '))
nome4 = str(input('4º Aluno. '))
lista = [nome1, nome2, nome3, nome4]
escolhido= random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))