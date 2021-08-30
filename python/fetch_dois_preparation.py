import psycopg2
from psycopg2 import Error
import csv

def evolution_des_erreurs(propos, initial_all_documents, initial_all_documents_grouped):
    totaux = []

    totaux.append(propos)

    # total des documents à traiter
    cursor.execute(open("../bibliographie/stats/totaux/total_all_documents.sql", "r").read())
    record = cursor.fetchone()
    current_all_documents = record[0]
    totaux.append(current_all_documents)

    # total des documents différents à traiter
    cursor.execute(open("../bibliographie/stats/totaux/total_all_documents_grouped.sql", "r").read())
    record = cursor.fetchone()
    current_all_documents_grouped = record[0]
    totaux.append(current_all_documents_grouped)
        
    # total des documents gérés
    cursor.execute(open("../bibliographie/stats/totaux/total_good_documents.sql", "r").read())
    record = cursor.fetchone()
    current_good_documents = record[0]
    totaux.append(current_good_documents)

    # total des documents groupés gérés
    cursor.execute(open("../bibliographie/stats/totaux/total_good_documents_grouped.sql", "r").read())
    record = cursor.fetchone()
    current_good_documents_grouped = record[0]
    totaux.append(current_good_documents_grouped)

    # % des documents traités
    if (initial_all_documents != 0):
        totaux.append(int((initial_all_documents - current_all_documents)/initial_all_documents*100))
    else:
        totaux.append('xxx')

    # % des documents groupés traités
    if (initial_all_documents_grouped != 0):
        totaux.append(int((initial_all_documents_grouped - current_all_documents_grouped)/initial_all_documents_grouped*100))
    else:
        totaux.append('xxx')

    return totaux

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database="new_brc5")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    
    # initialization
    cursor.execute(open("../bibliographie/0_full_trim.sql", "r", encoding='utf-8').read())

    # on_enleve_points_virgules_en_trop
    cursor.execute(open("../bibliographie/5_on_enleve_points_virgules_en_trop.sql", "r", encoding='utf-8').read())
    cursor.execute(open("../bibliographie/6_on_ajoute_points_virgules_manquants.sql", "r", encoding='utf-8').read())
    cursor.execute(open("../bibliographie/7_correction_de_csv.sql", "r", encoding='utf-8').read())

    cursor.execute(open("../bibliographie/10_global_script.sql", "r", encoding='utf-8').read())

    list_totaux = []

    totaux = evolution_des_erreurs("Initialisation de la fonction trim et des tables", 0, 0)
    initial_all_documents = totaux[1]
    initial_all_documents_grouped = totaux[2]

    list_totaux.append(totaux)

    # pmid and dois
    cursor.execute(open("../bibliographie/20_pmid_et_dois.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("pmid and dois", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)

    # epuration_docs_d_elements_vides
    cursor.execute(open("../bibliographie/25_epuration_docs_d_elements_vides.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("epuration_docs_d_elements_vides", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)

    # basic_four_elements
    cursor.execute(open("../bibliographie/30_basic_four_elements.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("basic_four_elements", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)

    # four_elements_e_page
    cursor.execute(open("../bibliographie/35_four_elements_e_page.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("four_elements_e_page", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)

    # four_elements_s_page
    cursor.execute(open("../bibliographie/38_four_elements_s_page.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("four_elements_s_page", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)
    
    # 8_elements_cassables
    cursor.execute(open("../bibliographie/40_8_elements_cassables.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("8_elements_cassables", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)
    
    # 7_elements_cassables
    cursor.execute(open("../bibliographie/50_7_elements_cassables.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("7_elements_cassables", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)

    # 5_elements_cassables
    cursor.execute(open("../bibliographie/60_5_elements_cassables.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("5_elements_cassables", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)
    
    # 3_elements_cassables
    cursor.execute(open("../bibliographie/70_3_elements_cassables.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("3_elements_cassables", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)
    
    # bis_3_elements_cassables
    cursor.execute(open("../bibliographie/70_bis_3_elements_cassables.sql", "r", encoding='utf-8').read())
    totaux = evolution_des_erreurs("bis_3_elements_cassables", initial_all_documents, initial_all_documents_grouped)
    list_totaux.append(totaux)

    cursor.execute(open("../bibliographie/80_suppression_submitted.sql", "r", encoding='utf-8').read())
    cursor.execute(open("../bibliographie/100_compacted_good_documents_table.sql", "r", encoding='utf-8').read())
    
    
    # we write the results in an csv file
    f = open('../../output/bilan_curation_biblios.csv', 'w', newline='')
    writer = csv.writer(f)

    # write the rows to the csv file
    writer.writerow(['Script', 'Nombre de documents', 'Nombre de documents regroupés', 'Nombre de bons documents', 'Nombre de bons documents regroupés', '% de documents gérés', '% de documents groupés gérés'])
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