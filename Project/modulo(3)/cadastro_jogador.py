from main import *
from operator import itemgetter
banner('DICIONARIO - CADASTRO JOGADOR')
#Um unico cadastro
"""
dados = {}
lista_gols = []
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
soma_gols = 0
for i in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {i}: '))
    soma_gols += gols
    lista_gols.append(gols)
dados['gols'] = lista_gols
dados['total'] = soma_gols

print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for i, valor in enumerate(lista_gols):
 print(f'Partida {i}º .... Gols: {valor}')

"""
#v2.0
dados = {} #principal
partidas = [] #armazena os gols

dados['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {dados["nome"]} jogou: '))

for c in range(0, jogos):
    partidas.append(int(input(f'Quantos gols na partida {c}: ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)

print(f'Informações armazenadas | {dados}')

for i, valor in dados.items():
    print(f'{i:<8}: {valor}')
print()

print('*-*' * 5, f'O jogador {dados["nome"]} jogou {jogos} partidas','*-*' * 5)
for i, valor in enumerate(partidas):
     print(f'Partida - {i} .... | Gols: {valor}')
print(f'Total de gols: {dados["total"]}')

#partidas.clear()  # <- limpa a lista para o próximo jogador