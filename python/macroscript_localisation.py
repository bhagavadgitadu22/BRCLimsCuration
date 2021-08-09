import psycopg2
from psycopg2 import Error
import csv

def evolution_des_erreurs(propos, initial_faux_dico, initial_fausses_souches):
    totaux = []

    totaux.append(propos)

    # total des entrées du dico
    cursor.execute(open("../localisation/stats/totaux/total_dico.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées correctes dans le dico
    cursor.execute(open("../localisation/stats/totaux/total_corrects_dico.sql", "r").read())
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
    cursor.execute(open("../localisation/stats/totaux/total_souches.sql", "r").read())
    record = cursor.fetchone()
    totaux.append(record[0])

    # total des entrées correctes du dico utilisées dans les souches
    cursor.execute(open("../localisation/stats/totaux/total_corrects_souches.sql", "r").read())
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
                                  database="new_brc2")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()


    # initialization
    cursor.execute(open("../localisation/10_english_world.sql", "r").read())
    cursor.execute(open("../localisation/11_french_world.sql", "r").read())
    cursor.execute(open("../localisation/12_mixed_world.sql", "r").read())

    list_totaux = []

    totaux = evolution_des_erreurs("Construction de la table des pays ISO", 0, 0)
    initial_faux_dico = totaux[3]
    initial_fausses_souches = totaux[7]

    list_totaux.append(totaux)
    
    
    # Traduction des noms de pays du français à l'anglais
    print("Traduction des noms de pays du français à l'anglais")
    cursor.execute(open("../localisation/20_de_francais_a_anglais.sql", "r").read())
    totaux = evolution_des_erreurs("Traduction des noms de pays du français à l'anglais", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # On vire les acronymes de UK et USA
    print("On vire les acronymes de UK et USA")
    cursor.execute(open("../localisation/30_virer_uk_et_usa.sql", "r").read())
    totaux = evolution_des_erreurs("On vire les acronymes de UK et USA", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Quand il y a un 'ville, pays' on met la ville dans localisation détaillée
    print("Quand il y a un 'ville, pays' on met la ville dans localisation détaillée")
    cursor.execute(open("../localisation/40_separation_ville_de_pays_pour_format_virgule.sql", "r").read())
    totaux = evolution_des_erreurs("Quand il y a un 'ville, pays' on met la ville dans localisation détaillée", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)

    # Quand il y a juste une ville on la met dans localisation détaillée et on la remplace par le pays
    print("Quand il y a juste une ville on la met dans localisation détaillée et on la remplace par le pays")
    cursor.execute(open("../localisation/45_de_ville_a_pays.sql", "r").read())
    totaux = evolution_des_erreurs("Quand il y a juste une ville on la met dans localisation détaillée et on la remplace par le pays", initial_faux_dico, initial_fausses_souches)
    list_totaux.append(totaux)
    
    
    # we write the results in an csv file
    f = open('../../output/bilan_curation_localisation.csv', 'w', newline='')
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