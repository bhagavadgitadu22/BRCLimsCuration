import pandas as pd
from pandas.core.frame import DataFrame
import psycopg2

def column_width(writer, name, df):
    worksheet = writer.sheets[name]  # pull worksheet object

    workbook  = writer.book
    my_format = workbook.add_format()
    my_format.set_align('center')

    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            )) + 1  # adding a little extra space
        worksheet.set_column(idx, idx, min(max_len, 100), my_format)  # set column width

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

champs = [col[0] for col in colonnes if 'xxx' not in col[0]]
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

    column_width(writer, "bilan", df)

    idx = 0
    for champ in champs:
        cursor.execute("SELECT "+champ+", COUNT(*) FROM e_souche WHERE sch_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401) AND xxx_sup_dat IS NULL AND "+champ+" IS NOT NULL GROUP BY "+champ+" ORDER BY COUNT(*) DESC LIMIT 100;")
        records = cursor.fetchall()

        values_field = []
        uses_field = []
        freqs_field = []
        for record in records:
            values_field.append(record[0])
            uses_field.append(record[1])
            if quantites[idx] != 0:
                freqs_field.append(round(int(record[1]/quantites[idx]), 2))
            else:
                freqs_field.append('xxx')

        df_field = pd.DataFrame()
        df_field["valeurs"] = values_field
        df_field["nombre d'utilisations"] = uses_field
        df_field["frequences"] = freqs_field
        df_field.to_excel(writer, sheet_name=champ, index=False)

        column_width(writer, champ, df_field)

        idx += 1
