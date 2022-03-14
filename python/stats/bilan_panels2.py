import pandas as pd
import psycopg2

xls = pd.ExcelFile('C:/Users/Public/Documents/220314_Panels_all_info-1.xlsx')

dict = ['Teaching', 'EUCAST', 'ECOR', 'colicins', 'Ecoli receivers']

# connect to an existing database
connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True

# create a cursor to perform database operations
cursor = connection.cursor()
sql = open("../analyse/last_version_souches_cip_avec_suppressions.sql", "r", encoding='utf-8').read()

with pd.ExcelWriter("C:/Users/Public/Documents/bilan_panels.xlsx") as writer:
    for name in dict:
        df = pd.read_excel(xls, name)
        col = df.columns[0]

        denom = []
        refs_equis = []
        catalogue = []

        for elmt in df[col]:
            cursor.execute("SELECT sch_denomination, sch_references_equi, sch_catalogue FROM last_version_souches_cip WHERE sch_identifiant SIMILAR TO '"+str(elmt)+"T?'")
            record = cursor.fetchone()
            if record is not None:
                denom.append(record[0])
                refs_equis.append(record[1])
                catalogue.append(record[2])
            else:
                denom.append("")
                refs_equis.append("")
                catalogue.append("")
        
        df["Dénomination"] = denom
        df["Références équivalentes"] = refs_equis
        df["Catalogue"] = catalogue
        df.to_excel(writer, sheet_name=name, index=False)
