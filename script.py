# NAO USEI IA :)

import csv

import limpeza as lmp
import estatistica as est

vendas_path = '/home/debian/Documents/exercicio_estatistica/clientes_vendas.csv'


# Abrir dados de venda
with open(vendas_path, newline='') as csv_file:
    vendas_csv = csv.reader(csv_file, delimiter=',')

    vendas_lista = list(vendas_csv)
    vendas_lista = lmp.limpeza_str(vendas_lista, ['nome', 'estado', 'satisfacao'])
    vendas_lista = lmp.limpeza_numeros(vendas_lista, ['idade'], int)
    vendas_lista = lmp.limpeza_numeros(vendas_lista, ['tempo_resposta'], float)

    media_idade = est.calc_media(vendas_lista, 'idade')
    media_tempo_resposta = est.calc_media(vendas_lista, 'tempo_resposta')

    moda_idade = est.calc_moda(vendas_lista, 'idade')
    mediana_idade = est.calc_mediana(vendas_lista, 'idade')
    print(mediana_idade)