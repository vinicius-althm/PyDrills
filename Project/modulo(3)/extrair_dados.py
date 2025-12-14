from main import banner
banner(' Listas - Extrair dados ')

lista_numeros = []
continuar = True
while continuar:
    pergunta = input('Digite um numero:').strip()
    #verificando se o campo esta preenchido
    if not pergunta:
        print('O campo nao foi preenchido. Tente novamente')
        continue
    pergunta = int(pergunta)
    lista_numeros.append(pergunta)
    print('Valor adicionado com sucesso - ✅')
    #Deseja continuar?
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if not op:
            print('Digite S ou N. Tente novamente')
            continue
        if op in 'N':
            continuar = False
            break
        elif op in 'S':
            break

print(f'Lista original => {lista_numeros}')
print(f'Lista em ordem DESC (SORTED) => {sorted(lista_numeros, reverse=True)}')
print(f'Total de numeros digitados => {len(lista_numeros)}')
if 5 in lista_numeros:
    print(f'Verificando a existencia do numero (5) -  {lista_numeros.count(5)}º ocorrência')
else:
    print('Valor 5 não foi encontrado')