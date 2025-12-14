from main import banner
from random import randint
banner(' Valores - Maior e Menor presentes em uma Tupla ')
#Quantidade de elementos
numero_elementos = 5
#Armazenar os valores em uma lista
numeros = []
for _ in range(numero_elementos):
    #Gerar numeros aleatorios
    num_random = randint(1, 10)
    #Adicionar na lista
    numeros.append(num_random)
#Converter a lista em uma tupla
tupla_aleatoria = tuple(numeros)
    
print(f'Sorteei os valores: ', tupla_aleatoria)
max_valor = max(tupla_aleatoria)
min_valor = min(tupla_aleatoria)

print(f'Maior valor: {max_valor}')
print(f'Menor valor: {min_valor}')