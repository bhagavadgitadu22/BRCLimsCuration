import csv

path = '/mnt/gaia/my_home/chryseobacterium2/'

f_lpsn = open(path+'chryseo_lpsn.csv', 'r', newline='')
records = csv.reader(f_lpsn, delimiter=';')
chryseos_lpsn = [record[0].strip() for record in records]
f_lpsn.close()

print()

f_gtdb = open(path+'chryseo_types_gtdb.csv', 'r', newline='')
records = csv.reader(f_gtdb, delimiter=',')
chryseos_gtdb = [record[1] for record in records]
f_gtdb.close()

for c_lpsn in chryseos_lpsn:
    present = False
    new=c_lpsn.strip(' "')
    if "Corynebacterium kalinowskii" == c_lpsn:
        print("")
        print(c_lpsn)
        print("")
    for c_gtdb in chryseos_gtdb:
        if new in c_gtdb:
            present=True
    if not(present):
        print(c_lpsn)
