import csv
import agate

""" tabela com o geocode dos semaforos da cidade do recife """

tipo_especifico = {'semaforo': agate.Text()}
tab_semaforo = agate.Table.from_csv('bases/localizacao_semaforos.csv', column_types=tipo_especifico, delimiter=';')

exclude_columns = ['localizacao1', 'localizacao2',
                   'funcionamento', 'utilizacao',
                   'sinalsonoro', 'sinalizadorciclista'
                   ]

tab_semaforo_localizacao = tab_semaforo.exclude(exclude_columns)

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
with open('bases/logradouro_num_semaforo.csv', newline='', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=',')
    for row in dados_obj:
        base.append(row)

print(len(base))
exit()
tab_infracoes_semaforo = agate.Table(base, colunas, tipos)

""" juntando as tabelas """
joined_tab = tab_infracoes_semaforo.join(tab_semaforo_localizacao, 'num_semaforo', 'semaforo')

joined_tab.to_csv('bases/final/tab_infracoes_semaforos.csv')
