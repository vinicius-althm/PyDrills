

from main import banner
banner(' Analise de dados ')
valores = []
cont = 1
while cont < 5:
    text = int(input(f'{cont} - Digite um numero: '))
    cont += 1
    valores.append(text)
dados = tuple(valores)
contagem = dados.count(9)
posicao = None
numeros_pares = [num_par for num_par in dados if num_par % 2 == 0]

print(f'Total de dados: {len(dados)}')
print(f'Você digitou os valores {dados}')
print(f'O numero 9 apareceu {contagem} vezes')
if 3 in dados:
    posicao = dados.index(3) + 1
    print(f'O numero 3 foi digitado pela primeira vez na posicao {posicao}')
else:
    print(f'O numero 3 não foi localizado em nenhuma posicao da tupla')

print(f'Numero par digitado: {numeros_pares}')



