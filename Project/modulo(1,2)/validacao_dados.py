
from time import sleep
from datetime import datetime
import pytz

data_hora = pytz.timezone("America/Sao_Paulo")
dt_local = datetime.now(data_hora)
dt_padrao = dt_local.strftime("%d/%m/%Y %H:%M:%S")
print(f'{" Bem-vindo ":=^25}' )

sexo = str(input(f'Digite o seu sexo M/F: ')).strip().upper()
while sexo not in 'MmFf':
    sleep(1)
    sexo = str(input(f'informações invalidas.\nDigite o seu sexo M/F: ')).strip().upper()

print(f'Carregando...')
sleep(1)
print(f'[{dt_padrao}] => Informações registradas. Sexo - {sexo}')
with open ('logs/dados_armazenados.txt', "a", encoding="utf-8") as arquivo:
    arquivo.write(f'\n[{dt_padrao}] => Informações registradas. Sexo - {sexo}')

print(f'[{dt_padrao}] => Fim do programa')
