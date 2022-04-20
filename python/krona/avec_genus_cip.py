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
for record in genus_cip:
    genus = record[1].replace("'", '').replace('"', '')

    found = False
    for elmt in genus_complete:
        if elmt[0] == genus:
            found = True
            break

    if not(found):
        if genus not in ex:
            ex.append(genus)

for e in ex:
    print(e)

#list(reversed(line_genus)
