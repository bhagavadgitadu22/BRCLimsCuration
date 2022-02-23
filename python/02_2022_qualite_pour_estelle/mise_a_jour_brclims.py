import csv

f_avec_numero = open('../../output/qualite_avec_numero.csv', 'r', newline='', encoding="latin-1")
rows_avec_numero = csv.reader(f_avec_numero, delimiter=';')

f_sans_numero = open('../../output/qualite_sans_numero.csv', 'r', newline='', encoding="latin-1")
rows_sans_numero = csv.reader(f_sans_numero, delimiter=';')

for row in rows_avec_numero:
    print(row)

for row in rows_sans_numero:
    print(row)