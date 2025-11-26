from time import sleep

print(f'\n{" KPI - Analisando informações ":-^60}\n')

registros = []
homem_mais_velho = 0
nome_homem_velho = ''
total_mulheres = 0
soma_idade = 0

for i in range(1,5):
    try:
        print(f'{f" Cliente {i} "::^40}')
        nome = input(' - Nome completo: ').strip().upper()
        idade = int(input(' - Informa sua idade: '))
        sexo = input(' - Gênero (M / F): ').strip().upper()

        # Soma de idades
        soma_idade += idade

        # Homem mais velho
        if sexo == 'M' and idade > homem_mais_velho:
            homem_mais_velho = idade
            nome_homem_velho = nome

        # Mulheres com menos de 20
        if sexo == 'F' and idade < 20:
            total_mulheres += 1

        # Registro individual
        registro = {
            "nome": nome,
            "idade": idade,
            "sexo": sexo
        }
        registros.append(registro)

    except Exception as erroRegistro:
        print(f'Erro ao registrar informações: {erroRegistro}')

# Estatísticas finais
media_grupo = soma_idade / len(registros)

print('\n== Informações dos clientes cadastrados ==\n')
sleep(1)

for r in registros:
    print(f'Nome: {r["nome"]} | Idade: {r["idade"]} | Sexo: {r["sexo"]}')
    sleep(0.5)

print('\n== Análise geral do grupo ==\n')
print(f'Média de idade do grupo: {media_grupo:.2f}')
print(f'Nome do homem mais velho: {nome_homem_velho} ({homem_mais_velho} anos)')
print(f'Total de mulheres com menos de 20 anos: {total_mulheres}')
print(f'Soma das idades: {soma_idade}')
