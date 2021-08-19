import psycopg2
from psycopg2 import Error
import requests
from xml.dom import minidom
import csv

def try_dois(list_dois, records):
    list_erreurs = []
    erreurs = 0
    i = 0

    for row in records:
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
            list_erreurs.append(row)
            erreurs += 1

        i += 1
        if i%100 == 0:
            print(str(i)+" (erreurs : "+str(erreurs)+")")
    
    return list_dois, list_erreurs

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
    cursor.execute(open("../bibliographie/1000_python_request.sql", "r", encoding='utf-8').read())

    mobile_records = cursor.fetchall()

    # first try with crossref
    list_dois, list_erreurs = try_dois([], mobile_records)
    print("Bilan de l'essai : "+str(len(list_dois))+" dois trouvées pour "+str(len(list_erreurs))+" erreurs")

    # second try with crossref
    list_dois2, list_erreurs2 = try_dois(list_dois, list_erreurs)
    print("Bilan de l'essai : "+str(len(list_dois2))+" dois trouvées pour "+str(len(list_erreurs2))+" erreurs")

    # third try with crossref
    list_dois3, list_erreurs3 = try_dois(list_dois2, list_erreurs2)
    print("Bilan de l'essai : "+str(len(list_dois3))+" dois trouvées pour "+str(len(list_erreurs3))+" erreurs")
    
    # we write the results in an csv file
    f = open('../../output/bilan_recuperation_dois.csv', 'w', newline='')
    writer = csv.writer(f)

    # write the rows to the csv file
    writer.writerow(['Title', 'Year', 'Volume', 'First page', 'DOI', 'Identifiants'])
    writer.writerows(list_dois)

    # we write the results in an csv file
    f2 = open('../../output/bilan_recuperation_dois_echecs.csv', 'w', newline='')
    writer = csv.writer(f2)

    # write the rows to the csv file
    writer.writerow(['Title', 'Year', 'Volume', 'First page', 'Identifiants'])
    writer.writerows(list_erreurs)

    # close the file
    f.close()
    f2.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")