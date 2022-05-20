CREATE OR REPLACE FUNCTION extract_date(elmt timestamp without time zone) RETURNS text AS $$
	BEGIN
		RETURN CASE
			WHEN elmt IS NULL THEN ''
			ELSE CONCAT(
				EXTRACT(YEAR FROM elmt), '-',
				CASE
					WHEN EXTRACT(MONTH FROM elmt)<10 THEN CONCAT('0', EXTRACT(MONTH FROM elmt)::text)
					ELSE EXTRACT(MONTH FROM elmt)::text
				END, '-',
				CASE
					WHEN EXTRACT(DAY FROM elmt)<10 THEN CONCAT('0', EXTRACT(DAY FROM elmt)::text)
					ELSE EXTRACT(DAY FROM elmt)::text
				END
			)
		END;
	END;
$$ LANGUAGE plpgsql;
