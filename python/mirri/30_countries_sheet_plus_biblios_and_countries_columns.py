import psycopg2
import csv

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

cursor = get_cursor("brc_db")
cursor.execute(open("../envoi_souches/mirri/extract_date_function.sql", "r").read())
cursor.execute(open("../envoi_souches/mirri/mirri_biblio_par_id.sql", "r").read())
cursor.execute(open("../envoi_souches/mirri/mirri.sql", "r").read())
records = cursor.fetchall()


# gestion des biblis
f_biblis = open('../../output/mirri/bilan_biblis.csv', 'r', encoding="utf-8", newline='')
biblis = csv.reader(f_biblis, delimiter=';')

biblis_par_id = {}
correspondances_biblis = []
numero_bibli  = 0
for elmt in biblis:
    ids_elmt = elmt[0]
    type_elmt = elmt[1]
    val_elmt = elmt[2]

    if not(type_elmt == "doi" or type_elmt == "pmid"):
        numero_bibli += 1
        list = [numero_bibli, val_elmt, '', '', elmt[3], elmt[4], elmt[5], '', elmt[6], elmt[7]]
        correspondances_biblis.append(list)

    for id_elmt in ids_elmt.split(','):
        int_id = int(id_elmt)
        if int_id not in biblis_par_id:
            biblis_par_id[int_id] = []

        if type_elmt == "doi" or type_elmt == "pmid":
            biblis_par_id[int_id].append(val_elmt)
        else:
            biblis_par_id[int_id].append(numero_bibli)

# gestion des géographies
cursor.execute(open("../envoi_souches/mirri/mirri_geography.sql", "r").read())
records_pays = cursor.fetchall()

pays_par_id = {}
correspondances_pays = []
numero_pays  = 0
for record in records_pays:
    ids_elmt = record[2]
    pays = record[0]
    lieu_precis = record[1]

    if str(pays) == 'None':
        pays = 'Unknown'
    if lieu_precis == '':
        lieu_precis = 'Unknown'

    numero_pays += 1
    list = [numero_pays, pays, '', '', lieu_precis]
    correspondances_pays.append(list)

    for id_elmt in ids_elmt.split(','):
        int_id = int(id_elmt)
        pays_par_id[int_id] = numero_pays

# gestion des strains
rows_strains = []
for record in records:
    xxx_id = record[0]
    row = [r for r in record[1:]]
    row[25] = pays_par_id[xxx_id]
    refs = ""
    if xxx_id in biblis_par_id:
        for ref in biblis_par_id[xxx_id]:
            if refs != '':
                refs += ';'
            refs += str(ref)
    row[26] = refs

    rows_strains.append(row)

f_strains = open('../../output/mirri/sheet_strains.csv', 'w', encoding="utf-8", newline='')
writer_strains = csv.writer(f_strains, delimiter=';')
writer_strains.writerows(rows_strains)
f_strains.close()

f_literature = open('../../output/mirri/sheet_literature.csv', 'w', encoding="utf-8", newline='')
writer_literature = csv.writer(f_literature, delimiter=';')
writer_literature.writerows(correspondances_biblis)
f_literature.close()

f_pays = open('../../output/mirri/sheet_pays.csv', 'w', encoding="utf-8", newline='')
writer_pays = csv.writer(f_pays, delimiter=';')
writer_pays.writerows(correspondances_pays)
f_pays.close()

f_biblis.close()