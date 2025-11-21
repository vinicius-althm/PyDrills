from time import sleep

num1 = int(input(f'Digite o primeiro numero: '))
num2 = int(input(f'Digite o segundo numero: '))
opcao = 0
print(f'Carregando menu de opções ...')
sleep(1.5)
while opcao != 5:
    print(f'{"":=^50}')
    print(f"""
    [ 1 ] somar\n
    [ 2 ] multiplicar\n
    [ 3 ] maior\n
    [ 4 ] novos números\n
    [ 5 ] sair do programa)
    """)
    print(f'{"":=^50}')
    opcao = int(input(f'Selecione uma opcao:'))
    sleep(1.5)
    if opcao == 1:
        soma  = num1 + num2
        print(f'A soma de {num1} + {num2} é : {soma}')
    elif opcao == 2:
        mult = num1 * num2
        print(f'A multiplicação de {num1} x {num2} é : {mult}')
    elif opcao == 3:
        if num1 > num2:
          maior = num1
          print(f'O  numero1 ({maior})\n é maior que o numero2 ({num2})')
        else:
            maior = num2
            print(f'O  numero2 ({maior})\n é maior que o numero1 ({num1})')
    elif opcao == 4:
        num1 = int(input(f'Digite o primeiro valor: '))
        num2 = int(input(f'Digite o segundo valor: '))
    elif opcao == 5:
        print(f'Fim do programa. :)')
        break
    else:
        print(f'Opção invalida. Digite uma opção valida:')
print('=-=' * 20)



