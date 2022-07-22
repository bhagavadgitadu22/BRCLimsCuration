import csv

def pays(str):
    if str == 'TWN':
        return 'Taiwan'
    if str == 'FRA':
        return 'France'
    if str == 'DEU':
        return 'Germany'
    if str == 'ISR':
        return 'Israel'
    if str == 'CHN':
        return 'China'
    if str == 'GBR':
        return 'UK'
    if str == 'ESP':
        return 'Spain'
    if str == 'ZAF':
        return 'South Africa'
    if str == 'SVN':
        return 'Slovenia'
    if str == 'IND':
        return 'India'
    if str == 'ATA':
        return 'Antarctica'
    if str == 'CHE':
        return 'Switzerland'
    if str == 'CHL':
        return 'Chile'
    if str == 'DZA':
        return 'Algeria'
    if str == 'GUY':
        return 'Guyana'
    if str == 'HUN':
        return 'Hungary'
    if str == 'JPN':
        return 'Japan'
    if str == 'PRT':
        return 'Portugal'
    if str == 'KOR':
        return 'South Korea'

path = 'Y:/chryseobacterium2/33_souches_types_avec_fastas.csv'
f_fastas = open(path, 'r', newline='')
records = csv.reader(f_fastas, delimiter=',')

liste_fastas = []
for record in records:
    line = [record[i] for i in range(len(record))]
    liste_fastas.append(line)

f_fastas.close()

path2 = 'Y:/chryseobacterium2/chryseo_infos.csv'
f_bacdive = open(path2, 'r', newline='')
records2 = csv.reader(f_bacdive, delimiter=',')

liste_bacdive = []
i = 0
for record2 in records2:
    if i > 0:
        if record2[0] != "":
            line = [record2[i] for i in range(len(record2))]
            line.append("")
            line.append("")
            liste_bacdive.append(line)
    else:
        i += 1

path3 = 'Y:/chryseobacterium2/chryseo_genomes.csv'
f_bacdive_genomes = open(path3, 'r', newline='')
records3 = csv.reader(f_bacdive_genomes, delimiter=',')

current_line = []
for record3 in records3:
    if record3[0] != "":
       for line in liste_bacdive:
            if line[0] == record3[0]:
                current_line = line

    if current_line != []:
        if current_line[10] == "":
            current_line[10] = record3[7]
            current_line[11] = record3[8].replace('GCA', 'GCF')
        else:
            current_line[10] = current_line[10]+", "+record3[7]
            current_line[11] = current_line[11]+", "+record3[8].replace('GCA', 'GCF')
    else:
        print(record3)

f_bacdive_genomes.close()

solutions = []
solutions_infos = []
not_found = []
compteur = 0
for fasta in liste_fastas: 
    bool = False

    for line in liste_bacdive:
        nums = line[11].split(', ')  
        for num in nums:
            if num != '' and num in fasta[0]:
                sol = [line[2], fasta[0]+'.fna']
                solutions.append(sol)
                sol_i = [line[1], line[2], "", line[9], "", pays(line[7]), line[8], "", "", "", line[6], "", "", "yes"]
                solutions_infos.append(sol_i)
                bool = True

    if not(bool):
        not_found.append(fasta)
        compteur += 1

print(compteur)

f_final = open('../../output/infos_bigsdb_fastas.csv', 'w', newline='')
writer_final = csv.writer(f_final, delimiter=';')
writer_final.writerows(solutions)
f_final.close()

f_final2 = open('../../output/infos_bigsdb_infos.csv', 'w', newline='')
writer_final2 = csv.writer(f_final2, delimiter=';')
writer_final2.writerows(solutions_infos)
f_final2.close()

f_final3 = open('../../output/infos_bigsdb_not_found.csv', 'w', newline='')
writer_final2 = csv.writer(f_final3, delimiter=';')
writer_final2.writerows(not_found)
f_final3.close()
