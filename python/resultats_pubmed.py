import csv

f = open('../../output/resultats_de_pubmed.csv', 'r', newline='')
references = [line.split('|') for line in f]

f2 = open('../../output/bilan_bonnes_pmid.csv', 'w', newline='')
writer = csv.writer(f2, delimiter='|')

n_erreur = 0
not_found = 0
good = 0
ambiguous = 0

pmid = []

for ref in references:
    if len(ref) == 2:
        n_erreur += 1
    else:
        if "NOT_FOUND" in ref[len(ref)-1]:
            not_found += 1
        elif "AMBIGUOUS" in ref[len(ref)-1]:
            ambiguous += 1
        else:
            good += 1
            pmid.append(ref)

# write the rows to the csv file
writer.writerows(pmid)

print(n_erreur)
print(not_found)
print(ambiguous)
print(good)
