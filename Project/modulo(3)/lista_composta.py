from main import banner

banner('Analise de dados -  Peso dos clientes')
pessoas = []
dados = []
maior_peso = menor_peso = None

for p in range(1, 5):
     dados.append(str(input(f'Digite o nome do {p}º pessoa: ')))
     dados.append(float(input(f'Digite o peso da {p}º pessoa: ')))
     peso = dados[1]
     if maior_peso is None or peso > maior_peso:
        maior_peso = peso
     if menor_peso is None or peso < menor_peso:
        menor_peso = peso
     pessoas.append(dados[:])
     dados.clear()

print(f'Total de pessoas: {len(pessoas)}')
print('*' * 25)
print('Peso dos clientes')
for pessoa in pessoas:
    nome = pessoa[0]
    peso = pessoa[1]
    print(f'{nome.upper():.<15} | {peso}Kg')
print(f'O maior peso foi de {maior_peso} Kg')
print(f'O menor peso foi de {menor_peso} Kg')

print('*' * 25)
print(f'{pessoas}')