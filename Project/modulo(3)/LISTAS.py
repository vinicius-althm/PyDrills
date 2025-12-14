from main import banner


banner(' Listas em python - Variaveis compostas ')

lista = [1,2,3,4,5,6,7,8,9]
print(f'Lista  inicial -  {lista}')
lista.append(10) # adiciona novo valor no final da lista
lista.remove(6) #remove a primeira ocorrencia do valor
lista.insert(0,11) #adiciona um novo valor e ordena os indices
lista.pop(6)
print(f'Lista modificada - {lista} ')

