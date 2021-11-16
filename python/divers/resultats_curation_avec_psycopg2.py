import psycopg2
import csv

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def get_all_souches(cursor):
    cursor.execute(open("../curation/validation_curation/10_parenteles_taxonomie.sql", "r").read())

    cursor.execute(open("../curation/validation_curation/20_toutes_souches.sql", "r").read())
    records = cursor.fetchall()
    
    return records

def main():
    # on établit les connections avec les 2 bdds
    cursor = get_cursor("brc_db")
    cursor_curated = get_cursor("new_brc3")

    # on récupère toutes les souches de la bdd
    souches = get_all_souches(cursor)
    souches_curated = get_all_souches(cursor_curated)

    # dont on extrait les ids
    # pour vérifier qu'il y a strictement moins d'ids après la curation
    ids = [record[0] for record in souches]
    ids_curated = [record[0] for record in souches_curated]

    schs_apparus = []
    i = 0
    for id_c in ids_curated:
        if id_c not in ids:
            schs_apparus.append(souches_curated[i])
        i += 1

    # on récupère les ids_supprimés de la cip
    # on lève une erreur s'il y a un id supprimé pas de cip
    schs_supprimes = []
    schs_supprimes_hors_cip = []
    i = 0
    for id in ids:
        if id not in ids_curated:
            if souches[i][2] == 401:
                schs_supprimes.append(souches[i])
            else:
                schs_supprimes_hors_cip.append(souches[i])
        i += 1

    print("ids_apparus")
    print([elmt[1] for elmt in schs_apparus])
    print("")
    print("ids_supprimes")
    print([elmt[1] for elmt in schs_supprimes])
    print("")
    print("ids_supprimes_hors_cip")
    print([elmt[1] for elmt in schs_supprimes_hors_cip])

    souches_a_garder = []
    for sch in souches:
        if sch not in schs_supprimes and sch not in schs_supprimes_hors_cip:
            souches_a_garder.append(sch)

    souches_a_garder_curated = []
    for sch_c in souches_curated:
        if sch_c not in schs_apparus:
            souches_a_garder_curated.append(sch_c)

    print("de "+str(len(souches))+" souches à "+str(len(souches_a_garder)))
    print("de "+str(len(souches_curated))+" souches curées à "+str(len(souches_a_garder_curated)))

    # et qu'aucun id hors de cip n'a été modifié
    # et pour récupérer les ids de cip modifiés et supprimés
    souches_modifiees = []
    souches_modifiees_hors_cip = []

    str_base = open("../curation/validation_curation/25_toutes_souches_avec_infos.sql", "r").read()

    i = 0
    for sch in souches_a_garder:
        xxx_id = sch[0]
        cursor.execute(str_base+" WHERE t_souche.xxx_id = "+str(xxx_id))
        record = cursor.fetchone()

        cursor_curated.execute(str_base+" WHERE t_souche.xxx_id = "+str(xxx_id))
        record_curated = cursor_curated.fetchone()

        if record != record_curated:
            if record[len(record)-7] != 401 or record_curated[len(record_curated)-7] != 401:
                souches_modifiees_hors_cip.append(record)
            else:
                souches_modifiees.append(record_curated)

        if i%1000 == 0:
            print(str(i)+" souches traitees")
        i+=1

    print("")
    print(str(len(souches_modifiees))+" modifiees")
    print("")
    print(str(len(souches_modifiees_hors_cip))+" modifiees hors cip")
    print("")
    print([elem[0] for elem in souches_modifiees_hors_cip])

    f = open('../../output/hors_cip_modifies.csv', 'w', newline='')
    writer = csv.writer(f, delimiter=';')
    writer.writerows(map(lambda x: [x], [elem[0] for elem in souches_modifiees]))
    f.close()

main()