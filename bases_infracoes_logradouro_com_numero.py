import csv
import agate
from geopy.geocoders import Bing

""" tabela com infracoes tendo os endereços com numeros """

colunas = []
with open('bases/bases_tratadas/colunas.csv', newline='', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=',')
    for row in dados_obj:
        for i in row:
            colunas.append(i)

colunas.extend(['tipo_logradouro', 'logradouro'])

tipos = []
for i in range(len(colunas)):
    tipos.append(agate.Text())

base = []
with open('bases/bases_tratadas/logradouro_com_numero.csv', newline='', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=',')
    for row in dados_obj:
        base.append(row)

""" google\bing maps """

geolocator = Bing('token')

linhas_google_maps = []

with open('bases/bases_finalizadas/tab_infracoes_log_com_numero.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in base[0:9500]:
        local = geolocator.geocode(row[10], exactly_one=True, timeout=5)
        if local:
            row.extend([local.latitude, local.longitude])
            linhas_google_maps.append(row)
            print(row)
            writer.writerow(row)
