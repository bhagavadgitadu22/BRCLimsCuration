import csv

def addFather(line_genus, nodes_cleared, names_cleared, father):
    fatherName = names_cleared[father][0]
    grandFather = nodes_cleared[father][0]
    typeGrandFather = nodes_cleared[father][1]

    if grandFather != '1':
        if typeGrandFather in ['domain', 'phylum', 'class', 'order', 'family', 'genus', 'superkingdom']:
            line_genus.append(fatherName)
        line_genus = addFather(line_genus, nodes_cleared, names_cleared, grandFather)

    return line_genus

print("nodes_cleared")
f = open('../../output/new_taxdump/nodes.dmp', 'r', newline='')
records = csv.reader(f, delimiter='|')
nodes = [record[:3] for record in records]
f.close()

cat = []
genus_cleared = {}
fathers_cleared = {}
for node in nodes:
    for idx in range(len(node)):
        node[idx] = node[idx].replace('\t', '')

    if node[2] == 'genus':
        genus_cleared[node[0]] = [node[1], node[2]]
    elif node[2] != 'species':
        fathers_cleared[node[0]] = [node[1], node[2]]

    if node[2] not in cat:
        cat.append(node[2])

print(cat)

print("names_cleared")
f = open('../../output/new_taxdump/names.dmp', 'r', newline='')
records = csv.reader(f, delimiter='|')
names = [record for record in records]
f.close()

names_cleared = {}
for name in names:
    for idx in range(len(name)):
        name[idx] = name[idx].replace('\t', '')

    if name[3] == 'scientific name':
        names_cleared[name[0]] = [name[1]]
for name in names:
    if name[3] == 'synonym':
        names_cleared[name[0]].append(name[1])

print("lets_go")
print(len(genus_cleared))
print("")
lines = []
count = 0
for key, value in genus_cleared.items():
    for name in names_cleared[key]:
        line_genus = [name]
        father = value[0]

        line_genus = addFather(line_genus, fathers_cleared, names_cleared, father)
        if line_genus[-1] == 'Bacteria' or line_genus[-1] == 'Archaea':
            lines.append(line_genus)

        count += 1
        if count%50 == 0:
            print(count)

f = open('../../output/genus_complete.csv', 'w', newline='')
writer = csv.writer(f, delimiter=';')
writer.writerows(lines)
f.close()
