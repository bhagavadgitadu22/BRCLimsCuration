import psycopg2
from psycopg2 import Error

try:
    # connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="brc_db3")
    connection.autocommit = True

    # create a cursor to perform database operations
    cursor = connection.cursor()

    local_dir = "../curation/30_balancelles/"

    # operations
    print('10_souches_lyo')
    cursor.execute(open(local_dir+"10_souches_lyo.sql", "r", encoding='utf-8').read())

    print('20_excel_stockeur_1')
    cursor.execute(open(local_dir+"20_excel_stockeur_1.sql", "r", encoding='utf-8').read())

    print('25_ids_balancelles_stockeur_1')
    cursor.execute(open(local_dir+"25_ids_balancelles_stockeur_1.sql", "r", encoding='utf-8').read())

    print('26_emplacements_libres_par_balancelle_stockeur_1')
    cursor.execute(open(local_dir+"26_emplacements_libres_par_balancelle_stockeur_1.sql", "r", encoding='utf-8').read())

    print('30_excel_stockeur_2')
    cursor.execute(open(local_dir+"30_excel_stockeur_2.sql", "r", encoding='utf-8').read())

    print('35_ids_balancelles_stockeur_2')
    cursor.execute(open(local_dir+"35_ids_balancelles_stockeur_2.sql", "r", encoding='utf-8').read())

    print('36_emplacements_libres_par_balancelle_stockeur_2')
    cursor.execute(open(local_dir+"36_emplacements_libres_par_balancelle_stockeur_2.sql", "r", encoding='utf-8').read())

    print('40_correspondance_lots_balancelles_stockeur_1')
    cursor.execute(open(local_dir+"40_correspondance_lots_balancelles_stockeur_1.sql", "r", encoding='utf-8').read())

    print('50_correspondance_lots_balancelles_stockeur_2')
    cursor.execute(open(local_dir+"50_correspondance_lots_balancelles_stockeur_2.sql", "r", encoding='utf-8').read())

    print('60_update_stockeur')
    #cursor.execute(open(local_dir+"60_update_stockeur.sql", "r", encoding='utf-8').read())

    print('70_differents_rangements')
    #cursor.execute(open(local_dir+"70_differents_rangements.sql", "r", encoding='utf-8').read())
    
    print('80_supprimer_lieux_stockage_vides')
    #cursor.execute(open(local_dir+"80_supprimer_lieux_stockage_vides.sql", "r", encoding='utf-8').read())

    print('90_supprimer_tables_inutiles')
    #cursor.execute(open(local_dir+"90_supprimer_tables_inutiles.sql", "r", encoding='utf-8').read())

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")