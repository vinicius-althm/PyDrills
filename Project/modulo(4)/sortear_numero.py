from main import *
from time import sleep
from random import randint
banner('SORTEANDO NUMEROS')

def sorteio(lista):
    menu_exercicio('INICIANDO O SORTEIO')
    for i in range(1, 6):
        numeros = randint(0, 99)
        print(f'Sorteando o {i}º : {numeros}')
        sleep(0.5)
        lista.append(numeros)
def somaPar(numeros):
    print('Soma dos numeros pares')
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Para os valores da lista: {numeros} | A soma dos numeros pares: {soma}')

lista_numeros = []
sorteio(lista_numeros)
somaPar(lista_numeros)