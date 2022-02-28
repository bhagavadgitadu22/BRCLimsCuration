import csv

f = open('../../output/souches_coryne.csv', 'r', newline='')
records = csv.reader(f, delimiter=';')
ids = [record[0] for record in records]
f.close()

chaine = '('
for id in ids:
    if 'CIP ' not in id:
        id = id.replace('CIP', 'CIP ')
    if chaine != '(':
        chaine += '),('
    chaine += "'"+str(id)+"'"
chaine += ')'

print(chaine)

str = '"xxx_id","xxx_cre_dat","xxx_cre_usr","xxx_maj_dat","xxx_maj_usr","xxx_sup_dat","xxx_sup_usr","sch_col_id","sch_statut","sch_nature_depot","sch_taxonomie","sch_origine","sch_nature_prelevement","sch_lieu","sch_auteur_acquisition","sch_depositaire","sch_mutante","sch_redacteur","sch_conservation","sch_atmosphere_incubation","sch_identifiant","sch_temp_id","sch_cpt_id","sch_denomination","sch_synonymes","sch_references_equi","sch_version","sch_remarque_version","sch_origine_rejet","sch_dat_acquisition","sch_privee","sch_catalogue","sch_infos_catalogue","sch_mot","sch_mta_demandee","sch_type","sch_reference","sch_pure","sch_genotype","sch_com_identite","sch_prix","sch_temps_culture","sch_temperature_incubation","sch_com_pheno","sch_dat_pheno","sch_lieu_precis","sch_gps_longitude","sch_gps_latitude","sch_dat_prelevement","sch_dat_isolement","sch_isole_par","sch_denomination_sujet","sch_age_sujet","sch_com_epidemio","sch_com_autres","sch_parutions_endnote","sch_com_docs","sch_bibliographie","sch_qualite_synthese","sch_qualite_numero","sch_qualite_dat_approbation","sch_qualite_approbateur","sch_autres_coll","sch_article","sch_classe_emballage","sch_classification","sch_clinique","sch_historique","sch_isole_a_partir_de","sch_ogm","sch_patho_animal","sch_patho_ogm","sch_patho_plante","sch_phenotype","sch_proprietes","sch_restriction_diffusion","sch_references_sequence","sch_type_souche","sch_pto_id"'

print("e_souche."+str.replace('","', ', e_souche.').replace('"', ''))
