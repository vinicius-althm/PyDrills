from random import randint
from time import sleep

maquina_win = 0
maquina_loser = 0
usuario_win = 0
usuario_loser = 0
text = ' '
while True:
    print(f'{" GAME - PAR OU IMPAR ":*^40}')
    valor = int(input(f'Digite um valor: '))
    maquina_op = randint(1, 10)
    total = valor + maquina_op
    escolha = ' '
    sleep(1)
    while escolha not in 'PI':
        escolha = str(input(f'Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Você digitou {valor}  e a maquina {maquina_op}.')
    if escolha == 'P':
        if total % 2 == 0:
            text = 'É par'
            usuario_win +=1
            maquina_loser +=1
            print('-=-' * 30)
            print(f'A soma do valor é {total} : {text}')
            print('VOCÊ VENCEU A MAQUINA! - Vamos continuar... :D')
            continue
            sleep(1)
        else:
            print(f'A soma do valor é {total} : {text}')
            print('A MAQUINA VENCEU,QUE PENA! - O JOGO SERÁ ENCERRADO...')
            maquina_win +=1
            usuario_loser +=1
            break
            sleep(1)
    elif escolha == 'I':
        if total % 2 != 0:
            text = 'É impar'
            usuario_win +=1
            maquina_loser +=1
            print(f'A soma do valor é {total} : {text}')
            print('VOCÊ VENCEU A MAQUINA! - Vamos continuar... :D')
            continue
            sleep(1)
        else:
            print(f'A soma do valor é {total} : {text}')
            print('A MAQUINA VENCEU,QUE PENA! - O JOGO SERÁ ENCERRADO...')
            maquina_win +=1
            usuario_loser +=1
            break
            sleep(1)
print(f'Total de vitorias do usuario: {usuario_win} | Derrotas: {usuario_loser} ')
print(f'Total de vitorias da maquina: {maquina_win} | Derrotas: {maquina_loser} ')


