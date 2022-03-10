import os
import re

def test_match(pattern, file):
    id_cip = ''
    match = re.match(pattern, file)
    if match:
        id_cip = match.group(0)
    return id_cip

local_path = '/mnt/gaia/cip'
path = local_path+'/SEQUENCAGETOTAL/FICHIERRESULTATSSEQUENCES'
dir_list = os.listdir(path)

file = ""
ids_cip = {}
c = 0

ct = 0
cf = 0

pattern1 = '^(CIP)?-?[0-9]{6}T?'
pattern2 = '^(CIP)?[0-9]{1,2}(-|.)[0-9]+T?'
pattern3 = '^CRBIP[0-9]{1,3}-[0-9]+T?'
pattern4 = '^CIPA[0-9]{1,3}T?'

pattern1_lot = '^[0-9]+'

# file is the number p2m
fake_ids = []
for file in dir_list:
    # on traite chaque dossier de p2m
    if os.path.isdir(os.path.join(path, file)) and file[0].isdigit():
        path2 = path+'/'+file
        dir_list2 = os.listdir(path2)

        # création du dico avec toutes les infos utiles
        extra_files = []
        ids_concerned = []

        # f2 is the type of file : fasta, fasta.flt...
        for f2 in dir_list2:
            path3 = path2+'/'+f2

            if not(os.path.isdir(path3)):
                extra_files.append(path3)
            else:
                dir_list3 = os.listdir(path3)

                # f3 are the names of the genomes' files
                for f3 in dir_list3:
                    id_found = True
                    if test_match(pattern1, f3) != '':
                        id_cip = test_match(pattern1, f3)
                    elif test_match(pattern2, f3) != '':
                        id_cip = test_match(pattern2, f3)
                    elif test_match(pattern3, f3) != '':
                        id_cip = test_match(pattern3, f3)
                    elif test_match(pattern4, f3) != '':
                        id_cip = test_match(pattern4, f3)
                    else:
                        fake_ids.append(path3+'/'+f3)
                        id_found = False

                    if id_found:
                        str_lot = f3.replace(id_cip, '')
                        # if str_lot not in ['', '.log', '.ctg.fasta'] and str_lot[0] not in ['_', '-']:
                        #     print(f3)
                        #     print(f3.replace(id_cip, ''))
                        if str_lot not in [''] and str_lot[0] in ['_', '-']:
                            lot_cip = str_lot[1:]
                            if '_' in str_lot[1:]:
                                lot_cip = str_lot[1:].split('_')[0]
                            elif '.' in str_lot[1:]:
                                lot_cip = str_lot[1:].split('.')[0]

                            if lot_cip != '' and lot_cip[0] != 'S':
                                print(path3+'/'+f3)
                                print(lot_cip.strip('-'))
                            else:
                                lot_cip = ''

                            # if test_match(pattern1_lot, str_lot[1:]) != '':
                            #     lot_cip = test_match(pattern1_lot, str_lot[1:])
                            # else:
                            #     if str_lot[1] != 'S':
                            #         print(str_lot[1:])
                            #         cf += 1
                            # ct+=1
        c += 1

print(ct-cf)
print(cf)

