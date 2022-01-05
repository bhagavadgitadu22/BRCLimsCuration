from Bio import Entrez

Entrez.email = "martinboutroux@outlook.fr"

# handle = Entrez.efetch(db="bioproject", id="PRJEB10936")
# records = Entrez.parse(handle) 
# for record in records: 
#       print(record)

handle2 = Entrez.efetch(db="biosample", id="ERS4774371")
result2 = Entrez.parse(handle2)

print("coucou")
print(result2)

for i in result2:
    print(i)

handle2.close()