-- on corrige les erreurs d'orthographe genus ou de species 
--(que des updates pas besoin de toucher à t_souche donc)

UPDATE t_donneedico
SET don_lib = 'Bacteroides'
WHERE don_dic_id = 3755 
AND don_lib IN ('Bactéroides', 'Bacteroïdes');

UPDATE t_donneedico
SET don_lib = 'linens'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Brevibacterium'
AND t_donneedico.don_lib = 'limens';

UPDATE t_donneedico
SET don_lib = 'terregena'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Comamonas'
AND t_donneedico.don_lib = 'terregana';

UPDATE t_donneedico
SET don_lib = 'testosteroni'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Comamonas'
AND t_donneedico.don_lib = 'testosteronii';

UPDATE t_donneedico
SET don_lib = 'pseudodiphtheriticum'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Corynebacterium'
AND t_donneedico.don_lib = 'pseudodiphtheritium';

UPDATE t_donneedico
SET don_lib = 'Cupriavidus'
WHERE don_dic_id = 3755 
AND don_lib = 'Cuparividus';

UPDATE t_donneedico
SET don_lib = 'Erysipelothrix'
WHERE don_dic_id = 3755 
AND don_lib = 'Erysipelothrine';

UPDATE t_donneedico
SET don_lib = 'rhusiopathiae'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Erysipelothrix'
AND t_donneedico.don_lib = 'rusopathiae';

UPDATE t_donneedico
SET don_lib = 'Flammeovirga'
WHERE don_dic_id = 3755 
AND don_lib = 'Flammeivirga';

UPDATE t_donneedico
SET don_lib = 'palleronii'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Hydrogenophaga'
AND t_donneedico.don_lib = 'plleronii';

UPDATE t_donneedico
SET don_lib = 'pneumoniae'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Klebsiella'
AND t_donneedico.don_lib = 'pneumaoniae';

UPDATE t_donneedico
SET don_lib = 'casei'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Lactobacillus'
AND t_donneedico.don_lib = 'caseï';

UPDATE t_donneedico
SET don_lib = 'urethralis'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Moraxella'
AND t_donneedico.don_lib = 'uretralis';

UPDATE t_donneedico
SET don_lib = REPLACE(t_donneedico.don_lib, 'Mucilaginibacter ', '')
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Mucilaginibacter'
AND t_donneedico.don_lib LIKE '%Mucilaginibacter%';

UPDATE t_donneedico
SET don_lib = 'freudenreichii'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Propionibacterium'
AND t_donneedico.don_lib = 'freudenrichii';

UPDATE t_donneedico
SET don_lib = 'thoenii'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Propionibacterium'
AND t_donneedico.don_lib = 'thoenii pb identification 16S';

UPDATE t_donneedico
SET don_lib = 'suberifaciens'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Rhizorhapis'
AND t_donneedico.don_lib = 'Rhizorhapis suberifaciens';

UPDATE t_donneedico
SET don_lib = 'fermentans'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Saccharicrinis'
AND t_donneedico.don_lib = 'Saccharicrinis fermentans';

UPDATE t_donneedico
SET don_lib = 'ganghwensis'
FROM t_donneedico AS tdd_genus
WHERE t_donneedico.don_dic_id = 3755 
AND tdd_genus.don_code = t_donneedico.don_parent 
AND tdd_genus.don_lib = 'Thalassotalea'
AND t_donneedico.don_lib = 'Thalassotalea ganghwensis';

UPDATE t_donneedico
SET don_lib = 'Vibrio carchariae'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio carchar V.har', 'Vibrio carchar.v.har');

UPDATE t_donneedico
SET don_lib = 'Vibrio diazotrophicus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio diazotrophic.', 'Vibrio diazotrophicu');

UPDATE t_donneedico
SET don_lib = 'Vibrio furnissii'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio furnissi', 'Vibrio funissii');

UPDATE t_donneedico
SET don_lib = 'Vibrio harveyi'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio harveryi');

UPDATE t_donneedico
SET don_lib = 'Vibrio mytili'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio mytilii');

UPDATE t_donneedico
SET don_lib = 'Vibrio parahaemolyticus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio parahaemolit.', 'Vibrio parahaemolyt.', 'Vibrio parahaemolyti');

UPDATE t_donneedico
SET don_lib = 'Vibrio splendidus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio spledidus', 'Vibrio spledid. like', 'Vibrio spledidus lik');

UPDATE t_donneedico
SET don_lib = 'Vibrio fluvialis'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibro fuvialis');

UPDATE t_donneedico
SET don_lib = 'Sphingobacterium spiritivorum'
WHERE don_dic_id = 3755 
AND don_lib IN ('Sphingoba.spiritivo.');

UPDATE t_donneedico
SET don_lib = 'Sphingobacterium mizutae'
WHERE don_dic_id = 3755 
AND don_lib IN ('Sphingob. mizutae', 'Sphingobac. mizutae');

UPDATE t_donneedico
SET don_lib = 'Enterococcus malodoratus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Enterococcus malado', 'Enterococcus maladoratus');

UPDATE t_donneedico
SET don_lib = 'Enterococcus cecorum'
WHERE don_dic_id = 3755 
AND don_lib IN ('Enterococcus cicorum');

UPDATE t_donneedico
SET don_lib = 'Cytophaga johnsonae'
WHERE don_dic_id = 3755 
AND don_lib IN ('cytophaga johnsonde');

UPDATE t_donneedico
SET don_lib = 'Acinetobacter'
WHERE don_dic_id = 3755 
AND don_lib IN ('Acinetobacteraceae');

UPDATE t_donneedico
SET don_lib = 'Achromobacter'
WHERE don_dic_id = 3755 
AND don_lib IN ('Archromobacter');

UPDATE t_donneedico
SET don_lib = 'Enterobacter'
WHERE don_dic_id = 3755 
AND don_lib IN ('Enterobacteriaceae');

UPDATE t_donneedico
SET don_lib = 'Leptotrichia'
WHERE don_dic_id = 3755 
AND don_lib IN ('Letrotrichia');

UPDATE t_donneedico
SET don_lib = 'Streptobacillus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Steptobacillus');

UPDATE t_donneedico
SET don_lib = 'Streptococcus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Steptococcus');

UPDATE t_donneedico
SET don_lib = 'Tumebacillus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Tumibacillus');

UPDATE t_donneedico
SET don_lib = 'Vibrio'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio sp.', 'Vibrio sp', 'vibrio sp', 'Vibrio Nb 11310');

UPDATE t_donneedico
SET don_lib = 'Vibrio pelagius'
WHERE don_dic_id = 3755 
AND don_lib IN ('Vibrio pelagius I');

UPDATE t_donneedico
SET don_lib = 'Marinitoga lauensis'
WHERE don_dic_id = 3755 
AND don_lib IN ('Strain LG1');

UPDATE t_donneedico
SET don_lib = 'Rhodococcus'
WHERE don_dic_id = 3755 
AND don_lib IN ('Brodococcus');
