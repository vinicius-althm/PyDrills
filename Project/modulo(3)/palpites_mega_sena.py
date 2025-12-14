from main import *
from random import randint

banner('Palpites Mega Sena')

lista = [] # Lista temporaria
jogos = [] #Lista principal
cont_jogos = 1 #contador de jogos
quantidade_jogos = int(input('Quantos jogos deseja sortear? ')) #Entrada de dados

while cont_jogos <= quantidade_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    jogos.append(lista[:])
    lista.clear()
    cont_jogos += 1
print('*=' * 3, f'SORTEANDO {quantidade_jogos} jogos', '*=' * 3)
for i, l  in enumerate(jogos):
    print(f'Jogo {i + 1}º: {sorted(l)}')