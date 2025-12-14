from main import banner

banner('Matriz')

#Matriz preenchida
#matriz = [[0,0,0],[0,0,0],[0,0,0]]
matriz = [[],[],[]]
for li in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite um valor para a matriz [{li}] [{col}]: '))
        matriz[li].append(num)

        #é possivel utilizar assim
        #matriz[li][col] = num

#print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()