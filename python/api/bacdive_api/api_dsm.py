import bacdive

client = bacdive.BacdiveClient('martin.boutroux@pasteur.fr', 'hercule1821')

# the search method fetches all BacDive-IDs matching your query
# and returns the number of IDs found
query = {"taxonomy": "Chryseobacterium"}
count = client.search(**query)
print(count, 'strains found.')

# the retrieve method lets you iterate over all strains
# and returns the full entry as dict
# Entries can be further filtered using a list of keys (e.g. ['keywords'])
for strain in client.retrieve():
    print(strain)
