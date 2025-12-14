from main import banner
banner(' Listas - Unificar valores ')

lista_numeros = [[], []]
pares = []
impar = []

print('Para encerrar digite [0]')

while True:
    num = int(input('Digite um numero inteiro: '))
    if num == 0:
        print('Encerrando o programa')
        break
    if num % 2 == 0:
        lista_numeros[0].append(num)
        pares.append(num)
        print('Numero par adicionado')
    else:
        lista_numeros[1].append(num)
        impar.append(num)
        print('Numero impar adicionado ')



print(f'Resultado final |  {lista_numeros}')

print(f'Resultado final v2 | Sublistas: {[pares, impar]}')

