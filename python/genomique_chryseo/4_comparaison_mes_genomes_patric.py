import csv

path = 'Y:/chryseobacterium2/BVBRC_genome.csv'
f_patric = open(path, 'r', newline='')
records = csv.reader(f_patric, delimiter=',')

liste_patric = []
i = 0
for record in records:
    if i > 0:
        line = [record[0], record[15], record[32], "", record[68], record[65], "", record[70], record[72], "", "", "", str(record[12]+" "+record[13]), "", "", record[33], record[44], record[39], record[40], "", record[41], record[46]]
        liste_patric.append(line)
    else:
        i += 1

f_patric.close()

f_final = open('../../output/patric_restructure.csv', 'w', newline='')
writer_final = csv.writer(f_final, delimiter=';')
writer_final.writerows(liste_patric)
f_final.close()
