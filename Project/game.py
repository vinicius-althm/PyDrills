from random import randint
from time import sleep

def verificar_resultado(jogador, maquina, itens):
    if jogador == 3:
        print('Encerrando o programa...')
        sleep(1)
        exit()
    if jogador == maquina:
        return f'EMPATE! Ambos escolheram {itens[jogador]}'
    elif (jogador == 0 and maquina == 2) or (jogador == 1 and maquina == 0) or (jogador == 2 and maquina == 1):
        return f'Jogador VENCEU! Escolheu {itens[jogador]} | Máquina perdeu! Escolheu {itens[maquina]}'
    else:
        return f'Jogador PERDEU! Escolheu {itens[jogador]} | Máquina venceu! Escolheu {itens[maquina]}'

print(' BEM-VINDO AO GAME ')

itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)

print(''' Escolha uma opção: 
    [0] - Pedra
    [1] - Papel
    [2] - Tesoura
    [3] - Encerrar o programa
''')
while True:
    try:
        jogador = int(input('Qual sua escolha? '))
        if jogador not in [0, 1, 2, 3]:
            print("Escolha inválida! Tente novamente.")
            sleep(1)
        else:
            sleep(1)
            print(verificar_resultado(jogador, maquina, itens))
    except ValueError:
        print("Entrada inválida! Digite um número entre 0 e 3.")


