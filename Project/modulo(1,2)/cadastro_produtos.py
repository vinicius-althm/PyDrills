
import json

itens = []
total_itens = 0
total_custo = 0
valor_acima_mil = 0
produto_barato = ' '
continuar_cadastro = True


texto = "Cadastro de Produtos"
largura = 40

#Loop principal
while continuar_cadastro:
    print("*" * largura)  # linha superior
    print(f"*{texto:^{largura - 2}}*")  # texto centralizado com bordas laterais
    print("*" * largura)  # linha inferior
#Validando o nome do produto
    while True:
        nome_produto = str(input(f'Digite o nome do produto: ')).strip().upper()
        if not nome_produto:
            print('O campo esta vazio, digite um nome para o produto')
        else:
            print(f'Nome do produto preenchido ✅')
            break

# Validando o preço do produto
    while True:
        preco_produto = input(f'Informe o preço do produto: R$')
        if not preco_produto:
            print('O campo esta vazio, digite o preço para o produto')
        if not preco_produto.replace('.', '', 1).isdigit():
            print('Digite apenas números para o preço')
            continue
        print(f'Preço incluido ✅')
        preco_produto = float(preco_produto)
        if preco_produto >= 1000:
            valor_acima_mil += 1
        break  # sai do loop quando o preço for válido

    itens.append({"produto": nome_produto,"preço": preco_produto})

# Quantidade de itens
    total_itens += 1
# Valor total de itens
    total_custo +=preco_produto

# Validando se o cliente deseja continuar a operação
    while True:
        opcao = input(f'Deseja continuar? [S/N]: ').strip().upper()
        if not opcao:
           print('O campo esta vazio, digite uma opao valida para continuar: [S/N]')
           continue
        if opcao[0] == 'N':
            print('ℹ️ - Encerrando operação | Cadastro de produtos')
            continuar_cadastro = False  # encerra o loop externo
            break
        elif opcao[0] == 'S':
            break
        else:
            print('Opção inválida, digite apenas S ou N')


print(f'{"Produtos cadastrados até o momento: ":*^30}')

# Exibir em JSON bonito
#print(json.dumps(itens, indent=4, ensure_ascii=False))

print(f'Total de itens: {total_itens}')

print(f'Custo total: {total_custo}')
#Recuperando somente o valor do produto
precos = [item["preço"] for item in itens]
#Recuperando somente o nome do produto
index_preco = precos.index(min(precos))
produto_barato = itens[index_preco]
#Maior e menor valor
print(f'Menor preço: R$ {min(precos):.2f} | Maior preço: R$ {max(precos):.2f}')
print(f'Produtos acima de mil reais: {valor_acima_mil}')
print(f'Prodruto mais barato custa - {produto_barato["produto"]} - {produto_barato["preço"]}')

# Dados em formato de chave-valor
for item in itens:
     print(f'Produto: {item["produto"]} | Preço: R$ {item["preço"]:.2f}')

