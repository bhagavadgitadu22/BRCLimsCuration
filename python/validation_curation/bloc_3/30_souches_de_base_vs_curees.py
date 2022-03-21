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
    cursor_curated = get_cursor("restart_db_cured2")

    name = ["taxonomie", "isole_a_partir_de_translated", "isole_a_partir_de_trimmed", "origine", "refs_equis", "strain_designation"]
    legendes = {}
    legendes["taxonomie"] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur"]
    legendes["isole_a_partir_de_translated"] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur", "Ancienne origine", "Nouvelle origine"]
    legendes["isole_a_partir_de_trimmed"] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur", "Ancienne origine", "Nouvelle origine"]
    legendes["origine"] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur", "Ancien isolé à partir de", "Nouveau isolé à partir de"]
    legendes["refs_equis"] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur", "Suppressions", "Ajouts", "Historique"]
    legendes["strain_designation"] = ["Identifiant CIP", "Version", "Ancienne valeur", "Nouvelle valeur", "Historique", "Collection de souche", "Collection de valeur", "Check collection", "Ancien dico", "Nouveau dico", "Ancienne string_val", "Nouvelle string_val"]
    differences = {}
    for elmt in name:
        differences[elmt] = []

    str_base = open("../curation_bloc_3/validation_curation/20_toutes_souches_avec_infos.sql", "r").read()

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

        alpha = 1

        # taxonomie
        if record[len(record)-7-alpha] != record_curated[len(record)-7-alpha]:
            differences["taxonomie"].append([identifiant_cip, version, record[len(record)-8-alpha], record_curated[len(record)-8-alpha]])

        # isole_a_partir_de
        if record[69] != record_curated[69]:
            if record[69].replace(' ', '').replace('*', '').replace('\\n', '').lower() != record_curated[69].replace(' ', '').replace('*', '').replace('\\n', '').lower():
                differences["isole_a_partir_de_translated"].append([identifiant_cip, version, record[69], record_curated[69], record[len(record)-5-alpha], record_curated[len(record)-5-alpha]])
            else:
                differences["isole_a_partir_de_trimmed"].append([identifiant_cip, version, record[69], record_curated[69], record[len(record)-5-alpha], record_curated[len(record)-5-alpha]])

        # origine
        if record[len(record)-5-alpha] != record_curated[len(record)-5-alpha]:
            differences["origine"].append([identifiant_cip, version, record[len(record)-5-alpha], record_curated[len(record)-5-alpha], record[69], record_curated[69]])

        # refs_equis
        if record[27] != record_curated[27]:
            break_cured = record_curated[27].split(";")
            break_pure = record[27].split(";")

            add = []
            for elmt_break in break_cured:
                if elmt_break not in break_pure:
                    add.append(elmt_break)

            sup = []
            for elmt_break in break_pure:
                if elmt_break not in break_cured and elmt_break != '':
                    sup.append(elmt_break)

                    words = elmt_break.split(' ')
                    for w in words:
                        if w not in bilan_words:
                            bilan_words[w] = 0
                        bilan_words[w] += 1

            differences["refs_equis"].append([identifiant_cip, version, record[27], record_curated[27], str(sup), str(add), record[68]])

        #strain_designation
        if record[len(record)-1-alpha] != record_curated[len(record)-1-alpha]:
            row = [identifiant_cip, version]

            baso = record[len(record)-1-alpha]
            dico = record[len(record)-2-alpha]
            baso_cured = record_curated[len(record)-1-alpha]
            dico_cured = record_curated[len(record)-2-alpha]

            coll_souche = record_curated[len(record)-11-alpha]
            coll_cured = record_curated[len(record)-alpha]

            for i_baso in range(len(baso_cured)):
                if i_baso >= len(baso):
                    if baso_cured[i_baso] != "":
                        row.append("xxx")
                        row.append(str(baso_cured[i_baso]))
                        row.append(record[68])
                        row.append(coll_souche)
                        row.append(str(coll_cured[i_baso]))
                        row.append(coll_souche == coll_cured[i_baso])
                        row.append("xxx")
                        row.append(str(dico_cured[i_baso]))
                elif baso[i_baso] != baso_cured[i_baso]:
                    row.append(str(baso[i_baso]))
                    row.append(str(baso_cured[i_baso]))
                    row.append(record[68])
                    row.append(coll_souche)
                    row.append(str(coll_cured[i_baso]))
                    row.append(coll_souche == coll_cured[i_baso])
                    row.append(str(dico[i_baso]))
                    row.append(str(dico_cured[i_baso]))
            row.append(str(record[len(record)-1-alpha]))
            row.append(str(record_curated[len(record)-1-alpha]))

            differences["strain_designation"].append(row)

        # on s'occupe de souches qui ont d'autres champs qui différent pour comprendre ce qui cloche
        if record[len(record)-10-alpha:] == record_curated[len(record)-10:] and record[12] == record_curated[12] and record[69] == record_curated[69] and record[13] == record_curated[13] and record[27] == record_curated[27]:
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
        legendes_uniques[elmt] = legendes[elmt][2:]
        differences_uniques[elmt] = []
    for elmt in name:
        for diff in differences[elmt]:
            if diff[2:] not in differences_uniques[elmt]:
                differences_uniques[elmt].append(diff[2:])
    
    write_excel(name, legendes_uniques, differences_uniques, "bilan_curation_lignes_uniques")

    rows_words = []
    for w in bilan_words:
        row = [w, bilan_words[w]]
        print(row)
        rows_words.append(row)
    f_vides = open('../../output/bilan_words.csv', 'w', encoding="utf-8", newline='')
    writer_vides = csv.writer(f_vides, delimiter=';')
    writer_vides.writerows(rows_words)
    f_vides.close()

main()
