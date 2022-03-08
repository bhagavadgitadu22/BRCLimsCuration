import pandas as pd
import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def get_names_params(cursor, df, tab_idens, param, stri):
    str_idens_used = "('"
    for elmt in tab_idens:
        for id in elmt:
            if id not in str_idens_used:
                if str_idens_used != "('":
                    str_idens_used += "','"
                str_idens_used += id
    str_idens_used += "')"

    col_nombs = []
    col_idens = []
    col_hists = []
    col_colls = []

    df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
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

            str_sql = "SELECT xxx_id, sch_identifiant, sch_version, sch_historique, col_descr FROM last_version_souches WHERE "+param+" SIMILAR TO CONCAT('%', '"+maj_prenom[0]+"', '[ .a-z]+', '"+fam+"', '%')"
            if str_idens_used != "('')":
                str_sql += " AND sch_identifiant NOT IN "+str_idens_used

            cursor.execute(str_sql)
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
        tab_idens.append(identifiants)
        col_idens.append(str_idens)
        col_hists.append(str_hists)
        col_colls.append(str_colls)

        if index % 10 == 0:
            print(index)
    
    df["Nombres ("+stri+")"] = col_nombs
    df["Identifiants ("+stri+")"] = col_idens
    df["Valeurs ("+stri+")"] = col_hists
    df["Collections ("+stri+")"] = col_colls

    return df, tab_idens, col_nombs

cursor = get_cursor("restart_db_pure")

cursor.execute(open("../analyse/last_version_souches_toutes_collections.sql", "r").read())

xls_milieux = pd.ExcelFile('../../output/Fermetures 2000-2022.xlsx')

df = pd.read_excel(xls_milieux, 'unités_fermées')
col_nom = df.columns[2]

df, tab_idens, col_nombs_1 = get_names_params(cursor, df, [], "sch_historique", "historique")
df, tab_idens, col_nombs_2 = get_names_params(cursor, df, tab_idens, "sch_isole_par", "isole_par")
df, tab_idens, col_nombs_3 = get_names_params(cursor, df, tab_idens, "deposant", "deposant")

total = []
for i in range(len(col_nombs_1)):
    total.append(col_nombs_1[i]+col_nombs_2[i]+col_nombs_3[i])
df["Totaux"] = total

with pd.ExcelWriter("../../output/souches_linked_to_fermetures.xlsx") as writer:
    df.to_excel(writer, sheet_name="unites_fermees", index=False)
