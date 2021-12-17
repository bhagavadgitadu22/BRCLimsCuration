import requests
from xml.dom import minidom

str = "Int. J. Syst. Bacteriol., 1998, 48, 184"
str = "International Journal of Systematic and Evolutionary Microbiology, 1980, 30, 352"
row = str.split(', ')
print(row)

erreurs = 0
multi = 0

parameters = {
    "redirect": "false",
    "pid": "martinboutroux@outlook.fr",
    "title": row[0],
    "date": row[1],
    "volume": row[2],
    "spage": row[3],
    "multihit": True
}
response = requests.get("https://doi.crossref.org/openurl", params=parameters, timeout=100)

dat = minidom.parseString(response.content)
tagname = dat.getElementsByTagName('query')

if len(tagname) != 0:
    if tagname[0].hasAttribute('status'):
        if tagname[0].attributes['status'].value != "unresolved":
            if tagname[0].attributes['status'].value == "multiresolved":
                multi += 1

            tagdoi = dat.getElementsByTagName('doi')
            doi = tagdoi[0].firstChild.nodeValue

            elmt = []
            elmt.append(row[0])
            elmt.append(row[1])
            elmt.append(row[2])
            elmt.append(row[3])
            elmt.append(doi)
            elmt.append(row[4])
            elmt.append(row[5])
            print(elmt)
        else :
            print(row)
            erreurs += 1