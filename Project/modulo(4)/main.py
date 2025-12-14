from datetime import datetime
data_atual = datetime.now()
data_hr = data_atual.strftime('%d/%m/%Y %H:%M:%S')

def banner (texto, largura = 30):
    print('*' * largura)
    print(f"*{texto:^{largura-2}}*")
    print(f'{data_hr:^{largura-2}}')
    print('*' * largura)
