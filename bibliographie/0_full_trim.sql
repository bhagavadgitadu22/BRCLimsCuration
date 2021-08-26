CREATE OR REPLACE FUNCTION full_trim(elmt text) RETURNS text AS $$
	BEGIN
		RETURN btrim(REPLACE(REPLACE(REPLACE(REPLACE(elmt, CHR(127), ''), CHR(9), ''), CHR(13), ''), CHR(10), ''), ';. :-');
	END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION array_unique( anyarray ) 
  returns anyarray immutable strict language sql as $$
  select array( select distinct unnest( $1 ) ); $$;

CREATE OR REPLACE FUNCTION array_unique_sorted( anyarray ) 
  returns anyarray immutable strict language sql as $$
  select array( select distinct unnest( $1 ) order by 1 ); $$;

/* ### TAINT there ought to be a simpler, declarative solution */
CREATE OR REPLACE FUNCTION array_unique_stable( text[] )
  returns text[] immutable strict parallel safe language plpgsql as $$
  declare
    R         text[] = '{}';
    ¶element  text;
  begin
    foreach ¶element in array $1 loop
      if not array[ ¶element ] && R then
        R :=  R || array[ ¶element ];
        end if;
      end loop;
    return R; end; $$;