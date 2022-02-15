#exercicio 22
#programa que lÊ um triangulo e mostra o valor do seno consseno e tangente.

from math import cos, sin, radians, tan
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print('O angulo {} tem o seno de {:.2f}'. format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE {:.2f}'.format(angulo,tangente))
