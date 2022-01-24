import os
import pandas as pd
import csv
import requests
import json

path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

total_fake = 0
for f in dir_list:
    if '~$' not in f and f.endswith(".xlsx") and f != "final_ids.xlsx" and f != "Staphylococcus2.xlsx":
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
        requetes = []

        for sheet_name in sheet_names:
            print(sheet_name)

            sheet = pd.read_excel(xlsx, sheet_name)
            
            # on récupère numéros des 3 colonnes d'intérêt
            col_care = -1
            col_rm = -1
            col_wgs = -1
            for col in range(len(sheet.columns)):
                if sheet.iloc[2, col] == 'CARE ID':
                    col_care = col
                if sheet.iloc[2, col] == 'Provider RM ID':
                    col_rm = col
                if sheet.iloc[2, col] == 'WGS sequencing data raw reads':
                    col_wgs = col
            if col_care == -1 or col_rm == -1 or col_wgs == -1:
                print('trouble')

            for i in range(3, len(sheet)):
                care_id = sheet.iloc[i, col_care]
                rm_id = sheet.iloc[i, col_rm]
                wgs_raw = sheet.iloc[i, col_wgs]

                if not(pd.isnull(wgs_raw)) and str(wgs_raw) != 'na' and str(wgs_raw) != 'Pending':
                    short_wgs_raw = wgs_raw.replace('?term=', '').strip('/').split('/')[-1].split('?')[0].split('\n')[0].split('[')[0]
                    
                    row = [str(rm_id), care_id, short_wgs_raw]

                    if short_wgs_raw not in requetes:
                        if "ERS" in short_wgs_raw or "PRJEB" in short_wgs_raw or "ERX" in short_wgs_raw:
                            url = requests.get('https://www.ebi.ac.uk/ena/portal/api/filereport?result=read_run&fields=fastq_ftp&format=JSON&accession='+short_wgs_raw)
                            text = url.text
                            data = json.loads(text)

                            for elmt in data:
                                row2 = row
                                row2.append(elmt['run_accession'])
                                true_rows.append(row)
                        else:
                            row2 = row
                            row2.append(short_wgs_raw)
                            true_rows.append(row)
                
                else:
                    row = [care_id, rm_id, wgs_raw]
                    fake_rows.append(row)
        
        # on écrit fichier texte avec les infos utiles
        f_ids = open(path+'/'+genus+'/ids.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_ids, delimiter=';')
        writer.writerows(true_rows)
        f_ids.close()

        f_ids = open(path+'/'+genus+'/juste_sra.txt', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_ids, delimiter=';')
        writer.writerows([[elmt[3]] for elmt in true_rows])
        f_ids.close()

        f_fake_ids = open(path+'/'+genus+'/fake_ids.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_fake_ids, delimiter=';')
        writer.writerows(fake_rows)
        f_fake_ids.close()

        total_fake += len(fake_rows)

print(total_fake)
        