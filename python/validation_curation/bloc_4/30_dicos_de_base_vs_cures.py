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

def write_sheet(wb, name, dico):
    sheet = wb.create_sheet(name)
    sheet.append(["Identifiant", "Statut", "Ancienne valeur", "Nouvelle valeur"])

    for elmt in dico:
        sheet.append(elmt)

    style_sheet(sheet)

def write_excel(name, dicos, filename):
    wb = Workbook()

    for elmt in name:
        write_sheet(wb, elmt, dicos[elmt])

    del wb["Sheet"]
    wb.save(str("../../output/bloc_4/"+filename+".xlsx"))

def create_dico(records, records_curated):
    dico = []

    for row in records:
        id_taxo = row[0]

        for row_cured in records_curated:
            if row_cured[0] == id_taxo:
                status = 'same'
                if row[1] != row_cured[1] or row[2] != row_cured[2]:
                    status = 'modified'

                if row[2] is None and row_cured[2] is None:
                    dico.append([str(id_taxo), status, row[1], row_cured[1]])
                elif row[2] is not None and row_cured[2] is None:
                    dico.append([str(id_taxo), status, "xxx", row_cured[1]])
                elif row[2] is None and row_cured[2] is not None:
                    dico.append([str(id_taxo), status, row[1], "xxx"])
                records_curated.remove(row_cured)

    for row_cured in records_curated:
        dico.append([str(row_cured[0]), 'modified', "xxx", row_cured[1]])
    
    return dico

def main():
    name = ["taxonomie"]
    dicos = {}

    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    # taxonomie
    sql_taxo = "SELECT t_donneedico.xxx_id, don_lib, t_donneedico.xxx_sup_dat FROM t_donneedico JOIN t_dico ON don_dic_id = t_dico.xxx_id WHERE dic_nom = 'Taxonomie' AND dic_grp_collection = '[401]'"
    cursor.execute(sql_taxo)
    locs = cursor.fetchall()

    cursor_curated.execute(sql_taxo)
    locs_curated = cursor_curated.fetchall()

    dicos["taxonomie"] = create_dico(locs, locs_curated)

    write_excel(name, dicos, "bilan_curation_dicos")

main()
