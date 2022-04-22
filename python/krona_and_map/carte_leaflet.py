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
    elif pays == 'Korea (Republic of)':
        return "Korea"

    return pays

path_to_file = '../../output/geo-countries_zip/archive/countries.geojson'
with open(path_to_file) as f:
    gj = geojson.load(f)

f = open('../../output/countries_brclims.csv', 'r', newline='')
records = csv.reader(f, delimiter=',')
nombres_par_pays = [record for record in records]
f.close()

list_pays = []
for country in reversed(gj['features']):
    pays_geojson = country["properties"]["ADMIN"]

    boo = False
    for nb_p_pa in nombres_par_pays[1:]:
        pa = ajustement(nb_p_pa[1])

        if pa in pays_geojson or pa.split(' (')[0] in pays_geojson:
            boo = True

            nbs = nb_p_pa[0].split('|')
            for nb in nbs:
                country["properties"][nb.split(':')[0]] = nb.split(':')[1]
    
    if not(boo):
        gj['features'].remove(country)

with open('../../output/countries_with_dates.geojson', 'w') as f:
    geojson.dump(gj, f)
