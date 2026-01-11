from main import *
from time import sleep
banner('MAIOR NUMERO')

def maior_numero(*valores):

    maior = max(valores)
    menor = min(valores)
    total = len(valores)
    menu_exercicio(f'Total de numeros passados como parametro: {total}\n'
    f'Maior numero digitado: {maior}\n'
    f'Menor numero digitado: {menor}\n'
    f'Numeros digitados: {list(valores)}'
    )
    """
    print(f'Total de numeros passados como parametro: {total}')
    print(f'Maior numero digitado: {maior}')
    print(f'Menor numero digitado: {menor}')
    print(f'Numeros digitados: {list(valores)}')
    """


lista = []
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º número: '))
    lista.append(numero)

maior_numero(*lista)
