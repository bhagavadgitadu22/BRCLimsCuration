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

def write_sheet(wb, name, dico, legende):
    sheet = wb.create_sheet(name)
    sheet.append(legende)

    for elmt in dico:
        sheet.append(elmt)

    #style_sheet(sheet)

def main():
    cursor_curated = get_cursor("restart_db_cured2")

    f = open('../../output/souches_creees.csv', 'r', newline='')
    records = csv.reader(f, delimiter=';')
    ids_souches_apparues = [record[0] for record in records]
    f.close()

    # puis l'on compare les éléments un par un
    sql_care = 'SELECT sch_identifiant, sch_dat_acquisition, sch_denomination, path, sch_proprietes, \
					  t_origine.don_lib, pto_lib, sch_isole_a_partir_de, t_lieu.don_lib, sch_dat_prelevement, \
					  sch_bibliographie, sch_temperature_incubation, sch_historique, t_deposant.don_lib, \
					  t_souche.xxx_cre_usr_id, t_souche.xxx_maj_usr_id, sch_statut, sch_col_id FROM t_souche \
                      LEFT JOIN chemins_taxonomie ON t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie \
                      LEFT JOIN t_donneedico AS t_lieu ON t_lieu.xxx_id = t_souche.sch_lieu \
                      LEFT JOIN t_donneedico AS t_origine ON t_origine.xxx_id = t_souche.sch_origine \
                      LEFT JOIN t_donneedico AS t_deposant ON sch_depositaire = t_deposant.xxx_id \
                      LEFT JOIN t_pathogenicite ON t_pathogenicite.xxx_id = sch_pto_id'

    bilan =  []

    cursor_curated.execute(open("../curation_bloc_3/validation_curation/10_parenteles_taxonomie.sql", "r", encoding='utf-8').read())

    for id in ids_souches_apparues:
        cursor_curated.execute(sql_care+' WHERE t_souche.xxx_id = '+str(id))
        record_curated = cursor_curated.fetchone()

        bilan.append(record_curated)
    
    wb = Workbook()
    write_sheet(wb, "souches_apparues", bilan, ["Identifiant", "Date d'acquisition", "Dénomination", "Taxonomie", "Propriétés", 
                                                        "Origine", "Pathogénicité", "Isolé à partir de", "Lieu", "Date de prélèvement", 
                                                        "Bibliographie", "Tempréature d'incubation", "Historique", "Déposant", 
                                                        "xxx_cre_usr_id", "xxx_maj_usr_id", "sch_statut", "sch_col_id"])
    del wb["Sheet"]
    wb.save(str("../../output/apparitions_souches.xlsx"))

main()