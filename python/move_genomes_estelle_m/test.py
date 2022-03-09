import os

def testIfExists(path, id, elmt):
    exist = False
    path_id = path
    if id != '':
        path_id = path+'/'+id
    dir_list_id = os.listdir(path_id)

    for elmt_in_id in dir_list_id:
        if os.path.isdir(os.path.join(path_id, elmt_in_id)) and elmt in elmt_in_id:
            exist = True
            print(elmt)
            print(exist)

    return exist

path = 'V:/SEQUENCAGETOTAL/FICHIERRESULTATSSEQUENCES'
dir_list = os.listdir(path)

file = ""
for f in dir_list:
    if os.path.isdir(os.path.join(path, f)) and f[0].isdigit():
        file = f

print(file)

path2 = path+'/'+file
dir_list2 = os.listdir(path2)

# création du dico avec toutes les infos utiles
ids_cip = {}
for f2 in dir_list2:
    path3 = path2+'/'+f2

    if not(os.path.isdir(path3)):
        print(f2)
    else:
        dir_list3 = os.listdir(path3)

        for f3 in dir_list3:
            id_cip = f3.split('_')[0].replace("CIP", '')
            if id_cip not in ids_cip:
                ids_cip[id_cip] = {}

            lot_cip = f3.split('.')[0].split('_', 1)[1]
            if lot_cip not in ids_cip[id_cip]:
                ids_cip[id_cip][lot_cip] = {}

            local_dir = path3.split('/')[-1]
            if local_dir not in ids_cip[id_cip][lot_cip]:
                ids_cip[id_cip][lot_cip][local_dir] = []

            local_file = path3+'/'+f3
            if local_file not in ids_cip[id_cip][lot_cip][local_dir]:
                ids_cip[id_cip][lot_cip][local_dir].append(local_file)

print(ids_cip)

path_aim = 'V:/CONTROLE_SOUCHE'
dir_list_aim = os.listdir(path_aim)

for id_cip in ids_cip:
    if not(testIfExists(path_aim, '', id_cip)):
        os.mkdir(os.path.join(path_aim, id_cip))

    print(ids_cip[id_cip])
    for lot_cip in ids_cip[id_cip]:
        path_id = path_aim+'/'+id_cip  
        if not(testIfExists(path_aim, id_cip, lot_cip)):
            os.mkdir(path_id+'/'+lot_cip)

        path_lot = path_id+'/'+lot_cip
        for dir_cip in ids_cip[id_cip][lot_cip]:
            if not(testIfExists(path_id, lot_cip, dir_cip)):
                os.mkdir(path_lot+'/'+dir_cip)

        
