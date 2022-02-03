import requests
import json
import csv

def main():
    # we write the results in an csv file
    f_dois = open('../../output/dois_a_corriger.csv', 'r', newline='')
    rows = csv.reader(f_dois, delimiter=',')

    i = 0
    # first try with crossref
    corrections = []
    for row in rows:
        if i >= 1:
            response = requests.get("https://doi.crossref.org/search/doi?pid=martinboutroux@outlook.fr&format=json&doi="+row[2])
            
            try:
                dat = json.loads(response.content)

                journal = ""
                if dat["container-title"] is not None:
                    journal = dat["container-title"]
                annee = ""
                if dat["created"]["date-parts"][0] is not None:
                    annee = dat["created"]["date-parts"][0]
                volume = ""
                if "volume" in dat["created"]:
                    volume = dat["created"]["volume"]
                page = ""
                if dat["page"] is not None and str(dat["page"]) != "null":
                    page = dat["page"]
                doi = row[2]

                if ',' in journal:
                    print(journal+', '+str(annee)+', '+str(volume)+', '+page+', '+doi)

                if journal=="" or annee=="":
                    print("Some information are missing: "+journal+', '+str(annee)+', '+str(volume)+', '+page+', '+doi)   
                else:
                    ref = journal+', '+str(annee)+', '+str(volume)+', '+page+', doi:'+doi
                    corr = [row[0], row[1], ref]
                    corrections.append(corr)                

            except json.decoder.JSONDecodeError:
                print("This doi is not right: "+row[2])               

        i += 1
        if i%10 == 0:
            print(i)

    f_write_dois = open('../../output/dois_corrigees.csv', 'w', newline='')
    writer = csv.writer(f_write_dois, delimiter='|')
    writer.writerows(corrections)

    # close the file
    f_dois.close()

main()