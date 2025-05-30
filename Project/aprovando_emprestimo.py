from time import sleep

casa = float(input(f'Valor da casa: R$'))
salario = float(input(f'Salario do comprador: R$'))
anos = int(input(f'Anos de financiamento: '))
minimo = salario * 0.3
prestacao = casa/(anos * 12)
print(f'Processando informações...' )
sleep(2)
print(f'para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de {prestacao:.2f}' )

if prestacao > minimo:
    print(f'Empréstimo reprovado. '
          f'Para aprovação o valor da prestação não pode ultrapassar os 30%. '
          f'Valor da parcela {prestacao:.2f} | o que você consegue pagar: {minimo:.2f} ')

else:
    print(f'Empréstimo aprovado. Valor a pagar mensal: R${prestacao:.2f}')