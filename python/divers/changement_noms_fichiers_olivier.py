def change_names(string):
    a_file = open("..\..\\"+string+".fa", "r")
    list_of_lines = a_file. readlines()

    corrections = 0
    for i in range(len(list_of_lines)):
        if '>' in list_of_lines[i]:
            corrections += 1
            #print(list_of_lines[i])
            #print('>'+list_of_lines[i].split('|')[1].split(' ')[0])
            list_of_lines[i] = '>'+list_of_lines[i].split('|')[1].split(' ')[0]+'\n'

    a_file = open("..\..\pour olivier\\"+string+"_new.fa", "w")
    a_file. writelines(list_of_lines)

    return corrections

corrections = change_names("CP018917_Sm-UMH5_aa")
print(corrections)
corrections = change_names("CP018925_Sm-UMH3_aa")
print(corrections)
