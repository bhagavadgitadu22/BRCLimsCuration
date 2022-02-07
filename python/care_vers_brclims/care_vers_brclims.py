import os
import pandas as pd
import psycopg2
import requests
import json

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
            ref_pubmed = sheet.iloc[i, 21]
            ref_doi = sheet.iloc[i, 22]
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
            taxo = taxonomie+' '+subspecies
            if taxo == 'Salmonella enterica VII':
                taxo = 'Salmonella enterica'
            cursor.execute("SELECT sch_taxonomie FROM chemins_taxonomie WHERE path = '"+taxo+"'")
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
            elif sector == 'Food' or sector == 'Agro-food industrial environment':
                sch_origine = 7936452
            else:
                print("origine non renseignée")
                print(sector)

            # biosafety
            if biosafety == '2':
                sch_pto_id = 2695

            # sch_isole_a_partir_de
            sch_isole_a_partir_de = matrix

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

            # sch_dat_prelevement
            sch_dat_prelevement = date

            # sch_bibliographie
            sch_bibliographie = ""
            ref = ref_pubmed
            if not(isinstance(ref_pubmed, str)):
                ref = ref_doi

                if "doi" in ref:
                    doi = ref.split("/", 3)[-1]
                    response = requests.get("https://doi.crossref.org/search/doi?pid=martinboutroux@outlook.fr&format=json&doi="+doi)
                
                    try:
                        dat = json.loads(response.content)
                        journal = ""
                        if dat["container-title"] is not None:
                            journal = dat["container-title"]
                        annee = ""
                        if dat["created"]["date-parts"][0] is not None:
                            annee = dat["created"]["date-parts"][0]
                        volume = ""
                        if "volume" in dat["created"]:
                            volume = dat["created"]["volume"]
                            if "issue" in dat["created"] and '('+dat["created"]["issue"]+')' != '()':
                                volume+='('+dat["created"]["issue"]+')'
                        pages = ""
                        if dat["page"] is not None and str(dat["page"]) != "null":
                            pages = dat["page"]

                        if journal=="" or annee=="":
                            print("Some information are missing: "+journal+', '+str(annee)+', '+str(volume)+', '+pages+', '+doi)   
                        else:
                            sch_bibliographie = journal+', '+str(annee)+', '+str(volume)+', '+pages+', doi:'+doi      
                    except json.decoder.JSONDecodeError:
                        print("This doi is not right: "+doi)
            elif "pubmed" in ref:
                pubmed = ref.strip('/').split("/")[-1]

                response = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id="+pubmed+"&retmode=json&tool=my_tool&email=martinboutroux@outlook.fr")
                try:
                    dat = json.loads(response.content)["result"][pubmed]

                    journal = ""
                    if "source" in dat:
                        journal = dat["source"]
                    annee = ""
                    if "pubdate" in dat:
                        annee = dat["pubdate"].split(" ")[0]
                    volume = ""
                    if "volume" in dat:
                        volume = dat["volume"]
                        if "issue" in dat and '('+dat["issue"]+')' != '()':
                            volume+='('+dat["issue"]+')'
                    pages = ""
                    if "pages" in dat:
                        pages = dat["pages"]

                    if journal=="" or annee=="":
                        print("Some information are missing: "+journal+', '+str(annee)+', '+str(volume)+', '+pages+', '+pubmed)   
                    else:
                        sch_bibliographie = journal+', '+str(annee)+', '+str(volume)+', '+pages+', pmid:'+pubmed
                except json.decoder.JSONDecodeError:
                    print("This doi is not right: "+pubmed)
            else:
                sch_bibliographie = ref      

            # sch_temperature_incubation
            sch_temperature_incubation = temp

            # sch_historique
            if not(isinstance(rm, str)):
                rm = rm.strftime('%Y/%m')
            sch_historique = str(date)+', '+person+', '+org.replace(" - ", ', ')+': strain '+rm

            # sch_deposant
            sch_depositaire = 6348115
