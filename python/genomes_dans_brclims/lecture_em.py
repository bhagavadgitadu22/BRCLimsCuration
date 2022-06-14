import csv
import re

def test_match(pattern, file):
    id_cip = ''
    match = re.match(pattern, file)
    if match:
        id_cip = match.group(0)
    return id_cip

f = open('../../output/em_maj_perso.csv', 'r', newline='')
records = csv.reader(f, delimiter=';')

pattern1 = '^(CIP)?-?[0-9]{6}T?'
pattern2 = '^(CIP)?[0-9]{1,2}(-|.)[0-9]+T?'
pattern3 = '^CRBIP[0-9]{1,3}-[0-9]+T?'
pattern4 = '^CIPA[0-9]{1,3}T?'

rows = []
yes = 0
no = 0
for record in records:
    f3 = record[0].replace('CIPCRBIP', 'CRBIP')

    bool = True
    id_cip = ''
    lot_cip = ''
    if test_match(pattern1, f3) != '':
        id_cip = test_match(pattern1, f3)
    elif test_match(pattern2, f3) != '':
        id_cip = test_match(pattern2, f3)
    elif test_match(pattern3, f3) != '':
        id_cip = test_match(pattern3, f3)
    elif test_match(pattern4, f3) != '':
        id_cip = test_match(pattern4, f3)
    else:
        bool = False
        no += 1
    
    if bool:
        yes += 1
        if '_' in f3.replace(id_cip, ''):
            lot_cip = f3.replace(id_cip, '').split('_')[1].replace('\n', ' ')
    
    if id_cip != '':
        row = [id_cip, lot_cip, record[1], record[2]]
        rows.append(row)

f.close()

print(yes)
print(no)

f2 = open('../../output/infos_de_p2m.csv', 'w', newline='')
writer = csv.writer(f2, delimiter=';')
writer.writerows(rows)
f2.close()
