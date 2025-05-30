from colorama_config import mensagem_erro, mensagem_sucesso, mensagem_aviso, mensagem_normal

from datetime import date
anoAtual = date.today().year
contMaior = 0
contMenor = 0
for p in range(1,8):
    nascimento = int(input(f'{p}º - Qual a data  sua data de nascimento?: '))
    idade = anoAtual - nascimento
    contMaior += 1 if idade >= 21 else 0
    contMenor += 1 if idade < 21 else 0
    result = mensagem_sucesso(f'Maior idade. Idade atual é : {idade} anos') if idade >=21 else mensagem_aviso(f'Menor idade. Idade atual é : {idade} anos')
mensagem_sucesso(f'Ao ano tivemos {contMaior} pessoas maiores de idade')
mensagem_aviso(f'Ao ano tivemos {contMenor} pessoas menores de idade')