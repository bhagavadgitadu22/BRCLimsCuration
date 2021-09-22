#!/usr/bin/env python
import html
import re
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

import psycopg2


comptage_cles = []

def remove_curlystags(string=None):
    if string is not None and string != '':
        return html.unescape(re.sub(r'\</?[a-zA-Z ="0-9]+/?\>', '', string))
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

    Souche = Base.classes.t_souche
    Dico = Base.classes.t_donneedico
    Collection = Base.classes.t_collection

    return {'souche': Souche, 'dico': Dico, 'collection': Collection}

def main():
    # initialisation
    engine = create_engine(f"postgresql://postgres:hercule1821@localhost:5432/brc_db")
    tables = get_table_objects(engine)

    engine_curated = create_engine(f"postgresql://postgres:hercule1821@localhost:5432/brc_db")
    tables_curated = get_table_objects(engine_curated)

    # on récupère tous les ids de souches puis on les parcourt un à un
    liste_ids = liste_ids_souches(engine, tables)
    liste_ids_curated = liste_ids_souches(engine_curated, tables_curated)

    for xxx_id in liste_ids_curated:
        if xxx_id not in liste_ids:
            print("Un id de plus une fois la base curée ce n'est vraiment pas normal...")
            return False

    # on ne garde que souches de cip
    # en vérifiant d'abord que les autres n'ont pas été modifiées
    collections_cip = []
    Collection = tables['collection']
    with Session(bind=engine, future=True) as session:
        statement = select(Collection).where(Collection.col_clg_id == 401)

        for row in session.execute(statement):
            collections_cip.append(row.t_collection.xxx_id)

    ids_deleted = []
    for xxx_id in liste_ids:
        if xxx_id in liste_ids_curated:
            souche = get_souche(xxx_id, engine, tables)
            souche_curated = get_souche(xxx_id, engine_curated, tables_curated)

            if souche != souche_curated:
                # checker si ça fait bien partie de la collection de la cip
                if souche["sch_col_id"] not in collections_cip or souche_curated["sch_col_id"] not in collections_cip:
                    print("Erreur : une souche hors de la CIP a été modifié")
                    return False

                else:
                    comparaison_souche(xxx_id, engine, tables, engine_curated, tables_curated)

        else:
            # on garde la trace des ids_supprimes, qui doivent correspondre à des ids 2xxxxx
            ids_deleted.append(xxx_id)

def liste_ids_souches(engine, tables):
    Souche = tables['souche']

    with Session(bind=engine, future=True) as session:
        statement = select(Souche).order_by(Souche.xxx_id)
        
        liste_ids = []
        for souche in session.execute(statement):
            xxx_id = souche.t_souche.xxx_id
            liste_ids.append(xxx_id)

    return liste_ids

def get_souche(xxx_id, engine, tables):
    

def comparaison_souches(xxx_id, engine, tables, engine_curated, tables_curated):
    elmt = get_caracs_souche(xxx_id, engine, tables)
    elmt_curated = get_caracs_souche(xxx_id, engine_curated, tables_curated)

def get_caracs_souche(xxx_id, engine, tables):
    Souche = tables['souche']
    Dico = tables['dico']

    with Session(bind=engine, future=True) as session:
        statement = select(Souche).where(Souche.xxx_id == xxx_id)
        souche = session.execute(statement).one()

        xxx_id = souche.t_souche.xxx_id

        rows_lieu = select(Dico).where(Dico.xxx_id == souche.t_souche.sch_lieu)
        row_lieu = session.execute(rows_lieu).one()

        rows_patho = select(Dico).where(Dico.xxx_id == souche.t_souche.sch_patho_animal)
        row_patho = session.execute(rows_patho).one()

        elmt = {'sch_identifiant': souche.t_souche.sch_identifiant, 

                'sch_historique': souche.t_souche.sch_historique, 

                'dico_lieu': row_lieu.t_donneedico.don_lib, 
                'sch_lieu_precis': souche.t_souche.sch_lieu_precis, 
                'sch_dat_acquisition': souche.t_souche.sch_dat_acquisition, 

                'dico_patho_animal' : row_patho.t_donneedico.don_lib, 
                
                'sch_taxonomie': souche.t_souche.sch_taxonomie, 
                
                'sch_temperature_incubation': souche.t_souche.sch_temperature_incubation}

    return elmt

main()