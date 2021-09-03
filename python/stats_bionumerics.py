import time
import matplotlib.pyplot as plt

f = open('../../output/Bionumerics-stats-2015-2021.csv', 'r', newline='')
connections = [line.split('|') for line in f][1:]

struct_time = []
struct_time_debut = []
for conn in connections:
    date_debut = conn[6]
    temps_debut = conn[0]

    date_fin = conn[7]
    temps_fin = conn[1]
    
    struct_time.append([time.strptime(date_debut+";;;"+temps_debut, "%d/%m/%Y;;;%H:%M:%S"), time.strptime(date_fin+";;;"+temps_fin, "%d/%m/%Y;;;%H:%M:%S"), conn[3]])
    struct_time_debut.append(time.strptime(date_debut+";;;"+temps_debut, "%d/%m/%Y;;;%H:%M:%S"))

dates_ordonnees = sorted(struct_time_debut)

nb_users = []
for date in dates_ordonnees:
    n_user = 0

    users = []
    for t in struct_time:
        if t[0] <= date and date <= t[1] and t[2] not in users:
            n_user += 1
            users.append(t[2])
    
    nb_users.append(n_user)
    if len(nb_users)%100 == 0:
        print(len(nb_users))

max_users = max(nb_users)
print("max:"+str(max_users))

i_max = []
for i in range(len(nb_users)):
    if nb_users[i] == max_users:
        i_max.append(i)

print("i_max"+str(i_max))

dates_max = [dates_ordonnees[i] for i in i_max]

print("dates_max"+str(dates_max))

for d_max in dates_max:
    print("")
    print("d_max"+str(d_max))

    t_max = []
    for t in struct_time:
        if t[0] <= d_max and d_max <= t[1]:
            t_max.append(t)

    c_max = []
    for conn in connections:
        date_debut = conn[6]
        temps_debut = conn[0]

        date_fin = conn[7]
        temps_fin = conn[1]

        for tm in t_max:
            if time.strptime(date_debut+";;;"+temps_debut, "%d/%m/%Y;;;%H:%M:%S") == tm[0] and time.strptime(date_fin+";;;"+temps_fin, "%d/%m/%Y;;;%H:%M:%S") == tm[1]:
                c_max.append(conn)
                print(conn[5]+'   '+conn[3])

_ = plt.hist(nb_users, bins='auto')  # arguments are passed to np.histogram
plt.title("Simultaneous users")
plt.xlabel("Number of simultaneous users")
plt.ylabel("Number of times it happened")
plt.show()
