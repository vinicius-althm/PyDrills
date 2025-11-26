soma = 0
cont = 0
for numeros in range (1, 501, 2):
    if numeros % 3 == 0:
        cont = cont + 1
        soma = soma + numeros
        #print(f' Divisivel por 3: {numeros}')
print(f'A soma de todos os {cont} valores solicitados é : {soma}')