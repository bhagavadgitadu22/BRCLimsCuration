import os
import pandas as pd
import csv
import numpy as np

path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

for f in dir_list:
    if f.endswith(".xlsx"):
        # créer dossier d'un genus
        genus = f.split('.')[0]
        print(genus)
        if not os.path.exists(path+'/'+genus):
            os.makedirs(path+'/'+genus)

        xlsx = pd.ExcelFile(path+'/'+f)
        sheet_names = xlsx.sheet_names  # see all sheet names
        sheet_names.remove('Working')

        for sheet_name in sheet_names:
            print(sheet_name)
            # créer dossier d'un fournisseur pour genus en cours
            if not os.path.exists(path+'/'+genus+'/'+sheet_name):
                os.makedirs(path+'/'+genus+'/'+sheet_name)

            sheet = pd.read_excel(xlsx, sheet_name)
            rows = []

            # pour chaque feuille de l'excel récupérer les infos utiles
            for i in range(3, len(sheet)):
                care_id = sheet.iloc[i, 1]
                rm_id = sheet.iloc[i, 42]
                wgs_raw = sheet.iloc[i, 27]

                if not(pd.isnull(wgs_raw) and str(wgs_raw) != 'na' and str(wgs_raw) != 'Pending'):
                    print(wgs_raw)
                    short_wgs_raw = wgs_raw.split('/')[-1].split('?')[0]
                    # wgs_assembly = sheet.iloc[i, 28]

                    row = [care_id, rm_id, wgs_raw, short_wgs_raw]
                    print(row)
                    rows.append(row)

                # sanity check on vérifie qu'au moins un id pour chaque ligne
                if pd.isnull(care_id) and pd.isnull(rm_id):
                    print(i)

            # on écrit fichier texte avec les infos utiles
            f_ids = open(path+'/'+genus+'/'+sheet_name+'/ids.csv', 'w', newline='', encoding='utf-8')
            writer = csv.writer(f_ids, delimiter='|')
            writer.writerows(rows)
            f_ids.close()
            