import psycopg2
import csv

def main():
    # Connect to an existing database
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="brc_db")
    conn.autocommit = True

    # Create a cursor to perform database operations
    cursor = conn.cursor()

    f = open('../../output/new_biblios.csv', 'r', newline='')
    biblios = [line.split('|') for line in f]

    for bib in biblios:
        identifiants = bib[2]
        new_texte = bib[1]

        for id in identifiants:
            cursor.execute("UPDATE t_souche SET sch_bibliographie = "+new_texte+" WHERE xxx_id = "+id+";");


    # initialization
    cursor.execute(open("../en_preparation/bibliographie/1000_python_request.sql", "r", encoding='utf-8').read())

    #mobile_records = cursor.fetchmany(20)
    mobile_records = cursor.fetchall()

    # we write the results in an csv file
    f_good = open('../../output/dois_recuperees_11_2021.csv', 'a', newline='')
    writer_good = csv.writer(f_good, delimiter='|')
    #writer_good.writerow(['Title', 'Year', 'Volume', 'First page', 'DOI', 'Identifiants'])

    # we write the results in an csv file
    f_bad = open('../../output/dois_echouees_11_2021.csv', 'a', newline='')
    writer_bad = csv.writer(f_bad, delimiter='|')
    #writer_bad.writerow(['Title', 'Year', 'Volume', 'First page', 'Identifiants'])

    # first try with crossref
    try_dois(mobile_records, writer_good, writer_bad)

    # close the file
    f_good.close()
    f_bad.close()

main()