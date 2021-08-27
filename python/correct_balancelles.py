import psycopg2
from psycopg2 import Error

try:
    # connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="new_brc5")
    connection.autocommit = True

    # create a cursor to perform database operations
    cursor = connection.cursor()

    # operations
    print('0_custom_order')
    cursor.execute(open("../balancelles/0_custom_order.sql", "r", encoding='utf-8').read())

    print('10_souches_lyo')
    cursor.execute(open("../balancelles/10_souches_lyo.sql", "r", encoding='utf-8').read())

    print('20_excel_stockeur_1')
    cursor.execute(open("../balancelles/20_excel_stockeur_1.sql", "r", encoding='utf-8').read())

    print('25_ids_balancelles_stockeur_1')
    cursor.execute(open("../balancelles/25_ids_balancelles_stockeur_1.sql", "r", encoding='utf-8').read())

    print('30_excel_stockeur_2')
    cursor.execute(open("../balancelles/30_excel_stockeur_2.sql", "r", encoding='utf-8').read())

    print('35_ids_balancelles_stockeur_2')
    cursor.execute(open("../balancelles/35_ids_balancelles_stockeur_2.sql", "r", encoding='utf-8').read())

    print('40_correspondance_lots_balancelles_stockeur_1')
    cursor.execute(open("../balancelles/40_correspondance_lots_balancelles_stockeur_1.sql", "r", encoding='utf-8').read())

    print('50_correspondance_lots_balancelles_stockeur_2')
    cursor.execute(open("../balancelles/50_correspondance_lots_balancelles_stockeur_2.sql", "r", encoding='utf-8').read())

    print('60_update_stockeur')
    cursor.execute(open("../balancelles/60_update_stockeur.sql", "r", encoding='utf-8').read())

    print('70_supprimer_lieux_stockage_vides')
    cursor.execute(open("../balancelles/70_supprimer_lieux_stockage_vides.sql", "r", encoding='utf-8').read())

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")