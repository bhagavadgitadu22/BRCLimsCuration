import pandas as pd
import csv

xls_milieux = pd.ExcelFile('../../output/all_infos_p2m.xlsx')
df = pd.read_excel(xls_milieux, 'all')

f = open('../../output/infos_de_p2m.csv', 'r', newline='')
records = csv.reader(f, delimiter=';')
ids_csv = [[record[0].replace("CIP", '').replace("CRBIP", '').replace("_", '').replace("-", '').replace(".", '').replace(" ", '').replace("T", ''), record[1].replace("_", '').replace("-", '').replace(".", '').replace(" ", ''), record[0], record[1]] for record in records]

ct = 0
cf = 0
count = 0

c_id = []
v_id = []
c_lot = []
v_lot = []

df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    id_cip = row[0].replace("CIP", '').replace("CRBIP", '').replace("_", '').replace("-", '').replace(".", '').replace(" ", '').replace("T", '')
    lot_cip = str(row[1]).replace("_", '').replace("-", '').replace(".", '').replace(" ", '')

    bool = False
    concordance_id = False
    concordance = []
    valeur_id = ''
    valeur_lot = ''
    for record in ids_csv:
        if id_cip == record[0]:
            concordance_id = True
            valeur_id = record[2]
            concordance.append(record)
    
    # si on a trouvé une concordance d'id on peut chercher une concordance de lots
    if concordance != []:
        concordance_lot = False
        bool2 = False
        for record in concordance:
            if lot_cip == record[1]:
                ct += 1
                concordance_lot = True
                valeur_lot = record[3]
                bool2 = True
        if not(bool2) and lot_cip != 'nan':
            cf +=1
        
    c_id.append(concordance_id)
    c_lot.append(concordance_id)
    v_id.append(valeur_id)   
    v_lot.append(valeur_lot)

    count += 1
    if count%1000 == 0:
        print(count)

f.close()

print(ct)
print(cf)

df["Id validé"] = c_id
df["Lot validé"] = c_lot
df["Valeur d'id"] = v_id
df["Valeur de lot"] = v_lot

with pd.ExcelWriter("../../output/all_infos_p2m_crossed.xlsx") as writer:
    df.to_excel(writer, sheet_name="all_complete", index=False)
