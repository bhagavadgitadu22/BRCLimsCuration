import os
import pandas as pd
import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

path = 'X:/crbtous/genomes_care'
dir_list = os.listdir(path)

cursor = get_cursor("db_post_curation")
local_dir = "../curation/30_balancelles/"
cursor.execute(open("C:/Users/mboutrou/Documents/scripts/curation_bloc_1/validation_curation/10_parenteles_taxonomie.sql", "r", encoding='utf-8').read())

for f in dir_list:
    if f == "SalmonellaIP.xlsx":
        xlsx = pd.ExcelFile(path+'/'+f)
        sheet = pd.read_excel(xlsx, 'IP (121)')

        for i in range(3, len(sheet)):
            taxonomie = sheet.iloc[i, 3]
            subspecies = sheet.iloc[i, 4]
            serotype = sheet.iloc[i, 6]
            reason = sheet.iloc[i, 8]
            biosafety = sheet.iloc[i, 10]
            sector = sheet.iloc[i, 13]
            matrix = sheet.iloc[i, 14]
            country = sheet.iloc[i, 15]
            date = sheet.iloc[i, 17]
            ref = sheet.iloc[i, 21]
            medium = sheet.iloc[i, 23]
            temp = sheet.iloc[i, 24]
            wgs = sheet.iloc[i, 27]
            sttype = sheet.iloc[i, 32]
            rm = sheet.iloc[i, 42]
            org = sheet.iloc[i, 43]
            person = sheet.iloc[i, 44]
            email = sheet.iloc[i, 45]

            # denomination
            sch_denomination = taxonomie+' '+subspecies

            # taxonomie
            sch_taxonomie = ''
            cursor.execute("SELECT sch_taxonomie FROM chemins_taxonomie WHERE path = '"+taxonomie+' '+subspecies+"'")
            record = cursor.fetchone()
            if record is not None:
                sch_taxonomie = record[0]
            else:
                print("taxonomie à créer")
                print(taxonomie+' '+subspecies)

            if country == 'USA':
                country = "United States of America"            
            if country == 'Korea':
                country = "Korea (Republic of)"
            if country == 'The Netherlands':
                country = "Netherlands"
            if country == 'Democratic  Republic of the Congo':
                country = "Congo (Democratic Republic of the)"
            if country == 'UK':
                country = "United Kingdom of Great Britain and Northern Ireland"
            if country == 'Vietnam':
                country = "Viet Nam"

            # proprietes
            sch_proprietes = reason+' '+serotype

            # sector
            sch_origine = ''
            if sector == 'Human':
                sch_origine = 139
            elif sector == 'Animal':
                sch_origine = 140
            elif sector == 'Natural Environment':
                sch_origine = 141
            elif sector == 'Food':
                sch_origine = 7936452
            else:
                print("origine non renseignée")
                print(sector)

            # lieu
            sch_lieu = ''
            if isinstance(country, str):
                cursor.execute("SELECT don_lib FROM t_donneedico WHERE don_dic_id = 3758 AND xxx_sup_dat IS NULL AND don_lib = '"+country+"'")
                record = cursor.fetchone()
                if record is not None:
                    sch_lieu = record[0]
                else:
                    print("pays non renseigné 2")
                    print(country)
            else:
                print("pays non renseigné 1")
                print(country)
