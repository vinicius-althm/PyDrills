from main import banner
from random import randint
banner(' Listas - Maior e menor ')

lista_valores = []
for  i in range(5):
    valores = int(input(f'{i} - Digite um valor: '))
    lista_valores.append(valores)


maximo = max(lista_valores)
minimo = min(lista_valores)
pos_max = []
pos_min = []

print(f'Lista de valores: {lista_valores}')
"""
#versao 1.0
print(f'Maior valor: {maximo} -> localizado na posicao => ', end="")

for pos, valor in enumerate(lista_valores):
    if valor == maximo:
        print(f'{pos + 1}...', end="")
print('\n')
print(f'Menor valor: {minimo} -> localizado na posicao =>', end ="")
for pos, valor in enumerate(lista_valores):
    if valor == minimo:
        print(f'{pos + 1}... ', end="")

"""
#Versao 2.0
for pos, valor in enumerate(lista_valores):
    if valor == maximo:
        pos_max.append(pos + 1)

    if valor == minimo:
        pos_min.append(pos + 1)

print(f'Maior valor: {maximo} -> localizado na posicao => {pos_max}', )
print(f'Maior valor: {minimo} -> localizado na posicao => {pos_min}', )