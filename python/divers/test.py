str_where = ' WHERE xxx_id IN '+str()

print(open("../curation/validation_curation/25_toutes_souches_avec_infos.sql", "r").read()+str_where)