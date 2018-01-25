import re

def formata_endereco(linhas):

    linhas_semaforo = []
    linhas_log_com_numero = []
    linhas_log_remanescentes = []

    regex_semaforo = r'\s(SEMAF[A-Z]+)[\,\s\.\:A-Z0]+([1-9\d]+)'
    regex_log_remanescentes = r'(.+,)\s+(?:APOS|LADO OPOSTO|[A-Z\s]+LADO|EM FRENTE)?(?:[A-Z\s]+PUBLICA)?(?:[A-Z\s]+SENTIDO)?(.+)'
    regex_log_com_numero = r'(.*?),[A-Za-z\s\.\º]+(\b\d{1,4})'

    for linha in linhas:
        logradouro = linha[8]
        busca = re.search(regex_semaforo, logradouro)
        if busca:
            linha.append('semaforo')
            linha.extend([busca.group(2)])
            linhas_semaforo.append(linha)
        else:
            busca = re.search(regex_log_com_numero, logradouro)
            if busca:
                linha.append('logradouro_com_numero')
                linha.extend([busca.group(1) + ', ' + busca.group(2) + ', RECIFE'])
                linhas_log_com_numero.append(linha)
            else:
                busca = re.search(regex_log_remanescentes, logradouro)
                if busca:
                    linha.append('logradouro_aproximado')
                    linha.extend([busca.group(1) + busca.group(2) + ', RECIFE'])
                    linhas_log_remanescentes.append(linha)
                else:
                    linha.append('logradouro_aproximado')
                    linha.append(logradouro + ', RECIFE')
                    linhas_log_remanescentes.append(linha)

    dict = {
            'logradouro_num_semaforo': linhas_semaforo,
            'logradouro_com_numero': linhas_log_com_numero,
            'logradouro_aproximado': linhas_log_remanescentes
    }

    return dict