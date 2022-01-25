#exercicio 17
#Faça um algoritimo de aluguel de carro

dias = int(input('QUantos dias alugado?'))
km = float(input('Quantos km rodado?'))
pagamento = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(pagamento))