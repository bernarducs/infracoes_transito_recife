import csv
import agate
from geopy.geocoders import GoogleV3

""" tabela com infracoes tendo o número do semaforo como logradouro """

colunas = []
with open('bases/colunas.csv', newline='', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=',')
    for row in dados_obj:
        for i in row:
            colunas.append(i)

colunas.extend(['tipo_logradouro', 'logradouro'])

tipos = []
for i in range(len(colunas)):
    tipos.append(agate.Text())

base = []
with open('bases/logradouro_aproximado.csv', newline='', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=',')
    for row in dados_obj:
        base.append(row)

""" google maps """

geolocator = GoogleV3('AIzaSyBASZ1tfUIL7XMmIGU6Ksy0zUINeSkSVRM')

linhas_google_maps = []

with open('bases/final/tab_infracoes_sobras.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in base[0:2450]:
        local = geolocator.geocode(row[9], exactly_one=True, timeout=5)
        if local:
            row.extend([local.latitude, local.longitude])
            linhas_google_maps.append(row)
            print(row)
            writer.writerow(row)


