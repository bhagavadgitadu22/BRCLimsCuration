import pandas as pd
import psycopg2

xls_packs = pd.ExcelFile('/home/calvin/Downloads/Panels_WGS.xlsx')
dict = ['Teaching', 'ECOR', 'EUCAST', 'WDCM', 'Ecoli receivers', 'colicins']

# je lis mon fichier ligne par ligne pour choper les infos des identifiants, pour sheet 1 puis 2

with pd.ExcelWriter("/home/calvin/Downloads/caracs_des_plus_commandes.xlsx") as writer:
    connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="localhost",
                                    port="5432",
                                    database="brc_db")
    connection.autocommit = True

    # create a cursor to perform database operations
    cursor = connection.cursor()
    sql = open("../analyse/analyse_provenance_commandes/souches_commandees_vs_non_commandees.sql", "r", encoding='utf-8').read()
    cursor.execute(sql)
    records = cursor.fetchall()

    data = []
    print(len(records))
    i = 0
    for record in records:
        id_brc = record[0]
        id_ligne = [elmt for elmt in record]

        exists_in_one_panel = "No" 
        # on parcourt tous les packs à chaque fois pour voir s'il y a des correspondances
        for name in dict:
            df = pd.read_excel(xls_packs, name)
            col = df.columns[0]
            exists = "No"        

            for id_pack in df[col]:
                if id_brc == id_pack:
                    exists = "Yes"
                    exists_in_one_panel = "Yes"
            id_ligne.append(exists)
        id_ligne.append(exists_in_one_panel)

        data.append(id_ligne)

        i += 1
        if i%100 == 0:
            print(i)

    cols = ['Identifiant', 'Denomination', 'Commandes totales', 'Commandes 10 ans', 'Au catalogue', 'Genome', 'Commentaire genome']
    for name in dict:
        cols.append(name)
    cols.append('In at least one panel')
    df_total = pd.DataFrame(data, columns = cols)
    df_total.to_excel(writer, sheet_name='bilan', index=False)
