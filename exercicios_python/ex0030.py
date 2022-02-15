# exercicio 30
#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
print('-=-' * 10)
velocidade = float(input('Qaul a velocidade do veiculo? '))

if velocidade > 80:
    print('Você foi multado por exceder o limite de velocidade.')
    multa = float(velocidade-80) * 7
    print('Você deverá pagar uma multa no valor de R$ {:.2f}.'. format(multa))
else:print('você não foi multado, diricja com segurança.')