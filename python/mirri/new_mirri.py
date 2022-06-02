import psycopg2
from mirri.entities.strain import StrainMirri
from mirri.entities.growth_medium import GrowthMedium
import pycountry
from mirri.io.writers.mirri_excel import write_mirri_excel
from mirri.validation.entity_validators import validate_strain

def get_growth_media():
    sql = open("../envoi_souches/mirri/mirri.sql", "r", encoding='utf-8').read()
    cursor.execute(sql)
    media = cursor.fetchall()

    gms = {}
    for medium in media:
        gm = GrowthMedium()
        gm.acronym = medium[1]
        gm.description = medium[2]
        gms[str(medium[0])] = gm
    return gms

def serialize_strain(row, session, tables, log_fhand):
    strain = StrainMirri()

    strain.id.collection = 'CIP'
    
    strain.id.number = row[1]
    strain.other_numbers = row[2]
    strain.restriction_on_use = row[3]
    strain.nagoya_protocol = row[4]
    strain.other_numbers = row[5]

    strain.risk_group = row[6]
    strain.taxonomy.organism_type = row[7]
    strain.taxonomy.genus = row[8]
    strain.taxonomy.species = row[9]
    strain.taxonomy.subspecies = row[10]

    strain.taxonomy.infrasubspecific_name = row[11]
    strain.status = row[12]
    strain.history = row[13]
    strain.deposit.who = row[14]
    strain.deposit.date = row[15]

    strain.collect.date = row[16]
    strain.isolation.date = row[17]
    strain.catalog_inclusion_date = row[18]
    strain.growth.recommended_temp = row[19]
    strain.growth.recommended_media = row[20]

    strain.form_of_supply = row[21]
    strain.other_numbers = row[22]
    pyinstance = pycountry.countries.get(name=row[23])
    strain.collect.location.country = pyinstance.alpha_3
    strain.genetics.gmo = row[24]
    ###bibliography

    strain.isolation.substrate_host_of_isolation = row[26]
    strain.remarks = row[27]

    # complément lieu
    strain.collect.location.site = row[28]

    errors = validate_strain(strain)
    if not errors:
        return strain

    for error in errors:
        log_fhand.write(f'{strain.id.strain_id}: {error}\n')

# connect to an existing database
connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="localhost",
                                port="5432",
                                database="new_db")
connection.autocommit = True

# create a cursor to perform database operations
cursor = connection.cursor()

cursor.execute(open("../envoi_souches/mirri/mirri_last_version_souches_cip.sql", "r", encoding='utf-8').read())
cursor.execute(open("../envoi_souches/mirri/extract_date_function.sql", "r", encoding='utf-8').read())

sql = open("../envoi_souches/mirri/mirri.sql", "r", encoding='utf-8').read()
cursor.execute(sql)
strains = cursor.fetchall()

growth_media = get_growth_media(cursor)

strains = []
for row in strains:
    strain = serialize_strain(row)
    strains.append(strain)

write_mirri_excel(path=out_path, strains=strains, growth_media=growth_media.values(), version="20200601")
