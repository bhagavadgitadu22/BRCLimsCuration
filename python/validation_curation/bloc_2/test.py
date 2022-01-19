import psycopg2

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

str_base = open("../curation_bloc_2/validation_curation/20_toutes_souches_avec_infos.sql", "r").read()

cursor = get_cursor("brc_db_pure")
cursor_curated = get_cursor("brc_db_cured2")

cursor.execute(str_base+" WHERE t_souche.sch_identifiant = 'SB3386'")
record = cursor.fetchone()

cursor_curated.execute(str_base+" WHERE t_souche.sch_identifiant = 'SB3386'")
record_curated = cursor_curated.fetchone()

if record != record_curated:
    print("aie")

for i in range(len(record)):
    if record[i] != record_curated[i]:
        print("")
        print(record[i])
        print(record_curated[i])