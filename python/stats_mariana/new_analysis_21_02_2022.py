from openpyxl.workbook.workbook import Workbook
import psycopg2
from openpyxl.styles import Border, Side, Alignment, Font

def redimension_cell_width(ws):
    dims = {}
    for row in ws.rows:
        for cell in row:
            if cell.value:
                line_max = max([len(str(elmt)) for elmt in cell.value.split('\n')])
                max_ = max((dims.get(cell.column_letter, 0), line_max))
                dims[cell.column_letter] = max_
    for col, value in dims.items():
        ws.column_dimensions[col].width = value

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
    redimension_cell_width(sheet)
    borders_cells(sheet)

def sheet_error(wb, cursor):
    cursor.execute(open("../analyse/corynebacterium/corynebacterium_antibios_mariana_new.sql", "r").read())
    records = cursor.fetchall()

    sheet = wb.create_sheet("antibios_coryne")

    # on s'occupe des colonnes du fichier de klebsiella
    cols = ["Id", "Souche", "Denomination"]
    antibios = []
    for record in records:
        liste = record[9]
        for elmt in liste:
            if elmt is not None and elmt not in antibios:
                antibios.append(elmt)
    
    antibios_sorted = sorted(antibios)

    for elmt in antibios_sorted:
        cols.append(elmt)
        cols.append('Diamètre')
    print(cols)
    sheet.append(cols)

    # puis on remplit ces colonnes
    for record in records:
        row = [record[0], record[1], record[2]]
        for elmt in antibios_sorted:
            row.append("")
            row.append("")

        noms_antibios = record[9]
        resultats_antibios = record[10]
        diametres_antibios = record[11]
        
        if not(len(noms_antibios) == 1 and noms_antibios[0] is None):
            for i in range(len(noms_antibios)):
                idx = cols.index(noms_antibios[i])

                if resultats_antibios is not None:
                    row[idx] = resultats_antibios[i]

                row[idx+1] = diametres_antibios[i]

        sheet.append(row)

def create_excel(path):
    # on récupère la liste des identifiants valides
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="brc_db")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    wb = Workbook()
    sheet_error(wb, cursor)

    del wb["Sheet"]
    wb.save(str(path))

create_excel(r"C:\Users\Public\Documents\analyse_antibios_coryne.xlsx") 
