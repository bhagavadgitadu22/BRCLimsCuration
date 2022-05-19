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

def inTree(dico, result, nombre):
    if result[0] in dico:
        if len(result) > 1:
            dico[result[0]] = inTree(dico[result[0]], result[1:], nombre)
        else:
            print("element dans dico mais pas de suite bizarre...")
    else:
        if len(result) > 1:
            dico[result[0]] = {}
            dico[result[0]] = inTree(dico[result[0]], result[1:], nombre)
        else:
            dico[result[0]] = nombre
    return dico

def addNodes(dico, root):
    totalLocal = 0
    for elmt in dico:
        if isinstance(dico[elmt], int):
            totalLocal += dico[elmt]
        else:
            node = ET.SubElement(root, "node", name=elmt)
            totalLocal += addNodes(dico[elmt], node)

    # à ce stade le noeud est terminé je peux compter le nombre d'éléments dans root
    number = ET.SubElement(root, "grams")
    ET.SubElement(number, "val").text = str(totalLocal)
    return totalLocal

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

        dico = inTree(dico, result, nombre)

root = ET.Element("krona")

attr = ET.SubElement(root, "attributes", magnitude="grams")
ET.SubElement(attr, "attribute", display="Number").text = "grams"

ET.SubElement(root, "color", attribute="grams", valueStart="0", valueEnd="55", hueStart="120", hueEnd="240")

dat = ET.SubElement(root, "datasets")
ET.SubElement(dat, "dataset").text = "CIP"

addNodes(dico, root)

tree = ET.ElementTree(root)
ET.indent(tree, '  ')
tree.write("krona_and_map/krona/filename.xml", encoding="utf-8", xml_declaration=True)
