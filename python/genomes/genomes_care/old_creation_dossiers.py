from Bio import Entrez
import xml.etree.ElementTree as ET

Entrez.email = "martinboutroux@outlook.fr"

handle = Entrez.efetch(db="bioproject", id="PRJEB10936")
tree = ET.parse(handle)
root = tree.getroot()
str = ET.tostring(root, encoding='utf8', method='xml')
print(str)
#for record in records: 
#    çprint(record)

handle2 = Entrez.efetch(db="biosample", id="ERS4774371")
tree = ET.parse(handle2)
root = tree.getroot()
str = ET.tostring(root, encoding='utf8', method='xml')
#print(str)

#for child in root:
#   print(child.tag, child.attrib)

handle2.close()
