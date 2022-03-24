from decimal import ROUND_DOWN
import psycopg2
import csv
from openpyxl.workbook.workbook import Workbook
from openpyxl.styles import Border, Side, Alignment, Font

def redimension_cell_width(ws):
    dims = {}
    for row in ws.rows:
        for cell in row:
            if cell.value:
                # longueur max parmi != lignes de cellule
                line_max = max([len(str(elmt)) for elmt in str(cell.value).split('\n')])
                # cell.column_letter correspond à la taille que ça a de par les lignes précédentes déjà analysées
                # on garde donc max taille entre cellules précédentes et celle analysée
                max_ = max((dims.get(cell.column_letter, 0), line_max))
                dims[cell.column_letter] = min(max_, 100)
    for col, value in dims.items():
        ws.column_dimensions[col].width = value

def borders_cells(sheet):
    thin = Side(border_style="thin", color="000000")

    for row in sheet.rows:
        for cell in row:
            if cell.value:
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)

def wrap_lines(sheet):
    for row in sheet.rows:
        for cell in row:
            cell.alignment = Alignment(wrapText=True)

def style_sheet(sheet):
    header = list(sheet.rows)[0]
    for cell in header:
        cell.font  = Font(bold=True)
    
    wrap_lines(sheet)
    redimension_cell_width(sheet)
    borders_cells(sheet)

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def write_sheet(wb, name, legende, dico):
    sheet = wb.create_sheet(name)
    sheet.append(legende)

    for elmt in dico:
        sheet.append(elmt)

    style_sheet(sheet)

def write_excel(name, legendes, differences):
    wb = Workbook()

    for elmt in name:
        write_sheet(wb, elmt, legendes[elmt], differences[elmt])

    del wb["Sheet"]
    wb.save(str("../../output/bilan_lexicographique_isole_a_partir_de.xlsx"))

def main():
    f = open('../../output/cip_modifies.csv', 'r', newline='')
    rows = list(csv.reader(f, delimiter=';'))

    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    name = ["Human", "Environment", "Food", "Animal", "Plant"]
    legendes = {}
    differences = {}
    for elmt in name:
        legendes[elmt] = ["Isolé à partir de", "Nombre de souches affectées", 'Souches affectées']
        differences[elmt] = {}

    str_base = open("../curation_bloc_3/validation_curation/20_toutes_souches_avec_infos.sql", "r").read()

    i = 0
    for row in rows:
        id_cip = row[0]

        cursor.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record = cursor.fetchone()

        cursor_curated.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record_curated = cursor_curated.fetchone()

        identifiant_cip = record[22]
        version = str(record[28])

        alpha = 1

        # origine
        if record[len(record)-5-alpha] != record_curated[len(record)-5-alpha]:
            for terme in name:
                if record_curated[len(record)-5-alpha] == terme and terme.lower() not in record_curated[69].lower():
                    if record_curated[69] not in differences[terme]:
                        differences[terme][record_curated[69]] = []
                    differences[terme][record_curated[69]].append(str(identifiant_cip)+' version '+str(version))

        if i%1000 == 0:
            print(str(i)+" souches traitees")
        i+=1

    differences_triees = {}
    for elmt in name:
        differences_triees[elmt] = []

        for key in differences[elmt]:
            nombre_value = len(differences[elmt][key])
            str_value = ""
            for value in differences[elmt][key]:
                if str_value != "":
                    str_value += ", "
                str_value += value
            line = [key, str(nombre_value), str_value]
            differences_triees[elmt].append(line)

    write_excel(name, legendes, differences_triees)

main()
