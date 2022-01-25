#exercicio 020
#faça um programa que cálcula um triÂngulo retângulo e suas medidas
#co = float(input('Digite a medida do cateto oposto: '))
#ca = float(input('Digite a medida do cateto adjascente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('Ahipetuna vai medir {:.2f}'. format(hi))
from math import hypot
co = float(input('Catetos oposto: '))
ca = float(input('Cateto adjascente: '))
hip = hypot(co, ca)
print('A medida da hipotenusa vale{:.2f}'.format(hip))