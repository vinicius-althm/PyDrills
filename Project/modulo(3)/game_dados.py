from main import *
from random import randint
from time import sleep
from operator import itemgetter

banner(' DICIONARIO - JOGO DE DADOS ')

lista = []

print('*=' * 3, "Valores Sorteados", '*=' * 3)
for i in range(4):
    numero = randint(1, 6)
    print(f'Player {i + 1}º tirou o valor {numero}')
    sleep(1)
    dados = {
        'player': i + 1,
        'numero': numero
    }
    lista.append(dados)

#print(lista)
print('*-*' * 5, 'RANKING DOS PLAYERS', '*-*' * 5)

#Ordenando pelo maior numero
ranking = sorted(lista, key=itemgetter('numero'), reverse=True)

for i, p in enumerate(ranking, 1):
    print(f"{i}º lugar → Player {p['player']} com {p['numero']}")