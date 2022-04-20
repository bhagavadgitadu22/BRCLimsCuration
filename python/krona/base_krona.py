import csv

def addFather(line_genus, nodes_cleared, names_cleared, father):
    fatherName = names_cleared[father]
    grandFather = nodes_cleared[father][0]

    if grandFather != '1':
        line_genus.append(nodes_cleared[father][1])
        line_genus = addFather(line_genus, nodes_cleared, names_cleared, grandFather)

    return line_genus

print("nodes_cleared")
f = open('C:/Users/mboutrou/Downloads/new_taxdump/nodes.dmp', 'r', newline='')
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
f = open('C:/Users/mboutrou/Downloads/new_taxdump/names.dmp', 'r', newline='')
records = csv.reader(f, delimiter='|')
names = [record for record in records]
f.close()

names_cleared = {}
for name in names:
    for idx in range(len(name)):
        name[idx] = name[idx].replace('\t', '')

    if name[3] == 'scientific name' or name[3] == 'synonym':
        if name[0] not in names_cleared:
            names_cleared[name[0]] = [name[1]]
        else:
            names_cleared[name[0]].append(name[1])

print("lets_go")
print(len(genus_cleared))
print("")
lines = []
count = 0
for key, value in genus_cleared.items():
    line_genus = [names_cleared[key][0]]
    father = value[0]

    line_genus = addFather(line_genus, fathers_cleared, names_cleared, father)
    if line_genus[-1] == 'Bacteria':
        lines.append(line_genus)

    count += 1
    if count%50 == 0:
        print(count)

f = open('C:/Users/mboutrou/Documents/output/genus_complete.csv', 'w', newline='')
writer = csv.writer(f, delimiter=';')
writer.writerows(lines)
f.close()
