
#Versão 2.0
from datetime import datetime
import os
diretorio = os.getcwd() #Caminho completo do projeto
dir_log = 'logs' #Nome do diretorio
path = os.path.join(diretorio, dir_log) #Caminho do projeto/diretorio logs

if not os.path.exists(path): #Se não existir, o diretorio é criado
    os.mkdir(path)

arquivo_nome = os.path.join(path,'dados_armazenados.txt')  # Nome fixo do arquivo com o caminho completo
# Abre o arquivo em modo append (adicionar no final), com encoding utf-8
with open(arquivo_nome, 'a', encoding='utf-8') as arquivos:
    arquivos.write(f"\n--- Nova execução em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---\n")
    while True:
        try:
            text = input('Digite um texto: ')
            if text == '':
                break
            arquivos.write(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] => {text}\n')  # Adiciona no final do arquivo
        except Exception as Error:
            print(f"Erro ao inserir informações - {Error}")

print('Fim do programa. Dados adicionados em', arquivo_nome)
