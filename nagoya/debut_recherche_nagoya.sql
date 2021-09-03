SELECT full_trim(sch_com_identite)
FROM t_souche
WHERE sch_com_identite != ''
ORDER BY char_length(sch_com_identite);
