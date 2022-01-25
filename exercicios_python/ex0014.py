#exercicio 11
#faça um programa que meça o tamanho de uma parede e calcule a quantidade de tinta que precisa para pintá-la
#cada litro pinta 2m²
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('A parede tem a área de {:.2f}'. format(area))
tinta = area / 2
print('Para pintar sua parede,\n é necessário {:.2f} litros de tinta'. format(tinta))