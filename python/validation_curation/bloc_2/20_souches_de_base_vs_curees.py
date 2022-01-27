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
                                  password="postgres",
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

    cursor = get_cursor("brc_db_pure")
    cursor_curated = get_cursor("brc_db_cured")

    name = ["historique", "refs_equis", "localisation", "bibliographie", "denomination", "temps_culture", "temp_incubation", "basonyme", "deposant"]
    legendes = {}
    differences = {}
    for elmt in name:
        legendes[elmt] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur"]
        differences[elmt] = []
    legendes["localisation"] = ["Ancienne localisation", "Nouvelle localisation", "Ancien lieu précis", "Nouveau lieu précis"]

    str_base = open("../curation_bloc_2/validation_curation/20_toutes_souches_avec_infos.sql", "r").read()

    i = 0
    for row in rows:
        id_cip = row[0]

        cursor.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record = cursor.fetchone()

        cursor_curated.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record_curated = cursor_curated.fetchone()

        identifiant_cip = record[22]
        version = str(record[28])

        bool = False

        # historique
        if record[68] != record_curated[68]:
            differences["historique"].append([identifiant_cip, version, record[68], record_curated[68]])
            bool = True

        # refs_equis
        if record[27] != record_curated[27]:
            differences["refs_equis"].append([identifiant_cip, version, record[27], record_curated[27]])
            bool = True

        # localisation
        if record[83] != record_curated[83] or record[47] != record_curated[47]:
            rep = [identifiant_cip, version, record[83], record_curated[83], record[47], record_curated[47]]
            differences["localisation"].append(rep)
            bool = True

        # bibliographie
        if record[59] != record_curated[59]:
            differences["bibliographie"].append([identifiant_cip, version, str(record[59]), str(record_curated[59])])
            bool = True

        # denomination
        if record[25] != record_curated[25]:
            differences["denomination"].append([identifiant_cip, version, str(record[25]), str(record_curated[25])])
            bool = True

        # temps_culture
        if record[43] != record_curated[43]:
            differences["temps_culture"].append([identifiant_cip, version, str(record[43]), str(record_curated[43])])
            bool = True

        # temp_incubation
        if record[44] != record_curated[44]:
            differences["temp_incubation"].append([identifiant_cip, version, str(record[44]), str(record_curated[44])])
            bool = True

        # basonyme
        if record[len(record)-1] != record_curated[len(record)-1]:
            row = [identifiant_cip, version, str(record[len(record)-1]), str(record_curated[len(record)-1])]
            baso = record[len(record)-1]
            dico = record[len(record)-2]
            baso_cured = record_curated[len(record)-1]
            dico_cured = record_curated[len(record)-2]
            for i_baso in range(len(baso)):
                if baso[i_baso] != baso_cured[i_baso]:
                    row.append(str(dico[i_baso]))
                    row.append(str(baso[i_baso]))
                    row.append(str(dico_cured[i_baso]))
                    row.append(str(baso_cured[i_baso]))
            differences["basonyme"].append(row)
            bool = True

        # deposant
        if record[len(record)-5] != record_curated[len(record)-5]:
            differences["deposant"].append([identifiant_cip, version, str(record[len(record)-5]), str(record_curated[len(record)-5])])
            bool = True

        # on s'occupe de souches qui ont d'autres champs qui différent pour comprendre ce qui cloche
        if not(bool):
            print(identifiant_cip)
            for i_record in range(len(record)):
                if record[i_record] != record_curated[i_record]:
                    print(i_record)
                    print(record[i_record])
                    print(record_curated[i_record])
                    print("")

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
