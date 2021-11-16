import psycopg2
import csv

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="hercule1821",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def main():
    cursor = get_cursor("restart_db_pure")
    cursor_curated = get_cursor("restart_db_cured")

    cursor.execute("SELECT * FROM t_souche WHERE xxx_id = 490145")
    record = cursor.fetchone()

    cursor_curated.execute("SELECT * FROM t_souche WHERE t_souche.xxx_id = 247071")
    record_curated = cursor_curated.fetchone()

    print("coucou")
    print(record)
    print(record[7])

    if record[7] is None:
        print(True)

main()