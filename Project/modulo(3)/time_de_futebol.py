from main import banner
banner('Time de futebol')

print('**Informe os 20 primeiros times do campeonato**')
classificacao_brasileirao_2025 = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Mirassol",
    "Botafogo",
    "Bahia",
    "Fluminense",
    "São Paulo",
    "Grêmio",
    "Red Bull Bragantino",
    "Corinthians",
    "Atlético Mineiro",
    "Vasco da Gama",
    "Ceará",
    "Internacional",
    "Vitória",
    "Santos",
    "Fortaleza",
    "Juventude",
    "Sport Recife"
)
print('Lista do campeonato brasileiro')

print('**' *20)
#ordem alfabetica
print(f'Ordem alfabetica:\n', sorted(classificacao_brasileirao_2025))
print('Os primeiros 5 times do campeonado:\n', classificacao_brasileirao_2025[:5])
print('Os ultimos 4 times do campeonado:\n', classificacao_brasileirao_2025[-4:])
print(f'O Corinthians esta em - {classificacao_brasileirao_2025.index("Corinthians") + 1}º colocado')
print('**' *20)


for index, nome in enumerate(classificacao_brasileirao_2025):
    print(f'Posição:{index + 1}º - {nome}')

