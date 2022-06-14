SELECT * 
FROM (SELECT xxx_id, sch_identifiant, 
ARRAY_AGG(DISTINCT regex_brc ORDER BY regex_brc) FILTER (WHERE regex_brc IS NOT NULL) AS brc,
ARRAY_AGG(DISTINCT regex_excel ORDER BY regex_excel) FILTER (WHERE regex_excel IS NOT NULL) AS excel
FROM (SELECT xxx_id, sch_identifiant, 
	  (REGEXP_MATCHES(cpr_com, '[0-9]{6}', 'g'))[1] AS regex_brc,
	  (REGEXP_MATCHES(p2m, '[0-9]{6}', 'g'))[1] AS regex_excel
FROM souches_avec_infos) AS a
GROUP BY xxx_id, sch_identifiant) AS b
WHERE brc != excel
AND NOT (ARRAY_LENGTH(brc, 1) = 1 AND brc[1] = ANY(excel));

SELECT * 
FROM (SELECT xxx_id, sch_identifiant,
ARRAY_AGG(DISTINCT regex_brc ORDER BY regex_brc) FILTER (WHERE regex_brc IS NOT NULL) AS brc,
ARRAY_AGG(DISTINCT regex_excel ORDER BY regex_excel) FILTER (WHERE regex_excel IS NOT NULL) AS excel
FROM (SELECT xxx_id, sch_identifiant,
	  (REGEXP_MATCHES(cpr_com, '[0-9]{6}', 'g'))[1] AS regex_brc,
	  (REGEXP_MATCHES(p2m, '[0-9]{6}', 'g'))[1] AS regex_excel
FROM souches_avec_infos) AS a
GROUP BY xxx_id, sch_identifiant) AS b
WHERE brc IS NULL;

SELECT xxx_id, sch_identifiant, array_to_string(ARRAY_AGG(p2m), ', ')
FROM souches_sans_infos
GROUP BY xxx_id, sch_identifiant;
