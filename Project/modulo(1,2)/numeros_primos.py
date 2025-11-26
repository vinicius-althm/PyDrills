from colorama_config import mensagem_erro, mensagem_sucesso, mensagem_aviso, mensagem_normal


print("=" * 30)
print('Exercicio - Numeros primos')
print("=" * 30)

num = int(input('Digite um numero inteiro: '))
result = 0
for c in range( 1, num + 1):
    if num % c == 0:
        mensagem_sucesso(f'{c}')
        result += 1
    else:
        mensagem_normal(f'{c}')

print (f' O numero {num} foi divisivel {result} vezes')

info = mensagem_sucesso(f'O número é primo') if result == 2 else mensagem_erro(f'O número não é primo')
