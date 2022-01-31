import os
from bioinfokit.analys import fastq

path = 'X:/crbtous/genomes_grimonti'
dir_list = os.listdir(path)

for genus in dir_list:
    if not(genus.endswith(".xlsx")) and genus != 'sratoolkit.2.11.3-win64':
        print(path+'TableauGrimonti.csv')
        fastq.sra_bd(file=path+'/'+'TableauGrimonti.csv', t=16, other_opts='--outdir '+path)