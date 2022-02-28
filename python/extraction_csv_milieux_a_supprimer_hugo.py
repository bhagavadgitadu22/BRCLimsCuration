import pandas as pd
import csv

xls_milieux = pd.ExcelFile('C:/Users/mboutrou/Documents/output/milieux_a_supprimer.xlsx')

df_vides = pd.read_excel(xls_milieux, 'milieux_vides')
col_numero = df_vides.columns[0]

milieux_vides = []
for id_brc in df_vides[col_numero]:
    milieux_vides.append(id_brc)

f_vides = open('../../output/milieux_vides.csv', 'w', newline='')
writer_vides = csv.writer(f_vides, delimiter=';')
writer_vides.writerows(map(lambda x: [x], [elem for elem in milieux_vides]))
f_vides.close()

df_non_vides = pd.read_excel(xls_milieux, 'milieux_non_vides')
col_numero = df_non_vides.columns[0]
col_remplacant = df_non_vides.columns[6]

milieux_non_vides = []
df_non_vides = df_non_vides.reset_index()  # make sure indexes pair with number of rows
for index, row in df_non_vides.iterrows():
    mil = []
    mil.append(row[col_numero])

    if 'MEDIUM' in str(row[col_remplacant]):
        mil.append(row[col_remplacant].split('MEDIUM')[1].strip(' '))
    else:
        mil.append(row[col_remplacant])

    milieux_non_vides.append(mil)

f_non_vides = open('../../output/milieux_non_vides.csv', 'w', newline='')
writer_non_vides = csv.writer(f_non_vides, delimiter=';')
writer_non_vides.writerows(milieux_non_vides)
f_non_vides.close()
