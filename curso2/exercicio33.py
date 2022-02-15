'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

comprador = input('Digite o seu nome: ')
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do funcionário? '))
ano = int(input('Quantos anos você pretende pagar? '))
prestacao = valor / (ano*12)
minimo = salario * 30/100
print('Sr. {}:\n Valor da casa {:.2f}:\n'. format(comprador, valor))
print(('Salário {:.2f}:\nprestacao {:.2f}:\nAnos de financiamento {} anos.\n').format(salario, prestacao, ano))
if prestacao <= minimo:
    print('Emprestimo pode ser concedido.')
else:
    print('Emprestimo negado. a prestação no valor de {:.2f} excede os 30% do salário.'.format(prestacao))
