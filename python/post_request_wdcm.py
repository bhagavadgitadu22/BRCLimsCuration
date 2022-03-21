import requests
import re
import csv

url = 'http://ccinfo.wdcm.org/search/basic/'

f_vides = open('../../output/bilan_words.csv', 'r', newline='')
records = csv.reader(f_vides, delimiter=';')

rows = []
count = 0
for record in records:
    row = [record[0], record[1]]

    m = re.findall(r'[0-9]+', record[0])

    if count%10 == 0:
        print(count)
    count += 1

    if len(m) == 0:
        myobj = {'query': record[0]}
        x= ""
        x = requests.post(url, data = myobj)

        m = re.findall(r'Total ([0-9]+) results.', x.text)

        total = int(m[0])

        coll_yes = False
        if total > 0:
            m2 = re.findall(r'[0-9]+. ([A-Z]+) ', x.text)

            for coll_m2 in m2:
                if coll_m2 == record[0]:
                    coll_yes = True
            if not(coll_yes):
                print("")
                print(record[0])
                print(m2)

        row.append(coll_yes)
        rows.append(row)

f_vides2 = open('../../output/bilan_words2.csv', 'w', encoding="utf-8", newline='')
writer_vides2 = csv.writer(f_vides2, delimiter=';')
writer_vides2.writerows(rows)
f_vides2.close()

f_vides.close()
