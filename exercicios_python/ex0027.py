# exercicio 27
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição
# ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite a sua frase: ')).upper().strip()
print('A letra A aparece {} vezes no texto.'.format(frase.count('A')))
print('A primeira A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
