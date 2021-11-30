import csv

f = open('../../output/dois_echouees_11_2021.csv', 'r', newline='')
references = [line.split('|')[0:4] for line in f]

for ref in references:
    ref.append('')
    ref.append('9dce962273126d7f7ac63ac37da3f8759108')

f2 = open('../../output/dois_echouees_11_2021_pour_pubmed.csv', 'w', newline='')
writer = csv.writer(f2, delimiter='|')

# write the rows to the csv file
writer.writerows(references)

# close the file
f.close()
f2.close()
