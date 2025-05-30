from colorama_config import mensagem_erro, mensagem_sucesso, mensagem_aviso, mensagem_normal
from datetime import date

ano = date.today().year

atleta = input('Informe o nome do atleta: ').lower().strip()
nascimento = int(input('Informe o ano de nascimento: '))
idade = ano - nascimento
categorias = ['Mirim', 'Infantil', 'Júninho', 'Sênior', 'Master']

match idade:
    case idade if idade <= 9:
        mensagem_aviso(f'Categoria {categorias[0]}')
    case idade if idade <= 14:
        mensagem_aviso(f'Categoria {categorias[1]}')
    case idade if idade<= 19:
        mensagem_sucesso(f'Categoria {categorias[2]}')
    case idade if idade <= 25:
         mensagem_sucesso(f'Categoria {categorias[3]}')
    case idade if idade >= 25:
        mensagem_erro(f'Categoria {categorias[4]}')






