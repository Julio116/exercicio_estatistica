import math

import estatistica as est

def get_colunas_indexes(header, colunas, tipo_num=None):
    """achar as posicoes das colunas desejadas no header"""
    colunas_indices = {}

    for coluna in colunas:
        colunas_indices[coluna] = (header.index(coluna), tipo_num)

    return colunas_indices


def get_coluna_index(lista_csv, coluna, tipo_num=None):
    header = lista_csv[0]
    colunas_indice = get_colunas_indexes(header, [coluna], tipo_num)

    coluna_indice = list(colunas_indice.values())
    coluna_indice = coluna_indice.pop()
    coluna_indice = coluna_indice[0]

    return coluna_indice


def limpeza_str(lista_csv, colunas):
    """Higienizar as colunas do tipo string"""
    header = lista_csv[0]
    colunas_indices = get_colunas_indexes(header, colunas)
    
    # lowercase nas colunas desejadas
    for linha in lista_csv[1:]:
        for coluna_str in colunas:
            coluna_index = colunas_indices[coluna_str][0]
            linha[coluna_index] = linha[coluna_index].lower()
    
    return lista_csv


def limpeza_numeros(lista_csv, colunas, tipo_num):
    """Higienizar as colunas numericas"""
    header = lista_csv[0]
    colunas_indices = get_colunas_indexes(header, colunas, tipo_num)

    for coluna_indice in colunas_indices.values():
        num_linha = 1

        for linha in lista_csv[1:]:
            numero = linha[coluna_indice[0]]

            if numero == '':
                linha[coluna_indice[0]] = '0'
                numero = linha[coluna_indice[0]]
            
            if type(numero) == str:
                caracteres_invalidos = ['-']

                for char in caracteres_invalidos:
                    if char in numero:
                        linha[coluna_indice[0]] = '0'
                        numero = linha[coluna_indice[0]]

                # trocando , por . nos numeros float
                if ',' in numero or '.' in numero:
                    numero = numero.replace(',', '.')
                    linha[coluna_indice[0]] = float(numero)
                else:
                    if coluna_indice[1] == float:
                        linha[coluna_indice[0]] = float(numero)
                    elif coluna_indice[1] == int:
                        linha[coluna_indice[0]] = int(numero)
            lista_csv[num_linha] = linha
            num_linha += 1

        media = est.calc_media(lista_csv, header[coluna_indice[0]])

        # trocar valores invalidos por medias
        for linha in lista_csv[1:]:
            numero = linha[coluna_indice[0]]

            if numero == 0:
                numero = media
            
            linha[coluna_indice[0]] = math.floor(numero)

    return lista_csv