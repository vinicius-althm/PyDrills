"""

#List principal
teste = []
#Lista secundaria
galera = []
#Adicionando valores - Lista Teste
teste.append('Vinicius')
teste.append(26)
#Adicionando lista galera na lista Teste
galera.append(teste[:])
teste[0] = 'Thomas'
teste[1] = 3
galera.append(teste[:])
print('*' * 25)
#print(galera)


#Criando lista de forma manual

galera = [['Vinicius', 26], ['Thomas', 3], ['Sabrina',26]]
#print(galera)

#for pessoa in galera:
    #print(f'{pessoa[0]} tem {pessoa[1]} anos')

galera = [] # Lista principal
dados = [] #Lista auxiliar
totmaior = totmenor = 0

for index in range(0,3):
    dados.append(str(input('Digite um nome do cliente: ')))
    dados.append(int(input('Digite a idade do cliente: ')))
    dados.append(str(input('Digite o sexo do cliente: ')))
    galera.append(dados[:]) #Copia os dados para a lista principal
    dados.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totmenor += 1

print('*' * 25)
print(f'Temos {totmaior} pessoas maiores de idade e {totmenor} pessoa(s) menor(es) de idade')
"""
