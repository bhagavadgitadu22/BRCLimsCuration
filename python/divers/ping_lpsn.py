import requests
import csv


f = open('../../output/erreurs_taxonomie.csv', 'r')
erreurs = [line.strip('\n').split('|') for line in f]
f.close()

i = 0
j = 0

ok_rows = []
fake_rows = []
for erreur in erreurs:
   response = requests.head("https://lpsn.dsmz.de/search?word="+erreur[2])
   head = dict(**response.headers)
   if 'Location' in head:
      ok_rows.append(erreur)
      j += 1
   else:
      fake_rows.append(erreur)
      a = 3

   i += 1
   if i%10 == 0:
      print(str(i)+' erreurs dont '+str(j)+' ok')

f2 = open('../../output/fausses_erreurs_taxonomie.csv', 'w', newline='')
writer2 = csv.writer(f2, delimiter='|')
writer2.writerows(ok_rows)
f2.close()

f3 = open('../../output/vraies_erreurs_taxonomie.csv', 'w', newline='')
writer3 = csv.writer(f3, delimiter='|')
writer3.writerows(fake_rows)
f3.close()
