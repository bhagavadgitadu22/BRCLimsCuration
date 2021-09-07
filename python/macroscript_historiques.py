import psycopg2
from psycopg2 import Error

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
    cursor.execute(open("../bibliographie/0_full_trim.sql", "r", encoding='utf-8').read())

    # 0_souches_a_modifier
    print("0_souches_a_modifier")
    cursor.execute(open("../historique_bacillus/0_souches_a_modifier.sql", "r").read())

    # 5_virer_strains_ok
    print("5_virer_strains_ok")
    cursor.execute(open("../historique_bacillus/5_virer_strains_ok.sql", "r").read())

    # 0_souches_a_modifier
    print("0_souches_a_modifier")
    cursor.execute(open("../historique_bacillus/0_souches_a_modifier.sql", "r").read())
    
    # 10_numero_de_strain
    print("10_numero_de_strain")
    cursor.execute(open("../historique_bacillus/10_numero_de_strain.sql", "r").read())
    
    # 15_lines_historique
    print("15_lines_historique")
    cursor.execute(open("../historique_bacillus/15_lines_historique.sql", "r").read())

    # 16_correct_lines
    print("16_correct_lines")
    cursor.execute(open("../historique_bacillus/16_correct_lines.sql", "r").read())

    # 20_new_historiques
    print("20_new_historiques")
    cursor.execute(open("../historique_bacillus/20_new_historiques.sql", "r").read())

    # 25_suppression_tables
    print("25_suppression_tables")
    cursor.execute(open("../historique_bacillus/25_suppression_tables.sql", "r").read())

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")