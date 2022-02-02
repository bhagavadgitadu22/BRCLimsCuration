import os
from bioinfokit.analys import fastq

#path = '/mnt/gaia/crbip/crbtous/genomes_care'
path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

for genus in dir_list:
    if genus == "Salmonella":
        print(path+'/'+genus+'/'+'missing.csv')
        fastq.sra_bd(file=path+'/'+genus+'/'+'missing.csv', t=16, other_opts='--outdir '+path+'/'+genus)