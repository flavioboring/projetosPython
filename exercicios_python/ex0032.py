# exercicio 32
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km  para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância que você vai percorrer.'))
if distancia <= 200:
    preço = distancia * 1.50
else:
    preço = distancia * 1.10

print('VocÊ vai percorrer {},\ne vai receber {}'. format(distancia, preço))