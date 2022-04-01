import os
import csv
import requests

#path = '/mnt/gaia/crbip/crbtous/genomes_care'
path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

for genus in dir_list:
    # on parcourt les dossiers de genus créés
    #if not(genus.endswith(".xlsx")) and genus != 'sratoolkit.2.11.3-win64' and genus != '.DS_Store' and genus != 'Staphylococcus2':
    if genus == 'Escherichia':
        # à chaque fois on lit la listes d'errs pour ce genus
        f = open(path+'/'+genus+'/'+'ids.csv', 'r', newline='')
        rows = csv.reader(f)
        for row in rows:
            genome = row[0].split(';')[-1]
            print(genome)

            # pour chaque err on récupère les liens ftp des fichiers fasta avec le site de l'ena
            url = 'https://www.ebi.ac.uk/ena/portal/api/filereport?accession='+genome+'&result=read_run&fields=fastq_ftp'
            r = requests.get(url, stream=True)
            print(url)
            print(str(r.content))
            ftp = str(r.content).split('\\n')[1].split('\\t')[1]

            ftp1 = ftp.split(';')[0]
            name_ftp1 = ftp1.split('/')[-1]
            ftp2 = ftp.split(';')[1]
            name_ftp2 = ftp2.split('/')[-1]

            # puis on utilise ces liens pour télécharger les deux fichiers fasta associés à chaque err
            fastq1 = requests.get('http://'+ftp1, stream=True)
            with open(path+'/'+genus+'/'+name_ftp1, 'wb') as f1:
                for chunk in fastq1.raw.stream(1024, decode_content=False):
                    if chunk:
                        f1.write(chunk)

            fastq2 = requests.get('http://'+ftp2, stream=True)
            with open(path+'/'+genus+'/'+name_ftp2, 'wb') as f2:
                for chunk in fastq2.raw.stream(1024, decode_content=False):
                    if chunk:
                        f2.write(chunk)
