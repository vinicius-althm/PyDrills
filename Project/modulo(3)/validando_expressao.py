from main import banner
banner(' Listas - Validando expressao ')


pilha = []
exp = input('Digite uma expressao :')
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressao valida')
else:
    print('Expressao invalida')






