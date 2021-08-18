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

    list_dois = []
    erreurs = 0
    i = 0

    for row in mobile_records:
        parameters = {
            "redirect": "false",
            "pid": "martinboutroux@outlook.fr",
            "title": row[0],
            "date": row[1],
            "volume": row[2],
            "spage": row[3]
        }
        response = requests.get("https://doi.crossref.org/openurl", params=parameters, timeout=100)

        dat = minidom.parseString(response.content)
        tagname = dat.getElementsByTagName('query')

        if tagname[0].attributes['status'].value != "unresolved":
            tagdoi = dat.getElementsByTagName('doi')
            doi = tagdoi[0].firstChild.nodeValue

            elmt = []
            elmt.append(row[0])
            elmt.append(row[1])
            elmt.append(row[2])
            elmt.append(row[3])
            elmt.append(doi)
            elmt.append(row[4])
            list_dois.append(elmt)
        else :
            erreurs += 1

        i += 1
        if i%10 == 0:
            print(str(i)+" (erreurs : "+str(erreurs)+")")
            
    # we write the results in an csv file
    f = open('../../output/bilan_recuperation_dois.csv', 'w', newline='')
    writer = csv.writer(f)

    # write the rows to the csv file
    writer.writerow(['Title', 'Year', 'Volume', 'First page', 'DOI', 'Identifiants'])
    writer.writerows(list_dois)

    # close the file
    f.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")