CREATE OR REPLACE FUNCTION full_trim(elmt text) RETURNS text AS $$
	BEGIN
		RETURN btrim(REPLACE(REPLACE(REPLACE(REPLACE(elmt, CHR(127), ''), CHR(9), ''), CHR(13), ''), CHR(10), ''), ';. ():-');
	END;
$$ LANGUAGE plpgsql;