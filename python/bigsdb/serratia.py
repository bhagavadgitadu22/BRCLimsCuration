import os
import re
import psycopg2
import csv

def get_cursor(db_name):
    conn = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database=db_name)
    conn.autocommit = True

    return conn.cursor()

def test_match(pattern, file):
    id_cip = ''
    match = re.match(pattern, file)
    if match:
        id_cip = match.group(0)
    return id_cip

cursor = get_cursor("brc_db")
str_sql = open("../envoi_souches/bigsdb.sql", 'r').read()

path = 'X:/PROJETS_SCIENTIFIQUES/SERRATIA/Sandrine/GenomesSerratiaCIP'
dir_list = os.listdir(path)

rows = []
header = ['id', 'isolate', 'aliases', 'country', 'continent', 'region', 'year', 'source', 'species', 'phylum', 'class', 'order', 'family', 'genus', 'subspecies', 'genome_status', 'seq_centre', 'data_source', 'type_strain', 'bioproject_accession', 'biosample_accession', 'comments', 'assembly_filename', 'sequence_method']
rows.append(header)

count = 1
for file in dir_list:
    if not(os.path.isdir(file)):
        file0 = file
        iden = ""
        if not(re.search('^(CIP|CRBIP)', file)) and re.search('(CIP|CRBIP).*$', file):
            file = re.search('(CIP|CRBIP).*$', file).group(0)

        if re.match('^CIP[0-9]{6}-?T?', file):
            iden = re.match('^CIP[0-9]{6}-?T?', file).group(0)
        elif re.match('^CIP[0-9]{2}-[0-9]{1,3}-?T?', file):
            iden = re.match('^CIP[0-9]{2}-[0-9]{1,3}-?T?', file).group(0)
        elif re.match('^CIPA[0-9]{3}-?T?', file):
            iden = re.match('^CIPA[0-9]{3}-?T?', file).group(0)
        elif re.match('^CRBIP[0-9]{2}-[0-9]{3}-?T?', file):
            iden = re.match('^CRBIP[0-9]{2}-[0-9]{3}-?T?', file).group(0)
        else:
            print(file)
        iden = iden.replace('-', '')
        iden = iden.replace(' ', '')
        
        local_sql = str_sql+" AND REPLACE(REPLACE(sch_identifiant, ' ', ''), '.', '') = '"+iden+"'"
        cursor.execute(local_sql)
        record = cursor.fetchone()
        if record is None:
            print(iden)
        else:
            isolate = file.split('.scfd')[0].split('.fasta')[0]
            row = [count, isolate, record[1], record[2], '', record[3], record[4], record[5], record[6], '', '', '', '', record[7], record[8], 'finished', '', '', record[9], '', '', '', file0, 'Illumina']
            rows.append(row)
            count += 1

f_genomes = open('../../output/genomes_bigsdb.csv', 'w', newline='')
writer_genomes = csv.writer(f_genomes, delimiter=';')
writer_genomes.writerows(rows)
f_genomes.close()
