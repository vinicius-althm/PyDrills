from main import *
from time import sleep
banner('CONTADOR')

def contador(inicio, fim, passo):
    print(f'inicio: {inicio}, fim: {fim}, passo: {passo}')
    cont = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if cont < fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM')

i = int(input('Digite o inicio:'))
f = int(input('Digite o fim:'))
p = int(input('Digite o passo:'))

contador(i,f,p)