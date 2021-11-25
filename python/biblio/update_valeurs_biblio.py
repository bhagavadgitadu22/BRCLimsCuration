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

    # On ouvre le fichier avec les biblios à mettre à jour
    f = open('../../output/new_biblios.csv', 'r', newline='')
    biblios = [line.split('|') for line in f]

    for bib in biblios:
        identifiants = bib[2]
        new_texte = bib[1]

        for id in identifiants:
            cursor.execute("UPDATE t_souche SET sch_bibliographie = "+new_texte+" WHERE xxx_id = "+id+";")

    # Close the file
    f.close()

main()