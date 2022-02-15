#Expressões regulares
import re
texto = ('Eu sou Flávio, e estou aprendendo a programar em python! ainda em 2022, não pode ficar'
         'para 2023, -96')

padrao = '[-0-9]'
resultado = re.search(padrao, texto, re.DOTALL)
if resultado:
    print(f'*{resultado.group()}*')
else:
    print(padrao, "não encontrado")
resultado = re.findall(padrao, texto)
print(resultado)

