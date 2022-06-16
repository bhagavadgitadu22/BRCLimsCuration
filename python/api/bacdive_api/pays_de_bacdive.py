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

cursor = get_cursor("restart_db_pure")
cursor.execute(open("../analyse/souches_sans_pays_avec_dsm.sql", 'r').read())
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

        print(record[0] + ' ' + record[2])
        for strain in client.retrieve():
            denom_dsm = ''
            if 'species' in strain['Name and taxonomic classification']:
                denom_dsm = strain['Name and taxonomic classification']['species']
            if 'isolation' in strain['Isolation, sampling and environmental information']:
                country = ''
                location = ''
                if 'country' in strain['Isolation, sampling and environmental information']['isolation']:
                    country = strain['Isolation, sampling and environmental information']['isolation']['country']
                if 'geographic location' in strain['Isolation, sampling and environmental information']['isolation']:
                    location = strain['Isolation, sampling and environmental information']['isolation']['geographic location']

                if country != '' or location != '':
                    print(record[3] + ' ' + denom_dsm)
                    print(country + ' ' + location)
    else:
        good += 1

        # the retrieve method lets you iterate over all strains
        # and returns the full entry as dict
        # Entries can be further filtered using a list of keys (e.g. ['keywords'])
        for strain in client.retrieve():
            denom_dsm = ''
            if 'species' in strain['Name and taxonomic classification']:
                denom_dsm = strain['Name and taxonomic classification']['species']
            if 'isolation' in strain['Isolation, sampling and environmental information']:
                country = ''
                location = ''
                if 'country' in strain['Isolation, sampling and environmental information']['isolation']:
                    country = strain['Isolation, sampling and environmental information']['isolation']['country']
                if 'geographic location' in strain['Isolation, sampling and environmental information']['isolation']:
                    location = strain['Isolation, sampling and environmental information']['isolation']['geographic location']

                if country != '' or location != '':
                    row = [record[0], record[3], denom_dsm, (record[3]!=denom_dsm), record[1], record[2], country, location]
                    rows.append(row)

    i += 1
    if i%20 == 0:
        print(i)

print("")
print(good)
print(bad)
print(weird)

f_genomes = open('../../output/souches_cip_sans_pays.csv', 'w', newline='')
writer_genomes = csv.writer(f_genomes, delimiter=';')
writer_genomes.writerows(rows)
f_genomes.close()
