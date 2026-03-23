# NAO USEI IA :)

import csv
import math


vendas_path = '/home/debian/Documents/exercicio_estatistica/clientes_vendas.csv'


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


def calc_media(lista_csv, coluna):
    valores_coluna = []
    coluna_indice = get_coluna_index(lista_csv, coluna, float)

    for linha in lista_csv[1:]:
        valor = linha[coluna_indice]
        valor = int(valor)
        valores_coluna.append(int(valor))

    n = len(valores_coluna)
    media = sum(valores_coluna) / n

    return media


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

        media = calc_media(lista_csv, header[coluna_indice[0]])

        # trocar valores invalidos por medias
        for linha in lista_csv[1:]:
            numero = linha[coluna_indice[0]]

            if numero == 0:
                numero = media
            
            linha[coluna_indice[0]] = math.floor(numero)

    return lista_csv


def calc_moda(lista_csv, coluna):
    coluna_indice = get_coluna_index(lista_csv, coluna)
    coluna_elementos = []

    for linha in lista_csv[1:]:
        coluna_elementos.append(linha[coluna_indice])
    
    frequencias = {}

    for elem in coluna_elementos:
        freq_elem = coluna_elementos.count(elem)
        frequencias[elem] = freq_elem
    
    # mais de uma moda falta
    frequencias_lista = list(frequencias.values())
    moda = max(frequencias_lista)
    
    return moda


def calc_mediana(lista_csv, coluna):
    coluna_indice = get_coluna_index(lista_csv, coluna)
    coluna_elementos = []

    for linha in lista_csv[1:]:
        coluna_elementos.append(linha[coluna_indice])
    
    coluna_elementos.sort()
    indice_meio = len(coluna_elementos) / 2

    if indice_meio % 2 != 0:
        mediana = coluna_elementos[math.floor(indice_meio)]
    else:
        val1_indice = math.floor(indice_meio)
        val2_indice = math.ceil(indice_meio)

        val1 = coluna_elementos[val1_indice]
        val2 = coluna_elementos[val2_indice]

        mediana = (val1 + val2) / 2
    
    return mediana


# Abrir dados de venda
with open(vendas_path, newline='') as csv_file:
    vendas_csv = csv.reader(csv_file, delimiter=',')

    vendas_lista = list(vendas_csv)
    vendas_lista = limpeza_str(vendas_lista, ['nome', 'estado', 'satisfacao'])
    vendas_lista = limpeza_numeros(vendas_lista, ['idade'], int)
    vendas_lista = limpeza_numeros(vendas_lista, ['tempo_resposta'], float)

    media_idade = calc_media(vendas_lista, 'idade')
    media_tempo_resposta = calc_media(vendas_lista, 'tempo_resposta')

    moda_idade = calc_moda(vendas_lista, 'idade')
    mediana_idade = calc_mediana(vendas_lista, 'idade')
    print(mediana_idade)