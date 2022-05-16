import geojson
import csv

def ajustement(pays):
    if pays == 'Viet Nam':
        return "Vietnam"
    elif pays == 'United Kingdom of Great Britain and Northern Ireland':
        return "England"
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
        return "South Korea"
    elif pays == 'United States of America':
        return "USA"

    return pays

path_to_file = 'preparation_map/world.geojson'
with open(path_to_file) as f:
    gj = geojson.load(f)

f = open('preparation_map/countries_brclims.csv', 'r', newline='')
records = csv.reader(f, delimiter=',')
nombres_par_pays = [record for record in records]
f.close()

list_pays = []
count_countries = 0
countries_used = []
for country in reversed(gj['features']):
    pays_geojson = country["properties"]["name"]

    boo = False
    for nb_p_pa in nombres_par_pays[1:]:
        nb = nb_p_pa[0]
        pa = ajustement(nb_p_pa[1])

        if pa in pays_geojson or pa.split(' (')[0] in pays_geojson:
            boo = True
            country["properties"]["nombre"] = nb

            count_countries += 1
            countries_used.append(nb_p_pa[1])
        
    if "nombre" not in country["properties"]:
        country["properties"]["nombre"] = 0

print(count_countries)
for nb_p_pa in nombres_par_pays[1:]:
    if nb_p_pa[1] not in countries_used:
        print(nb_p_pa[1])

with open('map/countries_with_numbers.geojson', 'w') as f:
    geojson.dump(gj, f)
