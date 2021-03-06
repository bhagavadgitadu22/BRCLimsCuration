import pandas as pd
import os
import shutil

xls = pd.ExcelFile('../../transfert_p2m_try_2/50_transfert_infos_p2m.xlsx')

#pos_genome = 5
pos_genome = 2

list_ids = []
df = pd.read_excel(xls, 'genomes')
df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    if row[1].split('/')[pos_genome] not in list_ids:
        list_ids.append(row[1].split('/')[pos_genome])

sub_ids = list_ids[:1]
print(sub_ids)
print(len(sub_ids))

df = pd.read_excel(xls, 'metafiles')
df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    id = row[1].split('/')[pos_genome]

    if id in sub_ids:
        old_location = row[0]
        new_location = row[1]

        print('')
        print(old_location)
        print(new_location)

        if not(os.path.exists(old_location)):
            print('aie')

df = pd.read_excel(xls, 'genomes')
df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    id = row[1].split('/')[pos_genome]

    if id in sub_ids:
        old_location = row[0]
        new_location = row[1]

        print('')
        print(old_location)
        print(new_location)

        if not(os.path.exists(old_location)):
            print('aie2')
