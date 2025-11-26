pares = []
for numero  in range(1,7):
    num  = int(input(f'Digite o {numero}º numero: '))
    if num % 2 == 0:
        pares.append(num)

soma = sum(pares)
cont = len(pares)

print(f' Você informou {cont} numeros PARES e a soma foi {soma} ')

