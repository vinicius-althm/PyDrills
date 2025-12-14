from main import *

banner('DICIONARIOS - UNINDO DICIONARIOS')

lista_pessoas = []

registros = 0
soma_idade = 0
media_idade = 0


while True:
    nome_cliente = str(input('Digite o nome do cliente: '))
    if not nome_cliente:
        print('Campo => [NOME] esta vazio. Por favor preencher')
        continue

    while True:
        idade = input('Digite a idade do cliente: ').strip()
        if  idade == "":
            print('Campo => [IDADE] esta vazio. Por favor preencher')
        elif idade.isnumeric():
            idade = int(idade)
            break
        else:
            print('Campo => [IDADE] deve conter apenas números')

    while True:
        sexo = input('Digite o sexo do cliente: ').strip().upper()
        if sexo == "":
            print('Campo => [SEXO] esta vazio. Por favor preencher')
        elif sexo not in 'FM':
            print('Campo => [SEXO] preencher somente com F ou M')
        else:
            break #encerrao o loop interno

    pessoas = {
        'nome': nome_cliente,
        'idade': idade,
        'sexo': sexo,
    }  # principal
    lista_pessoas.append(pessoas)
    registros += 1
    soma_idade += idade
    media_idade = soma_idade / registros

    # --- validação da entrada ---
    while True:
        op = input('Quer continuar? [S/N] ').strip().upper()

        if op in ('S', 'N'):
            break
        print('Entrada inválida! Digite apenas S ou N.')

    # --- tomada de decisão ---
    if op == 'N':
        print('Programa finalizado pelo administrador')
        break

#--------------------------------------------------------------------#
#--------------------------- RESULTADO FINAL -----------------------#
#--------------------------------------------------------------------#

print('*-' * 15, 'LISTA DE CADASTROS', '-*' * 15)
print(f'A) Total de cadastrados: {'':<5}{registros}')
print(f'B) Media da idade:{'':<10} {media_idade:.1f}')
print()
mulheres =  [p for p in lista_pessoas if p['sexo'] == 'F']
print()
if mulheres:
    print("\nMulheres cadastradas:")
    print(f'{"Nome":<12}{"Idade":>6}')
    for m in mulheres:
        print(f'{m["nome"]:<12}{m["idade"]:>6}')
else:
    print('\nNenhuma mulher foi cadastrada.')

print(f'{"Nome":<10}{"Idade":>8}{"Sexo":>8}')
for i in lista_pessoas:
    print(f'{i["nome"]}{i["idade"]:>6} anos{i["sexo"]:>4}.')

print()
print('Pessoas com idade acima da media\n')
for m in lista_pessoas:
    if m['idade'] >= media_idade:
        print(f'{m["nome"]:<12}{m["idade"]:>6}')
print('<<<<PROGRAMA ENCERRADO>>>>')