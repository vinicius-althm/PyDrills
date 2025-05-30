from colorama import init, Fore, Back, Style
# Inicializa o colorama (necessário no Windows)
init(autoreset=True)
# Configurações de cores
cor_erro = Fore.RED
cor_sucesso = Fore.GREEN
cor_avisos = Fore.YELLOW
cor_normal = Fore.WHITE
# Função para exibir mensagens com cores
def mensagem_erro(texto):
    print(cor_erro + texto)

def mensagem_sucesso(texto):
    print(cor_sucesso + texto)

def mensagem_aviso(texto):
    print(cor_avisos + texto)

def mensagem_normal(texto):
    print(cor_normal + texto)
