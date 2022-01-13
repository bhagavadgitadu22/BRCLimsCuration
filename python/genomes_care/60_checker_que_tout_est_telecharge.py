import os
import csv

def read_csv(ids, expected_errs):
    csvreader = csv.reader(ids)
    for row in csvreader:
        err = row[0]
        if err not in expected_errs:
            expected_errs.append(err)
    return expected_errs

#path = 'X:/crbtous/genomes_care'
path = '/mnt/gaia/crbip/crbtous/genomes_care'
dir_list = os.listdir(path)

# puis on lit les fichiers des différents dossiers pour voir si on a tout téléchargé
for genus in dir_list:
    if not(genus.endswith(".xlsx")) and genus != 'sratoolkit.2.11.3-win64':
        print("")
        print("")
        print(genus)
        print("")

        # on récupère liste de tous errs dont on a fasta pour ce génome
        local_files = os.listdir(path+'/'+genus)
        local_errs =  []
        for file in local_files:
            if not(file.endswith(".csv")) and not(file.endswith(".txt")):
                err = file.split(".")[0].split("_")[0]
                if err not in local_errs:
                    local_errs.append(err)

        # on récupère liste des errs qu'on voulait télécharger
        ids = open(path+'/'+genus+'/juste_sra.txt', 'r', newline='', encoding='utf-8')
        projects_ids = open(path+'/'+genus+'/juste_project_sra_smashed.txt', 'r', newline='', encoding='utf-8')
        samples_ids = open(path+'/'+genus+'/juste_sample_sra_smashed.txt', 'r', newline='', encoding='utf-8')

        expected_errs = read_csv(ids, [])
        expected_errs = read_csv(projects_ids, expected_errs)
        expected_errs = read_csv(samples_ids, expected_errs)
        
        # on compare les deux listes
        print("not downloaded")
        for err in expected_errs:
            if err not in local_errs:
                print(err)
            
        print("")
        print("downloaded")
        for err in expected_errs:
            if err in local_errs:
                print(err)

        for err in local_errs:
            if err not in expected_errs:
                print('ca c\'est vraiment bizarre : '+err)
