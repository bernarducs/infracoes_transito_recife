from csv import reader
import re
from geopy.geocoders import GoogleV3
import agate
import cttu_funcoes

""" tab semaforos """
tipo_especifico = {'semaforo': agate.Text()}
tab_semaforo = agate.Table.from_csv('bases/semaforos.csv', column_types=tipo_especifico, delimiter=';')

""" tab infracoes """
with open('bases/relatorio-de-multas-implantadas-em-2017.csv', 'r', encoding='utf-8') as csvfile:
    data_obj = reader(csvfile, delimiter=';')
    cttu_list_obj = list(data_obj)

cabecalhos = cttu_list_obj[0]
cabecalhos.append('tipologradouro')
cabecalhos.append('logradouro')

tipos = []
for i in cabecalhos:
    tipos.append(agate.Text())

linhas = cttu_list_obj[1:]

listas = cttu_funcoes.formata_log_semaforo(linhas)
linhas_semaforo = listas[0]
linhas_log_com_numero = listas[1]
linhas_remanescentes = listas[2]

print('base:', len(linhas_log_com_numero))

""" google maps """

geolocator = GoogleV3('AIzaSyBASZ1tfUIL7XMmIGU6Ksy0zUINeSkSVRM')
linhas_google_maps = []

for linha in linhas_log_com_numero[0:2000 ]:
    local = geolocator.geocode(linha[9], exactly_one=True, timeout=5)
    if local:
        print(linha[9])
        linha.extend([local.latitude, local.longitude])
        linhas_google_maps.append(linha)

cabecalhos_google = cabecalhos
cabecalhos_google.extend(['lat', 'lng'])
tipos_google = tipos
tipos_google.extend([agate.Text(), agate.Text()])

""" agate log com numero table """
tab_log_numero = agate.Table(linhas_google_maps, cabecalhos_google, tipos_google)

tab_log_numero.to_csv('bases/tab_log_com_numeros_google.csv')

exit()
""" agate semaforo table """
tab_infracoes_semaforo = agate.Table(linhas_semaforo, cabecalhos, tipos)

joined_tab = tab_infracoes_semaforo.join(tab_semaforo, 'logradouro', 'semaforo')

joined_tab.to_csv('bases/tab_infracoes_semaforo.csv')

