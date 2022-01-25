#exercicio 16
#faça um programa que cáclula o aumento do funcionário com 15%de aumento

funcionario = str(input('Digite o nome do funcionário: '))
salario = float(input('informe o salário do funcionário: '))
aumento = salario + (salario * 15/100)
print('Salário sem aumento: {} \no novo salario de {} é: {}' .format(salario, funcionario, aumento))
