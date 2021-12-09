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

    local_dir = "../curation/90_temperature/"
    cursor.execute(open(local_dir+"vers_de_vrais_nombres.sql", "r", encoding='utf-8').read())

main()