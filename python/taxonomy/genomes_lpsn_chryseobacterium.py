import lpsn
import csv
import urllib.request

client = lpsn.LpsnClient('martin.boutroux@pasteur.fr', 'hercule1821')

# the prepare method fetches all LPSN-IDs matching your query
# and returns the number of IDs found
count = client.search(taxon_name='Chryseobacterium', correct_name='yes')
print(count, 'entries found.')

# the retrieve method lets you iterate over all results
# and returns the full entry as dict
# Entries can be further filtered using a list of keys (e.g. ['keywords'])
strains_ids = []
for entry in client.retrieve():
    if "type_strain_names" in entry:
        for elmt in entry["type_strain_names"]:
            strains_ids.append(elmt)
    else:
        print(entry["full_name"])

path = "Y:/chryseobacterium/prokaryotes.csv"
f = open(path, 'r', newline='')
records = csv.reader(f, delimiter=',')

no = 0
yes = 0
for record in records:
    if record[2] in strains_ids:
        yes += 1

        print(record[-2])

        complement = record[-2].split('/')[-1]
        link = record[-2]+'/'+complement+'_genomic.fna.gz'
        urllib.request.urlretrieve(link, complement+'_genomic.fna.gz')
    else:
        no += 1

print("yes: " + str(yes))
print("no: " + str(no))
