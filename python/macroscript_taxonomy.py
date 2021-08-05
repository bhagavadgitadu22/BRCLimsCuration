import psycopg2
from psycopg2 import Error
import csv

def evolution_des_erreurs(propos, initial_faux_dico, initial_fausses_souches):
    totaux = []

    totaux.append(propos)

    # total des entrées du dico
    cursor.execute(open("../taxonomie/stats/totaux/total_dico.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées correctes dans le dico
    cursor.execute(open("../taxonomie/stats/totaux/total_corrects_dico.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées fausses du dico utilisées dans les souches
    totaux.append(totaux[1] - totaux[2])

    # % de correction du dico
    if (initial_faux_dico != 0):
        totaux.append(int((initial_faux_dico - totaux[3])/initial_faux_dico*100))
    else:
        totaux.append('xxx')
        
    # total des entrées du dico utilisées dans les souches
    cursor.execute(open("../taxonomie/stats/totaux/total_souches.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées correctes du dico utilisées dans les souches
    cursor.execute(open("../taxonomie/stats/totaux/total_corrects_souches.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées fausses du dico utilisées dans les souches
    totaux.append(totaux[5] - totaux[6])

    # % de correction des souches
    if (initial_fausses_souches != 0):
        totaux.append(int((initial_fausses_souches - totaux[7])/initial_fausses_souches*100))
    else:
        totaux.append('xxx')

    return totaux

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="new_brc3")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()


    # initialization
    cursor.execute(open("../taxonomie/10_table_taxonomie_lpsn.sql", "r").read())

    list_totaux = []

    totaux = evolution_des_erreurs("Construction de la table taxonomy à partir des données du LPSN", 0, 0)
    initial_faux_dico = totaux[3]
    initial_fausses_souches = totaux[7]

    list_totaux.append(totaux)
    

    # On enlève les termes du type 'pas de souche' dans la taxo
    print("On enlève les termes du type 'pas de souche' dans la taxo")
    cursor.execute(open("../taxonomie/14_pas_de_souche_degage.sql", "r").read())
    totaux = evolution_des_erreurs("On enlève les termes du type 'pas de souche' dans la taxo", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Enlever espaces avant/après éléments taxo (trim)
    print("Enlever espaces avant/après éléments taxo (trim)")
    cursor.execute(open("../taxonomie/15_trim_elements_taxo.sql", "r").read())
    totaux = evolution_des_erreurs("Enlever espaces avant/après éléments taxo (trim)", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Enlever les nulls du dico
    print("Enlever les nulls du dico")
    cursor.execute(open("../taxonomie/20_update_champs_null.sql", "r").read())
    totaux = evolution_des_erreurs("Enlever les nulls du dico", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Enlever les champs du type sp
    print("Enlever les champs du type sp")
    cursor.execute(open("../taxonomie/30_update_champs_sp.sql", "r").read())
    totaux = evolution_des_erreurs("Enlever les champs du type sp", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Enlever d'autres champs divers
    print("Enlever d'autres champs divers")
    cursor.execute(open("../taxonomie/31_update_champs_divers.sql", "r").read())
    totaux = evolution_des_erreurs("Enlever d'autres champs divers", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Enlever les termes vides ''
    print("Enlever les termes vides ''")
    cursor.execute(open("../taxonomie/32_update_champs_empty.sql", "r").read())
    totaux = evolution_des_erreurs("Enlever les termes vides ''", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Corriger manuellement certaines erreurs d'orthographe
    print("Corriger manuellement certaines erreurs d'orthographe")
    cursor.execute(open("../taxonomie/40_erreurs_orthographe_genus_ou_species.sql", "r").read())
    totaux = evolution_des_erreurs("Corriger manuellement certaines erreurs d'orthographe", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Passer en majuscules les noms de genus qui ne l'étaient pas
    print("Passer en majuscules les noms de genus qui ne l'étaient pas")
    cursor.execute(open("../taxonomie/41_genus_en_majuscules.sql", "r").read())
    totaux = evolution_des_erreurs("Passer en majuscules les noms de genus qui ne l'étaient pas", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On vire les accents
    print("On vire les accents")
    cursor.execute(open("../taxonomie/42_accents_vires.sql", "r").read())
    totaux = evolution_des_erreurs("On vire les accents", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Virer les acronymes d'Enterococcus
    print("Virer les acronymes d'Enterococcus")
    cursor.execute(open("../taxonomie/45_enteroccus.sql", "r").read())
    totaux = evolution_des_erreurs("Virer les acronymes d'Enterococcus", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On enlève les termes du type 'pas de souche' dans la taxo
    print("On enlève les termes du type 'pas de souche' dans la taxo")
    cursor.execute(open("../taxonomie/14_pas_de_souche_degage.sql", "r").read())
    totaux = evolution_des_erreurs("On enlève les termes du type 'pas de souche' dans la taxo", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Casser 'Genus species' en 2 termes 'Genus' et 'species'
    print("Casser 'Genus species' en 2 termes 'Genus' et 'species'")
    cursor.execute(open("../taxonomie/50_casser_en_2_genus_species.sql", "r").read())
    totaux = evolution_des_erreurs("Casser 'Genus species' en 2 termes 'Genus' et 'species'", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On enlève les serovar
    print("On enlève les serovar")
    cursor.execute(open("../taxonomie/60_virer_serovar.sql", "r").read())
    totaux = evolution_des_erreurs("On enlève les serovar", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On vire les doublons
    print("On vire les doublons")
    cursor.execute(open("../taxonomie/80_suppression_doublons_taxo.sql", "r").read())
    totaux = evolution_des_erreurs("On vire les doublons", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)


    # we write the results in an csv file
    f = open('../../output/bilan_curation_taxonomie.csv', 'w', newline='')
    writer = csv.writer(f)

    # write the rows to the csv file
    writer.writerow(['Script', 'Nombre total (dico)', 'Nombre correct (dico)', 'Erreurs totales (dico)', '% d\'erreurs corrigées (dico)', 'Nombre total avec taxo (souches)', 'Nombre correct (souches)', 'Erreurs totales (souches)', '% d\'erreurs corrigées (souches)'])
    writer.writerows(list_totaux)

    # close the file
    f.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")