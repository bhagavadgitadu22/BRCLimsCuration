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

def write_sheet(wb, name, dico):
    sheet = wb.create_sheet(name)
    sheet.append(["Identifiant", "Numéro de lot", "Ancien lieu", "Ancienne case", "Nouveau lieu", "Nouvelle case", "Ancien type de stockage", "Nouveau type de stockage"])

    for elmt in dico:
        sheet.append(elmt)

    style_sheet(sheet)

def main():
    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    cursor.execute(open("../curation/10_fonctions/10_custom_order.sql", "r").read())
    cursor_curated.execute(open("../curation/10_fonctions/10_custom_order.sql", "r").read())

    cursor.execute(open("../curation/validation_curation/40_emplacements_lots.sql", "r").read())
    souches = cursor.fetchall()

    cursor_curated.execute(open("../curation/validation_curation/40_emplacements_lots.sql", "r").read())
    souches_curated = cursor_curated.fetchall()

    # dont on extrait les ids
    ids = [record[2] for record in souches]
    ids_curated = [record[2] for record in souches_curated]

    # pour vérifier qu'autant de lots après et avant
    print("Nombre de lots avant : "+str(len(ids)))
    print("Nombre de lots après : "+str(len(ids_curated)))
    print("")

    ids_lots_disparus = []
    ids_lots_apparus = []

    for id_c in ids_curated:
        if id_c not in ids:
            ids_lots_disparus.append(id_c)

    print("ids_lots_disparus")
    print(ids_lots_disparus)
    print("")

    for id in ids:
        if id not in ids_curated:
            ids_lots_apparus.append(id)

    print("ids_lots_apparus")
    print(ids_lots_apparus)
    print("")

    # puis l'on compare les éléments un par un
    differences = []
    differences_accidentelles = []

    for id in ids:
        if id not in ids_lots_disparus and id not in ids_lots_apparus:
            idx_pure = ids.index(id)
            idx_cured = ids_curated.index(id)

            record_pure = souches[idx_pure]
            record_cured = souches_curated[idx_cured]

            if record_pure != record_cured:
                if record_pure[1] != 401 or record_cured[1] != 401:
                    differences_accidentelles.append([record_pure[0], record_pure[3], record_pure[5], record_pure[6], record_cured[5], str(record_cured[6]), record_pure[7], record_cured[7]])
                else:
                    differences.append([record_pure[0], record_pure[3], record_pure[5], record_pure[6], record_cured[5], str(record_cured[6]), record_pure[7], record_cured[7]])

    print("differences_accidentelles")
    print(differences_accidentelles)
    print("")

    ids = []
    for elmt in differences:
        if elmt[0] not in ids:
            ids.append(elmt[0])
    chaine_ids = '('+str(ids).strip('[]')+')'
    cursor.execute("SELECT sch_identifiant FROM t_souche WHERE sch_identifiant IN "+chaine_ids+" GROUP BY sch_identifiant ORDER BY custom_sort(sch_identifiant::text)")
    records = cursor.fetchall()
    ids_new = [record[0] for record in records]

    new_differences = []
    for id_new in ids_new:
        for diff in differences:
            if diff[0] == id_new:
                new_differences.append(diff)
    
    wb = Workbook()
    write_sheet(wb, "emplacements", new_differences)
    del wb["Sheet"]
    wb.save(str("../../output/changements_emplacements_lots.xlsx"))

main()
