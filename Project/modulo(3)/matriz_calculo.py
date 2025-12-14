from main import banner

banner('Matriz - Calculo')

matriz = [[],[],[]]
soma_coluna = 0
soma_par  = 0
maior_numero = 0

#Adicionando valores na matriz
for li in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite um valor para a matriz [{li}] [{col}]: '))
        matriz[li].append(num)
        if num % 2 == 0:
            soma_par += num

        if col == 2:
            soma_coluna += num

        if li == 2:
            maior_numero = max(matriz[1])

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'Soma dos numeros pares digitados: {soma_par}')
print(f'A soma dos numeros na coluna 3 é {soma_coluna}')
print(f'O maior numero da 2 linha é {maior_numero}')



"""
#Somando somente os numeros pares da matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f'Soma dos numeros pares digitados: {soma_par}')

#Coluna fixa, linha variavel - Soma da terceira coluna
for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f'A soma dos numeros na coluna 3 é {soma_coluna}')


#Verificando o maior numero da coluna
for c in range(0, 3):
   if c == 0:
       maior_numero = matriz[1][c]
   elif matriz[1][c] > maior_numero:
       maior_numero = matriz[1][c]
#Utilizando apenas a funcao max()
maior_numero = max(matriz[1])

print(f'O maior numero da 2 linha é {maior_numero}')

"""

