from main import *
banner('ESCOLA - BOLETIM')

lista = []
boletim = []

while True:
    nome_aluno = str(input('Nome do aluno:  ')).strip().upper()
    if not nome_aluno:
        print('Campo [Nome] vazio. Tente novamente.')
        continue
    #Loop para validar as notas
    # Nota 1
    while True:
        nota1 = input("Nota 1: ").strip()
        if nota1 != "":
            nota1 = float(nota1)
            break
        print("A Nota 1 não pode ficar vazia.")

    # Nota 2
    while True:
        nota2 = input("Nota 2: ").strip()
        if nota2 != "":
            nota2 = float(nota2)
            break
        print("A Nota 2 não pode ficar vazia.")

    media = (nota1 + nota2) / 2
    #Adicionando os valores digitados na lista
    lista.append(nome_aluno),lista.append([nota1,nota2]),lista.append(media)
    boletim.append(lista[:])
    lista.clear()

    op = input('Deseja continuar? [S/N]').strip().upper()
    if op == 'N':
        print('Finalizando cadastro de notas...')
        break
    elif op == 'S':
        continue

#print(f'Boletim dos alunos? {boletim}')
print(f'{"ID.":<4}{"Nome":<10}{"Media":>8}')
for index, valor in enumerate(boletim):
    print(f'{index:<4}{valor[0]:<10}{valor[2]:>8.1f}')
while True:
    print('*=' * 30)
    op = input('Mostrar notas de qual aluno? (digite 00 para finalizar): ')
    if op == '00':
        print('Finalizando consulta...')
        break
    op = int(op)
    if op <= len(boletim) - 1:
        print(f'Segue as notas do aluno solicitado\nNome: {boletim[op][0]} | Notas: {boletim[op][1]}')
    else:
        print('Não localizamos o ID do aluno. Tente novamente')