import pandas as pd
from pandas.core.frame import DataFrame
import psycopg2

# connect to an existing database
connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True

# create a cursor to perform database operations
cursor = connection.cursor()
cursor.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'e_souche';")
colonnes = cursor.fetchall()

champs = [col[0] for col in colonnes]
quantites = []
frequences = []

cursor.execute("SELECT COUNT(*) FROM e_souche WHERE sch_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401) AND xxx_sup_dat IS NULL;")
total = int(cursor.fetchone()[0])

for champ in champs:
    cursor.execute("SELECT COUNT(*) FROM e_souche WHERE sch_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401) AND xxx_sup_dat IS NULL AND "+champ+" IS NOT NULL;")
    quantites.append(int(cursor.fetchone()[0]))

frequences = [round(q/total, 2) for q in quantites]

with pd.ExcelWriter(r"C:\Users\Public\Documents\champs_utilises_dans_brclims.xlsx") as writer:
    df = pd.DataFrame()
    df["champs"] = champs
    df["frequences"] = frequences
    df.to_excel(writer, sheet_name="bilan", index=False)
