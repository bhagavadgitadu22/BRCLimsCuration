import pandas as pd
import os

xls_milieux = pd.ExcelFile('../../output/all_infos_p2m_crossed.xlsx')
df = pd.read_excel(xls_milieux, 'all_complete')

local_path = '/mnt/gaia/cip'
path = local_path+'/CONTROLE_SOUCHE'
dir_list = os.listdir(path)

short_list_files = [file_id.replace("CIP", '').replace("CRBIP", '').replace("_", '').replace("-", '').replace(".", '').replace(" ", '').replace("T", '') for file_id in dir_list]
print(len(short_list_files))

print("start of search")
df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    if bool(row[4]) and bool(row[5]):
        id_cip = row[0].replace("CIP", '').replace("CRBIP", '').replace("_", '').replace("-", '').replace(".", '').replace(" ", '').replace("T", '')
        lot_cip = str(row[1]).replace("_", '').replace("-", '').replace(".", '').replace(" ", '')

        dir_id = ''
        dir_lot = ''
        dir_fasta = ''
        for short_file_id in short_list_files:
            if short_file_id == id_cip and os.path.isdir(os.path.join(path, short_file_id)):
                dir_id = os.path.join(path, short_file_id)

                # on regarde s'il y a un dossier pour le lot à l'intérieur
                id_list = os.listdir(dir_id)
                for lot_dir in id_list:
                    if lot_dir == short_file_id+'-'+lot_cip and os.path.isdir(os.path.join(dir_id, lot_dir)):
                        dir_lot = os.path.join(dir_id, lot_dir)

                        # on regarde s'il y a un dossier pour le type de fasta à l'intérieur
                        lot_list = os.listdir(dir_lot)
                        for fasta_dir in lot_list:
                            if fasta_dir == row[2] and os.path.isdir(os.path.join(dir_lot, fasta_dir)):
                                dir_fasta = os.path.join(dir_lot, fasta_dir)

        if dir_id == '':
            dir_id = path+'/'+row[0].replace("CIP", '').replace("-", '.')
            #os.mkdir(dir_id)
            print(dir_id)

        if dir_lot == '':
            dir_lot = dir_id+'/'+row[0].replace("CIP", '').replace("-", '.')+'-'+row[1].replace("-", '.')
            #os.mkdir(dir_lot)
            print(dir_lot)

        if dir_fasta == '':
            dir_fasta = dir_lot+'/'+row[2]
            #os.mkdir(dir_fasta)
            print(dir_fasta)

        # si fichier dans un dir_fasta le copier coller dans dir_fasta
        # si fichier racine le mettre dans dir_lot
        # si pas fichier racine mais pas de dir_fasta le mettre dans un dossier 'pas_de_lot' ?


        

