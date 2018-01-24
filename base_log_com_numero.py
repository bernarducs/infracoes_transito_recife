import csv
import agate

""" tabela com infracoes tendo o número do semaforo como logradouro """

colunas = []
with open('bases/colunas.csv', newline='', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=',')
    for row in dados_obj:
        for i in row:
            colunas.append(i)

colunas.extend(['tipo_logradouro', 'num_semaforo'])

tipos = []
for i in range(len(colunas)):
    tipos.append(agate.Text())

base = []
with open('bases/logradouro_com_numero.csv', newline='', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=',')
    for row in dados_obj:
        base.append(row)

print(len(base))

# tab_infracoes_semaforo = agate.Table(base, colunas, tipos)
