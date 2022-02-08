import os
import pandas as pd
import psycopg2
import re
import requests
from xml.dom import minidom

def get_cursor(db_name, mdp):
    conn = psycopg2.connect(user="postgres",
                                  password=mdp,
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

path = '/mnt/gaia/crbip/crbtous/genomes_care'
mdp = 'postgres'
#path = 'X:/crbtous/genomes_care'
#mdp = 'hercule1821'
dir_list = os.listdir(path)

cursor = get_cursor("db_post_curation", mdp)
cursor.execute(open("../curation_bloc_1/validation_curation/10_parenteles_taxonomie.sql", "r", encoding='utf-8').read())

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

total = 0
unpublished = 0 
success = 0
for f in dir_list:
    if f == "SalmonellaIP.xlsx":
        xlsx = pd.ExcelFile(path+'/'+f)
        sheet = pd.read_excel(xlsx, 'IP (121)')

        for i in range(3, len(sheet)):
            ref_pubmed = sheet.iloc[i, 21]

            # sch_bibliographie
            sch_bibliographie = ""
            ref = ref_pubmed

            if isinstance(ref, str) and "pubmed" not in ref:
                total += 1

                if 'unpublished' in ref:
                    sch_bibliographie = ref
                    unpublished += 1

                if sch_bibliographie == "":
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

                            doi = ''
                            if len(tagname) != 0:
                                if tagname[0].hasAttribute('status'):
                                    if tagname[0].attributes['status'].value != "unresolved":
                                        if tagname[0].attributes['status'].value == "multiresolved":
                                            multi += 1

                                        tagdoi = dat.getElementsByTagName('doi')
                                        doi = tagdoi[0].firstChild.nodeValue
                                        success += 1

                                        print("")
                                        print(ref)
                                        print(response.request.url)
                                        print(doi)

                #if sch_bibliographie == "":
                #    sch_bibliographie = ref

        print(total)
        print(unpublished)
        print(success)
                    

