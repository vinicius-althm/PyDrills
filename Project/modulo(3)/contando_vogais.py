from main import banner
banner(f' Contando vogais  ')

texto = ('corinthians','bahia','carro','futebol')
vogais = 'aeiou'
for texto in texto:
    print(f'\nNa palavra {texto} temos => ', end="")
    for letra in texto:
        if letra.lower() in vogais:
            print(f'{letra.upper()}', end='')