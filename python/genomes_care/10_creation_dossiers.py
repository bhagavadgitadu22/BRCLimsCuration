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

        true_rows = []
        fake_rows = []

        for sheet_name in sheet_names:
            print(sheet_name)

            sheet = pd.read_excel(xlsx, sheet_name)

            # pour chaque feuille de l'excel récupérer les infos utiles
            for i in range(3, len(sheet)):
                care_id = sheet.iloc[i, 1]
                rm_id = sheet.iloc[i, 42]
                wgs_raw = sheet.iloc[i, 27]

                if not(pd.isnull(wgs_raw)) and str(wgs_raw) != 'na' and str(wgs_raw) != 'Pending':
                    short_wgs_raw = wgs_raw.replace('?term=', '').strip('/').split('/')[-1].split('?')[0].split('\n')[0].split('[')[0]
                    
                    row = [rm_id, short_wgs_raw]
                    if not(pd.isnull(care_id)):
                        row[0] = care_id
                    true_rows.append(row)
                
                else:
                    row = [care_id, rm_id, wgs_raw]
                    fake_rows.append(row)

        # on écrit fichier texte avec les infos utiles
        f_ids = open(path+'/'+genus+'/ids.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_ids, delimiter='|')
        writer.writerows(true_rows)
        f_ids.close()

        f_ids = open(path+'/'+genus+'/juste_sra.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_ids, delimiter='|')
        writer.writerows([[elmt[1]] for elmt in true_rows])
        f_ids.close()

        f_fake_ids = open(path+'/'+genus+'/fake_ids.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_fake_ids, delimiter='|')
        writer.writerows(fake_rows)
        f_fake_ids.close()
            