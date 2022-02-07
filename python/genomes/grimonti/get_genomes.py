import requests
import csv

#path = 'X:/crbtous/genomes_grimonti'
path = '/mnt/gaia/crbip/crbtous/genomes_grimonti'

f_ids = open(path+'/'+'TableauGrimonti.csv', 'r', newline='', encoding='utf-8')
csvreader = csv.reader(f_ids, delimiter=';')

for row in csvreader:
    genome = row[0]

    if '.' not in genome:
        genome = genome+'000000.1'
        print(genome)
    
        url = 'https://www.ebi.ac.uk/ena/browser/api/fasta/'+genome

        r = requests.get(url, stream=True)
        with open(path+'/'+genome+'.gzip', 'wb') as f:
            for chunk in r.raw.stream(1024, decode_content=False):
                if chunk:
                    f.write(chunk)
