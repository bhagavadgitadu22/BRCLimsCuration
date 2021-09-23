import psycopg2

connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="brc_db")
connection.autocommit = True

# Create a cursor to perform database operations
cursor = connection.cursor()

# initialization
cursor.execute(open("../curation/80_taxonomie/stats/parentele_de_toutes_taxonomies.sql ", "r").read())
records = cursor.fetchall()