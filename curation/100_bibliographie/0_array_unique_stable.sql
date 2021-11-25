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