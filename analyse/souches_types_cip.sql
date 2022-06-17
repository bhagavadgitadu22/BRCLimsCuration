SELECT EXTRACT(YEAR FROM sch_dat_acquisition), COUNT(*) AS total,
COUNT(*) FILTER (WHERE sch_type IS True) AS total_types,
COUNT(*) FILTER (WHERE sch_type IS False) AS total_not_types
FROM last_version_souches_cip
GROUP BY EXTRACT(YEAR FROM sch_dat_acquisition) 
ORDER BY EXTRACT(YEAR FROM sch_dat_acquisition) DESC
