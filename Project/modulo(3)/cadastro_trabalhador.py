from main import *
from datetime import datetime
banner('DICIONARIO - CADASTRO TRAB. ')

colaborador = {}
data = datetime.now()
ano_atual = data.year

colaborador['nome'] = input('Digite seu nome: ').strip().upper()
ano  = int(input('Digite seu ano de nascimento: '))
colaborador['idade'] =  ano_atual - int(ano)
ctps = int(input('Digite seu CTPS: '))
colaborador['ctps'] = ctps
if ctps != 0:
    ctps = int(ctps)
    colaborador['admissao'] = int(input('Digite seu contratacao: '))
    colaborador['salario'] = float(input('Digite seu salario: R$ '))
    colaborador['aposentadoria']  = (colaborador['admissao'] + 35) - ano_atual + colaborador['idade']
print()

print(f'{"ID": <10}{"COLAB"}')
for key, value in colaborador.items():
    print(f'{key:<10}: {value}')