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
    MilieuDeSouche = Base.classes.t_milieu_souche
    Milieu = Base.classes.t_milieu
    Patho = Base.classes.t_pathogenicite

    return {'souche': Souche, 'dico': Dico, 'milieudesouche': MilieuDeSouche, 'milieu': Milieu, 'patho': Patho}

def main():
    engine = create_engine(f"postgresql://postgres:hercule1821@localhost:5432/brc_db")
    tables = get_table_objects(engine)
    liste_ids = liste_souches(engine, tables)

    engine_curated = create_engine(f"postgresql://postgres:hercule1821@localhost:5432/brc_db")
    tables_curated = get_table_objects(engine_curated)
    liste_ids_curated = liste_souches(engine_curated, tables_curated)

    if len(liste_ids) != len(liste_ids_curated):
        return "Pas le même nombre de souches dans les deux listes !"
    
    for i in range(len(liste_ids)):
        if liste_ids[i] != liste_ids_curated[i]:
            return "Pas les mêmes souches dans les deux listes ! L'id "+str(liste_ids[i])+" ne correspond pas à l'id "+str(liste_ids_curated[i])

    print("Il y a bien le même nombre d'ids et dans le même ordre.")

def liste_souches(engine, tables):
    Souche = tables['souche']

    with Session(bind=engine, future=True) as session:
        statement = select(Souche).order_by(Souche.xxx_id)
        
        liste_ids = []
        for souche in session.execute(statement):
            elmt = {'xxx_id': souche.t_souche.xxx_id, 
                    'sch_taxonomie': souche.t_souche.sch_taxonomie, 
                    'sch_lieu': souche.t_souche.sch_lieu, 
                    'sch_lieu_precis': souche.t_souche.sch_lieu_precis, 
                    'sch_lieu_precis': souche.t_souche.sch_lieu_precis, 
                }

            liste_ids.append(souche.t_souche.xxx_id)

    return liste_ids

main()