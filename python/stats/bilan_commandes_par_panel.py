import pandas as pd
import psycopg2

xls_packs = pd.ExcelFile('/home/calvin/Downloads/Panels_WGS.xlsx')
dict = ['Teaching', 'ECOR', 'EUCAST', 'WDCM', 'Ecoli receivers', 'colicins']

# je lis mon fichier ligne par ligne pour choper les infos des identifiants, pour sheet 1 puis 2

with pd.ExcelWriter("/home/calvin/Downloads/max_commandes_vs_packs.xlsx") as writer:
    connection = psycopg2.connect(user="postgres",
                                    password="hercule1821",
                                    host="localhost",
                                    port="5432",
                                    database="brc_db")
    connection.autocommit = True

    # create a cursor to perform database operations
    cursor = connection.cursor()
    sql = open("../analyse/packs/souches_sequencees.sql", "r", encoding='utf-8').read()

    bilan_par_pack = {}
    for name in dict:
        bilan_par_pack[name] = []

    df_ans = pd.read_excel(xls_ids, duree)
    col = df_ans.columns[0]

    # on parcourt chaque id listé
    i = 0
    for id_brc in df_ans[col]:
        # et tous les packs à chaque fois pour voir s'il y a des correspondances
        for name in dict:
            df = pd.read_excel(xls_packs, name)
            col = df.columns[0]
            exists = "No"        

            for id_pack in df[col]:
                if id_brc == id_pack:
                    exists = "Yes"
            bilan_par_pack[name].append(exists)

        i += 1
        if i%10 == 0:
            print(i)

    for name in dict:
        df_ans[name] = bilan_par_pack[name]

    df_ans.to_excel(writer, sheet_name=duree, index=False)
