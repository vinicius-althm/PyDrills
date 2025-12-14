from num2words import  num2words
from main import banner
banner('Numeros por extenso')
total_num = []
while True:
    numero = int(input('Digite um numero inteiro entre 0 e 20: '))
    if numero < 0 or numero > 20:
        print('Numero invalido. Somente numeros entre 0 e 20, tente novamente.')
        continue
    numero_extenso = num2words(numero, lang='pt_BR', to='cardinal')
    total_num.append(numero)
    print(f'O numero digitado foi {numero_extenso}')

    op = input('Deseja continuar? [S/N] :').strip().upper()[0]
    if op in 'N':
        print('Programa encerrado')
        break

print('Total de numeros digitados: ', len(total_num))
print('Numeros digitados: ', total_num)
