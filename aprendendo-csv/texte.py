import csv

with open('aprendendo-csv/test.csv', 'w', encoding='utf-8') as arquivo:
    escrevercsv = csv.writer(arquivo)
    escrevercsv.writerow('sdasdasdasdasd')


