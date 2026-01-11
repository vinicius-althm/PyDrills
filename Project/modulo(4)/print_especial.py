from main import *
from time import sleep
banner('PRINT ESPECIAL')

def titulo(mensagem):
    espacamento = len(mensagem) + 4
    print('*' * espacamento)
    print(f'   {mensagem}   ')
    print('*' * espacamento)

titulo('DESENVOLVIMENTO - PYTHON ')