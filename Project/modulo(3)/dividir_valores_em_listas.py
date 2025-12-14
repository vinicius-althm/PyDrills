from main import banner
banner(' Listas - Dividir valores ')

lista_numeros = []
lista_par = []
lista_impar = []
print('Para encerrar digite [0]')

while True:
    num = int(input('Digite um numero inteiro: '))
    if num == 0:
        print('Encerrando o programa')
        break
    print('Valor adicionado na lista principal')
    if num % 2 == 0:
        lista_par.append(num)
        print('Numero par adicionado a lista_par')

    else:
        lista_impar.append(num)
        print('Numero par adicionado a lista_impar')



lista_numeros =  lista_par + lista_impar
print(f'Todas as listas: {lista_numeros}')
print(f'Lista de numeros par: {lista_par}')
print(f'Lista de numeros impar: {lista_impar}')
