import pandas as pd
import psycopg2

xls = pd.ExcelFile('C:/Users/mboutrou/Documents/bilan_panels.xlsx')

dict = ['Kleb-Taxo']

# connect to an existing database
connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="restart_db_cured")
connection.autocommit = True

# create a cursor to perform database operations
cursor = connection.cursor()
sql = open("../analyse/last_version_souches_cip_avec_suppressions.sql", "r", encoding='utf-8').read()

with pd.ExcelWriter("C:/Users/Public/Documents/bilan_panels_kleb.xlsx") as writer:
    for name in dict:
        df = pd.read_excel(xls, name)
        col = df.columns[0]

        rows = []

        for elmt in df[col]:
            cursor.execute("SELECT sch_historique, lieu_origine, sch_isole_a_partir_de FROM last_version_souches_cip WHERE REPLACE(sch_identifiant, ' ', '') SIMILAR TO '"+str(elmt)+"T?' OR sch_identifiant SIMILAR TO '"+str(elmt)+"T?'")
            record = cursor.fetchone()
            if record is not None:
                rows.append([elmt for elmt in record])
            else:
                rows.append(["", "", "", "", ""])
        
        df["Historique"] = [elmt[0] for elmt in rows]
        df["Lieu d'origine"] = [elmt[1] for elmt in rows]
        df["Isolé à partir de"] = [elmt[2] for elmt in rows]
        df.to_excel(writer, sheet_name=name, index=False)