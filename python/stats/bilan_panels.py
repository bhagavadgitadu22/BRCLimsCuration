import pandas as pd
import psycopg2

xls = pd.ExcelFile(r'C:\Users\Public\Documents\Panels_WGS.xlsx')

dict = ['Teaching', 'ECOR', 'EUCAST', 'WDCM','Ecoli receivers', 'colicins']

# connect to an existing database
connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True

# create a cursor to perform database operations
cursor = connection.cursor()
sql = open("../analyse/packs/souches_sequencees.sql", "r", encoding='utf-8').read()

with pd.ExcelWriter(r"C:\Users\Public\Documents\output.xlsx") as writer:
    for name in dict:
        df = pd.read_excel(xls, name)
        col = df.columns[0]
        a = []

        for elmt in df[col]:
            cursor.execute(sql+" AND sch_identifiant = '"+elmt+"'")
            record = cursor.fetchone()
            if record is not None:
                a.append("Yes")
            else:
                a.append("No")
        
        df["1546 - Séquençage total"] = a
        df.to_excel(writer, sheet_name=name, index=False)
