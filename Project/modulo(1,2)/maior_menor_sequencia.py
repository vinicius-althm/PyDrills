# Inicializando as variáveis para armazenar o maior e o menor peso
maior_peso = 0
menor_peso = float('inf')

# Loop para ler o peso de cinco pessoas
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa (em kg): '))
    if peso > maior_peso:
           maior_peso = peso
    if peso < menor_peso:
           menor_peso = peso
# Exibindo os resultados
print(f'\nO maior peso registrado foi {maior_peso:.2f} kg')
print(f'O menor peso registrado foi {menor_peso:.2f} kg')
