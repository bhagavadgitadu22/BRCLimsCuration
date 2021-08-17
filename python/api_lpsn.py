import lpsn

client = lpsn.LpsnClient('martin.boutroux@pasteur.fr', 'hercule1821')

# the prepare method fetches all LPSN-IDs matching your query
# and returns the number of IDs found
count = client.search(taxon_name='Sulfolobus', correct_name='yes')
print(count, 'entries found.')

# the retrieve method lets you iterate over all results
# and returns the full entry as dict
# Entries can be further filtered using a list of keys (e.g. ['keywords'])
for entry in client.retrieve():
    print(entry)