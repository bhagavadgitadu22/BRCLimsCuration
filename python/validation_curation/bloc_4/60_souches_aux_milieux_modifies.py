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
    cursor_curated = get_cursor("restart_db_cured2")

    str_mil = 'SELECT t_milieu_souche.xxx_id AS inter_id, t_milieu.xxx_id AS milieu_id, mil_numero, mil_designation_fr, mil_designation_en, t_souche.xxx_id AS souche_id, sch_identifiant, sch_version FROM t_milieu_souche JOIN t_milieu ON msc_mil_id = t_milieu.xxx_id JOIN t_souche ON msc_sch_id = t_souche.xxx_id'
    cursor.execute(str_mil)
    souches = cursor.fetchall()
    cursor_curated.execute(str_mil)
    souches_curated = cursor_curated.fetchall()

    # dont on extrait les ids
    ids = [record[0] for record in souches]
    ids_curated = [record[0] for record in souches_curated]

    inter_suppr = []
    inter_modif = []

    c = 0
    for id in ids:
        idx = ids.index(id)

        if id not in ids_curated:
            row_suppr = [elmt for elmt in souches[idx]]
            inter_suppr.append(row_suppr)
        else:
            idx_curated = ids_curated.index(id)

            if souches[idx] != souches_curated[idx_curated]:
                row_modif = []
                for ij in range(len(souches[idx])):
                    row_modif.append(souches[idx][ij])
                    row_modif.append(souches_curated[idx_curated][ij])
                inter_modif.append(row_modif)

        if c%1000 == 0:
            print(c)
        c += 1

    for id_curated in ids_curated:
        if id_curated not in ids:
            print("bizarre, vraiment bizarre...")

    wb = Workbook()

    legende = ["inter_id", "milieu_id", "mil_numero", "mil_designation_fr", "mil_designation_en", "souche_id", "sch_identifiant", "sch_version"]
    legende_long = []
    for l in legende:
        legende_long.append(l)
        legende_long.append(l+"_cured")
        
    write_sheet(wb, "inter_suppr", inter_suppr, legende)
    del wb["Sheet"]

    write_sheet(wb, "inter_modif", inter_modif, legende_long)
    wb.save(str("../../output/bloc_4/changements_sur_les_inters_milieux.xlsx"))

main()
