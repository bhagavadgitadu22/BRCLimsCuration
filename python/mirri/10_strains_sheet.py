import psycopg2

from mirri.entities.date_range import DateRange
from mirri.entities.publication import Publication
from mirri.entities.strain import StrainMirri
from mirri.entities.strain import StrainId
from mirri.entities.strain import OrganismType
from mirri.entities.growth_medium import GrowthMedium
import pycountry
from mirri.io.writers.mirri_excel import write_mirri_excel
from mirri.validation.entity_validators import validate_strain
from mirri.settings import (NO_RESTRICTION, NAGOYA_NO_RESTRICTIONS)

def get_growth_media(cursor):
    sql = open("../envoi_souches/mirri/mirri_milieux.sql", "r", encoding='utf-8').read()
    cursor.execute(sql)
    media = cursor.fetchall()

    gms = {}
    gm0 = GrowthMedium()
    gm0.acronym = '-1'
    gm0.description = 'No medium specified'
    gms['-1'] = gm0
    for medium in media:
        gm = GrowthMedium()
        gm.acronym = medium[0]
        gm.description = medium[1]
        gms[str(medium[0])] = gm
    return gms

def newDateRange(date):
    return DateRange(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]))

def newOtherRef(ref):
    ref = ref.strip()
    ref = ref.replace('  ', ' ')
    if 'NRRL : ' in ref:
        return ref.replace('NRRL : ', 'NRRL ')

    if ref.count(' ') == 1:
        return ref
    elif ref.count(' ') == 0:
        if 'CARE_' in ref:
            return ref.replace('CARE_', 'CARE ')
        if 'CIPT' in ref:
            return ref.replace('CIPT', 'CIPT ')
        if 'CIP' in ref:
            return ref.replace('CIP', 'CIP ')
        if 'CRBIP' in ref:
            return ref.replace('CRBIP', 'CRBIP ')
        if 'DSM' in ref:
            return ref.replace('DSM', 'DSM ')
        if 'MBIC' in ref:
            return ref.replace('MBIC', 'MBIC ')
        else:
            return ref
    else:
        return ref

def serialize_strain(row, bibli_tot):
    strain = StrainMirri()

    strain.id.collection = row[1].split(' ')[0]
    strain.id.number = row[1].split(' ')[1]

    if row[2] != '':
        list_of_refs = []
        for ref in row[2].split(';'):
            ref = newOtherRef(ref)
            if ref.count(' ') == 1:
                other_strain = StrainId(collection=ref.split(' ')[0], number=ref.split(' ')[1])
                list_of_refs.append(other_strain)
        strain.other_numbers = list_of_refs
    
    strain.restriction_on_use = NO_RESTRICTION
    strain.nagoya_protocol = NAGOYA_NO_RESTRICTIONS
    strain.risk_group = row[5]

    org_type = []
    if row[6] == 'Bacteria':
        org_type = [OrganismType(3)]
    strain.taxonomy.organism_type = org_type
    strain.taxonomy.genus = row[7]
    strain.taxonomy.species = row[8]
    strain.taxonomy.infrasubspecific_name = row[10]

    strain.status = row[11]
    strain.history = row[12]
    strain.deposit.who = row[13]

    if row[14] != '':
        strain.deposit.date = newDateRange(row[14])
    if row[15] != '':
        strain.collect.date = newDateRange(row[15])
    if row[16] != '':
        strain.isolation.date = newDateRange(row[16])
    if row[17] != '':
        strain.catalog_inclusion_date = newDateRange(row[17])

    if row[18].replace('°C', '') != '':
        strain.growth.recommended_temp = {"min":row[18].replace('°C', '') , "max":row[18].replace('°C', '') }
    else:
        strain.growth.recommended_temp = {"min":-1, "max":-1}
    
    strain.growth.recommended_media = [row[19]]
    
    strain.form_of_supply = [row[20]]

    country = row[22]
    if row[22] is None:
        country = 'Unknown'
    pyinstance = pycountry.countries.get(name=country)
    if pyinstance is None:
       strain.collect.location.country = "INW"
    else:
        strain.collect.location.country = pyinstance.alpha_3

    strain.genetics.gmo = bool(row[23])

    strain.isolation.substrate_host_of_isolation = row[25]
    strain.remarks = row[26]

    # complément lieu
    strain.collect.location.site = row[27]

    errors = validate_strain(strain)
    if not errors:
        return strain

    for error in errors:
        print(error)

# connect to an existing database
connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True

# create a cursor to perform database operations
cursor = connection.cursor()

#obj_path = '/home/calvin/Documents/mirri/'
obj_path = 'C:/Users/mboutrou/Documents/mirri/'
out_path = obj_path+'brclims_excel.xlsx'

bibli_tot = []

souches_concernees = "../envoi_souches/mirri/mirri_last_version_souches_pcc.sql"
cursor.execute(open(souches_concernees, "r", encoding='utf-8').read())
cursor.execute(open("../envoi_souches/mirri/extract_date_function.sql", "r", encoding='utf-8').read())

growth_media = get_growth_media(cursor)

sql = open("../envoi_souches/mirri/mirri.sql", "r", encoding='utf-8').read()
cursor.execute(sql)
rows = cursor.fetchall()

strains = []
for row_strain in rows:
    strain_serialized = serialize_strain(row_strain, bibli_tot)
    strains.append(strain_serialized)

write_mirri_excel(path=out_path, strains=strains, growth_media=growth_media.values(), version="20200601")
