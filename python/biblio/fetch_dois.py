import psycopg2
import requests
from xml.dom import minidom
import csv

def try_dois(records, writer_good, writer_bad):
    erreurs = 0
    multi = 0
    i = 0
    
    for row in records:
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

        if len(tagname) != 0:
            if tagname[0].hasAttribute('status'):
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
                    elmt.append(row[5])
                    writer_good.writerow(elmt)
                else :
                    writer_bad.writerow(row)
                    erreurs += 1

        i += 1
        if i%10 == 0:
            print(str(i)+" (erreurs : "+str(erreurs)+", multi : "+str(multi)+")")

def main():
    # Connect to an existing database
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="db")
    conn.autocommit = True

    # Create a cursor to perform database operations
    cursor = conn.cursor()

    # initialization
    cursor.execute(open("../curation/100_bibliographie/1000_python_request.sql", "r", encoding='utf-8').read())

    #mobile_records = cursor.fetchmany(10)
    mobile_records = cursor.fetchall()

    # we write the results in an csv file
    f_good = open('../../output/dois_recuperees_11_2021.csv', 'a', newline='')
    writer_good = csv.writer(f_good, delimiter='|')
    #writer_good.writerow(['Title', 'Year', 'Volume', 'First page', 'DOI', 'Identifiants', 'Lignes'])

    # we write the results in an csv file
    f_bad = open('../../output/dois_echouees_11_2021.csv', 'a', newline='')
    writer_bad = csv.writer(f_bad, delimiter='|')
    #writer_bad.writerow(['Title', 'Year', 'Volume', 'First page', 'Identifiants', 'Lignes'])

    # first try with crossref
    try_dois(mobile_records, writer_good, writer_bad)

    # close the file
    f_good.close()
    f_bad.close()

main()