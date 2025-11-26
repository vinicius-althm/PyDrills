primeiro = int(input(f'Digite o primeiro termo: '))
r = int(input(f'Razão: '))
decimo = primeiro + (10-1) * r

for n in range(primeiro, decimo + r, r):
    print(f'{n}', end='->')
print('Acabou!!')