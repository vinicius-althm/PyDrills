from main import banner
from datetime import datetime
data_atual = datetime.now()
data_hr = data_atual.strftime('%d/%m/%Y %H:%M:%S')
banner(' Lista de precos ')

materiais_escolares = (
    ("Caderno", 12.50),
    ("Lápis", 1.20),
    ("Borracha", 0.80),
    ("Caneta", 2.50),
    ("Mochila", 89.90),
    ("Estojo", 15.00),
    ("Régua", 3.40),
    ("Marca-texto", 4.90)
)
print(f'Data do cadasto: [{data_hr}]')

for pos in materiais_escolares:
    print(f"{pos[0]:.<30} R${pos[1]:>5.2f}")