DROP USER IF EXISTS u_brc_ro, u_brc_rw, u_brc_dba;

CREATE ROLE u_brc_ro LOGIN
  NOSUPERUSER NOINHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
COMMENT ON ROLE u_brc_ro IS 'Utilisateur avec accés en lecture seule sur BRCLims';
ALTER ROLE u_brc_ro WITH PASSWORD 'brc_ro_pwd';
-- Role: u_brc_rw

-- DROP ROLE u_brc_rw;

CREATE ROLE u_brc_rw LOGIN
  NOSUPERUSER NOINHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT u_brc_ro TO u_brc_rw;
COMMENT ON ROLE u_brc_rw IS 'Utilisateur avec accés en lecture/écriture sur BRCLims';
ALTER ROLE u_brc_ro WITH PASSWORD 'brc_rw_pwd';


-- Role: u_brc_dba

-- DROP ROLE u_brc_dba;

CREATE ROLE u_brc_dba LOGIN
  NOSUPERUSER NOINHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT u_brc_ro TO u_brc_dba;
GRANT u_brc_rw TO u_brc_dba;
COMMENT ON ROLE u_brc_dba IS 'Utilisateur avec accés DBA sur BRCLims';
ALTER ROLE u_brc_ro WITH PASSWORD 'brc_dba_pwd';
