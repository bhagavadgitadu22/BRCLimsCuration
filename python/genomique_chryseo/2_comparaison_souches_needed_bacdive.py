import csv

path = '/mnt/gaia/my_home/chryseobacterium2/'

f_lpsn = open(path+'chryseo_bacdive.csv', 'r', newline='')
records = csv.reader(f_lpsn, delimiter=',')
chryseos_bacdive = [record[5].strip() for record in records if (record[5] != '' and record[5] != 'species')]
f_lpsn.close()

f_gtdb = open(path+'chryseo_not_in_gtdb.csv', 'r', newline='')
records = csv.reader(f_gtdb, delimiter=',')
chryseos_gtdb = [record[0] for record in records]
f_gtdb.close()

for c_bacdive in chryseos_bacdive:
    new=c_bacdive
    for c_gtdb in chryseos_gtdb:
        if c_bacdive in c_gtdb:
            print(c_bacdive)
