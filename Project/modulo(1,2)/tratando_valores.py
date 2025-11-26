"""


#Solução 1
num = soma = cont = 0
num = int(input(f'Digite um numero [999 para encerrar]: '))
valores = []
while num != 999:
        soma  += num
        cont +=1
        num = int(input(f'Digite um numero [999 para encerrar]: '))
        valores.append(num)
print(f'O total de numeros digitados é: {cont} e a soma deles é {soma}')
print(f'Lista de valores inseridos: {valores[:-1]}')
"""
#Solução 2
soma = cont = 0
valores = []
while True:
    num = int(input(f'Digite um numero [999 para encerrar]: '))
    if num == 999:
        print(f'Programa encerrado!!')
        break
    soma  += num
    cont +=1
    valores.append(num)
print(f'O total de numeros digitados é: {cont} e a soma deles é {soma}')
print(f'Lista de valores inseridos: {valores}')