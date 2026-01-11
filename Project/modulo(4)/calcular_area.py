from main import *
from time import sleep
banner('Calcular Area')

def area(larg,comp):
    resultado  = larg * comp
    print(f'A area do terreno {larg} x {comp} é de {resultado} m²')

#Input de dados

largura = float(input('Digite a largura do terreno (m): '))

comprimento= float(input('Digite o comprimento do terreno (m): '))
sleep(1)
area(largura,comprimento)