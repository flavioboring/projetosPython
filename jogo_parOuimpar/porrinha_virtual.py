import random

nome = str(input('Digite seu nome: '))
computador = random.randint(0, 3)

while True:
    utilizador = int(input('Escolha um número entre 0 a 6: '))
    if utilizador <= 6:
      break

