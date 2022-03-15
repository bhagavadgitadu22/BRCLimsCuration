import pandas as pd
import os

xls = pd.ExcelFile('../../output/transfert_infos_p2m.xlsx')

list_ids = []
df = pd.read_excel(xls, 'genomes')
df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    if row[1].split('/')[5] not in list_ids:
        list_ids.append(row[1].split('/')[5])

sub_ids = list_ids[:10]

print(sub_ids)