DROP FUNCTION acad_ou_indus;

CREATE OR REPLACE FUNCTION acad_ou_indus(integer, varchar)
  RETURNS text AS
		$BODY$
	DECLARE
    	matches text;
	BEGIN
		IF $1 IN (0, 1, 2) THEN
			IF $2 = 'BRUKER DALTONIK GmbH' THEN
    			matches := 'industriel';
			ELSE
				matches := 'académique';
			END IF;
		ELSE
			matches := 'industriel';
		END IF;
    	return matches;
	END
$BODY$ LANGUAGE plpgsql;
