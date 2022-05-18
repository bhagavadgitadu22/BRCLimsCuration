from ete3 import NCBITaxa
import csv

ncbi = NCBITaxa()
# ncbi.update_taxonomy_database()

f = open('krona_and_map/krona/taxonomy_crbip.csv', 'r', newline='')
records_cip = csv.reader(f, delimiter=',', quotechar='"')
all_genus = [record[1] for record in records_cip]

taxIds = ncbi.get_name_translator(all_genus)

for record in records_cip:
    nombre = record[0]
    genus = record[1]
    species = record[2]
    subspecies = record[3]

    if genus not in taxId:
        print(genus)
    else:
        taxId = taxIds(genus)

f.close()
