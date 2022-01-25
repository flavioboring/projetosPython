#exercicio 15
#faça um algoritimo que leia um preço de um produtoemostre seu novo preço com 5% de desconto

produto = input('DIgite o nome do produto: ')
preco = float(input('Digite o preco do produto '))
desconto = preco - (preco *5/ 100)
print('o produto {}, custa {}\n preço com desconto {}'. format(produto, preco, desconto))