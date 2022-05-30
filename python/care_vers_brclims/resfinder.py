import urllib.request
import os
import pandas as pd

lines = []
link = "https://bitbucket.org/genomicepidemiology/resfinder_db/raw/fa32d9a3cf0c12ec70ca4e90c45c0d590ee810bd/phenotypes.txt"
with urllib.request.urlopen(link) as url:
    s = str(url.read())
    # I'm guessing this would output the html source code ?
    genes_rb = []
    classes_rb = []
    for elmt in s.split('\\n'):
        if '\\t' in elmt:
            genes_rb.append(elmt.split('\\t')[0].split('_')[0])
            classes_rb.append(elmt.split('\\t')[1])
        else:
            print(elmt)

genes_rb.append('mcr-1')
classes_rb.append('Polymyxin')

if len(genes_rb) != len(classes_rb):
    print("trouble!")

path = 'C:/Users/mboutrou/Documents/TR _AMR_database_pour_CARE'
dir_list = os.listdir(path)

genus_par_classe = {}
for f in dir_list:
    genus = f.split('.')[0]
    print(genus)
    genes_genus = []

    xlsx = pd.ExcelFile(path+'/'+f)
    sheet_names = xlsx.sheet_names  # see all sheet names

    # je lis les feuilles de l'excel en cours une à une
    for sheet_name in sheet_names:
        sheet = pd.read_excel(xlsx, sheet_name)
        
        # on récupère les numéros des 3 colonnes d'intérêt
        col_care = -1
        for col in range(len(sheet.columns)):
            if sheet.columns[col] == 'Genotype':
                col_care = col
        
        if col_care != -1:
            # pour chaque ligne de données je récupère l'identifiant intéressant (care ou rm) et le numéro wgs
            for i in range(1, len(sheet)):
                care_id = sheet.iloc[i, col_care]
                genes = care_id.split(', ')

                for gene in genes:
                    gene = gene.replace('oqx', 'Oqx')
                    if gene not in genes_genus:
                        genes_genus.append(gene)

    genus_par_classe[genus] = {}
    for gene in genes_genus:
        if gene in genes_rb:
            idx = genes_rb.index(gene)
            classe = classes_rb[idx]

            if classe not in genus_par_classe[genus]:
                genus_par_classe[genus][classe] = 0
            genus_par_classe[genus][classe] += 1
        else:
            print(gene)
