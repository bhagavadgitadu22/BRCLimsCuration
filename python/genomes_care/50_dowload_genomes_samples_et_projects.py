import os
from bioinfokit.analys import fastq

path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

# puis on télécharge les fatsq des projets comme dans 20
print("projets")
for genus in dir_list:
    if not(genus.endswith(".xlsx")) and genus != 'sratoolkit.2.11.3-win64':
        print(genus)
        print(path+'/'+genus+'/'+'juste_project_sra_smashed.txt')
        fastq.sra_bd(file=path+'/'+genus+'/'+'juste_project_sra_smashed.txt', t=16, other_opts='--outdir '+path+'/'+genus)

print("samples")
# puis on télécharge les fatsq des samples comme dans 20
for genus in dir_list:
    if not(genus.endswith(".xlsx")) and genus != 'sratoolkit.2.11.3-win64':
        print(genus) 
        print(path+'/'+genus+'/'+'juste_sample_sra_smashed.txt')
        fastq.sra_bd(file=path+'/'+genus+'/'+'juste_sample_sra_smashed.txt', t=16, other_opts='--outdir '+path+'/'+genus)
