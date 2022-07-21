from ete3 import NCBITaxa
import csv
import psycopg2
import xml.etree.cElementTree as ET

# TO MODIFY: les références à ma bdd locale
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

def countElements(dico):
    totalLocal = 0
    for elmt in dico:
        if isinstance(dico[elmt], int):
            totalLocal += dico[elmt]
        else:
            totalLocal += countElements(dico[elmt])
    return totalLocal

def addNodes(dico, root):
    totalLocal = countElements(dico)
    number = ET.SubElement(root, "grams")
    ET.SubElement(number, "val").text = str(totalLocal)
    
    for elmt in dico:
        if not(isinstance(dico[elmt], int)):
            if elmt != '':
                node = ET.SubElement(root, "node", name=elmt)
                addNodes(dico[elmt], node)
            else:
                addNodes(dico[elmt], root)

ncbi = NCBITaxa()
#ncbi.update_taxonomy_database()

# TO MODIFY: référence à mon fichier SQL que tu devras modifier pour aller chercher les taxonomies de ta base OWEY
str_sql = open("krona_and_map/krona/krona_taxos.sql", "r").read()

# TO MODIFY: référence à ma base de données locale
cursor = get_cursor("brc_db")
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
        if genus.lower() in taxIds:
            genus = genus.lower()
        else:
            print(genus, ' ', nombre)
    else:
        #if len(taxIds[genus]) > 1:
            #print("too many entries in ncbi:", genus)
        
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

dat = ET.SubElement(root, "datasets")
ET.SubElement(dat, "dataset").text = "CIP"

firstNode = ET.SubElement(root, "node", name="Taxonomy")
addNodes(dico, firstNode)

tree = ET.ElementTree(root)
#ET.indent(tree, '  ')
# TO MODIFY: création d'un fichier XML chemin à ajuster
tree.write("krona_and_map/krona/filename.xml", encoding="utf-8", xml_declaration=True)

# TO MODIFY: lecture de l'ancien fichier krona chemin à modifier
beginning = ""
with open("krona_and_map/krona/krona.html", 'r') as file:
    data = file.read().replace('\n', '')
    beginning = data[0:str.find(data, '<krona>')]

following = ""
# TO MODIFY: lecture du fichier XML chemin à ajuster
with open("krona_and_map/krona/filename.xml", 'r') as file:
    data = file.read().replace('\n', '')
    following = data[str.find(data, '<krona>'):]

# TO MODIFY: réécriture de l'ancien fichier krona chemin à modifier
writtenFile = open("krona_and_map/krona/krona.html", "w")
writtenFile.write(beginning+following+'</div></body></html>')
writtenFile.close()
