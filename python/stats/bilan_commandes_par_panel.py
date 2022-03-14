import pandas as pd
import psycopg2

xls_ids = pd.ExcelFile("C:/Users/Public/Documents/souches_les_plus_commandees.xlsx")
xls_packs = pd.ExcelFile('C:/Users/Public/Documents/Panels_WGS.xlsx')
dict = ['Teaching', 'ECOR', 'EUCAST', 'WDCM', 'Ecoli receivers', 'colicins']

# create a cursor to perform database operations
connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True
cursor = connection.cursor()

# je lis mon fichier ligne par ligne pour choper les infos des identifiants, pour sheet 1 puis 2
with pd.ExcelWriter("C:/Users/Public/Documents/max_commandes_vs_packs.xlsx") as writer:
    for duree in ['5 ans', '10 ans']:
        denom = []
        refs_equis = []
        catalogue = []

        bilan_par_pack = {}
        for name in dict:
            bilan_par_pack[name] = []

        df_ans = pd.read_excel(xls_ids, duree)
        col = df_ans.columns[0]

        # on parcourt chaque id listé
        i = 0
        for id_brc in df_ans[col]:
            str_sql = "SELECT sch_denomination, sch_references_equi, sch_catalogue FROM last_version_souches_cip WHERE sch_identifiant = '"+id_brc+"'"
            cursor.execute(str_sql)
            record = cursor.fetchone()

            if record is not None:
                denom.append(record[0])
                refs_equis.append(record[1])
                catalogue.append(record[2])
            else:
                denom.append("")
                refs_equis.append("")
                catalogue.append("")

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

        df_ans["Dénomination"] = denom
        df_ans["Références équivalentes"] = refs_equis
        df_ans["Catalogue"] = catalogue
        
        for name in dict:
            df_ans[name] = bilan_par_pack[name]

        df_ans.to_excel(writer, sheet_name=duree, index=False)
