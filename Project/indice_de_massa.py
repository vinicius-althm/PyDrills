from colorama_config import mensagem_erro, mensagem_sucesso, mensagem_aviso, mensagem_normal

peso = float(input('Informe o peso do paciente: '))
altura = input('Informe a altura do paciente: ')

# Verifica se a altura está sem ponto
if altura.isdigit():
    # Converte para float e divide por 100
    altura = float(altura) / 100
    imc = peso / (altura ** 2)
    match imc:
        case imc if imc <= 18.5:
            mensagem_erro('Abaixo do peso')
            mensagem_erro(f'Seu IMC é {imc}')
        case imc if 18.5 < imc <= 25:
            mensagem_sucesso('Peso ideal')
            mensagem_sucesso(f'Seu IMC é {imc}')
        case imc if 25 < imc <= 30:
            mensagem_aviso('Sobrepeso')
            mensagem_aviso(f'Seu IMC é {imc}')
        case imc if 30 < imc <= 40:
            mensagem_erro('Obesidade')
            mensagem_erro(f'Seu IMC é {imc}')
        case imc if imc > 40:
            mensagem_erro('Obesidade mórbida')
            mensagem_erro(f'Seu IMC é {imc}')
