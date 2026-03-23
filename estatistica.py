import math

import limpeza as lmp


def calc_media(lista_csv, coluna):
    valores_coluna = []
    coluna_indice = lmp.get_coluna_index(lista_csv, coluna, float)

    for linha in lista_csv[1:]:
        valor = linha[coluna_indice]
        valor = int(valor)
        valores_coluna.append(int(valor))

    n = len(valores_coluna)
    media = sum(valores_coluna) / n

    return media


def calc_moda(lista_csv, coluna):
    coluna_indice = lmp.get_coluna_index(lista_csv, coluna)
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
    coluna_indice = lmp.get_coluna_index(lista_csv, coluna)
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


def calc_variancia(lista_csv, coluna):
    pass
