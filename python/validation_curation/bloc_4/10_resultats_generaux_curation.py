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

def get_all_souches(c):
    c.execute(open("../curation_bloc_4/validation_curation/0_toutes_souches.sql", "r").read())
    records = c.fetchall()
    
    return records

def main():
    # on établit les connections avec les 2 bdds
    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    # on récupère toutes les souches de la bdd
    souches = get_all_souches(cursor)
    souches_curated = get_all_souches(cursor_curated)

    # dont on extrait les ids
    # pour vérifier qu'il y a strictement moins d'ids après la curation
    ids = [record[0] for record in souches]
    ids_curated = [record[0] for record in souches_curated]

    schs_apparus = []

    i = 0
    for id_c in ids_curated:
        if id_c not in ids:
            schs_apparus.append(souches_curated[i])
        i += 1

    # on récupère les ids_supprimés de la cip
    # on lève une erreur s'il y a un id supprimé pas de cip
    schs_supprimes = []
    i = 0
    for id in ids:
        if id not in ids_curated:
            schs_supprimes.append(souches[i])
        i += 1

    print("ids_apparus")
    print([elmt[1] for elmt in schs_apparus])
    print("")
    print("ids_supprimes")
    print([elmt[1] for elmt in schs_supprimes])
    print("")

    # on sauvegarde les ids archivés dans un excel
    fa = open('../../output/bloc_4/souches_supprimees.csv', 'w', newline='')
    writera = csv.writer(fa, delimiter=';')
    writera.writerows(map(lambda x: [x], [elem[1] for elem in schs_supprimes]))
    fa.close()

    count_id_missing = 0

    # puis l'on prend la liste de ce que l'on a archivé
    schs_archives = []
    schs_archives_hors_cip = []
    i = 0
    for id in ids:
        if id in ids_curated:
            i_curated = ids_curated.index(id)

            if souches[i][3] is None and souches_curated[i_curated][3] is not None:
                if souches[i][2] == 401 and souches_curated[i_curated][2] == 401:
                    schs_archives.append(souches[i])
                else:
                    schs_archives_hors_cip.append(souches[i])
        else:
            count_id_missing += 1
        i += 1

    print("count_id_missing")
    print(count_id_missing)

    print("ids_archives")
    print([elmt[1] for elmt in schs_archives])
    print("")
    print("ids_archives_hors_cip")
    print([elmt[1] for elmt in schs_archives_hors_cip])
    print("")

    souches_a_garder = []
    for sch in souches:
        if sch not in schs_supprimes and sch not in schs_archives and sch not in schs_archives_hors_cip:
            souches_a_garder.append(sch)

    souches_a_garder_curated = []
    for sch_c in souches_curated:
        if sch_c not in schs_apparus:
            souches_a_garder_curated.append(sch_c)

    print("de "+str(len(souches))+" souches à "+str(len(souches_a_garder)))
    print("de "+str(len(souches_curated))+" souches curées à "+str(len(souches_a_garder_curated)))

    # et qu'aucun id hors de cip n'a été modifié
    # et pour récupérer les ids de cip modifiés et supprimés
    souches_modifiees = []
    souches_archives_modifiees = []
    souches_modifiees_hors_cip = []

    cursor.execute(open("../curation_bloc_4/validation_curation/10_parenteles_taxonomie.sql", "r").read())
    cursor_curated.execute(open("../curation_bloc_4/validation_curation/10_parenteles_taxonomie.sql", "r").read())
    str_base = open("../curation_bloc_4/validation_curation/20_toutes_souches_avec_infos.sql", "r").read()

    i = 0
    for sch in souches_a_garder:
        xxx_id = sch[0]
        cursor.execute(str_base+" WHERE t_souche.xxx_id = "+str(xxx_id))
        record = cursor.fetchone()

        cursor_curated.execute(str_base+" WHERE t_souche.xxx_id = "+str(xxx_id))
        record_curated = cursor_curated.fetchone()

        if record != record_curated:
            if record[len(record)-12] == 401 and record_curated[len(record_curated)-12] == 401:
                if record[7] is None:
                    souches_modifiees.append(record)
                else:
                    souches_archives_modifiees.append(record)
            else:
                souches_modifiees_hors_cip.append(record_curated)

        if i%1000 == 0:
            print(str(i)+" souches traitees")
        i+=1

    print("")
    print(str(len(souches_modifiees))+" modifiees de cip")
    print("")
    print(str(len(souches_archives_modifiees))+" archives modifiees")
    print([elem[22] for elem in souches_archives_modifiees])
    print("")
    print(str(len(souches_modifiees_hors_cip))+" modifiees hors cip")
    print([elem[22] for elem in souches_modifiees_hors_cip])

    f = open('../../output/bloc_4/cip_modifies.csv', 'w', newline='')
    writer = csv.writer(f, delimiter=';')
    writer.writerows(map(lambda x: [x], [elem[0] for elem in souches_modifiees]))
    f.close()

main()