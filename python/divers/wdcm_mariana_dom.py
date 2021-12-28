import pandas as pd
import psycopg2
import re

wdcm_normes = pd.ExcelFile(r"e:\Users\Proprietaire\Downloads\Normes et WDM souches_DC.xlsx")
wdcm_mariana = pd.ExcelFile(r'e:\Users\Proprietaire\Downloads\211227_WDCM_Panel_MF.xlsx')

# je lis mon fichier ligne par ligne pour choper les infos des identifiants, pour sheet 1 puis 2
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
            short_wdcm = 'WDCM '+str(int(res.group(1)))
            
            if short_wdcm not in normes_eclates:
                normes_eclates[short_wdcm] = []
            if norme not in normes_eclates[short_wdcm]:   
                normes_eclates[short_wdcm].append(norme)
            
            if short_wdcm not in tests_eclates:
                tests_eclates[short_wdcm] = []
            if test not in tests_eclates[short_wdcm]:   
                tests_eclates[short_wdcm].append(test)

print(normes_eclates)
print(tests_eclates)

