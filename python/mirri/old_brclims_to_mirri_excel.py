#!/usr/bin/env python
import argparse
import html
import re
import sys
from itertools import chain
from pathlib import Path
from pprint import pprint

import pycountry
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.automap import name_for_collection_relationship
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.schema import MetaData, Table

from mirri.entities.date_range import DateRange
from mirri.entities.growth_medium import GrowthMedium
from mirri.entities.sequence import GenomicSequence
from mirri.entities.strain import StrainMirri, OrganismType, StrainId
from mirri.io.writers.mirri_excel import write_mirri_excel
from mirri.settings import (COMMERCIAL_USE_WITH_AGREEMENT, ONLY_RESEARCH,
                            NAGOYA_PROBABLY_SCOPE, NAGOYA_NO_RESTRICTIONS,
                            NAGOYA_DOCS_AVAILABLE)
from mirri.validation.entity_validators import validate_strain

CCS = ['ATCC', 'CAIM', 'CCUG', 'DSM', 'NCIMB', 'NCPPB', 'NCTC', 'NRRL', 'VTT',
       'CIP']

comptage_cles = []


def remove_curlystags(string=None):
    if string is not None and string != '':
        return html.unescape(re.sub(r'\</?[a-zA-Z ="0-9]+/?\>', '', string))
    else:
        return None


def remove_hard_lines(string=None):
    if string is not None and string != '':
        return re.sub(r'\r+\n+', '', string).strip()
    else:
        return None


def _name_for_collection_relationship(base, local_cls, referred_cls, constraint):
    if constraint.name in comptage_cles:
        comptage_cles.append(constraint.name)
        return constraint.name+str(comptage_cles.count(constraint.name))
    else:
        comptage_cles.append(constraint.name)
        return constraint.name
    # if this didn't work, revert to the default behavior
    


def get_table_objects(engine):
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True, name_for_collection_relationship=_name_for_collection_relationship)

    Bacteria = Base.classes.t_souche
    Dico = Base.classes.t_donneedico
    MilieuDeSouche = Base.classes.t_milieu_souche
    Milieu = Base.classes.t_milieu
    Patho = Base.classes.t_pathogenicite

    return {'bacteria': Bacteria, 'dico': Dico, 'milieudesouche': MilieuDeSouche, 'milieu': Milieu, 'patho': Patho}


def get_cmd_args():
    desc = "Import BRCLims data into the MIRRI Specification compliant excel file"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-o', '--out_file', help='Path to the file to write the exel file',
                        type=argparse.FileType('wb'), required=True)
    parser.add_argument('-v', '--spec_version', default='20200601',
                        help='Version of he specification of the given excel file')
    parser.add_argument('-u', '--db_user', help='Username of database',
                        required=True)
    parser.add_argument('-p', '--db_password', required=True,
                        help='Password of the database user')
    parser.add_argument('-H', '--db_host', required=True,
                        help='Host url of the database')
    parser.add_argument('-P', '--db_port', default=3306,
                        help='Port to connect to the database')
    parser.add_argument('--verbose', action='store_true',
                        help='use it if you want a verbose output')
    parser.add_argument('-l', '--log_file', default=sys.stdout,
                        type=argparse.FileType('wt'),
                        help='Log file to write down messages')

    args = parser.parse_args()

    return {'out_fhand': args.out_file, 'user': args.db_user,
            'version': args.spec_version, 'password': args.db_password,
            'host': args.db_host, 'port': args.db_port,
            'verbose': args.verbose, 'log_fhand': args.log_file}


def main():
    args = get_cmd_args()
    out_path = Path(args['out_fhand'].name)
    user = args['user']
    password = args['password']
    host = args['host']
    port = args['port']
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/test2")

    tables = get_table_objects(engine)

    do_growth_media = True
    do_bacteria = True

    if do_growth_media:
        growth_media = get_growth_media(engine, tables)

    if do_bacteria:
        bacterias = get_strains(engine, tables, log_fhand=args['log_fhand'])
    
    strains = chain(bacterias)

    write_mirri_excel(path=out_path, strains=strains, growth_media=growth_media.values(), version="20200601")


def get_strains(engine, tables, log_fhand=None):
    Strains = tables['bacteria']

    with Session(bind=engine, future=True) as session:
        statement = select(Strains).filter(Strains.xxx_id.in_([192410, 192644, 193553, 350145, 372219, 535200, 536686, 537806]))
        
        # statement = select(strains_table).where(strains_table.c.cect==20831)
        for strain in session.execute(statement):
            strain = serialize_strain(strain, session=session, tables=tables, log_fhand=log_fhand)
            if strain is not None:
                yield strain


def _get_risk_group(patho_id, session, tables):
    Patho = tables['patho']
    patho_select = select(Patho).where(Patho.xxx_id == patho_id)
    row = session.execute(patho_select).one()
    return int(row.t_pathogenicite.pto_lib)


def _get_taxon_name(sch_taxonomie, session, tables):
    TaxoDico = tables['dico']

    taxo_select = select(TaxoDico).where(TaxoDico.xxx_id == sch_taxonomie, TaxoDico.don_dic_id == 3755)
    rowsp = session.execute(taxo_select).scalar()
    specie = rowsp.don_lib
    code_parent = rowsp.don_parent

    genus_select = select(TaxoDico).where(TaxoDico.don_code == code_parent, TaxoDico.don_dic_id == 3755)
    rowge = session.execute(genus_select).scalar()
    genus = rowge.don_lib

    result = {}
    result['species'] = specie
    result['genus'] = genus

    return result


def _get_recommended_growth_remp(row):
    temp = int(row.t_souche.sch_temperature_incubation)
    return {'max': temp, 'min': temp}


def _get_recommended_growth_media(sch_id, session, tables):
    MilieuDeSouche = tables['milieudesouche']
    Milieu = tables['milieu']

    milieusouche_select = select(MilieuDeSouche).where(MilieuDeSouche.msc_sch_id == sch_id)
    row = session.execute(milieusouche_select).one()

    milieu_select = select(Milieu).where(Milieu.xxx_id == row.t_milieu_souche.msc_mil_id)
    row2 = session.execute(milieu_select).one()
    
    return [row2.t_milieu.mil_numero]


def _get_form_of_supply(sch_conservation, session, tables):
    SupplyDico = tables['dico']
    supply_select = select(SupplyDico).where(SupplyDico.xxx_id == sch_conservation)
    row = session.execute(supply_select).one()

    if row.t_donneedico.don_lib == 'Stockage Lyophilisat':
        return ['Lyo']
    else:
        return ['Cryo']


def _get_country(sch_lieu, session, tables):
    LocDico = tables['dico']
    country_select = select(LocDico).where(LocDico.xxx_id == sch_lieu)
    row = session.execute(country_select).one()
    return row.t_donneedico.don_lib


def serialize_strain(row, session, tables, log_fhand):
    strain = StrainMirri()
    brclims_id = row.t_souche.sch_identifiant
    strain.id.collection = 'CIP'
    strain.id.number = str(brclims_id)

    strain.restriction_on_use = ONLY_RESEARCH

    strain.nagoya_protocol = NAGOYA_NO_RESTRICTIONS

    # "risk_group", "label": "Risk Group"},
    strain.risk_group = _get_risk_group(row.t_souche.sch_pto_id, session, tables)

    # taxonomy.organism_type", "label": "Organism type"},
    strain.taxonomy.organism_type = [OrganismType("Bacteria")]
    
    # taxonomy.taxon_name", "label": "Taxon name"},
    taxonomy = _get_taxon_name(row.t_souche.sch_taxonomie, session, tables)
    #print(taxonomy)
    if 'genus' in taxonomy:
        strain.taxonomy.genus = taxonomy['genus']
        strain.taxonomy.interspecific_hybrid = None
        if 'species' in taxonomy:
            strain.taxonomy.species = taxonomy['species']

    # "growth.recommended_temp","label": "Recommended growth temperature"},
    strain.growth.recommended_temp = _get_recommended_growth_remp(row)

    # "growth.recommended_media","label": "Recommended medium for growth"},
    strain.growth.recommended_media = _get_recommended_growth_media(row.t_souche.xxx_id, session, tables)

    # "form_of_supply", "label": "Form of supply"},
    strain.form_of_supply = _get_form_of_supply(row.t_souche.sch_conservation, session, tables)

    # "collect.location", "label": "Geographic origin"},
    country = _get_country(row.t_souche.sch_lieu, session, tables)
    pyinstance = pycountry.countries.get(name=country)
    strain.collect.location.country = pyinstance.alpha_3
    # TODO: aclararse con el collect site
    strain.collect.location.site = row.t_souche.sch_lieu_precis

    errors = validate_strain(strain)
    if not errors:
        return strain

    for error in errors:
        log_fhand.write(f'{strain.id.strain_id}: {error}\n')


def get_growth_media(engine, tables):
    Mediums = tables['milieu']

    gms = {}
    with Session(bind=engine, future=True) as session:
        select_medium = select(Mediums)

        media = session.execute(select_medium)

        for medium in media:
            gm = GrowthMedium()
            gm.acronym = medium.t_milieu.mil_numero
            gm.description = medium.t_milieu.mil_designation_en
            gm.full_description = _gm_full_description(medium.t_milieu.mil_commentaire)
            gms[str(medium.t_milieu.xxx_id)] = gm
        return gms


def _gm_full_description(raw_med):
    raw_text = raw_med.splitlines(True)
    new_lines = []
    for line in raw_text:
        line = line.replace('\r\n', '').strip()
        if not line or line == '   ':
            continue
        new_lines.append(line)

    full_description = ", ".join(new_lines)
    if full_description:
       full_description = f'ingredients: {full_description}'
       full_description = html.unescape(full_description)
    return remove_curlystags(full_description)


if __name__ == '__main__':
    main()