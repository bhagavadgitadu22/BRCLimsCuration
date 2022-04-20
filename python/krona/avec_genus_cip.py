import csv

f = open('C:/Users/mboutrou/Documents/output/genus_cip.csv', 'r', newline='')
records_cip = csv.reader(f, delimiter=';')
genus_cip = [record for record in records_cip]
f.close()

f2 = open('C:/Users/mboutrou/Documents/output/genus_complete.csv', 'r', newline='')
records_complete = csv.reader(f2, delimiter=';')
genus_complete = [record for record in records_complete]
f2.close()

ex = []
lines = []
for record in genus_cip:
    genus = record[1].replace("'", '').replace('"', '')

    found = False
    for elmt in genus_complete:
        if elmt[0] == genus:
            line = [record[0]]
            for x in list(reversed(elmt)):
                line.append(x)
            line.append(record[2])
            line.append(record[3])
            
            lines.append(line)
            found = True
            break

    if not(found):
        if genus not in ex:
            ex.append(genus)

for e in ex:
    print(e)

f = open('C:/Users/mboutrou/Documents/output/bilan_genus.csv', 'w', newline='')
writer = csv.writer(f, delimiter=';')
writer.writerows(lines)
f.close()
