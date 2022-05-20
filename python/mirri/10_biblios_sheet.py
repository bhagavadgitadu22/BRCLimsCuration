import psycopg2
import re
import csv

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

cursor = get_cursor("new_db")
cursor.execute(open("../envoi_souches/mirri/mirri_last_version_souches_cip.sql", "r").read())
cursor.execute(open("../envoi_souches/mirri/mirri_biblio.sql", "r").read())
records = cursor.fetchall()

pattern = '^([0-9a-zA-ZÀ-ÿ .()\',-0-9]+),[ ]*([0-9]{4}),[ ]*([^,])+(,|:)[ ]*(S?e?[0-9-–]+A?)$'

biblis = []
for record in records:
    bibli = record[0]
    list = []

    if 'doi' in bibli:
        elmt = ""
        if 'doi:' in bibli:
            elmt = bibli.split('doi:')[1]
        elif 'doi :' in bibli:
            elmt = bibli.split('doi :')[1]
        elif 'doi.org/' in bibli:
            elmt = bibli.split('doi.org/')[1]
        
        if elmt != '':
            list = [str(record[1]), "doi", elmt]
        else:
            print("aie (doi) : '"+str(record)+"'")
            list = [str(record[1]), "bibli", bibli, '', '', '', '', '']

    elif 'pmid' in bibli.lower():
        if 'pmid:' in bibli:
            elmt = bibli.split('pmid:')[1]
        elif 'pmid ' in bibli:
            elmt = bibli.split('pmid ')[1]
        elif 'PMID:' in bibli:
            elmt = bibli.split('PMID:')[1]
        elif 'PMID ' in bibli:
            elmt = bibli.split('PMID ')[1]

        if elmt != '':
            list = [str(record[1]), "pmid", elmt]
        else:
            print("aie (pmid) : '"+str(record)+"'")
            list = [str(record[1]), "bibli", bibli, '', '', '', '', '']

    else:
        if re.match(pattern, bibli):
            elmt = bibli.split(',')
            result = re.match(pattern, bibli)

            fp = ''
            lp = ''
            if re.match('^[0-9a-zA-Z]+$', result[5]):
                fp = result[5]
            elif re.match('^[0-9a-zA-Z-]+$', result[5]):
                fp = result[5].split('-')[0]
                lp = result[5].split('-')[1]
            elif re.match('^[0-9a-zA-Z–]+$', result[5]):
                fp = result[5].split('–')[0]
                lp = result[5].split('–')[1]
            else:
                print("aie (page) : "+result[5])

            list = [str(record[1]), "bibli", bibli, result[1], result[2], result[3], fp, lp]
        else:
            list = [str(record[1]), "bibli", bibli, '', '', '', '', '']

    biblis.append(list)

f_biblis = open('../../output/mirri/bilan_biblis.csv', 'w', encoding="utf-8", newline='')
writer_biblis = csv.writer(f_biblis, delimiter=';')
writer_biblis.writerows(biblis)
f_biblis.close()
