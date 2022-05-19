from ete3 import NCBITaxa
import csv
import psycopg2
import xml.etree.cElementTree as ET

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

ncbi = NCBITaxa()
# ncbi.update_taxonomy_database()

str_sql = open("krona_and_map/krona/krona_taxos.sql", "r").read()
cursor = get_cursor("restart_db_cured")
cursor.execute(str_sql)
records_cip = cursor.fetchall()

taxosBRC = [record for record in records_cip]

all_genus = []
for taxoBRC in taxosBRC:
    if taxoBRC[1] not in all_genus:
        all_genus.append(taxoBRC[1])
taxIds = ncbi.get_name_translator(all_genus)
print(taxIds)

results = []
dico = {}
for taxoBRC in taxosBRC:
    nombre = taxoBRC[0]
    genus = taxoBRC[1]
    species = taxoBRC[2]
    subspecies = taxoBRC[3]

    if genus not in taxIds:
        print("fake:", genus)
    else:
        if len(taxIds[genus]) > 1:
            print("too many entries in ncbi:", genus)
        
        taxId = taxIds[genus][0]
        lineage = ncbi.get_lineage(taxId)

        result = []
        for parentId in lineage:
            if ncbi.get_rank([parentId])[parentId] in ['domain', 'phylum', 'class', 'order', 'family', 'genus', 'superkingdom']:
                result.append(ncbi.get_taxid_translator([parentId])[parentId])
        result.append(species)
        result.append(subspecies)

        
        results.append(result)



f = open('../../output/genus_complete.csv', 'w', newline='')
writer = csv.writer(f, delimiter=';')
writer.writerows(results)
f.close()

root = ET.Element("krona")

attr = ET.SubElement(root, "attributes", magnitude="grams")
ET.SubElement(attr, "attribute", display="Number").text = "number"

dat = ET.SubElement(root, "datasets", magnitude="grams")
ET.SubElement(dat, "dataset").text = "CIP"


tree = ET.ElementTree(root)
tree.write("filename.xml")

