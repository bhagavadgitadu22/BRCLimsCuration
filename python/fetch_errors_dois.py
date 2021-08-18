import psycopg2
from psycopg2 import Error
import requests
from xml.dom import minidom
import csv

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="new_brc4")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    # initialization
    cursor.execute(open("../bibliographie/30_avec_souches_origines.sql", "r", encoding='utf-8').read())

    mobile_records = cursor.fetchall()

    references = []

    for row in mobile_records:
        title = row[0]
        date = row[1]
        volume = row[2]
        page = row[3]
        ids = row[4]

        references.append([title, date, volume, page, ids])
    
    f = open('../../output/bilan_recuperation_dois_2.csv', 'r', newline='')
    references_good = [line.split(';') for line in f]

    references_bad = []
    for elmt in references:
        if elmt[:4] not in references_good:
            references_bad.append(elmt)

    # we write the results in an csv file
    f = open('../../output/bilan_erreurs_dois.csv', 'w', newline='')
    writer = csv.writer(f)

    # write the rows to the csv file
    writer.writerow(['Title', 'Year', 'Volume', 'First page', 'Identifiants'])
    writer.writerows(references_bad)

    # close the file
    f.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")