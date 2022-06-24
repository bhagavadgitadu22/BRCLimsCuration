DROP TABLE IF EXISTS panels_crbip_grouped;

COPY panels_crbip (identifiant, panel)
FROM '/csv/40_featured_collections/panels_crbip_utf8.csv'
DELIMITER ';';

SELECT identifiant, array_to_string(ARRAY_AGG(DISTINCT panel), ', ') AS panels
INTO panels_crbip_grouped
FROM panels_crbip
GROUP BY identifiant;
