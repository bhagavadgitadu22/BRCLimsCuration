import psycopg2
from psycopg2 import Error
import requests
from xml.dom import minidom
import csv

f = open('../../output/bilan_dois.csv', 'r', newline='')
references = [line.split('|')[:4] for line in f]

f2 = open('../../output/bilan_bonnes_dois.csv', 'r', newline='')
references_good = [line.split('|')[:4] for line in f2]

references_bad = []
for elmt in references:
    if elmt not in references_good:
        new_elmt = elmt+['', '9dce962273126d7f7ac63ac37da3f8759108']
        references_bad.append(new_elmt)

# we write the results in an csv file
f3 = open('../../output/bilan_erreurs_dois_pour_pubmed.csv', 'w', newline='')
writer = csv.writer(f3, delimiter='|')

# write the rows to the csv file
writer.writerows(references_bad)

# close the file
f.close()
f2.close()
f3.close()
