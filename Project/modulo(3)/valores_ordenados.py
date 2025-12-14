from main import banner
banner(' Listas - Ordenação sem o metodo sort() ')


lista = []
for i in range(0,5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posicao/indice {posicao} da lista')
                break
            posicao += 1
print(f'Os valores digitados: {lista}')
