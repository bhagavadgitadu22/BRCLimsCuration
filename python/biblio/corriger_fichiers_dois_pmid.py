import csv
import psycopg2

# dois
f = open('../../output/dois_recuperees_11_2021.csv', 'r', newline='')
references = [line.split('|') for line in f]

# Connect to an existing database
connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True

# Create a cursor to perform database operations
cursor = connection.cursor()

# initialization
cursor.execute("SELECT * FROM good_documents_grouped")
records = cursor.fetchall()

# un record par ligne de biblio par version de souche
# pour chacune je parcours references et je vois si une correspondance (une seule !)
compteurs = []
for record in records:
    i = 0
    rec = list(record[1:5])
    for ref in references:
        if rec == ref[:4]:
            i += 1
    compteurs.append(i)

    if len(compteurs)%500 == 0:
        print(len(compteurs))

print(len(compteurs))
print(compteurs.count(0))
print(compteurs.count(1))
print(compteurs.count(2))





