import psycopg2

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
    cursor_curated = get_cursor("brc_db_curated")

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

    # et qu'aucun id hors de cip n'a été modifié
    # et pour récupérer les ids de cip modifiés et supprimés
    str_where = ' WHERE t_souche.xxx_id NOT IN ('
    i = 0
    for sch in schs_apparus:
        if i>0:
            str_where += ','
        str_where += str(sch[0])
        i+=1
    for sch in schs_supprimes:
        if i>0:
            str_where += ','
        str_where += str(sch[0])
        i+=1
    for sch in schs_supprimes_hors_cip:
        if i>0:
            str_where += ','
        str_where += str(sch[0])
        i+=1
    str_where += ')'

    print("")
    print(open("../curation/validation_curation/25_toutes_souches_avec_infos.sql", "r").read()+str_where)

    schs_modifies_hors_cip = []

main()