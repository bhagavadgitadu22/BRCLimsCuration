-- on corrige les erreurs d'orthographe genus ou de species 
--(que des updates pas besoin de toucher à t_souche donc)

UPDATE t_donneedico
SET don_lib = 'linens'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Brevibacterium'
AND t_donneedico.don_lib = 'limens'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'terregena'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Comamonas'
AND t_donneedico.don_lib = 'terregana'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'testosteroni'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Comamonas'
AND t_donneedico.don_lib = 'testosteronii'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'pseudodiphtheriticum'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Corynebacterium'
AND t_donneedico.don_lib = 'pseudodiphtheritium'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Cupriavidus'
WHERE don_dic_id = 3755 
AND don_lib = 'Cuparividus'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Erysipelothrix'
WHERE don_dic_id = 3755 
AND don_lib = 'Erysipelothrine'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'rhusiopathiae'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Erysipelothrix'
AND t_donneedico.don_lib = 'rusopathiae'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Flammeovirga'
WHERE don_dic_id = 3755 
AND don_lib = 'Flammeivirga'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'palleronii'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Hydrogenophaga'
AND t_donneedico.don_lib = 'plleronii'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'pneumoniae'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Klebsiella'
AND t_donneedico.don_lib = 'pneumaoniae'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'casei'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Lactobacillus'
AND t_donneedico.don_lib = 'caseï'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'urethralis'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Moraxella'
AND t_donneedico.don_lib = 'uretralis'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = REPLACE(t_donneedico.don_lib, 'Mucilaginibacter ', '')
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Mucilaginibacter'
AND t_donneedico.don_lib LIKE '%Mucilaginibacter%'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'freudenreichii'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Propionibacterium'
AND t_donneedico.don_lib = 'freudenrichii'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'thoenii'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Propionibacterium'
AND t_donneedico.don_lib = 'thoenii pb identification 16S'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'suberifaciens'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Rhizorhapis'
AND t_donneedico.don_lib = 'Rhizorhapis suberifaciens'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'fermentans'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Saccharicrinis'
AND t_donneedico.don_lib = 'Saccharicrinis fermentans'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'ganghwensis'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Thalassotalea'
AND t_donneedico.don_lib = 'Thalassotalea ganghwensis'
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio carchariae'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio carchar V.har', 'Vibrio carchar.v.har')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio diazotrophicus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio diazotrophic.', 'Vibrio diazotrophicu')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio furnissii'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio furnissi', 'Vibrio funissii')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio harveyi'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio harveryi')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio mytili'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio mytilii')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio parahaemolyticus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio parahaemolit.', 'Vibrio parahaemolyt.', 'Vibrio parahaemolyti')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio splendidus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio spledidus', 'Vibrio spledid. like', 'Vibrio spledidus lik')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio fluvialis'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibro fuvialis')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Sphingobacterium spiritivorum'
WHERE don_dic_id = 3755 
AND don_lib IN ('Sphingoba.spiritivo.')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Sphingobacterium mizutae'
WHERE don_dic_id = 3755 
AND don_lib IN ('Sphingob. mizutae', 'Sphingobac. mizutae')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Enterococcus malodoratus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Enterococcus malado', 'Enterococcus maladoratus')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Enterococcus cecorum'
WHERE don_dic_id = 3755 
AND don_lib IN ('Enterococcus cicorum')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Cytophaga johnsonae'
WHERE don_dic_id = 3755 
AND don_lib IN ('cytophaga johnsonde')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Acinetobacter'
WHERE don_dic_id = 3755 
AND don_lib IN ('Acinetobacteraceae')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Achromobacter'
WHERE don_dic_id = 3755 
AND don_lib IN ('Archromobacter')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Enterobacter'
WHERE don_dic_id = 3755 
AND don_lib IN ('Enterobacteriaceae')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Leptotrichia'
WHERE don_dic_id = 3755 
AND don_lib IN ('Letrotrichia')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Streptobacillus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Steptobacillus')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Streptococcus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Steptococcus')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Tumebacillus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Tumibacillus')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio sp.', 'Vibrio sp', 'vibrio sp', 'Vibrio Nb 11310')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio pelagius'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio pelagius I')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Marinitoga lauensis'
WHERE don_dic_id = 3755 
AND don_lib IN ('Strain LG1')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Rhodococcus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Brodococcus')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Bacillus thuringiensis'
WHERE don_dic_id = 3755 
AND don_lib IN ('B. thuringiensis asturiensis', 'thuringiensis 0.718')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Bacillus thuringiensis fukuokaensis'
WHERE don_dic_id = 3755 
AND don_lib IN ('saturation faite=fukuokaensis')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Bacillus cereus'
WHERE don_dic_id = 3755 
AND don_lib IN ('cereus 0,746', 'cereus 0.613', 'cer.0,616')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Bacillus megaterium'
WHERE don_dic_id = 3755 
AND don_lib IN ('B. megaterium 0.480')
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = 'Vibrio vulnificus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio vulnific. bt1')
AND t_donneedico.xxx_sup_dat IS NULL;
