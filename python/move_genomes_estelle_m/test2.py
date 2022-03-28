import os
import re
from openpyxl.workbook.workbook import Workbook
from openpyxl.styles import Border, Side, Alignment, Font

def test_match(pattern, file):
    id_cip = ''
    match = re.match(pattern, file)
    if match:
        id_cip = match.group(0)
    return id_cip

def redimension_cell_width(ws):
    dims = {}
    for row in ws.rows:
        for cell in row:
            if cell.value:
                line_max = max([len(str(elmt)) for elmt in str(cell.value).split('\n')])
                max_ = max((dims.get(cell.column_letter, 0), line_max))
                dims[cell.column_letter] = max_
    for col, value in dims.items():
        ws.column_dimensions[col].width = value

def style_sheet(sheet):
    header = list(sheet.rows)[0]
    for cell in header:
        cell.font  = Font(bold=True)
    
    redimension_cell_width(sheet)
    borders_cells(sheet)

def borders_cells(sheet):
    thin = Side(border_style="thin", color="000000")

    for col in sheet.rows:
        for cell in col:
            if cell.value:
                cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)

#local_path = '/mnt/gaia/cip'
local_path = 'X:'
path = local_path+'/SEQUENCAGETOTAL/FICHIERRESULTATSSEQUENCES'
dir_list = os.listdir(path)

pattern1 = '^(CIP)?-?[0-9]{6}T?'
pattern2 = '^(CIP)?[0-9]{1,2}(-|.)[0-9]+T?'
pattern3 = '^CRBIP[0-9]{1,3}-[0-9]+T?'
pattern4 = '^CIPA[0-9]{1,3}T?'

count = 0

# liste des dossiers à éviter car on préviligie copie
dossiers_copie = []
for file in dir_list:
    # on traite chaque dossier de p2m
    if os.path.isdir(os.path.join(path, file)) and file[0].isdigit() and "copie" in file.lower():
        dossiers_copie.append(file.replace("-Copie", ""))

print(dossiers_copie)