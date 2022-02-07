import csv

f = open('C:/Users/mboutrou/Documents/output/liste_wgs.csv', 'r', newline='')
lines = csv.reader(f, delimiter=';')

for line in lines:
    print('https://www.ebi.ac.uk/ena/browser/view/'+line[0].split('/')[-1].split('_')[0])