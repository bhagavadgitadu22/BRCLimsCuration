import psycopg2
import pandas as pd


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

conn = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="restart_db_cured")
conn.autocommit = True

cursor = conn.cursor()
cursor.execute(open("../curation/20_collections_de_cip/liste_souches_bon_brclims.sql", "r").read())

xls_ids = pd.ExcelFile(r"C:\Users\Public\Documents\ids_archives_lors_de_curation.xlsx")

with pd.ExcelWriter(r"C:\Users\Public\Documents\ids_archives_vs_nouveaux_ids.xlsx") as writer:
    df = pd.read_excel(xls_ids, "ids_archives")
    id = df.columns[0]
    new = []

    for sch in df[id]:
        sql = "SELECT sch_identifiant FROM t_souche WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip) AND sch_references_equi SIMILAR TO '%"+sch+"%'"
        cursor.execute(sql)
        sch_new = cursor.fetchone()[0]
        new.append(sch_new)

    df["Nouvel identifiant CIP"] = new
    df.to_excel(writer, sheet_name="ids_archives", index=False)
    column_width(writer, "ids_archives", df)