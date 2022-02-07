import os
import csv
import urllib.request

path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

for genus in dir_list:
    if not(genus.endswith(".xlsx")):
        dir_genus = os.listdir(path+'/'+genus)

        for sheet in dir_genus:
            f_ids = open(path+'/'+genus+'/'+sheet+'/'+'ids.csv', newline='')
            rows = csv.reader(f_ids, delimiter='|')
            for row in rows:
                print(row)


#fullfilename = os.path.join('X:/crbtous/genomes_care', 'SRR020192.fastq.gz')
#urllib.request.urlretrieve('ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR020/SRR020192/SRR020192.fastq.gz', fullfilename)