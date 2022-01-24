import os
from bioinfokit.analys import fastq
import csv
import requests
import json

path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

# on récupère les errs des projets
for genus in dir_list:
    if not(genus.endswith(".xlsx")) and genus != 'sratoolkit.2.11.3-win64' and genus != '.DS_Store':
        samples_ids = open(path+'/'+genus+'/juste_sample_sra.txt', 'r', newline='', encoding='utf-8')
        csvreader = csv.reader(samples_ids)
        rows = []
        for row in csvreader:
            if row[0] not in rows:
                rows.append(row[0])

        errs = []
        for row in rows:
            url = requests.get('https://www.ebi.ac.uk/ena/portal/api/filereport?result=read_run&fields=fastq_ftp&format=JSON&accession='+row)
            text = url.text
            data = json.loads(text)

            for elmt in data:
                errs.append([elmt['run_accession']])

        if len(errs) > 0:
            print(genus)

        f_ids = open(path+'/'+genus+'/juste_sample_sra_smashed.txt', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_ids, delimiter='|')
        writer.writerows(errs)
        f_ids.close()