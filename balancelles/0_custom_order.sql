CREATE OR REPLACE FUNCTION custom_sort(text)
  RETURNS DECIMAL AS 
$$
	BEGIN
		IF trim($1) SIMILAR TO 'CIP A[0-9]+' THEN
			RETURN 1000000+(REGEXP_MATCHES($1, '[0-9]+'))[1]::decimal;
		ELSIF trim($1) SIMILAR TO 'CIP A[0-9]+T' THEN
			RETURN 1000000+(REGEXP_MATCHES($1, '[0-9]+'))[1]::decimal+0.0001;
			
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{2}.[0-9]+' THEN
			RETURN 2000000+(REGEXP_MATCHES($1, '[0-9]{2}.[0-9]+'))[1]::decimal;
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{2}.[0-9]+T' THEN
			RETURN 2000000+(REGEXP_MATCHES($1, '[0-9]{2}.[0-9]+'))[1]::decimal+0.0001;
			
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{1}.[0-9]+' THEN
			RETURN 3000000+(REGEXP_MATCHES($1, '[0-9]{1}.[0-9]+'))[1]::decimal;
		ELSIF trim($1) SIMILAR TO 'CIP [0-9]{1}.[0-9]+T' THEN
			RETURN 3000000+(REGEXP_MATCHES($1, '[0-9]{1}.[0-9]+'))[1]::decimal+0.0001;
			
		ELSIF trim($1) SIMILAR TO 'CIP 1[0-9]{5}' THEN
			RETURN 4000000+(REGEXP_MATCHES($1, '1[0-9]{5}'))[1]::decimal;
		ELSIF trim($1) SIMILAR TO 'CIP 1[0-9]{5}T' THEN
			RETURN 4000000+(REGEXP_MATCHES($1, '1[0-9]{5}'))[1]::decimal+0.0001;
		END IF;
	END;
$$ LANGUAGE plpgsql;