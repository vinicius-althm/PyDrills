from colorama_config import mensagem_erro, mensagem_sucesso, mensagem_aviso, mensagem_normal
from time import sleep

print(f'{"TECH PROD":=^40}')


while True:
    print(f'{"Registrando pagamento":^40}\n')
    preco = input('Preço das compras: R$').strip()
    if not preco:
        mensagem_erro('O campo não foi preenchido. Insira o valor da compra')
        sleep(2)
        continue
    preco = float(preco)

    while True:
            print(f'\n{"Formas de pagamento":=^40}')
            print('''
            [1] à vista (dinheiro/Pix)
            [2] à vista (cartão)
            [3] 2x  no cartão
            [4] 3x ou mais no cartão
    
            ''')
            opcao = input('Qual a forma de pagamento? ')
            if not opcao.isdigit():
                mensagem_erro('Informe uma opção válida!.')
                continue
            opcao = int(opcao)
            if opcao not in [1, 2, 3, 4]:
                mensagem_erro(f'\nOpção inválida. Escolha uma das opções listadas.')
                sleep(2)
                continue
            match opcao:
                case 1:
                    total = preco - (preco * 0.10)
                case 2:
                    total = preco - (preco * 0.05)
                case 3:
                    total = preco / 2
                case 4:
                    total = preco + (preco * 0.20)
                    totalparc = int(input('Quantas parcelas?'))
                    parcela =  total /totalparc
                    mensagem_sucesso(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f}')

            break  # Esse break garante que saímos do loop após uma seleção válida de pagamento

    mensagem_sucesso(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final\n')