import bacdive
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

client = bacdive.BacdiveClient('martin.boutroux@pasteur.fr', 'hercule1821')

cursor = get_cursor("brc_db")
cursor.execute(open("../analyse/souches_sans_origines_avec_dsm.sql", 'r').read())
records = cursor.fetchall()

good = 0
bad = 0
weird = 0
rows = []
i = 0
for record in records:        
    # the search method fetches all BacDive-IDs matching your query
    # and returns the number of IDs found
    query = {"culturecolno": record[2]}
    count = client.search(**query)

    if count == 0:
        bad += 1
    elif count > 1:
        weird += 1
    else:
        good += 1

        # the retrieve method lets you iterate over all strains
        # and returns the full entry as dict
        # Entries can be further filtered using a list of keys (e.g. ['keywords'])
        for strain in client.retrieve():
            if 'isolation' in strain['Isolation, sampling and environmental information']:
                origin = ''
                if 'sample type' in strain['Isolation, sampling and environmental information']['isolation']:
                    origin = strain['Isolation, sampling and environmental information']['isolation']['sample type']

                if origin != '':
                    row = [record[0], record[1], record[2], origin]
                    rows.append(row)

    i += 1
    if i%20 == 0:
        print(i)

print("")
print(good)
print(bad)
print(weird)

f_genomes = open('../../output/souches_cip_sans_origine.csv', 'w', newline='')
writer_genomes = csv.writer(f_genomes, delimiter=';')
writer_genomes.writerows(rows)
f_genomes.close()
