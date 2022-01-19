UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, 'DOI[ :]*', 'doi:')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO '%DOI%';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, 'doi', 'DOI')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO '%doi%';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, '(pmid|PMID)[ :]*', 'PMID: ')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO '%(pmid|PMID)%';
