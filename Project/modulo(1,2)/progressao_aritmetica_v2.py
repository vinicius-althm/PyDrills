
from time import sleep
print('=-=' * 15)
print(f'GERADOR PA')
print('=-=' * 15)
primeiro = int(input(f'PRIMEIRO TERMO: '))
razao = int(input(f'RAZÃO PA: '))
termo = primeiro
contador = 1

total_termos = 0
input_dados = 10

while input_dados != 0:
    total_termos += input_dados
    while contador <= total_termos:
            print(f'{termo} -> ', end="")
            termo += razao
            contador += 1
    print('Aguardando entrada de novos dados...')
    input_dados = int(input(f'\nQuantos termos você quer mostrar?'))
print(f'Total de termos -> {total_termos}')
print('Fim do programa')



