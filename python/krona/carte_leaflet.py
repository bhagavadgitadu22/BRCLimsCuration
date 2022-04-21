import geojson
import csv

def ajustement(pays):
    if pays == 'Viet Nam':
        return "Vietnam"
    elif pays == 'United Kingdom of Great Britain and Northern Ireland':
        return "United Kingdom"
    elif pays == 'Russian Federation':
        return "Russia"
    elif pays == 'Czechia':
        return "Czech Republic"
    elif pays == 'Syrian Arab Republic':
        return "Syria"
    elif pays == 'Côte d\'Ivoire':
        return "Ivory Coast"
    elif pays == 'Cabo Verde':
        return "Cape Verde"

    return pays


path_to_file = '/home/calvin/Documents/geo-countries_zip/archive/countries.geojson'
with open(path_to_file) as f:
    gj = geojson.load(f)

f = open('../../output/countries_brclims.csv', 'r', newline='')
records = csv.reader(f, delimiter='|')
nombres_par_pays = [record for record in records]
f.close()

list_pays = []
for country in reversed(gj['features']):
    list_pays.append(country["properties"]["ADMIN"])

for nb_p_pa in nombres_par_pays:
    nb = nb_p_pa[0]
    pa = ajustement(nb_p_pa[1])

    boo = False
    for lp in list_pays:
        if pa in lp or pa.split(' (')[0] in lp:
            boo = True
    if not(boo):
        print(pa)
