from os import forkpty
from openpyxl.workbook.workbook import Workbook
import psycopg2

def sheet_error(wb, cursor, file, name):
    cursor.execute(open("../analyse/analyse_depots/"+file, "r").read())
    records = cursor.fetchall()

    sheet = wb.create_sheet(name)
    cols = ["Année", "Nombre de souches"]
    liste_pays_uniques = []
    for record in records:
        liste_pays = record[2]
        for pays in liste_pays:
            if pays not in liste_pays_uniques:
                liste_pays_uniques.append(pays)
    for elmt in sorted(liste_pays_uniques):
        cols.append(elmt)
    print(cols)
    sheet.append(cols)

    for record in records:
        row = [record[0], record[1]]
        for i in range(len(liste_pays_uniques)):
            row.append(0)
        
        liste_pays = record[2]
        for pays in liste_pays:
            idx = cols.index(pays)
            row[idx] += 1
        
        sheet.append(row)

def create_excel(path):
    # on récupère la liste des identifiants valides
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="brc_db")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    wb = Workbook()
    sheet_error(wb, cursor, "depots_par_annee.sql", "recettes_eclatees")

    del wb["Sheet"]
    wb.save(str(path))

create_excel("/home/calvin/Documents/analyse_pays_qui_deposent_mariana.xlsx")
