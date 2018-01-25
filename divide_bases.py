import csv
import funcoes

with open('bases/relatorio-de-multas-implantadas-em-2017.csv', 'r', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=';')
    base = list(dados_obj)

colunas = base[0]
colunas.insert(0, 'id')

with open('bases/bases_tratadas/colunas.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(colunas)

linhas = base[1:]

for i, row in enumerate(linhas):
    row.insert(0, i)

base_apos_regex = funcoes.formata_endereco(linhas)

for key, value in base_apos_regex.items():
    with open('bases/bases_tratadas/' + str(key) + '.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerows(value[:])