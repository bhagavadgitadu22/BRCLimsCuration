import pandas as pd
import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

cursor = get_cursor("restart_db_pure")

xls_milieux = pd.ExcelFile('C:/Users/mboutrou/Documents/output/Fermetures 2000-2022.xlsx')

df = pd.read_excel(xls_milieux, 'unités_fermées')
col_nom = df.columns[2]

df = df.reset_index()  # make sure indexes pair with number of rows

col_nombs = []
col_idens = []
col_hists = []
col_colls = []
for index, row in df.iterrows():
    noms = [elmt.split('(')[0].strip() for elmt in row[col_nom].split('/')]

    identifiants = []
    historiques = []
    collections = {}
    for nom in noms:
        sep = nom.split(" ", 1)
        prenom = sep[0]
        fam = sep[1]
        if "'" in fam:
            fam = fam.split("'")[1]

        maj_prenom = ''.join([c for c in prenom if c.isupper()])

        cursor.execute("SELECT xxx_id, sch_identifiant, sch_version, sch_historique, col_descr FROM last_version_souches WHERE sch_historique SIMILAR TO CONCAT('%', '"+maj_prenom[0]+"', '[ .a-z]+', '"+fam+"', '%')")
        records = cursor.fetchall()

        for record in records:
            identifiants.append(record[1])
            historiques.append(record[3])
            if record[4] not in collections:
                collections[record[4]] = 1
            else:
                collections[record[4]] += 1

    str_idens = ''
    for iden in identifiants:
        if str_idens != '':
            str_idens += ', '
        str_idens += iden

    str_hists = ''
    for hist in historiques:
        if str_hists != '':
            str_hists += '\n'
        str_hists += hist

    str_colls = ''
    for coll in collections:
        if str_colls != '':
            str_colls += ', '
        str_colls += coll + ": " + str(collections[coll])

    col_nombs.append(len(identifiants))
    col_idens.append(str_idens)
    col_hists.append(str_hists)
    col_colls.append(str_colls)

    if index % 10 == 0:
        print(index)

df["Nombres"] = col_nombs
df["Identifiants"] = col_idens
df["Historiques"] = col_hists
df["Collections"] = col_colls

with pd.ExcelWriter(r"C:\Users\mboutrou\Documents\output\souches_linked_to_fermetures.xlsx") as writer:
    df.to_excel(writer, sheet_name="unites_fermees", index=False)
