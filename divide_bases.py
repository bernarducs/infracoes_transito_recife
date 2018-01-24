import csv
import funcoes

with open('bases/relatorio-de-multas-implantadas-em-2017.csv', 'r', encoding='utf-8') as csvfile:
    dados_obj = csv.reader(csvfile, delimiter=';')
    base = list(dados_obj)

colunas = base[0]

with open('bases/colunas.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(colunas)

linhas = base[1:]

base_apos_regex = funcoes.formata_endereco(linhas)

for key, value in base_apos_regex.items():
    with open('bases/' + str(key) + '.csv', 'w', encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(value[:])


