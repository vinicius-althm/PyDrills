from colorama_config import mensagem_erro, mensagem_sucesso, mensagem_aviso, mensagem_normal


frase = input('Insira uma frase qualquer:').strip().upper()
palavras = frase.split() #gerar uma lista
agrupar = '' .join(palavras) # Agrupar em uma string
inverso = ''
#utilizando
inverso = agrupar[::-1]
#Utilizando o for
"""for letra in range(len(agrupar) -1, -1, -1):
    inverso += agrupar[letra]
"""
print(f'O inverso de {agrupar} é -> {inverso}')
print(agrupar, inverso)
result = mensagem_sucesso('É um palindromo') if inverso == agrupar else mensagem_erro('Não é um palindromo')