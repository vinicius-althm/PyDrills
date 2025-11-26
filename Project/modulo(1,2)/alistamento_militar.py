from datetime import date

ano = date.today().year


nascimento = int(input( f'Em que ano você nasceu? '))
idade = int(ano - nascimento)
print(f'Quem nasceu em {nascimento} tem {idade} em {ano}')

if idade == 18:
    print(f'Hora exata de se alistar')
elif idade < 18:
    tempo =  18 - idade
    alistamento = ano + tempo
    print(f'Você ainda não completou 18 anos. Ainda faltam {tempo} anos')
    print(f'O ano do alistamento será em {alistamento}')

elif idade > 18:
    tempo = idade - 18
    alistamento = ano - tempo
    print(f'Você ja deveria ter se alistado há {tempo} anos')
    print(f'O ano do alistamento foi em {alistamento}')







