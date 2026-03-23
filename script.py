import csv
import math

import matplotlib.pyplot as plt
import numpy as np

import limpeza as lmp
import estatistica as est


vendas_path = '/home/debian/Documents/exercicio_estatistica/clientes_vendas.csv'
aeroporto_path = '/home/debian/Documents/exercicio_estatistica/dados_aeroporto.csv'


# abrir dados de venda
with open(vendas_path, newline='') as csv_file:
    vendas_csv = csv.reader(csv_file, delimiter=',')

    vendas_lista = list(vendas_csv)
    vendas_lista = lmp.limpeza_str(vendas_lista, ['nome', 'estado', 'satisfacao'])
    vendas_lista = lmp.limpeza_numeros(vendas_lista, ['idade'], int)
    vendas_lista = lmp.limpeza_numeros(vendas_lista, ['tempo_resposta'], float)

    media_tempo_resposta = est.calc_media(vendas_lista, 'tempo_resposta')
    moda_tempo_resposta = est.calc_moda(vendas_lista, 'tempo_resposta')
    mediana_tempo_resposta = est.calc_mediana(vendas_lista, 'tempo_resposta')
    variancia_tempo_resposta = est.calc_variancia(vendas_lista, 'tempo_resposta')
    desvio_padrao_tempo_resposta = math.sqrt(variancia_tempo_resposta)


    coluna_tempos_resposta = []
    col_indice_tempos = lmp.get_coluna_index(vendas_lista, 'tempo_resposta')

    for linha in vendas_lista[1:]:
        coluna_tempos_resposta.append(linha[col_indice_tempos])
    
    tempos = np.array(coluna_tempos_resposta)
    q1 = np.percentile(tempos, 25)
    q3 = np.percentile(tempos, 75)
    iqr = q3 - q1

    print('Media: ', media_tempo_resposta)
    print('Mediana: ', mediana_tempo_resposta)
    print('Moda: ', moda_tempo_resposta)
    print('Desvio: ', desvio_padrao_tempo_resposta)
    print('Variancia: ', variancia_tempo_resposta)
    print('IQR: ', iqr)

    # plotar os dados
    plt.hist(tempos, bins=6)
    plt.title('Histograma de tempos resposta')
    plt.xlabel('Valores')
    plt.ylabel('Frequencia')
    plt.show()


    plt.boxplot(tempos)
    plt.title('Boxplot de tempos resposta')
    plt.ylabel('Valores')
    plt.show()


# abrir dados do aeroporto
with open(aeroporto_path, newline='') as csv_file:
    aeroporto_csv = csv.reader(csv_file, delimiter=',')

    aeroporto_lista = list(aeroporto_csv)
    aeroporto_lista = lmp.limpeza_str(aeroporto_lista,
        ['passageiro', 'voo', 'companhia', 'origem', 'destino', 'status', 'portao'])
    
    # for l in aeroporto_lista:
    #     print(l)