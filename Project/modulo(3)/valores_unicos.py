from main import banner
banner(' Listas - Valores unicos ')

lista_numeros = []
continuar = True
while continuar:
    pergunta = input('Digite um numero:').strip()
    #verificando se o campo esta preenchido
    if not pergunta:
        print('O campo nao foi preenchido. Tente novamente')
        continue
    pergunta = int(pergunta)
    #Caso o numero nao esteja na lista
    if pergunta not in lista_numeros:
        lista_numeros.append(pergunta)
        print('Valor adicionado com sucesso - ✅')
    else:
        print('Valor duplicado. Tente novamente ❌')
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
print(f'Lista ordenada (SORTED) => {sorted(lista_numeros)}')



