import csv

# dois
f = open('../../output/dois_recuperees_11_2021.csv', 'r', newline='')
references = [line.split('|') for line in f]

nouvelles_lignes = []
for ref in references:
    ids = [elmt.strip("'") for elmt in ref[5].strip('][').split(', ')]
    lignes = [int(elmt) for elmt in ref[6].replace('\r\n', '').strip('][').split(', ')]
    biblio = ref[4]

    nombre_elmts = len(ids)
    i = 0
    while i < nombre_elmts:
        nouvelles_lignes.append([ids[i], lignes[i], ref[0]+", "+ref[1]+", "+ref[2]+", "+ref[3]+", doi:"+biblio])
        i += 1


# pmids
f2 = open('../../output/solutions_pubmed.csv', 'r', newline='')
references2 = [line.split('|') for line in f2]

finit = open('../../output/dois_echouees_11_2021.csv', 'r', newline='')
referencesinit = [line.split('|') for line in finit]

for ref in references2:
    if len(ref) > 5 and ref[6].replace('\r\n', '') != 'NOT_FOUND' and 'AMBIGUOUS' not in ref[6].replace('\r\n', ''):

        ids = []
        lignes = []
        for refinit in referencesinit:
            if ref[0:4] == refinit[0:4]:
                ids = [elmt.strip("'") for elmt in refinit[4].strip('][').split(', ')]
                lignes = [int(elmt) for elmt in refinit[5].replace('\r\n', '').strip('][').split(', ')]

        biblio = ref[6].replace('\r\n', '')

        nombre_elmts = len(ids)
        i = 0
        while i < nombre_elmts:
            nouvelles_lignes.append([ids[i], lignes[i], ref[0]+", "+ref[1]+", "+ref[2]+", "+ref[3]+", pmid:"+biblio])
            i += 1

# ecriture du fichier
f3 = open('../../output/dois_en_mode_eclate.csv', 'w', newline='')
writer = csv.writer(f3, delimiter='|')

# write the rows to the csv file
writer.writerows(nouvelles_lignes)

# close the file
f.close()
f2.close()
finit.close()
f3.close()
