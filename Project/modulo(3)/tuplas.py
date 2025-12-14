from main import banner

banner('Tuplas')
frutas = ('maça', 'banana', 'kiwi','uva')
numeros = (2,0,8,9,5,4,1)

#Modo 1 - Apresentando apenas os valores
for fruta in frutas:
    print(f'Vou comer {fruta}')
print(f'total de frutas disponiveis: {len(frutas)}')

print('*' * 25)

#Modo 2 - Apresentando o index e o valor, usando enumerate.
for index, fruta in enumerate(frutas):
    print(f'Posição {index}º - {fruta}')

print('*' * 25)
#Ordenando a tupla
print(sorted(frutas))
print(sorted(numeros))


