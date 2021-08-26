import psycopg2
from psycopg2 import Error
import requests
from xml.dom import minidom
import csv

def try_dois(records, writer_good, writer_bad):
    erreurs = 0
    multi = 0
    i = 0

    b_errors = False
    b_good = False

    for row in records:
        if b_errors and b_good:   
            parameters = {
                "redirect": "false",
                "pid": "martinboutroux@outlook.fr",
                "title": row[0],
                "date": row[1],
                "volume": row[2],
                "spage": row[3],
                "multihit": True
            }
            response = requests.get("https://doi.crossref.org/openurl", params=parameters, timeout=100)

            dat = minidom.parseString(response.content)
            tagname = dat.getElementsByTagName('query')

            if tagname[0].attributes['status'].value != "unresolved":
                if tagname[0].attributes['status'].value == "multiresolved":
                    multi += 1

                tagdoi = dat.getElementsByTagName('doi')
                doi = tagdoi[0].firstChild.nodeValue

                elmt = []
                elmt.append(row[0])
                elmt.append(row[1])
                elmt.append(row[2])
                elmt.append(row[3])
                elmt.append(doi)
                elmt.append(row[4])
                writer_good.writerow(elmt)
            else :
                writer_bad.writerow(row)
                erreurs += 1

            i += 1
            if i%10 == 0:
                print(str(i)+" (erreurs : "+str(erreurs)+", multi : "+str(multi)+")")
        else:
            if row[0] == "Int. J. Syst. Bacteriol" and row[1] == "1996" and row[2] == "46" and row[3] == "1189":
                b_good = True
            if row[0] == "Int. J. Syst. Bacteriol" and row[1] == "1996" and row[2] == "46" and row[3] == "1118":
                b_errors = True

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="new_brc5")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    # initialization
    cursor.execute(open("../bibliographie/1000_python_request.sql", "r", encoding='utf-8').read())

    mobile_records = cursor.fetchall()

    # we write the results in an csv file
    f_good = open('../../output/bilan_recuperation_dois.csv', 'a', newline='')
    writer_good = csv.writer(f_good)
    #writer_good.writerow(['Title', 'Year', 'Volume', 'First page', 'DOI', 'Identifiants'])

    # we write the results in an csv file
    f_bad = open('../../output/bilan_recuperation_dois_echecs.csv', 'a', newline='')
    writer_bad = csv.writer(f_bad)
    #writer_bad.writerow(['Title', 'Year', 'Volume', 'First page', 'Identifiants'])

    # first try with crossref
    try_dois(mobile_records, writer_good, writer_bad)

    # close the file
    f_good.close()
    f_bad.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")