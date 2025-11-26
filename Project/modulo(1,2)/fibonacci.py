print('=-=' * 20)

print(f'Sequência de fibonacci')
print('=-=' * 20)
num = int(input(f'Digite  quantos termos você quer visualizar: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2}', end="")
while cont <= num:
    t3 = t1 + t2
    print(f'-> {t3}', end="")
    t1 = t2
    t2 = t3
    cont +=1
exit()
print(' -> FIM')