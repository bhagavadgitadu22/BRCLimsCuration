import psycopg2
from psycopg2 import Error
import csv

def evolution_des_erreurs(propos, initial_faux_dico, initial_fausses_souches):
    local_dir = "../curation/50_localisation/"

    totaux = []

    totaux.append(propos)

    # total des entrées du dico
    cursor.execute(open(local_dir+"stats/totaux/total_dico.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées correctes dans le dico
    cursor.execute(open(local_dir+"stats/totaux/total_corrects_dico.sql", "r").read())
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
    cursor.execute(open(local_dir+"stats/totaux/total_souches.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées correctes du dico utilisées dans les souches
    cursor.execute(open(local_dir+"stats/totaux/total_corrects_souches.sql", "r").read())
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

    local_dir = "../curation/50_localisation/"
    
    # initialization
    print("Construction de la table des pays")
    cursor.execute(open(local_dir+"10_english_world.sql", "r", encoding='utf-8').read())
    cursor.execute(open(local_dir+"11_french_world.sql", "r", encoding='utf-8').read())
    cursor.execute(open(local_dir+"12_mixed_world.sql", "r", encoding='utf-8').read())

    
    print("Construction de la table des villes")
    cursor.execute(open(local_dir+"15_cities.sql", "r", encoding='utf-8').read())

    list_totaux = []

    totaux = evolution_des_erreurs("Construction de la table des pays et des villes", 0, 0)
    initial_faux_dico = totaux[3]
    initial_fausses_souches = totaux[7]

    list_totaux.append(totaux)

    """ à laisser tant que les problèmes de gestion de la corée ne sont pas résolus
    # On crée tables des villes coréennes
    cursor.execute(open(local_dir+"korea/0_south_korean_cities.sql", "r", encoding='utf-8').read())

    # On corrige les noms de lieux coréens erronés
    cursor.execute(open(local_dir+"korea/10_corrections.sql", "r", encoding='utf-8').read())

    # On réaffecte les souches vers Korea
    cursor.execute(open(local_dir+"korea/20_vers_south_korea_for_cities.sql", "r", encoding='utf-8').read())

    # On met à Corée du Sud toutes les souches post 1960
    print("On corrige les erreurs coréennes")
    cursor.execute(open(local_dir+"korea/30_isolees_apres_1960.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On corrige les erreurs coréennes", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    """

    # Enlever espaces avant/après localisation (trim)
    print("Enlever espaces avant/après localisation (trim)")
    cursor.execute(open(local_dir+"20_trim_elements_localisation.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Enlever espaces avant/après localisation (trim)", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    
    # Traduction des noms de pays du français à l'anglais
    print("Traduction des noms de pays du français à l'anglais")
    cursor.execute(open(local_dir+"25_de_francais_a_anglais.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Traduction des noms de pays du français à l'anglais", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    
    # On ajoute les majuscules nécessaires, on vire les accents inutiles
    print("On ajoute les majuscules nécessaires, on vire les accents inutiles")
    cursor.execute(open(local_dir+"26_ajout_majuscules_et_virer_accents.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On ajoute les majuscules nécessaires, on vire les accents inutiles", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On vire les acronymes de UK et USA
    print("On vire les acronymes de UK et USA")
    cursor.execute(open(local_dir+"30_virer_uk_et_usa.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On vire les acronymes de UK et USA", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    
    # Virer les erreurs d'orthographe des pays
    print("Virer les erreurs d'orthographe des pays")
    cursor.execute(open(local_dir+"35_virer_erreurs_orthographe_pays.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Virer les erreurs d'orthographe des pays", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    
    # Corriger d'autres erreurs d'orthographe
    print("Corriger d'autres erreurs d'orthographe")
    cursor.execute(open(local_dir+"36_autres_erreurs_orthographe.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Corriger d'autres erreurs d'orthographe", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Virer les erreurs d'orthographe des villes
    print("Virer les erreurs d'orthographe des villes")
    cursor.execute(open(local_dir+"37_erreurs_orthographe_villes.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Virer les erreurs d'orthographe des villes", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Virer les erreurs d'orthographe multiples
    print("Virer les erreurs d'orthographe multiples")
    cursor.execute(open(local_dir+"38_erreurs_a_souches_multiples.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Virer les erreurs d'orthographe multiples", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Peaufiner par souche
    print("Peaufiner par souche")
    cursor.execute(open(local_dir+"39_peaufinage_par_souches.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Peaufiner par souche", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On enlève les dates des noms de lieux
    print("On enlève les dates des noms de lieux")
    cursor.execute(open(local_dir+"40_virer_les_dates.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On enlève les dates des noms de lieux", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Quand il y a un 'ville, pays' on met la ville dans localisation détaillée
    print("Quand il y a un 'ville, pays' on met la ville dans localisation détaillée")
    cursor.execute(open(local_dir+"60_separation_ville_de_pays_pour_format_virgule.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Quand il y a un 'ville, pays' on met la ville dans localisation détaillée", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Quand il y a un 'pays, ville' on met la ville dans localisation détaillée
    print("Quand il y a un 'pays, ville' on met la ville dans localisation détaillée")
    cursor.execute(open(local_dir+"61_separation_ville_de_pays_pour_format_virgule_inverse.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Quand il y a un 'pays, ville' on met la ville dans localisation détaillée", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Quand pays entre parenthèses on l'extrait
    print("Quand pays entre parenthèses on l'extrait")
    cursor.execute(open(local_dir+"62_extraction_de_parentheses.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Quand pays entre parenthèses on l'extrait", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Quand il y a juste une ville on la met dans localisation détaillée et on la remplace par le pays
    print("Quand il y a juste une ville on la met dans localisation détaillée et on la remplace par le pays")
    cursor.execute(open(local_dir+"65_de_ville_a_pays.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Quand il y a juste une ville on la met dans localisation détaillée et on la remplace par le pays", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On vire les acronymes de UK et USA (second try)
    print("On vire les acronymes de UK et USA (second try)")
    cursor.execute(open(local_dir+"30_virer_uk_et_usa.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On vire les acronymes de UK et USA (second try)", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Virer les erreurs d'orthographe des pays (second try)
    print("Virer les erreurs d'orthographe des pays (second try)")
    cursor.execute(open(local_dir+"35_virer_erreurs_orthographe_pays.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("Virer les erreurs d'orthographe des pays (second try)", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    
    # On gère les pays encore entourés d'autres infos
    print("On gère les pays encore entourés d'autres infos")
    cursor.execute(open(local_dir+"70_pays_restants_dans_lieux.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On gère les pays encore entourés d'autres infos", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On vire les lieux inconnus et on met NULL comme lieu à la place
    print("On vire les lieux inconnus et on met NULL comme lieu à la place")
    cursor.execute(open(local_dir+"75_lieux_inconnus.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On vire les lieux inconnus et on met NULL comme lieu à la place", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    
    # On vire les doublons de lieux
    print("On vire les doublons de lieux")
    cursor.execute(open(local_dir+"80_suppression_doublons_de_lieux.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On vire les doublons de lieux", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On vire les doublons de lieux
    print("On vire les éléments inutilisées du dico")
    cursor.execute(open(local_dir+"85_suppression_elements_dico_inutilises.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("On vire les éléments inutilisées du dico", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Suppression des tables inutiles
    cursor.execute(open(local_dir+"90_suppression_tables_inutiles.sql", "r", encoding='utf-8').read())
    
    
    # we write the results in an csv file
    f = open('../../output/bilan_curation_localisation.csv', 'w', newline='')
    writer = csv.writer(f)

    # write the rows to the csv file
    writer.writerow(['Script', 'Nombre total (dico)', 'Nombre correct (dico)', 'Erreurs totales (dico)', '% d\'erreurs corrigées (dico)', 'Nombre total avec localisation (souches)', 'Nombre correct (souches)', 'Erreurs totales (souches)', '% d\'erreurs corrigées (souches)'])
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