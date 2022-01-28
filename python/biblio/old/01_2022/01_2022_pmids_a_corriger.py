import requests
import json
import csv

def main():
    # we write the results in an csv file
    f_dois = open('../../output/pmids_a_corriger.csv', 'r', newline='')
    rows = csv.reader(f_dois, delimiter=',')

    i = 0
    # first try with crossref
    corrections = []
    for row in rows:
        if i >= 1:
            response = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id="+row[2]+"&retmode=json&tool=my_tool&email=martinboutroux@outlook.fr")
            print("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id="+row[2]+"&retmode=json&tool=my_tool&email=martinboutroux@outlook.fr")
            try:
                dat = json.loads(response.content)["result"][row[2]]

                journal = ""
                if "source" in dat:
                    journal = dat["source"]
                annee = ""
                if "volume" in dat:
                    annee = dat["volume"]
                volume = ""
                if "issue" in dat:
                    volume = dat["issue"]

                ref = journal+', '+str(annee)+', '+str(volume)+', '+row[2]
                print(ref)
                corr = [row[0], row[1], ref]
                corrections.append(corr)                

            except json.decoder.JSONDecodeError:
                print("This doi is not right: "+row[2])               

        i += 1
        if i%10 == 0:
            print(i)

    f_write_dois = open('../../output/pmids_corrigees.csv', 'w', newline='')
    writer = csv.writer(f_write_dois, delimiter=',')
    writer.writerows(corrections)

    # close the file
    f_dois.close()

main()