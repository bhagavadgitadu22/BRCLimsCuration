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
                line_max = max([len(str(elmt)) for elmt in cell.value.split('\n')])
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

def write_excel(name, legendes, differences, filename):
    wb = Workbook()

    for elmt in name:
        write_sheet(wb, elmt, legendes[elmt], differences[elmt])

    del wb["Sheet"]
    wb.save(str("../../output/"+filename+".xlsx"))

def main():
    f = open('../../output/cip_modifies.csv', 'r', newline='')
    rows = csv.reader(f, delimiter=';')

    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    name = ["historique", "localisation", "pathogenicite", "taxonomie", "temperature", "bibliographie"]
    legendes = {}
    differences = {}
    for elmt in name:
        legendes[elmt] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur"]
        differences[elmt] = []
    legendes["localisation"] = ["Identifiant CIP", "Version", "Ancienne localisation", "Nouvelle localisation", "Ancien lieu précis", "Nouveau lieu précis"]

    str_base = open("../curation_bloc_1/validation_curation/25_toutes_souches_avec_infos.sql", "r").read()

    i = 0
    for row in rows:
        id_cip = row[0]

        cursor.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record = cursor.fetchone()

        cursor_curated.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record_curated = cursor_curated.fetchone()

        identifiant_cip = record[22]
        version = str(record[28])

        # 40_historique_bacillus
        if record[68].replace(" ", "") != record_curated[68].replace(" ", ""):
            differences["historique"].append([identifiant_cip, version, record[68], record_curated[68]])

        # 50_localisation
        if record[len(record)-11] != record_curated[len(record)-11] or record[47] != record_curated[47]:
            rep = [identifiant_cip, version, record[len(record)-11], record_curated[len(record)-11], record[47], record_curated[47]]

            differences["localisation"].append(rep)

        # 60_pathogenicite
        if record[len(record)-2] != record_curated[len(record)-2]:
            differences["pathogenicite"].append([identifiant_cip, version, str(record[len(record)-2]), str(record_curated[len(record_curated)-2])])

        # 80_taxonomie
        if record[len(record)-6] != record_curated[len(record)-6]:
            differences["taxonomie"].append([identifiant_cip, version, record[len(record)-6], record_curated[len(record_curated)-6]])

        # 90_temperature
        if record[44] != record_curated[44]:
            differences["temperature"].append([identifiant_cip, version, str(record[44]), str(record_curated[44])])

        # 100_bibliographie
        if record[59].replace(" ", "").replace("\n", "").replace("\r", "") != record_curated[59].replace(" ", "").replace("\n", "").replace("\r", ""):
            differences["bibliographie"].append([identifiant_cip, version, str(record[59]), str(record_curated[59])])

        if i%1000 == 0:
            print(str(i)+" souches traitees")
        i+=1

    write_excel(name, legendes, differences, "bilan_curation")

    legendes_uniques = {}
    differences_uniques = {}
    for elmt in name:
        legendes_uniques[elmt] = ["Ancienne valeur", "Nouvelle valeur"]
        differences_uniques[elmt] = []
    for elmt in name:
        for diff in differences[elmt]:
            if diff[2:] not in differences_uniques[elmt]:
                differences_uniques[elmt].append(diff[2:])
    legendes_uniques["localisation"] = ["Ancienne localisation", "Nouvelle localisation", "Ancien lieu précis", "Nouveau lieu précis"]

    write_excel(name, legendes_uniques, differences_uniques, "bilan_curation_lignes_uniques")

main()
