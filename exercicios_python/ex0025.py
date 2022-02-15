#exercicio 24
#Crie um programa que leia o nome de ua cidade e diga se ela começa ou não com onome 'Santo'

cidade = str(input('EM qual cidade você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')
