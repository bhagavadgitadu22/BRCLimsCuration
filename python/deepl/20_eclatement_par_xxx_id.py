import csv

f = open('../../output/isole_a_partir_de_traduits_sans_erreurs.csv', 'r', newline='')
isolats = [line.split('|') for line in f]

traduits_eclates = []

for isolat in isolats:
    ids = isolat[3].replace('\n', '').replace('{', '').replace('}', '').split(",")

    for id in ids:
        elmt = [isolat[0], isolat[1], id]
        traduits_eclates.append(elmt)

f2 = open('../../output/isole_a_partir_de_traduits_eclates.csv', 'w', newline='')
writer2 = csv.writer(f2, delimiter='|', lineterminator='\n')
writer2.writerows(traduits_eclates)
