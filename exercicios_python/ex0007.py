#Aula 7

#nome = input('Qual o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \na mutiplicação é {} \n adivisão é {:.2f}, \na divisão inteira é {} \ne a exponenciação é {},'.format(s, m, d, di, e
                                                                                                                   ))