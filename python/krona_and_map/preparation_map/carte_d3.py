import geojson
import csv

def ajustement(pays):
    if pays == 'Viet Nam':
        return "Vietnam"
    elif pays == 'United Kingdom of Great Britain and Northern Ireland':
        return "United Kingdom"
    elif pays == 'Russian Federation':
        return "Russia"
    elif pays == 'Syrian Arab Republic':
        return "Syria"
    elif 'Ivoire' in pays:
        return "Ivory Coast"
    elif pays == 'Korea (Republic of)':
        return "South Korea"
    elif pays == 'United States of America':
        return "United States"

    return pays

# TO MODIFY: latest version of the geojson available at: https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_sovereignty.geojson
path_to_file = 'krona_and_map/preparation_map/ne_50m_admin_0_sovereignty.geojson'
with open(path_to_file, encoding='utf8') as f:
    gj = geojson.load(f)

# TO MODIFY: ma requete sql à l'origine de ce csv: SELECT COUNT(*), don_lib FROM t_souche JOIN t_donneedico ON sch_lieu = t_donneedico.xxx_id WHERE sch_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401) AND t_souche.xxx_sup_dat IS NULL AND sch_catalogue IS True AND sch_mot IS False GROUP BY don_lib;
f = open('krona_and_map/preparation_map/countries_brclims.csv', 'r', newline='')
records = csv.reader(f, delimiter=',')
nombres_par_pays = [record for record in records]
f.close()

list_pays = []
count_countries = 0
countries_used = []
for country in reversed(gj['features']):
    pays_geojson = country["properties"]["ADMIN"]

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

# TO MODIFY: location of the geojson file
with open('krona_and_map/map/countries_with_numbers.geojson', 'w') as f:
    geojson.dump(gj, f)
