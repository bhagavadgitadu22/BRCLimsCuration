import psycopg2
from psycopg2 import Error
import requests
from xml.dom import minidom
import csv

def try_taxos(list_taxos, records):
    list_erreurs = []
    erreurs = 0
    i = 0

    for row in records:
        print(row[2])
        parameters = {
            "taxon_name": row[2]
        }
        response = requests.get("https://api.lpsn.dsmz.de/advanced_search", params=parameters, timeout=100)

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
        if i%10 == 0:
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
    cursor.execute(open("../taxonomie/stats/erreurs/erreurs_restantes_species.sql", "r", encoding='utf-8').read())

    mobile_records = cursor.fetchall()

    # first try with crossref
    list_taxos, list_erreurs = try_taxos([], mobile_records)
    print("Bilan de l'essai : "+str(len(list_taxos))+" taxos trouvées pour "+str(len(list_erreurs))+" erreurs")
    
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