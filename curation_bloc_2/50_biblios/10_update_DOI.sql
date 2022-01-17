UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, 'DOI[ :]*', 'doi:')
WHERE sch_bibliographie SIMILAR TO '%DOI%';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, 'doi', 'DOI')
WHERE sch_bibliographie SIMILAR TO '%doi%';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, '(pmid|PMID)[ :]*', 'PMID: ')
WHERE sch_bibliographie SIMILAR TO '%(pmid|PMID)%';
