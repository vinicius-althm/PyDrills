from main import *
from operator import itemgetter
banner('DICIONARIO - CADASTRO JOGADOR ::v2::')


time = []
while True:
    gols = []
    nome_jogador = str(input('Digite o nome do jogador: ')).strip().upper()
    jogos = int(input(f'Quantas partidas o jogador {nome_jogador} participou?: '))
    for jogo in range (0, jogos):
        gols_partida = int(input(f'Quantos gols na partida {jogo}º: '))
        gols.append(gols_partida)
    jogadores = {
        'jogador':nome_jogador,
        'jogos' : jogos,
        'gols': gols,
        'total': sum(gols)
    }
    time.append(jogadores)
    op = str(input('Deseja continuar? [S ou N]')).strip().upper()[0]
    if op == 'N':
        print('Finalizando programa...')
        break

#print(f'dados armazenados: {time}')
#Tabela larguras
w_cod = 4
w_jogador = 10
w_partidas = 10
w_gols = 10
w_total = 7
print(
    f'{"COD":>{w_cod}} | '
    f'{"JOGADOR":>{w_jogador}} | '
    f'{"PARTIDAS":>{w_partidas}} | '
    f'{"GOLS":>{w_gols}} | '
    f'{"TOTAL":>{w_total}}'
)
for cod, i in enumerate(time):
    gols_part= ','.join(map(str, i['gols']))
    print(
        f'{cod:>{w_cod}} | '
        f'{i["jogador"]:>{w_jogador}} | '
        f'{i["jogos"]:>{w_partidas}} | '
        f'{gols_part:>{w_gols}} | '
        f'{i["total"]:>{w_total}}'
    )
while True:
    busca = int(input(f'Mostrar dados de qual jogador [999 para sair]: '))
    if busca == 999:
        print('busca encerrada...')
        break
    if busca >=len(time):
        print(f'Erro ao consultar jogador. Valor não existe| Cod. {busca}')
    else:
        print('-'*10, f'FICHA TÉCNICA DO JOGADOR {time[busca]["jogador"]}', '-'*10)
        for i, gols in enumerate(time[busca]["gols"]):
            print(f'No jogo {i + 1}º  fez {gols} gols')
"""
           #Levantamento (tabela)
           print(
                f'{"COD":<{w_cod}} | '
                f'{"JOGADOR":<{w_jogador}} | '
                f'{"PARTIDAS":>{w_partidas}} | '
                f'{"GOLS":<{w_gols}} | '
                f'{"TOTAL":>{w_total}}'
            )
            gols_part = ','.join(map(str, time[busca]['gols']))

            print(
                f'{busca:<{w_cod}} | '
                f'{time[busca]["jogador"]:<{w_jogador}} | '
                f'{time[busca]["jogos"]:>{w_partidas}} | '
                f'{gols_part:<{w_gols}} | '
                f'{time[busca]["total"]:>{w_total}}'
            )
"""