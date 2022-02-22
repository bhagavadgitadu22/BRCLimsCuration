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
    cursor_curated = get_cursor("restart_db_cured")

    cursor.execute('SELECT * FROM t_lot ORDER BY xxx_id')
    souches = cursor.fetchall()

    cursor_curated.execute('SELECT * FROM t_lot ORDER BY xxx_id')
    souches_curated = cursor_curated.fetchall()

    # dont on extrait les ids
    ids = [record[0] for record in souches]
    ids_curated = [record[0] for record in souches_curated]

    # pour vérifier qu'autant de lots après et avant
    print("Nombre de lots avant : "+str(len(ids)))
    print("Nombre de lots après : "+str(len(ids_curated)))
    print("")

    ids_lots_disparus = []
    ids_lots_apparus = []
    ids_lots_modifies = []

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

    c = 0
    for id in ids:
        idx = ids.index(id)

        if souches[idx] != souches_curated[idx]:
            ids_lots_modifies.append(id)

        if c%1000 == 0:
            print(c)
        c += 1

    print("ids_lots_modifies")
    print(ids_lots_modifies)
    print("")

    # puis l'on compare les éléments un par un
    lots_archives = []

    sql_lot = 'SELECT t_souche.xxx_id, sch_identifiant, sch_version, t_lot.xxx_id, lot_numero, t_lot.xxx_sup_dat, don_lib, lot_qte_stock FROM t_lot LEFT JOIN t_souche ON lot_sch_id = t_souche.xxx_id LEFT JOIN t_donneedico ON lot_type = t_donneedico.xxx_id'

    for id in ids_lots_modifies:
        cursor.execute(sql_lot+' WHERE t_lot.xxx_id = '+str(id))
        record_pure = cursor.fetchone()

        cursor_curated.execute(sql_lot+' WHERE t_lot.xxx_id = '+str(id))
        record_cured = cursor_curated.fetchone()

        if record_pure[5] != record_cured[5]:
            # lot supprimé car c'était une fiche de spécification
            lots_archives.append([record_pure[1], record_pure[2], record_pure[4], record_pure[5], record_pure[6], record_pure[7]])
            bool = True
        if not(bool):
            print("bizarre, vraiment bizarre...")
    
    wb = Workbook()
    write_sheet(wb, "lots_archives", lots_archives, ["Ancien identifiant", "Ancienne version", "Ancien numéro de lot", "Ancienne date de suppression du lot", "Ancien type de lot", "Ancienne quantité"])
    del wb["Sheet"]
    wb.save(str("../../output/changements_sur_les_lots.xlsx"))

main()
