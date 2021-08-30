import requests
from xml.dom import minidom

parameters = {
    "usr": "martinboutroux@outlook.fr",
    "qdata": '<?xml version = "1.0" encoding="UTF-8"?><query_batch xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="2.0" xmlns="http://www.crossref.org/qschema/2.0" xsi:schemaLocation="http://www.crossref.org/qschema/2.0 http://www.crossref.org/qschema/crossref_query_input2.0.xsd"><head><email_address>your@email.org</email_address><doi_batch_id>01032012</doi_batch_id></head><body><query key="q1" enable-multiple-hits="true"><unstructured_citation>Hungate, B. A., &amp; Hampton, H. M. (2012). Ecosystem services: Valuing ecosystems for climate. Nature Climate Change, 2(3), 151-152.</unstructured_citation></query></body></query_batch>'
}

response = requests.get("https://doi.crossref.org/servlet/query", params=parameters, timeout=100)
print(response.content)
dat = minidom.parseString(response.content)

print(dat)