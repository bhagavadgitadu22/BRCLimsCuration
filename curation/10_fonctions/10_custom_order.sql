CREATE OR REPLACE FUNCTION cut_string(text, boolean)
  RETURNS decimal AS
$BODY$
	DECLARE
    	matches text[];
	BEGIN
		IF $2 = TRUE THEN
    		matches := REGEXP_MATCHES($1, '([0-9]{2}).[0-9]+');
		ELSE
			matches := REGEXP_MATCHES($1, '[0-9]{2}.([0-9]+)');
		END IF;
    	return matches[1]::decimal;
	END
$BODY$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION custom_sort(text)
  RETURNS DECIMAL AS 
$$
	BEGIN
		IF trim($1) SIMILAR TO 'CIP A[0-9]+' THEN
			RETURN 1000000+(REGEXP_MATCHES($1, '[0-9]+'))[1]::decimal;
		ELSIF trim($1) SIMILAR TO 'CIP A[0-9]+T' THEN
			RETURN 1000000+(REGEXP_MATCHES($1, '[0-9]+'))[1]::decimal+0.5;
			
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{2}.[0-9]+' THEN
			RETURN 2000000+cut_string($1, TRUE)*10000+cut_string($1, FALSE);
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{2}.[0-9]+T' THEN
			RETURN 2000000+cut_string($1, TRUE)*10000+cut_string($1, FALSE)+0.5;
			
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{1}.[0-9]+' THEN
			RETURN 3000000+(REGEXP_MATCHES($1, '[0-9]{1}.[0-9]+'))[1]::decimal;
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{1}.[0-9]+T' THEN
			RETURN 3000000+(REGEXP_MATCHES($1, '[0-9]{1}.[0-9]+'))[1]::decimal*1000+0.5;
			
		ELSIF trim($1) SIMILAR TO 'CIP 1[0-9]{5}' THEN
			RETURN 4000000+(REGEXP_MATCHES($1, '1[0-9]{5}'))[1]::decimal;
		ELSIF trim($1) SIMILAR TO 'CIP 1[0-9]{5}T' THEN
			RETURN 4000000+(REGEXP_MATCHES($1, '1[0-9]{5}'))[1]::decimal+0.5;
		END IF;
	END;
$$ LANGUAGE plpgsql;