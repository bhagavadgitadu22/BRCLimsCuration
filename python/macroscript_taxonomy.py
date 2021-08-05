import psycopg2
from psycopg2 import Error

def evolution_des_erreurs(initial_faux_dico, initial_fausses_souches):
    totaux = {}

    # total des entrées du dico
    cursor.execute(open("../taxonomie/stats/totaux/total_dico.sql", "r").read())
    record = cursor.fetchone()
    totaux["dico"] = record[0]

    # total des entrées correctes dans le dico
    cursor.execute(open("../taxonomie/stats/totaux/total_corrects_dico.sql", "r").read())
    record = cursor.fetchone()
    totaux["vrai_dico"] = record[0]

    # total des entrées fausses du dico utilisées dans les souches
    totaux["faux_dico"] = totaux["dico"] - totaux["vrai_dico"]

    # % de correction du dico
    if (initial_faux_dico != 0):
        totaux["percentage_dico"] = int((initial_faux_dico - totaux["faux_dico"])/initial_faux_dico*100)
    else:
        totaux["percentage_dico"] = 'xxx'
    # total des entrées du dico utilisées dans les souches
    cursor.execute(open("../taxonomie/stats/totaux/total_souches.sql", "r").read())
    record = cursor.fetchone()
    totaux["souches"] = record[0]

    # total des entrées correctes du dico utilisées dans les souches
    cursor.execute(open("../taxonomie/stats/totaux/total_corrects_souches.sql", "r").read())
    record = cursor.fetchone()
    totaux["vraies_souches"] = record[0]

    # total des entrées fausses du dico utilisées dans les souches
    totaux["fausses_souches"] = totaux["souches"] - totaux["vraies_souches"]

    # % de correction des souches
    if (initial_fausses_souches != 0):
        totaux["percentage_souches"] = int((initial_fausses_souches - totaux["faux_souches"])/initial_fausses_souches*100)
    else:
        totaux["percentage_dico"] = 'xxx'

    return totaux

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="new_brc")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")

    totaux = evolution_des_erreurs(0, 0)
    initial_faux_dico = totaux["faux_dico"]
    initial_fausses_souches = totaux["fausses_souches"]


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")