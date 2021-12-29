import pandas as pd
from openpyxl.workbook.workbook import Workbook
import psycopg2
import re

wdcm_normes = pd.ExcelFile(r"e:\Users\Proprietaire\Downloads\Normes et WDM souches_DC.xlsx")

df_normes = pd.read_excel(wdcm_normes, "Feuil1")

normes_eclates = {}
tests_eclates = {}

prog = re.compile('WDCM ([0-9]+)')

for i in range(len(df_normes)):
    norme = df_normes.iloc[i, 0]
    test = df_normes.iloc[i, 1]
    wdcms = [elmt.strip() for elmt in df_normes.iloc[i, 2].split(';')]

    for wdcm in wdcms:
        if wdcm != '':
            res = prog.search(wdcm)
            # short_wdcm = 'WDCM '+str(int(res.group(1)))
            short_wdcm = wdcm
            
            if short_wdcm not in normes_eclates:
                normes_eclates[short_wdcm] = []
            if norme not in normes_eclates[short_wdcm]:   
                normes_eclates[short_wdcm].append(norme)
            
            if short_wdcm not in tests_eclates:
                tests_eclates[short_wdcm] = []
            if test not in tests_eclates[short_wdcm]:   
                tests_eclates[short_wdcm].append(test)

# print(normes_eclates)
# print(tests_eclates)

wdcm_mariana = pd.ExcelFile(r'e:\Users\Proprietaire\Downloads\211227_WDCM_Panel_MF.xlsx')

df_mar = pd.read_excel(wdcm_mariana, "Feuil1")

connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True

cursor = connection.cursor()

wb = Workbook()
sheet = wb.create_sheet("name")
sheet.append(["id", "wdcm", "normes", "tests", "commandes 10 ans"])

for i in range(len(df_mar)):
    souche_cip = df_mar.iloc[i, 0]
    if not(pd.isnull(souche_cip)):
        # print(souche_cip)

        str_sql = open("../analyse/corynebacterium/get_wdcm.sql", "r", encoding='utf-8').read()
        complement_sql = " WHERE (t_commande.xxx_id IS NULL OR EXTRACT(YEAR FROM cmd_dat) > 2010) AND sch_identifiant = '"+souche_cip+"' GROUP BY sch_identifiant, (REGEXP_MATCHES(sch_references_equi, 'WDCM ?([0-9]+)'))[1];"

        cursor.execute(str_sql+complement_sql)
        record = cursor.fetchone()

        row = [souche_cip]
        if record is not None:
            local_wdcm = 'WDCM '+record[1]
            local_norme = ''
            local_test = ''
            if local_wdcm in normes_eclates:
                local_norme = '\n'.join(normes_eclates[local_wdcm])
            if local_wdcm in tests_eclates:
                local_test = '\n'.join(tests_eclates[local_wdcm])

            row = [souche_cip, local_wdcm, local_norme, local_test, record[2]]
            # print(row)
        if record is None:
            print(souche_cip)
        
        sheet.append(row)

del wb["Sheet"]
wb.save(r"C:\Users\Public\Documents\bilan_wdcm_mariana.xlsx")

