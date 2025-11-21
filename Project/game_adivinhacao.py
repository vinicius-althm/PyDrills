from random import randint
print(f'{"JOGO DA ADIVINHAÇÃO v2":=^50}')
print(f'Me chamo RedBot, acabei de pensar um número entre 0 e 10.\nSerá que você consegue adivinhar?')
palpites = 0
while True:
    computador = randint(0, 10)
    num = input(f'qual o seu palpite?:')
    palpites += 1
    if not num.isdigit():
        print(f'Digite apenas numeros. Tente novamente')
        continue
    num = int(num)
    if num == computador:
        print(f'Você Acertou!!. A maquina pensou no numero {num}')
    else:
        print(f'Você Errou!!. A maquina pensou no numero {computador}')

print(f'Total de palpites: {palpites}')