from openpyxl.workbook.workbook import Workbook
import psycopg2
from openpyxl.styles import Border, Side, Alignment, Font

def borders_cells(sheet):
    thin = Side(border_style="thin", color="000000")

    for col in sheet.rows:
        for cell in col:
            if cell.value:
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)

def wrap_lines(sheet):
    for col in sheet.rows:
        col[0].alignment = Alignment(wrapText=True)

def style_sheet(sheet):
    header = list(sheet.rows)[0]
    for cell in header:
        cell.font  = Font(bold=True)
    
    wrap_lines(sheet)
    borders_cells(sheet)

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()


cursor = get_cursor("db")

liste_attributs = 'SELECT att_nom, att_typ FROM t_attribut GROUP BY att_nom, att_typ;'
cursor.execute(liste_attributs)
records = cursor.fetchall()
attributs = [[record[0].replace("'", "''"), record[1]] for record in records]

str_string = "SELECT col_descr, COUNT(*), ARRAY_AGG(svl_valeur) FROM t_attribut LEFT JOIN t_string_val ON svl_att_id = t_attribut.xxx_id JOIN t_collection ON att_col_id = t_collection.xxx_id WHERE att_nom = '"
str_date = "SELECT col_descr, COUNT(*), ARRAY_AGG(dvl_valeur) FROM t_attribut LEFT JOIN t_date_val ON dvl_att_id = t_attribut.xxx_id JOIN t_collection ON att_col_id = t_collection.xxx_id WHERE att_nom = '"
str_boolean = "SELECT col_descr, COUNT(*), ARRAY_AGG(bvl_valeur) FROM t_attribut LEFT JOIN t_boolean_val ON bvl_att_id = t_attribut.xxx_id JOIN t_collection ON att_col_id = t_collection.xxx_id WHERE att_nom = '"
str_memo = "SELECT col_descr, COUNT(*), ARRAY_AGG(mvl_valeur) FROM t_attribut LEFT JOIN t_memo_val ON mvl_att_id = t_attribut.xxx_id JOIN t_collection ON att_col_id = t_collection.xxx_id WHERE att_nom = '"
str_dico_liste = "SELECT col_descr, COUNT(*), ARRAY_AGG(dlv_valeur) FROM t_attribut LEFT JOIN t_dico_liste_val ON dlv_att_id = t_attribut.xxx_id JOIN t_collection ON att_col_id = t_collection.xxx_id WHERE att_nom = '"
str_end = "' GROUP BY col_descr;"

liste = {}
nom_cols = []
for elmt in attributs:
    attr = elmt[0]
    type = elmt[1]

    line = {}

    str_sql = ''
    if elmt == 0:
        str_sql = str_string + attr + str_end
    if elmt == 1:
        str_sql = str_date + attr + str_end
    if elmt == 2:
        str_sql = str_boolean + attr + str_end
    if elmt == 2:
        str_sql = str_memo + attr + str_end
    if elmt == 7:
        str_sql = str_dico_liste + attr + str_end
    if elmt == 8:
        str_sql = str_dico_liste + attr + str_end
    
    cursor.execute(str_sql)
    records2 = cursor.fetchall()

    for r in records2:
        line[r[0]] = r[1]

        if r[0] not in nom_cols:
            nom_cols.append(r[0])

    liste[attr] = line

wb = Workbook()
sheet = wb["Sheet"]

cols = ['Attribut', 'Total']
nom_cols.sort()
for nc in nom_cols:
    cols.append(nc)
sheet.append(cols)

for attr in liste:
    row = [attr, 0]
    total = 0

    for nc in nom_cols:
        row.append(0)

    for coll in liste[attr]:
        idx = nom_cols.index(coll)
        row[idx+2] = liste[attr][coll]
        total += liste[attr][coll]

    row[1] = total
    sheet.append(row)

style_sheet(sheet)
wb.save('../../output/attr_persos.xlsx')
