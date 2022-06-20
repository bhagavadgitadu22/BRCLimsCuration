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
    wb.save(str("../../output/bloc_5/"+filename+".xlsx"))

def main():
    f = open('../../output/bloc_5/cip_modifies.csv', 'r', newline='')
    rows = csv.reader(f, delimiter=';')

    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    name = ["article", "taxonomie", "localisation", "isole_a_partir_de", "genome_1546", "featured_collections"]
    legendes = {}
    legendes["article"] = ["Identifiant CIP", "Version", "Ancien article", "Nouvel article"]
    legendes["taxonomie"] = ["Identifiant CIP", "Version", "Ancienne taxonomie", "Nouvelle taxonomie"]
    legendes["localisation"] = ["Identifiant CIP", "Version", "Ancien pays", "Nouveau pays", "Ancien lieu précis", "Nouveau lieu précis", "Ancien dico", "Nouveau dico"]
    legendes["isole_a_partir_de"] = ["Identifiant CIP", "Version", "Ancienne origine", "Nouvelle origine", "Ancien isolé à partir de", "Nouveau isolé à partir de"]
    legendes["genome_1546"] = ["Identifiant CIP", "Version", "Ancien code", "Nouveau code", "Ancien résultat", "Nouveau résultat", "Ancien commentaire", "Nouveau commentaire"]
    legendes["featured_collections"] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur"]
    differences = {}
    for elmt in name:
        differences[elmt] = []

    str_base = open("../curation_bloc_5/validation_curation/20_toutes_souches_avec_infos.sql", "r").read()

    i = 0
    bilan_words = {}
    for row in rows:
        id_cip = row[0]

        cursor.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record = cursor.fetchone()

        cursor_curated.execute(str_base+" WHERE t_souche.xxx_id = "+id_cip)
        record_curated = cursor_curated.fetchone()

        identifiant_cip = record[22]
        version = str(record[28])

        # taxonomie
        if record[len(record)-20] != record_curated[len(record)-20]:
            differences["article"].append([identifiant_cip, version, record[len(record)-20], record_curated[len(record)-20]])

        # taxonomie
        if record[len(record)-16] != record_curated[len(record)-16]:
            differences["taxonomie"].append([identifiant_cip, version, record[len(record)-16], record_curated[len(record)-16]])

        # localisation
        if record[len(record)-10] != record_curated[len(record)-10] or record[47] != record_curated[47]:
            differences["localisation"].append([identifiant_cip, version, record[len(record)-10], record_curated[len(record)-10], record[47], record_curated[47], record[len(record)-9], record_curated[len(record)-9]])

        # isole_a_partir_de
        if record[len(record)-13] != record_curated[len(record)-13] or record[69] != record_curated[69]:
            differences["isole_a_partir_de"].append([identifiant_cip, version, record[len(record)-13], record_curated[len(record)-13], record[69], record_curated[69]])

        # genome_1546
        if record[len(record)-1] != record_curated[len(record)-1] or record[len(record)-2] != record_curated[len(record)-2]:
            row = [identifiant_cip, version]
            
            codes = record[len(record)-3]
            resultats = record[len(record)-2]
            commentaires = record[len(record)-1]
            
            codes_cured = record_curated[len(record)-3]
            resultats_cured = record_curated[len(record)-2]
            commentaires_cured = record_curated[len(record)-1]

            for i_elmt in range(len(codes_cured)):
                code_cured = codes_cured[i_elmt]

                if codes is None or code_cured not in codes:
                    if resultats_cured[i_elmt] != "" or commentaires_cured[i_elmt] != "":
                        row.append("xxx")
                        row.append(codes_cured[i_elmt])
                        row.append("xxx")
                        row.append(resultats_cured[i_elmt])
                        row.append("xxx")
                        row.append(commentaires_cured[i_elmt])
                else:
                    i_elmt_pure = codes.index(code_cured)
                    if resultats[i_elmt_pure] != resultats_cured[i_elmt] or commentaires[i_elmt_pure] != commentaires_cured[i_elmt]:
                        row.append(codes[i_elmt_pure])
                        row.append(codes_cured[i_elmt])
                        row.append(resultats[i_elmt_pure])
                        row.append(resultats_cured[i_elmt])
                        row.append(commentaires[i_elmt_pure])
                        row.append(commentaires_cured[i_elmt])
            differences["genome_1546"].append(row)

        # featured_collections
        if record[len(record)-6] != record_curated[len(record)-6]:
            row = [identifiant_cip, version]

            baso = record[len(record)-6]
            dico = record[len(record)-7]
            baso_cured = record_curated[len(record)-6]
            dico_cured = record_curated[len(record)-7]

            coll_souche = record_curated[len(record)-19]
            coll_cured = record_curated[len(record)-5]

            for i_baso in range(len(baso_cured)):
                if i_baso >= len(baso):
                    if baso_cured[i_baso] != "":
                        row.append("xxx")
                        row.append(str(baso_cured[i_baso]))
                        row.append(coll_souche == coll_cured[i_baso])
                        row.append("xxx")
                        row.append(str(dico_cured[i_baso]))
                elif baso[i_baso] != baso_cured[i_baso]:
                    row.append(str(baso[i_baso]))
                    row.append(str(baso_cured[i_baso]))
                    row.append(coll_souche == coll_cured[i_baso])
                    row.append(str(dico[i_baso]))
                    row.append(str(dico_cured[i_baso]))

            differences["featured_collections"].append(row)

        idx_modified = [len(record)-20, len(record)-16, len(record)-10, len(record)-9, 47, len(record)-13, len(record)-12, 69, len(record)-1, len(record)-2, len(record)-3, len(record)-6, len(record)-5, len(record)-7, len(record)-15, len(record)-17, len(record)-11, 15, len(record)-14, 13, 12, len(record)-4]
        # on s'occupe de souches qui ont d'autres champs qui différent pour comprendre ce qui cloche
        for i_record in range(len(record)):
            if i_record not in idx_modified and record[i_record] != record_curated[i_record]:
                print(identifiant_cip)
                print(i_record)
                print(len(record)-i_record)
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
        legendes_uniques[elmt] = legendes[elmt][2:]
        differences_uniques[elmt] = []
    for elmt in name:
        for diff in differences[elmt]:
            if diff[2:] not in differences_uniques[elmt]:
                differences_uniques[elmt].append(diff[2:])
    
    write_excel(name, legendes_uniques, differences_uniques, "bilan_curation_lignes_uniques")

main()
