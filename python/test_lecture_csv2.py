import csv

f = open('../../output/souches_cpc.csv', 'r', newline='')
records = csv.reader(f, delimiter=';')
ids = [record[0] for record in records]
f.close()

chaine = '('
for id in ids:
    if chaine != '(':
        chaine += ','
    chaine += "'"+str(id)+"'"
chaine += ')'

print(chaine)
