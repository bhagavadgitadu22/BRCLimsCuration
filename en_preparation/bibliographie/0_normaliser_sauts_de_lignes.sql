UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+)*', E'\n', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+)*', E'\n', 'g');