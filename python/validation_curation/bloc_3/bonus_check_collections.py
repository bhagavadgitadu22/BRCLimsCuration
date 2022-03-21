import csv 

f_vides = open('../../output/colls_utiles.csv', 'r', newline='')
records = csv.reader(f_vides, delimiter=';')

str = ""
for record in records:
    str += '|'+record[0]

print(str)
f_vides.close()