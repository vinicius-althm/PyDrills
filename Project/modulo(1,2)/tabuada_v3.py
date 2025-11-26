
while True:
    print(f'{"TABUADA v3":=^50}')
    tab = int(input(f'Qual tabuada você quer ver?: '))
    if tab < 0:
        print(f'Programa encerrado')
        break
    for i in range (1,11):
        print(f'{tab} x {i} = {tab * i}')
    opcao = str(input(f'Deseja continuar?: [Y/N]: ')).strip().upper()
    if opcao == 'Y':
        continue
    else:
        print(f'Programa encerrado! ')
        break