#exercicio 12
#criar um programa que converta as moedas
real = float(input('Quanto de dinheiro você tem investido? R$:  '))
dolar = real / 5.46
print('Com R${:.2f} você pode comprar US${:.2f}.'. format(real, dolar))


