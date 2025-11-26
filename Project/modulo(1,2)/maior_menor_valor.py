from time import sleep

cont = media = soma = 0
valores = []
print(f'{"Verificando valores":=^30}')

while True:
    dados = int(input(f'informe um numero: '))
    pergunta = str(input(f'Deseja continuar? [Y/N]: ')).strip().upper()
    soma += dados
    cont += 1
    media = soma / cont
    valores.append(dados)
    maior_numero = max(valores)
    menor_numero = min(valores)
    if pergunta == 'Y':continue
    elif pergunta == 'N': print(f'Programa encerrado.')
    break
sleep(1)

print(f'{"Resultado":=^25}')

print(f'Apresentando todos os valores digitados: {valores}')
print(f'Quantidade de valores digitados: {cont}\nSoma dos valores: {soma}')
print(f'A média é: {media:.2f}')
print(f'O maior numero da sequencia é: {maior_numero}\nO menor numero da sequencia é: {menor_numero}')
print('*' * 25)
