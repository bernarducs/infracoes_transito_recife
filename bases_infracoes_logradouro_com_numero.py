import csv
import agate
from geopy.geocoders import Bing
from funcoes import retorna_ultima_linha_gravada

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

""" recupera a ultima linha salva """

ult_linha = retorna_ultima_linha_gravada('tab_infracoes_log_com_numero')

""" google \ bing maps """

geolocator = Bing('token')

linhas_google_maps = []

with open('bases/bases_finalizadas/tab_infracoes_log_com_numero.csv', 'a', newline='\n') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in base[ult_linha:]:
        local = geolocator.geocode(row[10], exactly_one=True, timeout=10)
        if local:
            row.extend([local.latitude, local.longitude])
            linhas_google_maps.append(row)
            print(row)
            writer.writerow(row)
