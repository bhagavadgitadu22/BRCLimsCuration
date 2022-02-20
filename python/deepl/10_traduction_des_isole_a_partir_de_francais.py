import csv
import deepl 

translator = deepl.Translator("6976202f-3a88-0f81-27db-1b2488db3223:fx") 

glossary_fr_to_en = translator.create_glossary(
    "My glossary",
    source_lang="FR",
    target_lang="EN",
    entries={"sol": "soil"},
)

f = open('../../output/isole_a_partir_de.csv', 'r', newline='')
isolats = [line.split('|') for line in f]

identiques = []
traduits = []

i = 0
for isolat in isolats:
    result = translator.translate_text_with_glossary(isolat[0], glossary_fr_to_en)
    
    if isolat[0] != result.text:
        traduit = [result.text, isolat[0], isolat[1], isolat[2].replace('\n', '')]
        traduits.append(traduit)
    else:
        identique = [isolat[0], isolat[1], isolat[2].replace('\n', '')]
        identiques.append(identique)

    if i%100 == 0:
        print(i)
    i += 1

f2 = open('../../output/isole_a_partir_de_traduits.csv', 'w', newline='')
writer2 = csv.writer(f2, delimiter='|', lineterminator='\n')
writer2.writerows(traduits)

f3 = open('../../output/isole_a_partir_de_identiques.csv', 'w', newline='')
writer3 = csv.writer(f3, delimiter='|', lineterminator='\n')
writer3.writerows(identiques)
