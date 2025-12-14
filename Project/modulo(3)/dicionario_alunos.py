from main import *

banner(' DICIONARIO - NOTA DOS ALUNOS ')


alunos = {}

alunos['nome'] = str(input('Nome do aluno: '))
alunos['media'] = float(input(f'Media do aluno {alunos["nome"]}: '))

if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situacao'] = 'Recuperação'
else:
    alunos['situacao'] = 'Reprovado'

print('*-*' * 30)
for chave, valor in alunos.items():
    print(f'{chave} do aluno: {valor}')