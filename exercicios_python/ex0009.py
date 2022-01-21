#exercicio 9
#faça um programa que mostra o dobro, triplo e raiz quadrada do número
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** 2
print('O resultado das operações vale. \n dobro {}\n triplo {}\n raiz quadrada {:.2f}'.format(dobro, triplo, raizQuadrada))
#ou faz assim
print('o Resultado das operações é: \n dobro {}\n triplo {}\n raiz quadrada {:.3f}.'.format((numero *2), (numero * 3), (numero ** 2)))
