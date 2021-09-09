import requests
from xml.dom import minidom

parameters = {
    "redirect": "false",
    "pid": "martinboutroux@outlook.fr",
    "title": "Int. J. Syst. Evol. Microbiol",
    "date": "2002",
    "volume": "52",
    "spage": "2065",
    "multihit": "true"
}
response = requests.get("https://doi.crossref.org/openurl", params=parameters, timeout=100)

dat = minidom.parseString(response.content)
tagname = dat.getElementsByTagName('query')

if tagname[0].attributes['status'].value != "unresolved":
    tagdoi = dat.getElementsByTagName('doi')
    doi = tagdoi[0].firstChild.nodeValue
    print(doi)
    if tagname[0].attributes['status'].value == "multiresolved":
        print("true")
