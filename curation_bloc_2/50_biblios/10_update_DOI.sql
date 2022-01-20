UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, '(doi|DOI)[ :]*', 'doi:', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO '%(doi|DOI)%';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, '(pmid|PMID)[ :]*', 'pmid:', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO '%(pmid|PMID)%';
