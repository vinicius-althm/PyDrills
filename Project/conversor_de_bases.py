from time import sleep

while True:

        numero = input('Digite um numero inteiro: ')
        if not numero.strip():  # Entrada vazia ou apenas espaços
            print("Erro: Nenhuma opção foi digitada. Tente novamente.\n")
            continue  # Retorna ao menu

        # Tenta converter a entrada para número
        try:
            numero = int(numero)
        except ValueError:
            print("Erro: Digite um número válido.\n")
            continue  # Retorna ao menu

        while True:
            print('Carregando opções...')
            sleep(2)
            print("="*50)
            print(f''' 
            Qual base você deseja converter: 
            [0] Para encerrar. 
            [1] Converter para Binário, OCTAL e HEXADECIMAL
            ''')
            print("="*50)

            opcao = input('Sua opção: ').strip()

            # Verificar se a entrada está vazia
            if not opcao:
                print("Erro: Nenhuma opção foi digitada. Tente novamente.\n")
                sleep(2)
                continue  # Retorna ao menu de opções

            # Tenta converter a opção para inteiro
            try:
                opcao = int(opcao)
            except ValueError:
                print("Erro: Digite um número válido para a opção.\n")
                sleep(2)
                continue  # Retorna ao menu de opções

            match opcao:
                case 0:
                    print(f'Programa encerrado!')
                    exit()
                case 1:
                    print(f' número => {numero} - Convertido para Binário: {bin(numero)[2:]}')
                    print(f' número => {numero} - Convertido para OCTAL: {oct(numero)[2:]}')
                    print(f' número => {numero} - Convertido para HEXADECIMAL: {hex(numero)[2:]}')
                case _:
                    print(f'Nenhuma opção selecionada')
                    continue
            sleep(2)  # Pausa de 2 segundos após mostrar a conversão
            print("\nVoltando ao início para digitar um novo número...\n")
            sleep(1)  # Pausa de 2 segundos antes de voltar ao início
            break