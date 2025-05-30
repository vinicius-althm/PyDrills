from colorama_config import mensagem_erro, mensagem_sucesso, mensagem_aviso, mensagem_normal

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1 + nota2 )/2

match media:
    case media if media < 5.0:
      mensagem_erro('Reprovado')
    case media if 5.0 <= media < 7.0:
        mensagem_aviso('Recuperação')
    case media if media >= 7.0:
      mensagem_sucesso('Aprovado')