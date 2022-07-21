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
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def write_sheet(wb, name, dico, legende):
    sheet = wb.create_sheet(name)
    sheet.append(legende)

    for elmt in dico:
        sheet.append(elmt)

    #style_sheet(sheet)

def main():
    cursor = get_cursor("restart_db_pure")
    cursor_cured = get_cursor("restart_db_cured")

    cursor.execute('SELECT * FROM t_planification ORDER BY xxx_id')
    souches = cursor.fetchall()

    cursor_cured.execute('SELECT * FROM t_planification ORDER BY xxx_id')
    souches_cured = cursor_cured.fetchall()

    # dont on extrait les ids
    ids = [record[0] for record in souches]
    ids_curated = [record[0] for record in souches_cured]

    # pour vérifier qu'autant de milieux après et avant
    print("Nombre de planification avant : "+str(len(ids)))
    print("Nombre de planification après : "+str(len(ids_curated)))
    print("")

    ids_planification_disparus = []
    ids_planification_apparus = []

    for id_c in ids_curated:
        if id_c not in ids:
            ids_planification_disparus.append(id_c)

    print("ids_planification_disparus")
    print(ids_planification_disparus)
    print("")

    for id in ids:
        if id not in ids_curated:
            ids_planification_apparus.append(id)

    print("ids_planification_apparus")
    print(ids_planification_apparus)
    print("")

    planifications_archives = []
    c = 0
    for id in ids:
        idx = ids.index(id)
        idx_cured = ids_curated.index(id)

        if souches[idx] != souches_cured[idx_cured]:
            if souches[idx][:len(souches[idx])-1] == souches_cured[idx][:len(souches[idx])-1]:
                cursor.execute("SELECT usr_nom, usr_prenom FROM t_utilisateur WHERE xxx_id = "+str(souches[idx][-1]))
                nom_pure = cursor.fetchone()
                cursor.execute("SELECT usr_nom, usr_prenom FROM t_utilisateur WHERE xxx_id = "+str(souches_cured[idx][-1]))
                nom_cured = cursor.fetchone()

                row = [souches[idx][0], souches_cured[idx_cured][0], nom_pure[0], nom_pure[1], nom_cured[0], nom_cured[1]]
                planifications_archives.append(row)
            else:
                print('AIE')

        if c%1000 == 0:
            print(c)
        c += 1
    
    wb = Workbook()
    write_sheet(wb, "lots_archives", planifications_archives, ["old_id", "new_id", "Ancien nom", "Ancien prénom", "Nouveau nom", "Nouveau prénom"])
    del wb["Sheet"]
    wb.save(str("../../output/bloc_5/changements_sur_les_planifications.xlsx"))

main()
