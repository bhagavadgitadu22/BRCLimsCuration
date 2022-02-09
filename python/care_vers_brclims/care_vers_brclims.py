import os
import pandas as pd
import psycopg2
import requests
import json
import re
from xml.dom import minidom
import csv

def get_cursor(db_name, mdp):
    conn = psycopg2.connect(user="postgres",
                                  password=mdp,
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def get_ref_doi(doi):
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
            return journal+', '+str(annee)+', '+str(volume)+', '+pages+', doi:'+doi
    except json.decoder.JSONDecodeError:
        print("This doi is not right: "+doi)
        return ""

#path = '/mnt/gaia/crbip/crbtous/genomes_care'
#mdp = 'postgres'
path = 'X:/crbtous/genomes_care'
mdp = 'hercule1821'

db_name = 'brc_db_cured'
dir_list = os.listdir(path)

journaux = [
    'U.S. Publ. Hlth. Rep',
    'Zbl. Bakt. I Orig',
    'Z. Immunforsch.',
    'Arch. urug. Med. Cir. Y Espec',
    'Proc. Soc. exp. Biol. and Med',
    'Phasenwechsel. Z. Hyg',
    'Int. J. system. Bact',
    'Publ. Hlth. Lab',
    'Amer. J. Hyg',
    'Arch. urug. Med. Cir. y Espec',
    'Zbl. Bakt. I Ref',
    'Proc. Soc. exp. Biol. and Med',
    'Bull. Soc. Path. exot',
    'Lancet f',
    'J. infect. Dis',
    'Ei-Sei Gaku Zasshi',
    'Acta path. microbial. scand',
    'Dtsch. tierdrztl. Wschr',
    'Ind. J. med. Res',
    'Publ. Hlth, Lab'
]

cursor = get_cursor(db_name, mdp)
cursor.execute(open("../curation_bloc_1/validation_curation/10_parenteles_taxonomie.sql", "r", encoding='utf-8').read())

for f in dir_list:
    if f == "SalmonellaIP.xlsx":
        xlsx = pd.ExcelFile(path+'/'+f)
        sheet = pd.read_excel(xlsx, 'IP (121)')

        liste_lignes = []
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
            elif sector == 'Natural Environment' or sector == 'Agro-food industrial environment':
                sch_origine = 141
            elif sector == 'Food':
                sch_origine = 7936452
            else:
                print("origine non renseignée")
                print(sector)

            # biosafety
            sch_pto_id = 2695
            if biosafety != 2:
                print("problème de biosafety !")
                print(biosafety)

            # sch_isole_a_partir_de
            sch_isole_a_partir_de = matrix

            # lieu
            sch_lieu = ''
            if isinstance(country, str):
                cursor.execute("SELECT xxx_id FROM t_donneedico WHERE don_dic_id = 3758 AND xxx_sup_dat IS NULL AND don_lib = '"+country+"'")
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
                    sch_bibliographie = get_ref_doi(doi)

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

            elif 'unpublished' in ref:
                sch_bibliographie = ref

            else:
                for elmt in journaux:
                    if elmt in ref:
                        end_params = ref.split(elmt)[1].strip(' .,')

                        journal = elmt.strip(' .,')
                        volume = end_params.split(',')[0].strip(' .,')
                        pages = end_params.split(',')[1].split(' (')[0].split('-')[0].strip(' .,')
                        search = re.search('\([0-9]+\)', end_params)
                        annee = search.group(0).strip('()')

                        parameters = {
                            "redirect": "false",
                            "pid": "martinboutroux@outlook.fr",
                            "title": journal,
                            "date": annee,
                            "volume": volume,
                            "spage": pages,
                            "multihit": True
                        }
                        response = requests.get("https://doi.crossref.org/openurl", params=parameters, timeout=100)

                        dat = minidom.parseString(response.content)
                        tagname = dat.getElementsByTagName('query')

                        if len(tagname) != 0:
                            if tagname[0].hasAttribute('status'):
                                if tagname[0].attributes['status'].value != "unresolved":
                                    if tagname[0].attributes['status'].value == "multiresolved":
                                        print("multi")

                                    tagdoi = dat.getElementsByTagName('doi')
                                    doi = tagdoi[0].firstChild.nodeValue
                                    sch_bibliographie = get_ref_doi(doi)
            
            if sch_bibliographie == "":
                sch_bibliographie = ref

            # sch_temperature_incubation
            sch_temperature_incubation = temp

            # sch_historique
            if not(isinstance(rm, str)):
                rm = rm.strftime('%Y/%m')
            sch_historique = '2022, '+person+', '+org.replace(" - ", ', ')+': strain '+rm

            # sch_depositaire
            sch_depositaire = 6348115

            ligne = [sch_denomination, sch_taxonomie, sch_proprietes, sch_origine, sch_pto_id, sch_isole_a_partir_de, sch_lieu, sch_dat_prelevement, sch_bibliographie, sch_temperature_incubation, sch_historique, sch_depositaire]
            liste_lignes.append(ligne)

        # on écrit fichier texte avec les infos utiles
        f_care = open('../../output/infos_care.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_care, delimiter='|')
        writer.writerows(liste_lignes)
        f_care.close()
